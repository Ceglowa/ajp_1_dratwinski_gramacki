import requests
import json
import os

CLARIN_URL = "http://ws.clarin-pl.eu/nlprest2/base/process"

PATH_TO_RESULTS = "data" + os.path.sep + "results_from_taggers"


def get_tagging_from_morphoDita(text, output_filename):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({"text": text,
                          "lpmn": "morphoDita",
                          "user": "xxx@yyy.com"})

    response = requests.request("POST", CLARIN_URL, headers=headers, data=payload)

    xml = response.text.encode('utf8')
    output_file = open(PATH_TO_RESULTS + os.path.sep + f"{output_filename}_morphoDita.xml", "wb")
    output_file.write(xml)


def get_tagging_from_wcrft2(text, output_filename):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({"text": text,
                          "lpmn": "wcrft2",
                          "user": "xxx@yyy.com"})
    response = requests.request("POST", CLARIN_URL, headers=headers, data=payload)

    xml = response.text.encode('utf8')
    output_file = open(PATH_TO_RESULTS + os.path.sep + f"{output_filename}_wcrft2.xml", "wb")
    output_file.write(xml)


def get_tagging_from_krnnt(text, output_filename):
    response = requests.request("POST", "http://localhost:9003", data=text.encode('utf-8'))

    xml = response.text.encode('utf-8')
    output_file = open(PATH_TO_RESULTS + os.path.sep + f"{output_filename}_krnnt.xml", "wb")
    output_file.write(xml)

if __name__ == '__main__':
    text = open("data/poleval_tagging_task/test-raw.txt", "r", encoding="utf-8").read()

    get_tagging_from_krnnt(text, "pol_eval_test_raw")
    get_tagging_from_morphoDita(text, "pol_eval_test_raw")
    get_tagging_from_wcrft2(text, "pol_eval_test_raw")
