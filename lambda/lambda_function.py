import json
import requests
import logging
import cfnresponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def unknownResponse(responseData, event, context):
    if "error" in responseData:
        result = cfnresponse.send(
            event, context, cfnresponse.FAILED, responseData)
    else:
        result = cfnresponse.send(
            event, context, cfnresponse.SUCCESS, responseData)
    return result


def callApi(event, context):
    try:
        response = requests.get(
            "http://worldtimeapi.org/api/timezone/Europe/" + event['ResourceProperties']['statename'])
        responseData = response.json()
        result = unknownResponse(responseData, event, context)
        return result
    except Exception as e:
        logger.info(e)
        cfnresponse.send(event, context, cfnresponse.FAILED, e)


def deleteRequest(event, context):
    responseData = {}
    responseData['data'] = "State Not defined"
    result = cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
    return result

def updateRequest(event, context):
    result = callApi(event, context)
    return result


def createRequest(event, context):
    result = callApi(event, context)
    return result


def lambda_handler(event, context):
    logger.info("Received Event: " + str(event))
    if event['RequestType'] == 'Delete':
        result = deleteRequest(event, context)
        return result
    elif event['RequestType'] == 'Update':
        result = updateRequest(event, context)
        return result
    elif event['RequestType'] == 'Create':
        result = createRequest(event, context)
        return result
    else:
        cfnresponse.send(event, context,cfnresponse.FAILED,{""})
