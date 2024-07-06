# kill process killmenow

exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}
