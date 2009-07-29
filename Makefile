include config.mk

CURRENT_INSTALL_DIR=$(INSTALL_DJANGO_DIR)/$(PROJECTNAME)
SUBDIRS=css locale pics templates \
    collection mediastore
MEDIADIRS=files/photo files/video files/audio
FILES=$(wildcard *.py) django.wsgi

all: subdirs

help:
	echo "all       - compile objecs"; \
	echo "install   - install objects"; \
	echo "clean     - clean project"; \
	echo "dump      - make database dump"; \
	echo "translate - prepare i18n"

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

include targets.mk
