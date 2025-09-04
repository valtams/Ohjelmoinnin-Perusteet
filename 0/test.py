import requests as req
import json
import creds
helix = "https://api.twitch.tv/helix"
appID = creds.appID
uat = creds.uat

url = helix + "/users?id=31239503"
headers = {"Client-id":appID,
           "Authorization":uat}

response = req.get(url, headers=headers)
response.raise_for_status()
data = response.json()
print(data["data"][0]["display_name"])
