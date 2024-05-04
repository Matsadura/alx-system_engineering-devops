file { "/home/${::USER}/.ssh/config":
  ensure  => present,
  content => "Host web1\n User ubuntu\n Hostname 54.196.38.185\n PubkeyAuthentication yes\n IdentityFile ~/.ssh/school"
}
