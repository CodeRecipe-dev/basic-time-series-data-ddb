import json
import os
import boto3
import simplejson as json
from dynamo_db_controller import DynamoDBController

def retrieve_data(event, context):
    print("received event: {}".format(json.dumps(event)))
    request_data = event["queryStringParameters"]
    ddb = boto3.resource('dynamodb')
    _ddb_controller = DynamoDBController(ddb)
    results = _ddb_controller.retrieve_data(request_data)
    response = {
        "statusCode": 200,
        "body": json.dumps(results)
    }
    return response

def write_data(event, context):
    print("received event: {}".format(json.dumps(event)))
    request_body = json.loads(event["body"])
    ddb = boto3.resource('dynamodb')
    _ddb_controller = DynamoDBController(ddb)
    results = _ddb_controller.write_data(request_body)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "data": request_body["data"]
        })
    }
    return response