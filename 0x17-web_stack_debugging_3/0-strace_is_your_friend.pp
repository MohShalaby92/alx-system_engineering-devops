# replace .phpp with .php in wp-settings.php

exec { 'fix-wordpress':
  command     => "/bin/sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
