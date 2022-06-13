FILES=stats/Stats.py stats/__init__.py setup.cfg
DOCS=LICENSE README.md

dist: ${FILES} ${DOCS}
	# make sure you have the latest version of Py`pa's build install
	python3 -m pip install --upgrade pip
	python3 -m build

upload: dist
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*
