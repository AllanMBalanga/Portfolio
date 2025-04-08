import requests

URL = "http://127.0.0.1:5000/"          #URL from main.py

parameters = {}
title = input("Video title:")
views = int(input("Video views:"))
likes = int(input("Video likes:"))

if title: parameters["title"] = title
if views: parameters["views"] = views
if likes: parameters["likes"] = likes

response = requests.post(URL + "videos/3", parameters)               #comma after additional URL yung ilalagay na input in key-value pairings
print(response.json())
