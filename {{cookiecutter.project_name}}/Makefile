.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync
	@uv run pre-commit install

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running {{ cookiecutter.type_checker }}"
	@uv run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}
{%- if cookiecutter.deptry == 'y' %}
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@uv run deptry {% if cookiecutter.layout == "src" %}src{% else %}.{% endif %}
{%- endif %}

.PHONY: audit
audit: ## Run security and dependency audits (bandit + pip-audit)
	@echo "🚀 Security audit: Running bandit"
	@uv run bandit -r {% if cookiecutter.layout == "src" %}src{% else %}{{cookiecutter.project_slug}}{% endif %} -c pyproject.toml
	@echo "🚀 Dependency vulnerability scan: Running pip-audit"
	@uv run pip-audit

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml --cov-report=term-missing
{%- else %}
	@uv run python -m pytest --doctest-modules
{%- endif%}

.PHONY: test-coverage
test-coverage: ## Run tests with coverage and generate HTML report
	@echo "🚀 Testing with coverage report"
{%- if cookiecutter.codecov == "y"%}
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=html --cov-report=term-missing
	@echo "📊 Coverage report generated: coverage_html_report/index.html"
{%- else %}
	@echo "⚠️  Coverage report requires codecov to be enabled"
{%- endif%}

.PHONY: test-parallel
test-parallel: ## Run tests in parallel for faster execution
	@echo "🚀 Running tests in parallel with pytest-xdist"
	@uv run python -m pytest -n auto

.PHONY: test-integration
test-integration: ## Run integration tests only
	@echo "🚀 Running integration tests"
	@uv run python -m pytest tests/integration/ -v

.PHONY: test-property
test-property: ## Run property-based tests with Hypothesis
	@echo "🚀 Running property-based tests with Hypothesis"
	@uv run python -m pytest tests/test_properties.py -v

.PHONY: test-mutation
test-mutation: ## Run mutation tests with mutmut
	@echo "🚀 Running mutation tests with mutmut"
	@uv run mutmut run
	@uv run mutmut results


.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "🚀 Removing build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

{%- if cookiecutter.publish_to_pypi == "y"%}

.PHONY: publish
publish: ## Publish a release to PyPI.
	@echo "🚀 Publishing."
	@uvx twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.
{%- endif%}

{%- if cookiecutter.mkdocs == "y" %}

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@uv run mkdocs serve

{%- endif %}

.PHONY: claude-info
claude-info: ## Show information about Claude Code integration
	@echo "📚 Claude Code Integration for {{cookiecutter.project_name}}"
	@echo ""
	@echo "This project includes .claude/ memory structure for Claude Code."
	@echo "Key files:"
	@echo "  • .claude/CLAUDE.md - Project overview"
	@echo "  • .claude/rules/code-style.md - Coding conventions"
	@echo "  • .claude/rules/testing.md - Test patterns"
	@echo "  • .claude/rules/best-practices.md - Quality standards"
	@echo "  • .claude/rules/deployment.md - CI/CD workflows"
	@echo ""
	@echo "In Claude Code, these files are automatically loaded and provide"
	@echo "context for helping you write, test, and maintain code."
	@echo ""
	@echo "Learn more: @.claude/rules/skills.md"


.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
