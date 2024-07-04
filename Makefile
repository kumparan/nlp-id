run-formatter:
	isort .
	black .
.PHONY: run-formatter

# Run test
test:
	pytest
.PHONY: test