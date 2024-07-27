# Puppet manifest to install and configure Nginx
exec { 'dist update':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

file {'/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '7624'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['dist update']
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
