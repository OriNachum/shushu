import pytest

from shushu import __version__
from shushu.cli import main


def test_default_prints_version(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out.strip()
    assert out == f"shushu {__version__}"


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out
