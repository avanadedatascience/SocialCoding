TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PKG_NAME="operations"

env: clean
	@echo $(TAG)Setting-up virtual environment$(END)
	virtualenv --python=/usr/bin/python ~/.virtualenvs/operations

	@echo $(TAG)Run: source ~/.virtualenvs/operations/bin/activate$(END)


init:
	@echo $(TAG)Installing dev requirements$(END)
	pip install --upgrade -r "requirements-dev.txt"

	@echo $(TAG)Installing $(PKG_NAME)$(END)
	pip install --upgrade --editable .

	@echo

uninstall:
	@echo $(TAG)Uninstalling $(PKG_NAME)$(END)
	- pip uninstall --yes $(PKG_NAME) &2>/dev/null

	@echo "Verifying..."
	cd .. && ! python -m $(PKG_NAME) --version &2>/dev/null

	@echo "Done"
	@echo

unittest:
	@echo $(TAG)Running unittest$(END)
	pytest --cov=operations tests/

clean:
	@echo $(TAG)Cleaning up$(END)
	rm -rf venv
	rm -rf ${PKG_NAME}.egg-info
	rm -rf *.egg dist build
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo

test-sdist:
	@echo $(TAG)Testing sdist build an installation$(END)
	python setup.py sdist
	pip install --force-reinstall --upgrade dist/*.gz
	which $(PKG_NAME)
	@echo


test-bdist-wheel:
	@echo $(TAG)Testing wheel build an installation$(END)
	python setup.py bdist_wheel
	pip install --force-reinstall --upgrade dist/*.whl
	which $(PKG_NAME)
	@echo

deploy:
	python setup.py sdist upload -r local
	python setup.py bdist_wheel upload -r local

flake:
	@echo $(TAG)Checking coding style$(END)
	flake8 $(PKG_NAME)

jenkins: flake unittest test-sdist

set-kernel:
	python -m ipykernel install --user --name=venv