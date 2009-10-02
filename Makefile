include config.mk

CURRENT_INSTALL_DIR=$(INSTALL_DJANGO_DIR)/$(PROJECTNAME)
SUBDIRS=css pics templates collection mediastore
MEDIADIRS=files/photo files/video files/audio
FILES=$(wildcard *.py) django.wsgi

all: subdirs

help:
	echo -en '\nUseful commands:\n\tinstall\n\tclean\n\ttranslate\n\tshow\n\tget\n\timport_db\n\timport_pics\n\n'

install: create_dir create_media install_files install_subdirs chown_all

clean: clean_subdirs
	rm -f $(wildcard *.pyc) *~

dump:
	grep PASS settings.py
	mysqldump -u $(PROJECTNAME) -p > $(PROJECTNAME).mysql.dump

translate:
	mkdir -p ./locale
	for i in ru; do \
		django-admin.py makemessages --locale $$i; \
	done

%.mo: %.po
	django-admin.py compilemessages

agent:
	. ./ssh-agent.sh

show:
	ssh $(SHELL_SSH) ls -l $(PRODUCTION_DIR)/$(PROJECTNAME)/dumps

get:
	scp $(SHELL_SSH):$(PRODUCTION_DIR)/$(PROJECTNAME)/dumps/`date '+%Y%m%d'`.* ./dumps/

import_db:
	dbdump=`ls ./dumps/*bz2|sort|tail -1`; \
	impsql=`dirname $$dbdump`/`basename $$dbdump .dump.bz2`.sql; \
	echo $$dbdump; \
	bzcat $$dbdump > $$impsql; \
	echo "\. $$impsql"; \
	./manage.py dbshell

import_pics:
	picsdump=`pwd`/`ls ./dumps/*tar|sort|tail -1`; \
	cd $(CURRENT_INSTALL_DIR)/media/itempics/; \
	tar xvf $$picsdump

include targets.mk
