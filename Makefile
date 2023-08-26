format:
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place .  \
	&& poetry run black --line-length 90 .  \
	&& poetry run isort --profile black .

test:
	poetry run python -m pytest --cov=lr_schedules tests

# Runs the nb, to generate output / figures
execute_readme:
	poetry run python -m nbconvert --to notebook --execute README.ipynb --output README.tmp.ipynb

readme: execute_readme
	poetry run python -m nbconvert --ExtractOutputPreprocessor.enabled=False --to markdown --output README.md README.tmp.ipynb

# run semantic release, and publish to pypi (strict, so will fail if no release)
release:
	poetry run semantic-release --strict version  \
	&& poetry run semantic-release changelog  \
	&& poetry run semantic-release publish  \
	&& poetry publish  \
	&& git push  \
	&& git push --tags
