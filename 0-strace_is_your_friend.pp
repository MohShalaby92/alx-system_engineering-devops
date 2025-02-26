C# replace .phpp with .php in wp-settings.php to fix apache  error
exec { 'fix wordpress':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
