import pytest
import os
import delegator
from click.testing import CliRunner
from mailprep.cli import mailprep

@pytest.mark.hitl
def test_hitl_display(pytestconfig,request):
    # NOTE(LucidOne): https://github.com/tiran/defusedxml/pull/24
    capmanager = pytestconfig.pluginmanager.getplugin('capturemanager')
    capmanager.suspend_global_capture(in_=True)
    try:
        test_path = os.path.dirname(request.fspath)
        testdata_filepath = os.path.join(test_path,"data","example_wikipedia.vcf")
        input("Press <enter> to display label")
        runner = CliRunner()
        result = runner.invoke(mailprep, ['--simulate',testdata_filepath])
        pdf_filepath = result.stdout.split("\n")[0].split(":")[1].strip()
        delegator.run("evince " + pdf_filepath)
        test_result = input("Did the label display correctly (Y/n)?: ").lower()
    finally:
        capmanager.resume_global_capture()
    if test_result != 'y':
        pytest.exit("Exiting test run: required test failed")
    if os.path.isfile(pdf_filepath):
        os.unlink(pdf_filepath)
    assert(True)

@pytest.mark.hitl
def test_hitl_print(pytestconfig,request):
    # NOTE(LucidOne): https://github.com/tiran/defusedxml/pull/24
    capmanager = pytestconfig.pluginmanager.getplugin('capturemanager')
    capmanager.suspend_global_capture(in_=True)
    try:
        input("Press <enter> to print label")
        test_path = os.path.dirname(request.fspath)
        testdata_filepath = os.path.join(test_path,"data","example_wikipedia.vcf")
        runner = CliRunner()
        result = runner.invoke(mailprep, [testdata_filepath])
        print(result.stdout)
        test_result = input("Did the label print correctly (Y/n)?: ").lower()
    finally:
        capmanager.resume_global_capture()
    if test_result != 'y':
        pytest.exit("Exiting test run: required test failed")
    assert(True)
