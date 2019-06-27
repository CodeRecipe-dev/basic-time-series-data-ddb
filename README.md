# Store Time Series Data in DynamoDB

![python](https://img.shields.io/badge/-python-555555.svg) ![serverless](http://public.serverless.com/badges/v3.svg)

This example shows how to store and retreive time series data in DynamoDB. When a user sends time series data such as logs, website usage, or user clicks, to AWS API Gateway, DynamoDB stores the data along with generated timestamp, so that the data can be easily retrieved in chronological order.

More info: https://coderecipe.ai/architectures/24198611

**Example Database Schema**

![schema](https://coderecipe-crlite-architectures-beta.s3.amazonaws.com/coderecipedevs/Store+Time+Series+Data+in+DynamoDB/latest_schema.png)

### Setup

**Download the code**


```
git clone https://github.com/CodeRecipe-dev/basic-time-series-data-ddb.git
```
 
**Deploy to the cloud**    


```
cd basic-time-series-data-ddb

npm install 

serverless deploy --stage beta
```      

### Usage 

To add data to the database, make a POST request with data in the "data" field:

```
curl -X POST \
  <POST_ENDPOINT> \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: <API_KEY>' \
  -d '{"data":"hello world"}'
```

To retrieve data for a specific transaction ID on a given day, make a get request with the date field and transactionId field as query parameter:

```
curl -X GET \
  '<GET_ENDPOINT>?date=2019-6-27&transactionId=1' \
  -H 'x-api-key: <API_KEY>'
```

The above query shows the following result:

```
[
    {
        "date": "2019-6-27",
        "timestamp": 1561658473000,
        "transactionId": "1",
        "data": "newer data for id 1"
    },
    {
        "date": "2019-6-27",
        "timestamp": 1561658468000,
        "transactionId": "1",
        "data": "data for id 1"
    }
]
```

To retrieve data for a specific day, make a GET request with the date field as query parameter:

```
curl -X GET \
  '<GET_ENDPOINT>?date=2019-6-27' \
  -H 'x-api-key: <API_KEY>'
```

**Removal**

To remove the stack, run the following command:


```
serverless remove --stage beta
```   
