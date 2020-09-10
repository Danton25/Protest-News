
import requests
import json

payload = {
                "key": "free",
                "id": "5S2Q5x8K",
                "data": {
    "text": "On 31 December, an unidentified group vandalized an ABSU office in Rupohi (Baksa district, Assam). The group also attacked six office-bearers that were inside the office room. However, they managed to escape from the scene.",
    "classes": [
        "peaceful protest",
        "riot",
        "violent protest",
        "silent protest",
        "operation",
        "hunger protest",
        "salary protest"

    ],
    "minCutOff": "0.2",
    "model": "model1"
}
        }

headers = {'content-type': 'application/json'}

response = requests.post("https://macgyver.services", data=json.dumps(payload), headers=headers)

print(response.text)