# Puppet script that installs and configure a Ngnix web server and adds a custom header.

exec { 'command':
  command  => 'sudo apt-get update;
  sudo apt-get install nginx -y
  sudo sed -i "/^http {/a \\tadd_header X-Served-By \$hostname;" /etc/nginx/nginx.conf
  sudo service nginx restart',
  provider => shell,
}
