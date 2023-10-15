# The Puppet manifest uses the exec resource type to execute a shell command to fix a WordPress site.

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
