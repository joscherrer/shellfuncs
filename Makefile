
all: prereq configure install

prereq:
	pdm install -G configure --no-self

configure: configure.py
	python3.8 configure.py

install:
	pdm install