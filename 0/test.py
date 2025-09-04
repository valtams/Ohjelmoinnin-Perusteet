from creds import appID, aat
import requests as req
import json
helix = "https://api.twitch.tv/helix"
userInput = input("Enter Channel Name > ")
url = helix + "/users?login=" + userInput
headers = {"Client-id":appID,
           "Authorization":aat}
resp = req.get(url, headers=headers)
data = resp.json()["data"][0]["id"]
print(userInput+"s userID is " + data)
