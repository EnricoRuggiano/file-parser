.PHONY: build install

ifeq ($(OS),Windows_NT)
BASH = bash.bat
else
BASH = bash
endif

build:
	poetry build
install:
	python3.8 -m pip install ./dist/file_parser-1.0.0-py3-none-any.whl
