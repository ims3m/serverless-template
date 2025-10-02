import os
import json


def lambda_handler(event, context):
    return json.stringfy({'status':'ok', 'status_code':'200'})