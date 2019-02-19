import pytest
import os
import delegator
from click.testing import CliRunner
from mailprep.cli import mailprep

def test_render_simulation(pytestconfig,request):
    # NOTE(LucidOne): https://github.com/tiran/defusedxml/pull/24
    capmanager = pytestconfig.pluginmanager.getplugin('capturemanager')
    capmanager.suspend_global_capture(in_=True)
    try:
        print(request.fspath)
        test_path = os.path.dirname(os.path.abspath(str(request.fspath)))
        testdata_filepath = os.path.join(test_path,"data","example_wikipedia.vcf")
        runner = CliRunner()
        result = runner.invoke(mailprep, ['--simulate',testdata_filepath])
        pdf_filepath = result.stdout.split("\n")[0].split(":")[1].strip()
        print(pdf_filepath)
        c = delegator.run("pdftotext " + pdf_filepath + " -")
    finally:
        capmanager.resume_global_capture()
    if os.path.isfile(pdf_filepath):
        os.unlink(pdf_filepath)
    assert(c.out == "Forrest Gump\n42 Plantation St.\nBaytown, LA\n30314\n\n\x0c")
