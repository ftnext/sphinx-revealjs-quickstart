# sphinx-revealjs-quickstart

A CLI to quickly scaffold presentation projects with Sphinx + sphinx-revealjs.

## Usage

```console
uvx sphinx-revealjs-quickstart -p project -a author
```

## Generated Files

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
    │       └── common.css
    ├── _templates/
    │   └── page.html
    ├── conf.py
    └── index.rst
```

## About the Generated Content

- `source/conf.py` and `source/_static/css/common.css` contain settings and styles that creator (nikkie) usually uses
- TODO: Make this customizable per project
