export PYTHONPATH:="."

lint-fix:
    just backend/lint-fix

infer-huggingface:
    cd backend && poetry run python -m model.huggingface