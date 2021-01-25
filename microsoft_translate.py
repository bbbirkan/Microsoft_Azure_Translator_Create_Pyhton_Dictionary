import requests, uuid, json,time
try:
    with open("azure_english.json", "r") as jsonFile:
        data = json.load(jsonFile)   
except:
    pass 
subscription_key = "take api key number and paste here" #web page =https://docs.microsoft.com/en-us/azure/cognitive-services/translator/?WT.mc_id=python-10851-chrhar
endpoint = "https://api.cognitive.microsofttranslator.com"

location = "write api location here"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['tr']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
f = open("source.txt", "r")
for line in f:
    time.sleep(1)
    line=str(line)
    line=line.replace("\n","")
    body = {
        'text':line
    }
    key = (body['text'])
    body = [body]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)

    response = request.json()

    response = str(response)
    response = response[29:-17]
    data[key] = response

    with open("azure_english.json", "w") as ok:
        json.dump(data, ok, ensure_ascii=False, indent=1)




