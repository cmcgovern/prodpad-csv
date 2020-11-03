import requests
import sys
import json
from requests.auth import HTTPBasicAuth
import urllib
import csv
import pandas as pd
import getopt, sys, traceback

help_message = """

Usage: python getRoadmapCSV.py -p <product> -o <csv file>
"""

class Usage(Exception):
	def __init__(self, msg):
		"""docstring for __init__"""
		self.msg = msg


def process(product, filename):
	"""docstring for process"""
	
	request_url = "https://test-e4f77ce669fd0b1a016a100f5c401029.apicentral.axwayamplify.com/api/roadmapcsv?productName=" + urllib.parse.quote(product)
	response = requests.get(request_url, auth=HTTPBasicAuth('3c7d2955-d959-4177-a6be-d708a32c5b40', ''))
	
	# Turn response into CSV file
	try:
		df = pd.DataFrame(json.loads(response.text))
		print(response.text)
		df.to_csv(filename, index=None, encoding="utf-8", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", doublequote=False)
	except Exception as e:
		traceback.print_exc(file=sys.stdout)
		#print(str(e))
		exit();


def main(argv=None):
	"""docstring for main"""
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "p:o:", ["product", "outputfile"])
		except getopt.error as msg:
			raise Usage(msg)
		
		product = None
		filename = None
		
		for option, value in opts:
			if option in ("-p", "--product"):
				product = value
			if option in ("-o", "--outputfile"):
				filename = value
		
		if product is None or filename is None:
			raise Usage(help_message)
		else:
			process(product, filename)
		
	except Usage as err:
		print (sys.argv[0].split("/")[-1] + ": " + str(err.msg))
		print ("\t for help usr --help")
		return 2

if __name__ == '__main__':
	main()