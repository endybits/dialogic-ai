install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	#python -m pytest -vv --cov=app test_*.py
	python -m pytest -vv