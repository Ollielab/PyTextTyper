python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine upload dist/*
rm -r dist
rm -r PyTextWriter.egg-info