# sphinx-revealjs-quickstart

A CLI to quickly scaffold presentation projects with Sphinx + sphinx-revealjs.

## Usage

```console
uvx sphinx-revealjs-quickstart -p project -a author
```

To also generate GitHub Pages deployment assets, add `--github-pages`:

```console
uvx sphinx-revealjs-quickstart --github-pages -p project -a author
```

This tool also accepts the same arguments as `sphinx-quickstart` (e.g. `-l`, `-v`, `--release`).
See the [sphinx-quickstart man page](https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html) for the full list.

## Generated Files

### Default

```text
.
├── Makefile
├── build/
└── source/
    ├── _static/
    │   └── css/
    │       └── common.css.jinja
    ├── conf.py
    └── index.rst
```

### With `--github-pages`

```text
.
├── .github/
│   └── workflows/
│       └── publish-pages.yml
├── Makefile
├── build/
└── source/
    ├── _static/
    │   └── css/
    │       └── common.css.jinja
    ├── _templates/
    │   └── page.html
    ├── conf.py
    └── index.rst
```

## About the Generated Content

- `source/conf.py` and `source/_static/css/common.css.jinja` contain settings and styles that creator (nikkie) usually uses

### Customizing `highlight_color`

The generated `conf.py` includes an `html_context` entry:

```python
html_context = {
    "highlight_color": "#5ae08e",
}
```

`common.css.jinja` is a Sphinx CSS template that reads this value at build time.
Change `highlight_color` to any CSS color value to update the `<strong>` tag color in your slides.
Remove the entry entirely to omit the `strong` color rule from the generated CSS.

### Customizing OGP metadata (with `--github-pages`)

When `--github-pages` is used, the generated `conf.py` also includes OGP-related entries in `html_context`:

```python
html_context = {
    "highlight_color": "#5ae08e",
    "twitter_site": "",
    "site_base_url": "",
}
```

These values are used by the generated `source/_templates/page.html` to render Open Graph and Twitter Card meta tags:

| Key | Description |
|---|---|
| `twitter_site` | Twitter/X account handle (e.g. `@yourname`) used in `twitter:site` meta tag |
| `site_base_url` | Base URL of your GitHub Pages site (e.g. `https://yourname.github.io/yourrepo`) used in `og:url` and `og:image` |

Fill in these values in `conf.py` after scaffolding.
