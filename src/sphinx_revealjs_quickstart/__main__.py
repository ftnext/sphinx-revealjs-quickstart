import argparse
import importlib.resources
from pathlib import Path

from sphinx.cmd.quickstart import generate
from sphinx.util.template import SphinxRenderer


def render_package_template(template_name: str, context: dict[str, object]) -> str:
    template_path = importlib.resources.files("sphinx_revealjs_quickstart").joinpath(
        "templates", template_name
    )
    return SphinxRenderer.render_from_file(template_path, context)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", required=True)
    parser.add_argument("-a", "--author", required=True)
    args = parser.parse_args()

    generate(
        {
            "quiet": True,
            "project": args.project,
            "author": args.author,
            "version": "",
            "language": "ja",
            "sep": True,
            "makefile": False,
            "batchfile": False,
            "extensions": [
                "sphinx.ext.githubpages",
                "sphinx_revealjs",
                "sphinx_revealjs.ext.footnotes",
                "sphinx_design",
                "sphinx_new_tab_link",
                "sphinxcontrib.budoux",
                "sphinx_revealjs_copycode",
                "sphinx_revealjs_ext_codeblock",
            ],
            # sphinx.cmd.quickstart.get_parser() default values
            "master": "index",
            "path": ".",
            "dot": "_",
            "suffix": ".rst",
        },
        overwrite=False,
    )

    context: dict[str, object] = {}

    common_css_file = Path("source/_static/css/common.css")
    common_css_file.parent.mkdir(parents=True, exist_ok=True)
    common_css_file.write_text(
        render_package_template("common.css.jinja", context) + "\n",
        encoding="utf-8",
    )

    with Path("source/conf.py").open("a", encoding="utf-8") as confpy:
        confpy.write(render_package_template("conf_append.py.jinja", context) + "\n")

    makefile = Path("Makefile")
    makefile.write_text(
        render_package_template("Makefile.jinja", context) + "\n",
        encoding="utf-8",
    )
