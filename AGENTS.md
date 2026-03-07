# CLAUDE.md

See @README.md for an overview of the tool, generated file structures, and user-facing customization options.

## Dev Setup

```bash
pip install -e ".[dev]"
pytest
```

## Architecture

The CLI entry point is `src/sphinx_revealjs_quickstart/__main__.py`. The `main()` function:

1. Parses args (inherits all `sphinx-quickstart` args via `parents=[sphinx_get_parser()]`)
2. Calls `sphinx.cmd.quickstart.generate()` to scaffold the base Sphinx project
3. Appends to the generated `source/conf.py` using `conf_append.py.jinja`
4. Writes `source/_static/css/common.css.jinja` and `Makefile` from their respective templates
5. Optionally writes `.github/workflows/publish-pages.yml` and `source/_templates/page.html` when `--github-pages` is given

Templates live in `src/sphinx_revealjs_quickstart/templates/*.jinja` and are rendered via Sphinx's `SphinxRenderer`.

## Two-Pass Rendering in `common.css.jinja`

`common.css.jinja` wraps part of its content in `{% raw %}` / `{% endraw %}`:

```
{% raw %}
{% if highlight_color %}
.reveal strong {
  color: {{ highlight_color }};
}
{% endif %}
{% endraw %}
```

**Why**: rendering happens twice:
- **Pass 1** (build time): `SphinxRenderer` renders `common.css.jinja` → produces `common.css.jinja` (the output file). The `{% raw %}` block passes Jinja2 syntax through unchanged.
- **Pass 2** (Sphinx build): Sphinx processes `common.css.jinja` as a static template, resolving `highlight_color` from `html_context` in `conf.py`.

Removing `{% raw %}` causes an `UndefinedError` at pass 1 because `highlight_color` is not in the render context at that point.

## Updating `tests/expected/`

Tests in `tests/test_main.py` compare generated files against snapshots in `tests/expected/`. When changing any template, update the corresponding expected file manually.

`sphinx_quickstart.time.strftime` is monkeypatched to return `"2099"` in all tests to make the generated copyright year deterministic.

## `--quiet` Is Always `True`

`generate()` is always called with `quiet=True` regardless of whether `--quiet` was passed on the command line. Passing `quiet=False` would trigger sphinx-quickstart's interactive prompt mode, which is not supported here.

## `conflict_handler="resolve"` in argparse

The parser uses `parents=[sphinx_get_parser()]` to inherit all sphinx-quickstart arguments. `conflict_handler="resolve"` is set to allow overriding conflicting options (e.g. `-p`, `-a`) without errors.
