# Puppet script that installs and configure a Ngnix web server and adds a custom header.

exec { 'command':
  command  => '
  sudo apt-get update;
  sudo apt-get install nginx -y
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
