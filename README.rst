Sublime Text 3 Configuration
============================

Install Package Control
-----------------------

View -> Show Console

Paster into console::

import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read()) 

See https://sublime.wbond.net/installation

Plugins
-------

SublimeGit: https://sublimegit.net/#installation


Install Configuration
---------------------

  cd ~/.config/sublime-text-3/Packages
  rm -rf User
  git clone 

Install Plugins
---------------

Directory::

  cd ~/.config/sublime-text-3/Packages

Theme::

  git clone https://github.com/buymeasoda/soda-theme/ "Theme - Soda"

Sublime Linter (ST 3 Compat)::

  git clone https://github.com/gfreezy/SublimeLinter.git
  cd SublimeLinter
  git checkout sublime-text-3
  
  (https://github.com/SublimeLinter/SublimeLinter3)

Mr Igor::

  git clone https://github.com/optilude/SublimeTextIgorPlugin.git

VCS Gutter:

git clone git://github.com/bradsokol/VcsGutter.git "VCS Gutter"

