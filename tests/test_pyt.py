
from click.testing import CliRunner
from pyt.cli import main

from pyt.settings import TEST_LOG_MSG


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])
    output = result.output.split('\n')
    filtered = [i for i in output if not i.strip().startswith(TEST_LOG_MSG) ]

    assert filtered[0] == '()'
    assert result.exit_code == 0
