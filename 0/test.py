from creds import appID, aat
import requests as req
import json
helix = "https://api.twitch.tv/helix"
userInput = input("Enter Channel Name > ")
url = helix + "/users?login=" + userInput
headers = {"Client-id":appID,
           "Authorization":aat}

response = req.get(url, headers=headers)
response.raise_for_status()
data = response.json()
print(data["data"][0]["id"])
