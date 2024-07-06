# Install an especific version of flask (2.1.0)
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
}
