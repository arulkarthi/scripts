#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
echo "            backup begins                 "
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

backupdirectoryname="/var/backups/days"

if [ ! -d $backupdirectoryname ]; then

echo "creating backup folder"

mkdir /var/backups/days

fi

usersql="root"
passwdsql="p@ssw0rd"

sqldbname="company"



#if [ -f $sqldbname ]; then

date=`date +%T+%A`
#archive="$date-$sqldbname.tgz"
backupfilename=$date-$sqldbname.gz

backupdir=$backupdirectoryname/$backupfilename

#fi



#mysqldump -u root -p $sqldbname | tar -cvzf $backupdirectoryname/$archive 

#mysqldump -u $usersql -p $sqldbname | gzip > $backupdirectoryname/$backupfilename

mysqldump -u $usersql $sqldbname | gzip > $backupdir

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
echo "            backup completed                "
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
