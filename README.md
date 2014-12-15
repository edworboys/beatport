Beatport API Wrapper
========

Handles authentication for the Beatport API

Installation
=========
```
python setup.py install
```

Basic Use
=========

Your Beatport Credentials are stored in the file `beatport-auth.json`. This package looks for that file when the `start` method is called. 

```
import beatport

try:
	beatport = beatport.API()
	beatport.start()

	ids = ','.join(['43949','8190'])
	data = {'ids':ids}

	response = beatport.request('catalog/3/releases', data)

	print response
except Exception as e:
	print e
	raise
```

