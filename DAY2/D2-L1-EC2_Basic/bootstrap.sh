#!/bin/sh
yum -y install httpd php php-mysql
chkconfig httpd on
/etc/init.d/httpd start
