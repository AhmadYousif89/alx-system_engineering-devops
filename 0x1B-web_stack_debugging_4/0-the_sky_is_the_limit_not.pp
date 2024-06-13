# Update the ulimit value inside the /etc/default/nginx file to fix the issue with the failling requests.

exec { 'update_nginx_ulimit':
  command => 'sed -i "s/^ulimit=.*/ULIMIT=\"-n 4096\"/Ig" /etc/default/nginx',
  path    => '/bin:/usr/bin:/usr/local/bin',
}

exec { 'restart_nginx_service':
  command => 'service nginx restart',
  path    => '/bin:/usr/bin:/usr/local/bin',
  require => Exec['update_nginx_ulimit'],
}
