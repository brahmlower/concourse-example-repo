
run:
	gunicorn --bind 0.0.0.0:8000 'buildings_api:wsgi.app("./settings.example.yml")'

test-lint:
	pylint -E -d E0202 ./src

test-inspec:
	inspec exec tests/inspec.rb

test-nose:
	nosetests ./tests/*.py

install: test-lint
	pip install .

uninstall:
	pip uninstall -y buildings_api

reinstall: uninstall install
