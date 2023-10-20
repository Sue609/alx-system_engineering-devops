# install_apache.pp

# Ensure Apache2 package is installed
package { 'apache2':
  ensure => installed,
}

# Ensure Apache2 service is running and enabled
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

