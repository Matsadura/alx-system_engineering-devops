# Create a file '/tmp/school', sets the owner/permissions/group and it's content
file { '/tmp/school':
file    => 'file',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet',
}
