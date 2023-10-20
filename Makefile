install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

gendiff-help:
	poetry run python -m gendiff.scripts.gendiff -h

gendiff-prob:
	poetry run python -m gendiff.scripts.gendiff /home/furia/python-project-50/gendiff/file1.json /home/furia/python-project-50/gendiff/file2.json

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests/test_gendiff.py

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml
	# poetry run pytest --cov
	# FUNCTION_VERSION=right pytest --cov-report term-missing --cov=gendiff/scripts tests/test_gendiff.py