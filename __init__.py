import logging
import requests
import azure.functions as func

webhook_url = 'https://hooks.slack.com/services/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'
slack_data = {'text': "We did it! :spaghetti:"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
            print (response)
            "Please pass a name on the query string or in the request body",
            status_code=400
        )
