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

# Run ApacheBench to test the server
exec { 'run_apache_bench':
   command => '/usr/bin/ab -c 100 -n 1000 http://localhost/',
   require => Service['apache2'],
}
