# Puppet manifest to install and configure Nginx
class { 'nginx': }

# Ensure the nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Create the root HTML page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Configure the default site with a 301 redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'], # Notify nginx to reload configuration
}

# Template for the default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => template('nginx/default.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
