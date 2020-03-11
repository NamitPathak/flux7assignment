import json

context={
}

event = {
  "RequestType": "Delete",
  "ResponseURL": "http://pre-signed-S3-url-for-response",
  "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/guid",
  "RequestId": "unique id for this create request",
  "ResourceType": "Custom::TestResource",
  "LogicalResourceId": "MyTestResource",
  "ResourceProperties": {
    "statename": "London"
  }
}

def eventrequest():
	return event
def contextrequest():
	return context

def main():
	eventrequest()
	contextrequest()

main()
