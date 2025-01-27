export PYTHONPATH:="."

train:
    poetry run python flows/training.py

lint-fix:
    poetry run isort .
    poetry run black .