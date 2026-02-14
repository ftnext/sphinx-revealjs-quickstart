import argparse
from pathlib import Path

from sphinx.cmd.quickstart import generate


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

    common_css_file = Path("source/_static/css/common.css")
    common_css_file.parent.mkdir(parents=True, exist_ok=True)
    common_css_file.write_text(
        """\
.reveal h1,
.reveal h2,
.reveal h3,
.reveal h4,
.reveal h5,
.reveal h6 {
  text-transform: none;
}

.reveal strong {
  color: #5ae08e;
}
"""
    )

    with Path("source/conf.py").open("a") as confpy:
        confpy.write(
            """
# -- Options for Reveal.js output -------------------------------------------------
revealjs_static_path = ["_static"]
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "history": True,
    "center": True,
    "transition": "none",
    "slideNumber": "c/t",
}
revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "CopyCode",
        "src": "revealjs/plugin/copycode/copycode.js",
    },
]

revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",
    "css/common.css",
]

# -- Options for sphinxcontrib-budoux -------------------------------------------------
budoux_targets = ["h1", "h2", "h3"]
"""
    )
