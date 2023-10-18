import requests
import ssl
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager


class CustomCipherAdapter(HTTPAdapter):

    def __init__(self, **kwargs):

        self.cipher_suite = cipher_suite

        super(CustomCipherAdapter, self).__init__(**kwargs)


    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers(self.cipher_suite)
        kwargs['ssl_context'] = context
        self.poolmanager = PoolManager(*args, **kwargs)


#url = 'https://test-lb-secure.xsolla.com/jdfhgjdfhg'
url = 'https://test-lb-ps.xsolla.com/health/major/'
# Config encryption algorithms

#cipher_suite = 'ECDHE-ECDSA-AES256-GCM-SHA384'

cipher_suite = 'ECDHE-ECDSA-AES128-GCM-SHA256'

adapter = CustomCipherAdapter()

session = requests.Session()

session.mount('https://', adapter)

response = session.get(url)


print('Status code:', response.status_code)

print('Content:', response.text)
