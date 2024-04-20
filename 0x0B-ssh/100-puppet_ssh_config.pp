# Setting up my client config file using puppet

file_line { 'ignore passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'set identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
