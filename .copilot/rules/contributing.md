# Contributing to agentic-uv

Guidelines for maintaining and improving the agentic-uv cookiecutter template.

## Before Making Changes

1. **Understand the Template System**
   - Template files use Jinja2 syntax
   - Variables: `{{cookiecutter.project_name}}`, `{{cookiecutter.author}}`, etc.
   - Conditionals: `{% if cookiecutter.mkdocs == 'y' %}...{% endif %}`
   - All available variables in `cookiecutter.json`

2. **Know the Structure**
   - Template lives in `{{cookiecutter.project_name}}/` directory
   - `hooks/` contains pre/post generation scripts
   - `docs/` is root documentation
   - `tests/` tests the template itself

3. **Generated Projects Must**
   - Have `.copilot/` directory with all 5 rule files
   - Keep `{{cookiecutter.project_slug}}/` empty (start clean)
   - Pass `make check` out of the box
   - Have 80%+ test coverage capability

## Making Template Changes

### Editing Generated Project Files

Files in `{{cookiecutter.project_name}}/` are templates. When editing:

```jinja2
# ✓ Good - uses variables
version = "{{cookiecutter.version}}"
author = "{{cookiecutter.author}}"

# ✓ Good - conditional sections
{% if cookiecutter.mkdocs == 'y' %}
docs:
  source: docs/
{% endif %}

# ✗ Bad - hardcoded values
version = "0.1.0"
author = "My Name"

# ✗ Bad - broken variable syntax
{{cookiecutter.project name}}  # Wrong var name
```

### Testing Template Changes

**Always test by generating a sample project:**

```bash
# Quick test with defaults
cookiecutter . --no-input

# Test with specific options
cookiecutter . --no-input layout=src type_checker=ty mkdocs=n

# Test all combinations (from tests/test_combinations.py)
pytest tests/test_combinations.py
```

**After generation, validate:**

```bash
cd example-project
make install
make check      # Must pass
make test       # Must pass
make claude-info  # Shows GitHub Copilot integration
ls -la .copilot/  # Verify all 5 rule files exist
```

## Specific Change Types

### Adding a New Configuration Option

1. Add variable to `cookiecutter.json`:
   ```json
   "new_feature": ["y", "n"]
   ```

2. Use it in template files:
   ```jinja2
   {% if cookiecutter.new_feature == 'y' %}
     # Include feature
   {% endif %}
   ```

3. Update `hooks/post_gen_project.py` to remove files if needed:
   ```python
   if "{{cookiecutter.new_feature}}" != "y":
       remove_file("new_feature_file.py")
   ```

4. Document in generated `.copilot/COPILOT.md` if user-facing

### Updating `.copilot/` Guidelines

The template includes `.copilot/COPILOT.md` and `.copilot/rules/*.md` for generated projects.

**When updating these files:**

1. Ensure all Jinja2 syntax is correct (author name, choices, paths)
2. Include example code that follows the guidelines
3. Reference other rule files with `@.copilot/rules/filename.md`
4. Keep language clear for non-native speakers

Example:

```markdown
# Testing Patterns

- **Framework:** pytest
- **Coverage:** {{cookiecutter.codecov and '80%+ enforced' or 'guided'}}
- **Type hints:** Required on all functions

See also: @.copilot/rules/best-practices.md
```

### Enhancing Code Quality

The template enforces high standards via `pyproject.toml`:

- **Linting:** ruff with 18+ rule sets (no changes without testing)
- **Type Checking:** mypy strict mode (document any exceptions)
- **Testing:** 80%+ coverage enforced (tight but achievable)
- **Security:** bandit checks + pip-audit (no false positives)

**When updating configs:**

1. Modify `{{cookiecutter.project_name}}/pyproject.toml` (the template)
2. Generate a test project: `cookiecutter . --no-input`
3. Run: `cd example-project && make check && make test`
4. Document reasoning in commit message
5. Update `.copilot/rules/best-practices.md` if major change

## Root Project Files

These affect the template itself, not generated projects:

| File | Change Rules |
|------|--------------|
| `cookiecutter.json` | Only add new options if they significantly vary generated projects |
| `hooks/*.py` | Test thoroughly; affects ALL generated projects |
| `mkdocs.yml` | Update author, repo URLs with Noel's info; update sidebar for new docs |
| `.github/workflows/` | Keep as reference only (root project, not for generated projects) |
| `README.md` (root) | Document template features, not usage |
| `docs/` (root) | Document how to use the template and its features |

## Testing Checklist

Before submitting changes:

- [ ] Generated project passes `make check`
- [ ] Generated project passes `make test`
- [ ] All `.copilot/` files exist and are correctly templated
- [ ] No hardcoded author names except in `cookiecutter.json`
- [ ] Repo URLs point to Noel's fork, not Florian's
- [ ] `.copilot/` links work: `@.copilot/rules/filename.md`
- [ ] Makefile targets work: `make test-coverage`, `make claude-info`
- [ ] Test coverage still achievable: example code can reach 80%
- [ ] Security checks pass: no obvious vulnerabilities
- [ ] Root project tests pass: `pytest tests/`

## Common Mistakes

❌ **Hardcoding values in templates:**
```python
# Bad - will be same in all generated projects
author = "Florian"
```

✅ **Use variables:**
```python
# Good - varies per project
author = "{{cookiecutter.author}}"
```

---

❌ **Breaking Jinja2 syntax:**
```python
{% if cookiecutter.feature == 'y' %}
code_here
# Missing endif!
```

✅ **Close all blocks:**
```python
{% if cookiecutter.feature == 'y' %}
code_here
{% endif %}
```

---

❌ **Complex conditionals in `.copilot/` markdown:**
```markdown
## Linting
{% if cookiecutter.type_checker == "mypy" %}
Uses mypy
{% else %}
Uses ty
{% endif %}
```

✅ **Keep markdown readable:**
```markdown
## Linting
- **Type Checker:** {{cookiecutter.type_checker}}
- **Linter:** ruff (18+ rule sets)
```

## Questions?

Reference:
- Jinja2 docs: https://jinja.palletsprojects.com/
- Cookiecutter docs: https://cookiecutter.readthedocs.io/
- agentic-uv docs: See `docs/` directory
- Generated project guide: `.copilot/COPILOT.md` (in template)
