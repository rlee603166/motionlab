from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth
import requests
import pandas as pd
import struct
import json

token = "OgOQzAz8VTochFQIAin3zPY5msGCShPC"

folder_id = 277583061491
offset=10
url = "https://api.box.com/2.0/files/{file_id}/content"
headers = {'Authorization': f'Bearer {token}'}

with open("shoulder.json", "r") as f:
    cache = json.load(f)

def save(cache, index):
    file_path = f"shoulder-{int(index/100)+1}.json"
    with open(file_path, 'w') as json_file:
        json.dump(cache, json_file)

for i in range(0, len(cache), 100):
    chunk = cache[i:i+100]
    save(chunk, i)


# def get_file(file):
#     print(file['id'])
#     response = requests.get(url.format(file_id=file['id']), headers=headers, stream=True)
#
#     print("got file")
#     if response.status_code == 200:
#         with open(file['name'], 'wb') as f:
#             for chunk in response.iter_content(chunk_size=8192): 
#                 f.write(chunk)
#         print(f"File downloaded successfully: {file['name']}")
#     else:
#         print(f"Error downloading file: {response.status_code}, {response.text}")
#
# test_file = {
#     "type": "file",
#     "id": "1808270002917",
#     "file_version": {"type": "file_version", "id": "1993173222117", "sha1": "478a20a0bd0c97eb87a9ddc74e53fc24df74e18e"},
#     "sequence_id": "0", "etag": "0", "sha1": "478a20a0bd0c97eb87a9ddc74e53fc24df74e18e", "name": "C0030Pre00leftdrink_1_Database_Export.xlsx"
# }
#
# get_file(test_file)
# cache = []
#
# def save(cache):
#     file_path = "shoulder.json"
#     with open(file_path, 'w') as json_file:
#         json.dump(cache, json_file)
#
# count = 0
# while True:
#     response = requests.get(url.format(folder_id=folder_id, offset=count+1), headers=headers)
#     data = response.json()
#     for item in data["entries"]:
#         if not item['name'].endswith(".xlsx"):
#             continue 
#
#         cache.append(item)
#         print(f"count: {count}, file: {item['name']}")
#         count+=1
#
#
#     print(f"file count: {len(cache)}")
#     save(cache)
#     print("shoulder successfully saved")
#
#     if len(data) == 0: break
#
# print("down")
