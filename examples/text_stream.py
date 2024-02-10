import os
from os import environ

from python_fcb import FCBClient, ImageToTextTask

api_key = environ["KEY"]
DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE = "{}/captcha_ms.jpeg".format(DIR)
EXPECTED_RESULT = "56nn2"


def process(path):
    captcha_fp = open(path, "rb")
    client = FCBClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTaskSmee(task)
    return job.get_captcha_text()


if __name__ == "__main__":
    print("Image: " + IMAGE)
    print("Result: " + str(process(IMAGE)))
    print("Expected: " + str(EXPECTED_RESULT))
