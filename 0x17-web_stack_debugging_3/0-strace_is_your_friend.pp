# Fixe the extension typo from 'phpp' to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-file-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
