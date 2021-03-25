![license](https://img.shields.io/github/license/HA71/pywhatcms.svg?style=popout-square)![pvers](https://img.shields.io/pypi/pyversions/pywhatcms.svg?style=popout-square)![size](https://img.shields.io/github/languages/code-size/HA71/pywhatcms.svg?style=popout-square)![pps](https://img.shields.io/pypi/format/pywhatcms.svg?style=popout-square)

![logo](https://whatcms.org/addons/whatcms/static/icon-f-padded.png )

# PyWhatCMS
Python package for whatcms.com API

The package provides a simple way to use the [whatcms.org](https://whatcms.org) API for detecting 467 different Content Management Systems (CMS)

## Installation
```
pip install pywhatcms
```

## Usage
First of all, import pywhatcms:
```python
from pywhatcms import whatcms
```
Query a domain:
```python
whatcms('API-KEY', 'blog.underc0de.org')
```

Obtain info:
```python
whatcms.code
whatcms.msg

whatcms.name
whatcms.version
whatcms.confidence
whatcms.cms_url
whatcms.id
whatcms.request
whatcms.request_web
```
