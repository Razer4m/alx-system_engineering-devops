# Define SSH client configuration file path
include stdlib

$file_path = '/etc/ssh/ssh_config'

# Ensure SSH client configuration is set to use private key and disable password authentication
file_line { 'Turn off passwd auth':
  path    => $file_path,
  line    => '    PasswordAuthentication no',
  replace   => true,
}

file_line { 'Declare identity file':
  path    => $file_path,
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
