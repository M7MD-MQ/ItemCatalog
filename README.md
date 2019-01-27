# Movies Catalog
This is an activity related to Full Stack Nanodegree with Udacity.

## Purpose of this activity:
- Understand How To Deploy An Application.

## Installation
- Get a Server : https://lightsail.aws.amazon.com 
- Create AWS Ubuntu 16.04 Instance	
- Enable Port 2200, 123, 80: Networking-->Add another	

## Startups setup:
- download update: `sudo apt-get update`
- update the server: `apt-get dist-upgrade`
- install apache2:`sudo apt-get install apache2`
- install mod-wsgi:`sudo apt-get install libapache2-mod-wsgi`
- install postgresql:`sudo apt-get install postgresql`
- install pip:`sudo apt-get install python-pip`
- install psycopg2:`sudo apt-get install python-psycopg2`
- install flask:`sudo apt-get install python-flask`
- install finger:`sudo apt-get install finger`
- set date and time: `sudo dpkg-reconfigure tzdata`

## Users Access Control
- add user: `sudo adduser grader`
- give grader sudo privilege: `sudo usermod -aG sudo student`
- locally do this, to create keys: `ssh-keygen`
- locally do this, copy public key:`cat id_rsa.pub`
- in the server do this, create .ssh dir:`mkdir .ssh`
- in the server do this, this file will store all the public keys that this account allowed to use.:`touch .ssh/authorized_keys`
- in the server do this, past public key here:`nano .ssh/authorized_keys`
- in the server do this, `chmod 700 .ssh`
- in the server do this, `chmod 644 .ssh/authorized_keys`
- to access the server form the terminal: `ssh usename@ip -p port -i ~/.ssh/id_rsa`
- force users to login only using the key pair, change PasswordAuthentication from yes to no : `sudo nano /etc/ssh/sshd_config` 
- `sudo service ssh restart `

## Fire Wall configuration
- change port 22 to 2200: `sudo vim /etc/ssh/sshd_config`
- `sudo ufw default deny incoming `
- `sudo ufw default allow outgoing`
- `sudo ufw allow 2200/tcp`
- `sudo ufw allow www `
- `sudo ufw allow ntp`
- `sudo ufw enable`
- `sudo service ssh restart `

## Database configuration
- sudo su - postgres
- CREATE USER catalog WITH PASSWORD [your password];
- ALTER USER catalog CREATEDB;
- CREATE DATABASE catalog WITH OWNER catalog;
- Connect to database $ \c catalog
- REVOKE ALL ON SCHEMA public FROM public;
- GRANT ALL ON SCHEMA public TO catalog;

## Deploying Settings
- go to www dir: `cd /var/www`
- create catalog dir: `mkdir ItemCatalog`
- go to catalog dir: `cd ItemCatalog`
- clone your project here: `sudo git clone {URL}`
- go back one step: `cd ..` 
- create wsgi file(my_flask_app.wsgi): `#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/ItemCatalog/ItemCatalog')
 
from my_flask_app import app as application
application.secret_key = 'super_secret_key'`
- go to site dir: `cd /etc/apache2/sites-available`
- create the configuration file (ItemCatalog.conf): `<VirtualHost *:80>
     ServerName 3.121.78.204
     ServerAdmin admin@3.121.78.204
     WSGIScriptAlias / /var/www/ItemCatalog/my_flask_app.wsgi
     <Directory /var/www/ItemCatalog/ItemCatalog/>
         Order allow,deny
         Allow from all
     </Directory>
     Alias /static /var/www/ItemCatalog/ItemCatalog/static
     <Directory /var/www/ItemCatalog/ItemCatalog/static/>
         Order allow,deny
         Allow from all
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     LogLevel warn
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>`
- `sudo a2ensite ItemCatalog`
- `sudo a2enmod wsgi`
- `sudo service apache2 restart`
## Requirements:
- Start a new Ubuntu Linux server instance on Amazon Lightsail.
- Follow the instructions provided to SSH into your server.
- Update all currently installed packages.
- Change the SSH port from 22 to 2200. Make sure to configure the Lightsail firewall to allow it.
- Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).
- Create a new user account named grader.
- Give grader the permission to sudo.
- Create an SSH key pair for grader using the ssh-keygen tool.
- Configure the local timezone to UTC.
- Install and configure Apache to serve a Python mod_wsgi application.
- Install and configure PostgreSQL.
- Install git.
- Clone and setup your Item Catalog project from the Github repository you created earlier in this Nanodegree program.
- Set it up in your server so that it functions correctly when visiting your server’s IP address in a browser.

## Third party resources used:
- https://github.com/chuanqin3/udacity-linux-configuration
- https://github.com/iliketomatoes/linux_server_configuration
- https://github.com/ddavignon/linux-server-configuration
- https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- https://linuxize.com/post/how-to-create-a-sudo-user-on-ubuntu/#disqus_thread
- http://manpages.ubuntu.com/manpages/xenial/en/man5/sshd_config.5.html
- https://www.digitalocean.com/community/tutorials/how-to-tune-your-ssh-daemon-configuration-on-a-linux-vpsv
- 
