set -x

poetry run pytest -cov=vellox --cov-fail-under=100 --cov-report=term-missing "${@}"