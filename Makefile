init:
	pip install -r requirements.txt

develop:
	python core/develop.py

test:
	nosetests test
