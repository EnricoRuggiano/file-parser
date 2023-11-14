.PHONY: build install pip-install test test-report

ifeq ($(OS),Windows_NT)
BASH = bash.bat
else
BASH = bash
endif

build:
	poetry build
install:
	poetry install
pip-install:
	python3.8 -m pip install ./dist/file_parser-1.0.0-py3-none-any.whl
test:
	pytest ./tests --html=./tests/report.html --self-contained-html
test-report:
	wkhtmltopdf ./tests/report.html ./tests/report.pdf
