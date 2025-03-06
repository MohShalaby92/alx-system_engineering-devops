# Fix nginx file descriptor limits
exec { 'fix file limit':
  command  => "sed -i '/worker_connections/c\\    worker_connections 4096;' /etc/nginx/nginx.conf",
  provider => 'shell',
}
-> exec { 'update ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 300000\"/' /etc/default/nginx",
  provider => 'shell',
}
-> exec { 'add worker rlimit':
  command  => "sed -i '/worker_processes/a\\    worker_rlimit_nofile 29000;' /etc/nginx/nginx.conf",
  provider => 'shell',
}
-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}

