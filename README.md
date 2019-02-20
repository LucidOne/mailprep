# mailprep

[![builds.sr.ht status](https://builds.sr.ht/~lucidone/mailprep.svg)](https://builds.sr.ht/~lucidone/mailprep?)

-----

**Table of Contents**

* [Overview](#overview)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Templates](#templates)
* [License](#license)

## Overview

[mailprep](https://git.sr.ht/~lucidone/mailprep) converts [vCard](https://en.wikipedia.org/wiki/VCard) data into physical labels with a *Dymo LabelWriter 4XL*.

## Usage

```console
$ mailprep --help
Usage: mailprep [OPTIONS] VCF_FILEPATH [TEMPLATE_FILEPATH]

Options:
  --printer TEXT   Printer Name
  --count INTEGER  number of labels to print
  --simulate       Generate output PDF without printing
  --help           Show this message and exit.
```

The default template is designed for 2.25" × 1.25" Uline S-12996 labels.

## Installation

mailprep is distributed on [PyPI](https://pypi.org) as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.5+ and PyPy.

```console
$ pip install mailprep
```

### Debian

The DYMO printer driver can be installed with

```console
$ apt-get install printer-driver-dymo
```


## Testing

### System Dependencies

#### Debian/Stretch

Testing requires `pdftotext` and `tox`

```console
$ apt-get install poppler-utils tox
```

### Automatic Tests
Automatic tests can be run via any of the following methods depending on your workflow

```console
$ python setup.py test
```

```console
$ hatch test
```

```console
$ tox
```

### HitL Tests
Human/Hardware in the Loop tests can be run manually if `xdg-open` can find a pdf reader and a printer is connected.

```console
$ hatch test --test-args "--hitl"
```

```console
$ tox -- --hitl
```

## Templates
Templates are stored as [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) and are evaluated using the Moustache template syntax. Currently the template processing is US-centric, but pull requests and test data is appreciated.

### Formatted name
`{{ fn }}` in the template is replaced with the [formatted name](https://tools.ietf.org/html/rfc2426#section-3.1.1) from the vCard.

### Address
Currently `mailprep` generate labels from the vCard [ADR Type Definition](https://tools.ietf.org/html/rfc2426#section-3.2.1). In the future it may make more sense to use the [LABEL Type Definition](https://tools.ietf.org/html/rfc2426#section-3.2.2) but it is unclear which produced more consistent results.

```
{{ adr_street }}
{{ adr_city }}, {{ adr_region }}
{{ adr_code }}
```

## License

mailprep is distributed under the terms of both

- [MIT License](https://choosealicense.com/licenses/mit)
- [Apache License, Version 2.0](https://choosealicense.com/licenses/apache-2.0)

at your option.

### Test data
The vCard test data is from [Wikipedia](https://en.wikipedia.org/wiki/Vcard#vCard_3.0)
and is licensed as [Creative Commons Attribution-ShareAlike](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License).
