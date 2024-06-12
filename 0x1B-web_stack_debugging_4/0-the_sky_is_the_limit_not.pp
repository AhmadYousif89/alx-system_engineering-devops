# Update the ulimit value inside the /etc/default/nginx file to fix the issue with the failling requests.

exec { 'update_nginx_ulimit':
  command => 'sed -i "s/ulimit=.*/ulimit=\"-n 256\"/g" /etc/default/nginx',
  path    => '/bin:/usr/bin:/usr/local/bin',
  onlyif  => 'grep "ulimit=" /etc/default/nginx',
}

exec { 'restart_nginx_service':
  command => 'service nginx restart',
  path    => '/bin:/usr/bin:/usr/local/bin',
  require => Exec['update_nginx_ulimit'],
}
