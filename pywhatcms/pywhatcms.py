import requests

def whatcms(key, url):

    r = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + key + '&url=' + url)
    data = r.json()

    whatcms.name = data['result']['name']
    whatcms.code = data['result']['code']
    whatcms.confidence = data['result']['confidence']
    whatcms.cms_url = data['result']['cms_url']
    whatcms.version = data['result']['version']
    whatcms.msg = data['result']['msg']
    whatcms.id = data['result']['id']
    whatcms.request = data['request']
    whatcms.request_web = data['request_web']

    print(f'''
Status Code : {whatcms.code}
Response Message : {whatcms.msg}

1) CMS - {whatcms.name}
2) CMS Version - {whatcms.version}
3) CMS Confidence - {whatcms.confidence}
4) CMS URL - {whatcms.cms_url}
5) CMS ID - {whatcms.id}
6) Request URL - {whatcms.request}
7) https://whatcms.org Response - {whatcms.request_web}
''')