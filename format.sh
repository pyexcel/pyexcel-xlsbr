isort $(find pyexcel_xlsbr -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyexcel_xlsbr
black -l 79 tests
