import os
import requests
from dotenv import load_dotenv
load_dotenv()

accessToken = os.environ.get("ACCESS_TOKEN")
endpoint = os.environ.get("ENDPOINT")
headers = {"Authorization": f"Bearer {accessToken}"}

report_data_query="""{
   getReportData(reportID: 149)
}"""


# r = requests.post(endpoint, json={"query": report_data_query}, headers=headers)
report_data = requests.post(endpoint, json={'query': report_data_query}, headers=headers)
if report_data.status_code == 200:
    print(report_data.json())
else:
    raise Exception(f"Query failed to run with a {r.status_code}.")