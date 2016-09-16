Sublime Text 3 Configuration
============================

Download
--------

Download and install Sublime Text 3.


Install Source Code Pro
-----------------------

Download and install Source Code Pro.

https://github.com/adobe-fonts/source-code-pro/releases


Install Package Control
-----------------------

Menu: View -> Show Console

Paster into console::

    import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read()) 

See https://sublime.wbond.net/installation

Plugins
-------

Strg+Shift+P -> "Install package":

JavaScript:

  * Sublime-Linter
  * Sublime-linter-contrib-eslint
  * AngularJS

Python:

  * Anaconda
  * MrIgor

Theme:

  * Theme Soda

Misc:

  * SublimeGit
  * SideBarEnhancements
  * Robot Framework Assistant
  * VCS Gutter

Install Configuration
---------------------

  cd ~/.config/sublime-text-3/Packages
  rm -rf User
  git clone 

Install Plugins
---------------

Directory::

  cd ~/.config/sublime-text-3/Packages

  git clone https://github.com/optilude/SublimeTextIgorPlugin.git


