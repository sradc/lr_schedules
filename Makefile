format:
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place .  \
	&& poetry run black --line-length 90 .  \
	&& poetry run isort --profile black .

test:
	poetry run python -m pytest --cov=lr_schedules tests

readme:
	python -m nbconvert --ExtractOutputPreprocessor.enabled=False --to custom --template=markdown.tpl --output README.md README.ipynb
