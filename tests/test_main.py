import sys
from pathlib import Path

import sphinx.cmd.quickstart as sphinx_quickstart

from sphinx_revealjs_quickstart.__main__ import main


def test_main_generates_project_files(tmp_path, monkeypatch):
    monkeypatch.setattr(sphinx_quickstart.time, "strftime", lambda _fmt: "2099")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        ["sphinx-revealjs-quickstart", "-p", "Demo", "-a", "Alice"],
    )

    main()

    conf_path = tmp_path / "source" / "conf.py"
    css_path = tmp_path / "source" / "_static" / "css" / "common.css"
    index_path = tmp_path / "source" / "index.rst"
    makefile_path = tmp_path / "Makefile"

    assert conf_path.exists()
    assert css_path.exists()
    assert index_path.exists()
    assert makefile_path.exists()

    expected_dir = Path(__file__).parent / "expected"
    expected_conf = (expected_dir / "conf.py").read_text()
    expected_css = (expected_dir / "common.css").read_text()
    expected_makefile = (expected_dir / "Makefile").read_text()

    assert conf_path.read_text() == expected_conf
    assert css_path.read_text() == expected_css
    assert makefile_path.read_text() == expected_makefile
