#! /bin/bash

echo "Starting to publish (Note that email is not acceptable for username)"

python3 -m pip install --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*

echo "$?"