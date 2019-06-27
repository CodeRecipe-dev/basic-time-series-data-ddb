import json
import os
import datetime
import time
from boto3.dynamodb.conditions import Key, Attr

class DynamoDBController:
    def __init__(self, ddb):
        self._ddb = ddb
        table_name = os.environ["TIME_SERIES_TABLE"]
        self._time_series_table = self._ddb.Table(table_name)

    def retrieve_data(self, request_data):
        date = request_data['date']
        filter_expression = None

        if "transactionId" in request_data:
            filter_expression=Key('transactionId').eq(request_data['transactionId'])

        response = self._time_series_table.query(
            KeyConditionExpression=Key('date').eq(date),
            FilterExpression=filter_expression,
            ScanIndexForward=False
        )
        items = response['Items']
        return items

    def write_data(self, request_data):
        now = datetime.datetime.now()
        date = self._get_todays_date(now)
        timestamp = int(time.time()) * 1000
        item_data = {
            'date': date,
            'timestamp': timestamp,
            'transactionId': request_data["transactionId"],
            'data': request_data["data"]
        }
        response = self._time_series_table.put_item(
           Item=item_data
        )
        return response

    def _get_todays_date(self, now):
        return "%d" % now.year + '-' + "%d" % now.month + '-' + "%d" % now.day

def main():
    pass

if __name__ == "__main__":
    main()
