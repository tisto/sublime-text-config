#!/bin/python2.6
import os
from fabric.api import local, lcd

plugins_dir = '~/.config/sublime-text-2/Packages/'
plugins = [
    # Python PEP-8 and PyFlakes Checker
    'git://github.com/vorushin/sublimetext_python_checker.git',
    # Trailing Spaces
    'git://github.com/SublimeText/TrailingSpaces.git',
    # Python Imports (mr.igor)
    'git://github.com/optilude/SublimeTextIgorPlugin.git',
    # JS Lint
    'git://github.com/eduardolundgren/Sublime-JSLint.git',
]

def install():
    if not os.path.exists('/usr/local/bin/igor'): 
        local('sudo pip install mr.igor')
    if not os.path.exists('/usr/local/bin/pep8'): 
        local('sudo pip install pep8')
    if not os.path.exists('/usr/local/bin/pyflakes'):
        local('sudo pip install pyflakes')
    for plugin_repo in plugins:
        install_plugin(plugin_repo)

def install_plugin(plugin_git_repo):
    git_repo_id = plugin_git_repo.split("/")[-1:][0][:-4]
    plugin_dir = plugins_dir + git_repo_id 
    if os.path.exists(os.path.expanduser(plugin_dir)):
        with lcd(plugin_dir): 
            local('git pull')
    else:
        with lcd(plugins_dir):   
            local('git clone %s' % plugin_git_repo) 

