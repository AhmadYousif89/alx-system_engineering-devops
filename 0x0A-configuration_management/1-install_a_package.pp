# Puppet script to install Flask version 2.1.0 using pip3

package { 'python3-pip':
    ensure => installed,
}

exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    # Check package idempotency
    unless  => '/usr/bin/pip3 show Flask | grep "Version: 2.1.0"',
}
