import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

ORG = "design07"
PROJECT = "Quantum"
PAT = os.getenv("ADO_PAT")

def get_pipeline_id(pipeline_name):

    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/pipelines?api-version=7.0"

    response = requests.get(
        url,
        auth=HTTPBasicAuth('', PAT)
    )

    pipelines = response.json()["value"]

    for p in pipelines:
        if p["name"].lower() == pipeline_name.lower():
            return p["id"]

    return None


def get_pipeline_runs(pipeline_id):

    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/build/builds?definitions={pipeline_id}&api-version=7.0"

    response = requests.get(
        url,
        auth=HTTPBasicAuth('', PAT)
    )

    builds = response.json()["value"]

    return builds[:3]