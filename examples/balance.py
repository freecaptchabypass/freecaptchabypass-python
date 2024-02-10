from os import environ
from pprint import pprint
from python_fcb import FCBClient, ImageToTextTask
from sys import argv

api_key = environ["KEY"]


def process():
    client = FCBClient(api_key)
    pprint(client.getBalance())


if __name__ == "__main__":
    pprint(process())
