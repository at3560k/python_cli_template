
from click.testing import CliRunner

from pyt.cli import main


def test_debug_log():
    runner = CliRunner()
    result = runner.invoke(main, ['--debug'])

    first_line = result.output.split('\n')[0]

    assert 'pyt.lib.customLog' in first_line
    assert 'log handler initialized' in first_line


def test_trace_log():
    runner = CliRunner()
    result = runner.invoke(main, ['--debug'])

    # TODO: find out why mangling is pyt.cli in test
    trace_lines = [i for i in result.output.split('\n')
        if '[pyt.cli' in i]

    assert 'Entering echome' in trace_lines[0]
