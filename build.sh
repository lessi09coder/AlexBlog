#!/usr/bin/env bash
# exit on error
set -o errexit

#Si utilizamos el enviroment poetry u otro:
# poetry install
pip install -r requirements.txt

python SUPERBLOG/manage.py collectstatic --no-input
python SUPERBLOG/manage.py migrate