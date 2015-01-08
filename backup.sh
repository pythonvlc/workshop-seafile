#!/bin/bash


# commands
ECHO_CMD=/bin/echo
SERVICE_CMD=/usr/sbin/service
MKDIR_CMD=/bin/mkdir
MYSQLDUMP_CMD=/usr/bin/mysqldump
RSYNC_CMD=/usr/bin/rsync


# params
SERVICE=seafile-server
DST_FOLDER=/var/backups/seafile/pythonvlc.`date +\%a`
LOG_FILE=$DST_FOLDER/seafile-backup.log
DB_FOLDER=$DST_FOLDER/databases
DATA_FOLDER=$DST_FOLDER/data
MYSQL_HOST=localhost
MYSQL_USER=seafile
MYSQL_PWD=el_password_que_corresponda
CCNET_DB=ccnet-db
SEAFILE_DB=seafile-db
SEAHUB_DB=seahub-db
DATASRC_FOLDER=/srv/pythonvlc/


# create folders
$MKDIR_CMD -p $DST_FOLDER
$MKDIR_CMD -p $DB_FOLDER
$MKDIR_CMD -p $DATA_FOLDER
$ECHO_CMD "Backup begin at `date`" > $LOG_FILE
# stop server
$SERVICE_CMD $SERVICE stop 2>> $LOG_FILE
# dump databases
$MYSQLDUMP_CMD -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PWD --opt $CCNET_DB > $DB_FOLDER/$CCNET_DB.sql 2>> $LOG_FILE
$MYSQLDUMP_CMD -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PWD --opt $SEAFILE_DB > $DB_FOLDER/$SEAFILE_DB.sql 2>> $LOG_FILE
$MYSQLDUMP_CMD -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PWD --opt $SEAHUB_DB > $DB_FOLDER/$SEAHUB_DB.sql 2>> $LOG_FILE
# rsync data
$RSYNC_CMD -az --delete $DATASRC_FOLDER $DATA_FOLDER 2>> $LOG_FILE
#start server
$SERVICE_CMD $SERVICE start 2>> $LOG_FILE
$ECHO_CMD "Backup end at `date`" >> $LOG_FILE
