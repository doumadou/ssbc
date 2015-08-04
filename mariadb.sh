#!/bin/sh
 chown -R mysql:mysql /var/lib/mysql
 mysql_install_db --user mysql > /dev/null
 mysqld_safe --user mysql &
 sleep 5s
 mysql -v < ./mariadb.sql
 sleep 5s
 ps -wef | grep mysql | grep -v grep | awk '{print $2}' | xargs kill -9
 mysqld_safe --user mysql &

