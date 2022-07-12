import requests
import json

config = json.loads(str(open('config.json').read()))



def getPassingTrains(station):
    reqUrl = "https://transportapi.com/v3/uk/train/station/"+station+"/live.json?app_id="+config['appId']+"&app_key="+config['appKey']+"&darwin=true&train_status=passenger&type=pass"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "TrainTTS Client" 
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    return response

def getDepartingTrains(station):
    reqUrl = "https://transportapi.com/v3/uk/train/station/"+station+"/live.json?app_id="+config['appId']+"&app_key=7995a63fce1941ee469c3a3e5dda54c5&darwin=true&train_status=passenger"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "TrainTTS Client" 
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    return response

