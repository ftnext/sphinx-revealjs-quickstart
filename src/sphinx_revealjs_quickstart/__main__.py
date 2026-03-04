import argparse
import importlib.resources
from pathlib import Path

from sphinx.cmd.quickstart import generate
from sphinx.cmd.quickstart import get_parser as sphinx_get_parser
from sphinx.util.console import bold
from sphinx.util.template import SphinxRenderer


def render_package_template(template_name: str, context: dict[str, object]) -> str:
    template_path = importlib.resources.files("sphinx_revealjs_quickstart").joinpath(
        "templates", template_name
    )
    return SphinxRenderer.render_from_file(template_path, context)


def main():
    parser = argparse.ArgumentParser(
        parents=[sphinx_get_parser()],
        conflict_handler="resolve",
    )
    parser.add_argument("--github-pages", action="store_true", default=False)
    args = parser.parse_args()

    generate(
        {
            "quiet": True,
            "project": args.project,
            "author": args.author,
            "version": args.version,
            "release": args.release,
            "language": args.language,
            "sep": args.sep if args.sep is not None else True,
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
            "master": args.master,
            "path": args.path,
            "dot": args.dot,
            "suffix": args.suffix,
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

    actions_file = Path(".github/workflows/publish-pages.yml")
    actions_file.parent.mkdir(parents=True, exist_ok=True)
    actions_file.write_text(
        render_package_template("publish-pages.yml.jinja", context) + "\n",
        encoding="utf-8",
    )

    page_html_file = Path("source/_templates/page.html")
    page_html_file.parent.mkdir(parents=True, exist_ok=True)
    page_html_file.write_text(
        render_package_template("page.html.jinja", context) + "\n",
        encoding="utf-8",
    )

    print(bold("Configure html_context in source/conf.py"))
