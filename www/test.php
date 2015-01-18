<?php

print "File owner: " . get_current_user(); 

$effProcessUser = posix_getpwuid(posix_geteuid());
print "<br>Effective process owner: ". $effProcessUser['name'];

$processUser = posix_getpwuid(posix_geteuid());
print "<br>Process owner: ". $processUser['name'];

print "<br>diques: " . file_get_contents("/var/www/index");

?>
