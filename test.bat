pip freeze
nosetests --with-coverage --cover-package pyexcel_xlsbr --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyexcel_xlsbr && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
