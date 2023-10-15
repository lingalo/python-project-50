install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

gendiff_help:
	poetry run python -m gendiff.scripts.gendiff -h

gendiff_prob:
	poetry run python -m gendiff.scripts.gendiff /home/furia/python-project-50/gendiff/file1.json /home/furia/python-project-50/gendiff/file2.json