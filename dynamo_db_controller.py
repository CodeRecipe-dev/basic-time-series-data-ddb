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

    def get_data(self, date):
        response = self._time_series_table.query(
            KeyConditionExpression=Key('date').eq(date),
            ScanIndexForward=False
        )
        items = response['Items']
        return items

    def add_data(self, request_data):
        now = datetime.datetime.now()
        date = self._get_todays_date(now)
        timestamp = int(time.time()) * 1000
        item_data = {
            'date': date,
            'timestamp': timestamp,
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