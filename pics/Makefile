TOP_DIR=..

include $(TOP_DIR)/config.mk

CURRENT_INSTALL_DIR=$(INSTALL_DJANGO_DIR)/$(PROJECTNAME)/pics
SUBDIRS=
FILES=$(wildcard *.png) $(wildcard *.gif) $(wildcard *.jpeg)

all:

install: create_dir install_subdirs install_files

clean:
	rm -f *~

include $(TOP_DIR)/targets.mk
