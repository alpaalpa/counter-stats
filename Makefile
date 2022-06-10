FILES=stats/Stats.py stats/__init__.py
DOCS=LICENSE README.md setup.py

dist: ${FILES} ${DOCS}
	python setup.py sdist bdist_wheel

upload: dist
	python -m twine upload dist/*