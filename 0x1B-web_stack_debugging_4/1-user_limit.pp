# A puppet script for changing the OS configuration so that it is possible to login with the holberton user.

$filename = '/etc/security/limits.conf'
$new_limit= '4096'

# Comment out any existing user lines in the file
exec { 'comment_existing_users':
  command => "sed -i 's/^\\s*\\w\\+\\s*\\(soft\\|hard\\).*$/# &/' ${filename}",
  path    => '/bin:/usr/bin:/usr/local/bin',
  onlyif  => "grep -P '^\\s*\\w+\\s*(soft|hard).*' ${filename}",
}
# Add the new rules to the file
exec { 'add_new_rules':
  command => "echo \"* soft nofile ${new_limit}\n* hard nofile ${new_limit}\" >> ${filename}",
  path    => '/bin:/usr/bin:/usr/local/bin',
  unless  => "grep -E '^\\* (soft|hard) nofile ${new_limit}' ${filename}",
  require => Exec['comment_existing_users'],
}
