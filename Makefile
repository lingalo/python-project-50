install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl