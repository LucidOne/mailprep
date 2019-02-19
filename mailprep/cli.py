import os
import pkg_resources
import sys
import tempfile

from loguru import logger
import click
import vobject
import pystache
import cairosvg
import delegator

@click.command()
@click.option('--printer', default='LabelWriter-4XL', help='Printer Name')
@click.option('--count', default=1, help='number of labels to print')
@click.option('-s','--simulate','simulate', default=False, is_flag=True, help='Generate output PDF without printing')
@click.option('-d','--debug','debug', default=False, is_flag=True, help='Log debugging messages to standard error')
@click.argument('vcf_filepath', metavar='VCARD')
@click.argument('template_filepath', metavar='[TEMPLATE]', default=None, required=False)
def mailprep(printer,count,simulate,debug,vcf_filepath,template_filepath):
    """mailprep converts vCard data into physical labels from SVG templates

    \b
    usage:
    $ mailprep contact.vcf template.svg
    """

    # Logger setup
    if 'LOGURU_LEVEL' not in os.environ.keys() and not debug:
        logger.remove()
        logger.add(sys.stderr, level="WARNING")

    logger.debug(os.path.abspath(vcf_filepath))
    with open(vcf_filepath) as f:
        vcard = vobject.readOne(f)

    if not template_filepath:
        svg_template = pkg_resources.resource_string(__name__, "template.svg")
    else:
        with open(template_filepath) as template_f:
            svg_template = template_f.read()

    svg_output = pystache.render(svg_template,
                                 {'fn': vcard.fn.value,
                                  'adr_street': vcard.adr.value.street,
                                  'adr_city': vcard.adr.value.city,
                                  'adr_region': vcard.adr.value.region,
                                  'adr_code': vcard.adr.value.code})

    (_,output_filepath) = tempfile.mkstemp(prefix='mailprep_',suffix='.pdf')
    logger.debug("Output: "+output_filepath)
    cairosvg.svg2pdf(bytestring=svg_output, write_to=output_filepath)

    cmd = "lp -d " + printer + " " + output_filepath

    if simulate:
        click.echo('output: %s' % output_filepath)
        logger.debug("Simulated: " + cmd)
    else:
        click.echo("Printing " + str(count) + " copies of " + vcf_filepath)
        for x in range(0, count):
            delegator.run(cmd)
            logger.debug("Executed: " + cmd)
