#\!/bin/bash
set -x
rm -rdf venv_test
virtualenv venv_test
. venv_test/bin/activate
pip install -r requirements_test.txt
coverage run --source=prpject -m unittest discover
coverage xml
pylint -f parseable -d I0011,R0801 project | tee pylint.out
set +x
#py.test --cov=mercury_libs/ tests/
