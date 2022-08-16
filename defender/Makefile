.DEFAULT_GOAL := all

init:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

build: clean init dev
	python setup.py build sdist bdist_wheel

clean:
	rm -rf build dist
	find . -name *.pyc -delete
	find . -name *.pytest_cache -exec rm -r {} +
	find . -name __pycache__ -exec rm -r {} +

test:
	PYTHONPATH=$${PWD}/src/:$${PWD}/test/:$${PYTHONPATH} python -m pytest test --junitxml=build/reports/junit.xml

coverage:
	PYTHONPATH=$${PWD}/src/:$${PYTHONPATH} python -m pytest --junitxml=build/reports/junit.xml --cov=src test --cov-report=term-missing --cov-report=xml
	mv coverage.xml build/reports/hw-coverage.xml

all: clean init dev coverage build docker

docker:
	DOCKER_BUILDKIT=1 docker build -t cybersecurity/defender:0.0.1 -f Dockerfile .



.PHONY: init dev build clean test coverage docker
