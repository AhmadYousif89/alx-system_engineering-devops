# Define the nginx configuration

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

# # Configure custom 404 page
# file { '/var/www/html/not_found.html':
#   ensure  => 'file',
#   content => "Ceci n'est pas une page",
# }

# file_line { 'configure 404 page':
#   ensure  => present,
#   line    => 'error_page 404 /not_found.html;',
#   path    => '/etc/nginx/sites-available/default',
#   require => Package['nginx'],
#   notify  => Service['nginx'],
# }
# restart nginx
# exec { 'restart service':
#   command => 'service nginx restart',
#   path    => '/usr/bin:/usr/sbin:/bin',
# }

# # start service nginx
# service { 'nginx':
#   ensure  => running,
#   require => Package['nginx'],
# }

# Restart nginx service
# service { 'nginx':
#   ensure  => 'running',
#   enable  => true,
#   require => Package['nginx'],
# }
