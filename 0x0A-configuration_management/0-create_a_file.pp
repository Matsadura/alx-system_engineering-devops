file { '/tmp/school':
file    => 'file',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet',
}
