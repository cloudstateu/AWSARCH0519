#!/bin/sh
yum -y install httpd php &&
chkconfig httpd on &&
/etc/init.d/httpd start &&
aws s3 cp s3://csa03-studentX/index.php /var/www/html