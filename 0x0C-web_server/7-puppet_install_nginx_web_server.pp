# Define a class for nginx configuration
class nginx_configuration {
  # Package installation and update
  package { 'nginx':
    ensure => 'installed',
  }

  # Update package repositories
  exec { 'apt-update':
    command => '/usr/bin/apt-get update -y',
    path    => ['/bin', '/usr/bin'],
    require => Package['nginx'],
  }

  # Give ownership to website files
  file { '/var/www/html':
    ensure  => 'directory',
    owner   => $facts['user'],
    group   => $facts['user'],
    recurse => true,
    mode    => '0755',
  }

  # Create index page
  file { '/var/www/html/index.nginx-debian.html':
    ensure  => 'file',
    content => '
    <!DOCTYPE html>
      <html>
        <head>
        <title>My Web Server</title>
        </head>
        <body style="font-family: Open Sans;">
          <h1 style="text-align: center; margin: 0; font-size: 5rem;">Hello World!</h1>
        </body>
      </html>',
    owner   => $facts['user'],
    group   => $facts['user'],
    mode    => '0644',
  }

  # Configure redirection
  file_line { 'configure redirection':
    ensure  => present,
    line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=w_u4iY45A_U permanent;',
    path    => '/etc/nginx/sites-available/default',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Configure custom 404 page
  file { '/var/www/html/not_found.html':
    ensure  => 'file',
    content => "Ceci n'est pas une page",
    owner   => $facts['user'],
    group   => $facts['user'],
    mode    => '0644',
  }

  file_line { 'configure 404 page':
    ensure  => present,
    line    => 'error_page 404 /not_found.html;',
    path    => '/etc/nginx/sites-available/default',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Restart nginx service
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => [File_line['configure redirection'], File_line['configure 404 page']],
  }
}

# Include the nginx_configuration class
include nginx_configuration
