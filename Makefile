PYTHON = python3

.PHONY: clean lint test build
default: clean lint test build

build:
	mkdir dist
	zip -r ./dist/auto_generated_pipieline_framework.zip ./auto_generated_pipieline_framework
	cp workflowRunner.py ./dist/workflowRunner.py
	cp environment.yaml ./dist/environment.yaml
	cp gcp_pip_install.sh ./dist/gcp_pip_install.sh
	cp requirements.txt ./dist/requirements.txt

clean:
	rm -rf dist/ build/ .eggs/ reports/ *.egg-info .coverage .pytest_cache/

lint:
	flake8 demo_prj
	@echo "Lint Complete!!"

test:
	$(PYTHON) setup.py test
