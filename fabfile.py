#!/usr/bin/python2.6
import os
from fabric.api import local, lcd

sublime_version = "2165"
install_dir = '/opt/sublime-text-2'
plugins_dir = '~/.config/sublime-text-2/Packages'
plugins = [
    # Python PEP-8 and PyFlakes Checker
    'git://github.com/vorushin/sublimetext_python_checker.git',
    # Trailing Spaces
    'git://github.com/SublimeText/TrailingSpaces.git',
    # Python Imports (mr.igor)
    'git://github.com/optilude/SublimeTextIgorPlugin.git',
    # JS Lint
    'git://github.com/eduardolundgren/Sublime-JSLint.git',
    # Git
    'git://github.com/kemayo/sublime-text-2-git.git',
]

def install():
    install_sublime_text_2()
    install_python_packages()
    install_sublime_text_plugins()
    install_pdb_sublime_text_support()
    install_python_checkers()
    install_patterns()


def install_sublime_text_2():
    if not os.path.exists('build'):
        local('wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202%20Build%202165.tar.bz2')
        local('tar xfvj Sublime\ Text\ 2\ Build\ %s.tar.bz2' % sublime_version)
        local('rm Sublime\ Text\ 2\ Build\ %s.tar.bz2' % sublime_version)
        local('mv Sublime\ Text\ 2 build')
    if os.path.exists('/usr/local/bin/sublime_text'):
        local('sudo rm /usr/local/bin/sublime_text')
    local('sudo ln -s /opt/sublime-text-2/build/sublime_text /usr/local/bin/sublime_text')

def install_python_packages():
    if not os.path.exists('bin/igor'):
        local('bin/pip install mr.igor')
    if not os.path.exists('/usr/local/bin/igor'):
        local('sudo ln -s %s/bin/igor /usr/local/bin/igor' % install_dir)


def install_sublime_text_plugins():
    for plugin_repo in plugins:
        install_plugin(plugin_repo)
    install_pdb_sublime_text_support()

def install_plugin(plugin_git_repo):
    git_repo_id = plugin_git_repo.split("/")[-1:][0][:-4]
    plugin_dir = plugins_dir + git_repo_id
    if os.path.exists(os.path.expanduser(plugin_dir)):
        with lcd(plugin_dir):
            local('git pull')
    else:
        with lcd(plugins_dir):
            local('git clone %s' % plugin_git_repo)

def install_pdb_sublime_text_support():
    local('bin/pip install --upgrade PdbSublimeTextSupport')
    if not os.path.exists('/usr/local/bin/subl'):
        local('sudo ln -s /opt/sublime-text-2/build/sublime_text /usr/local/bin/subl')
    if not os.path.exists('~/.pdbrc'):
        local('cp .pdbrc ~/')
    if not os.path.exists('/usr/local/bin/subl'):
        local('cp subl /usr/local/bin/')

def install_python_checkers():
    # Pep8
    if not os.path.exists('bin/pep8'):
        local('bin/pip install pep8')
    if os.path.exists('/usr/local/bin/pep8'):
        local('sudo rm /usr/local/bin/pep8')
    local('sudo ln -s %s/bin/pep8 /usr/local/bin/pep8' % install_dir)
    # Pyflakes
    if not os.path.exists('bin/pyflakes'):
        local('bin/pip install pyflakes')
    if os.path.exists('/usr/local/bin/pyflakes'):
        local('sudo rm /usr/local/bin/pyflakes')
    local('sudo ln -s %s/bin/pyflakes /usr/local/bin/pyflakes' % install_dir)
    if os.path.exists('%s/sublimetext_python_checker/local_settings.py' % plugins_dir):
        local('rm %s/sublimetext_python_checker/local_settings.py' % plugins_dir)
    local('cp templates/local_settings.py %s/sublimetext_python_checker' % plugins_dir)

def install_patterns():
    if os.path.exists('SublimeTextMisc'):
        with lcd('SublimeTextMisc'):
            local('git pull')
    else:
        local('git clone git://github.com/optilude/SublimeTextMisc.git')
    local('rsync -avz SublimeTextMisc/Packages/Buildout/ %s/Buildout/' % plugins_dir)
    local('rsync -avz SublimeTextMisc/Packages/Zope/ %s/Zope' % plugins_dir)
