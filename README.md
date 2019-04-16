# PyWhatcms
Python package for whatcms.com API

The package provides a simple way to use the whatcms.org API for detecting 467 different Content Management Systems

## Installation
```
pip install pywhatcms
```

## Usage
First of all, import pywhatcms:
```
from pywhatcms import whatcms
```
Query a domain:
```
whatcms('API-KEY', 'blog.underc0de.org')
```
Obtain info:
```
whatcms.name
whatcms.code
whatcms.confidence
whatcms.cms_url
whatcms.version
whatcms.msg
whatcms.id
whatcms.request
whatcms.request_web
```
