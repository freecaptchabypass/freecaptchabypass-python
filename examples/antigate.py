from os import environ
from re import TEMPLATE

from python_fcb import FCBClient
from python_fcb.tasks import AntiGateTask, AntiGateTaskProxyless
import json

api_key = environ["KEY"]

URL = "https://anti-captcha.com/tutorials/v2-textarea"

TEMPLATE_NAME = "CloudFlare cookies for a proxy"

VARIABLES = {}


def process():
    client = FCBClient(api_key)
    task = AntiGateTaskProxyless(
        website_url=URL,
        template_name=TEMPLATE_NAME,
        variables=VARIABLES,
    )
    job = client.createTaskSmee(task)
    solution = job.get_solution()
    return solution


if __name__ == "__main__":
    print("Website URL: " + URL)
    solution = process()
    print("Result: " + json.dumps(solution, indent=4))
