.PHONY: install test clean build publish

install:
	pip install -e .

install-deps:
	pip install -r requirements.txt

test:
	pytest

clean:
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	python -m build

publish:
	python -m twine upload dist/*

run:
	python vddownloader/app.py
