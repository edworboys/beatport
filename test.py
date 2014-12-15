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