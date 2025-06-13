#!/usr/bin/env bash

source .venv/bin/activate

python3 setup.py sdist

pip install dist/openpyutils-0.0.1.tar.gz

deactivate