import requests

def whatcms(key, url):
    whatcms.r = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + key + '&url=' + url).json()
    whatcms.name = whatcms.r['result']['name']
    whatcms.code = whatcms.r['result']['code']
    whatcms.confidence = whatcms.r['result']['confidence']
    whatcms.cms_url = whatcms.r['result']['cms_url']
    whatcms.version = whatcms.r['result']['version']
    whatcms.msg = whatcms.r['result']['msg']
    whatcms.id = whatcms.r['result']['id']
    whatcms.request = whatcms.r['request']
    whatcms.request_web = whatcms.r['request_web']
