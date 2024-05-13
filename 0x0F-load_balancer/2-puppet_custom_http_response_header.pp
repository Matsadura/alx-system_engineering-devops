# Configures nginx webserver in a new ubuntu environment

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'custom_header':
  command  => 'sed -i "24i\ add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  provider => 'shell',
}


exec { 'redirect_me':
  command  => 'sed -i "24i\ rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
