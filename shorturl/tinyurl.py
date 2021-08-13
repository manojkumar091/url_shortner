#!/usr/bin/env python 3
import contextlib

try:
	from urllib.parse import urlencode		

except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen

except ImportError:
	from urllib import urlopen


def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))	
	with contextlib.closing(urlopen(request_url)) as response:					
		return response.read().decode('utf-8 ')									
