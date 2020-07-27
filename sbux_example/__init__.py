import logging
import os
import azure.functions as func
from slack_webhook import Slack


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    slack_url = os.getenv('SLACK_URL')
    slack = Slack(url=(slack_url))
    req_body = req.get_json()
    logging.info(format(req_body))
    slack.post(text=f"system: {req_body['systemName']} \n"
               f"system model: {req_body['systemModel']} \n"
               f"current score: {req_body['currentScore']} \n"
               f"timestamp: {req_body['timestampIso8601']} \n"
               "description: {req_body['description']} \n"
               "resolution: {req_body['resolution']}"
               )
#    slack.post(text=f"system: {req_body}")
    logging.info('Successfully posted to Slack.')
    return func.HttpResponse(format(req_body))
