import json
import logging
import requests
from lambda_function import*
from eventrequest import*

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CHECKSTATUS = "SUCCESS"

def testlambda():
	response = lambda_handler(eventrequest(),contextrequest())
	try:
		assert response == CHECKSTATUS
		print("assertion passed")
	except:
		print("assertion failed")
			
def main():
    testlambda()
    
main()