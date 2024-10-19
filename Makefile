# Makefile

SHELL = /usr/bin/bash

.PHONY:test
test:
	python -m unittest

lint:
	python -m black -l 79 .
	-flake8 --ignore E251,E266,W391,W503,E241,E221
	-pylint .

coverage:
	coverage run -m unittest
	coverage report -m 

clean:
	find . -type f -name "*.pyc" -exec rm {} \;
	find . -type f -name "*.swp" -exec rm {} \;

all: clean lint test coverage


