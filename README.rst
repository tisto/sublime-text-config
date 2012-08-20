Plone Development with Sublime Text 2 on Ubuntu 12.04 LTS.

sudo add-apt-repository ppa:webupd8team/sublime-text-2
sudo apt-get update
sudo apt-get install sublime-text

cd /opt
git clone git@github.com:tisto/sublime-text-config.git sublime-text-2
cd /opt/sublime-text-2
virtualenv . --no-site-packages
bin/pip install fabric
bin/fab --list
bin/fab install

http://www.webupd8.org/2011/03/sublime-text-2-ubuntu-ppa.html

http://www.technoreply.com/how-to-install-sublime-text-2-on-ubuntu-12-04-unity/

