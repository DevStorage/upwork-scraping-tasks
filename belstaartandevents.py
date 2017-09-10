import json
import urllib.request
import progressbar
from time import sleep
import os.path


json_urls = [
    'https://progallerycdn.wix.com/_api/pro-gallery-webapp/v1/gallery/e59c31b8-2f06-41b5-9a89-35caaa1503d2/81578bc8-ce53-b7fe-e1b7-a4a11cd1bfaf/items/from/0/to/200?instance=aULyZbXUoe_hLZn4qu6EONlkop6H9fPU6v1oAc2pMlY.eyJpbnN0YW5jZUlkIjoiOGQ3OTRjMzItNjYwNC00N2JhLWIxZDItZmQyN2M5Zjc1YjVlIiwiYXBwRGVmSWQiOiIxNDI3MWQ2Zi1iYTYyLWQwNDUtNTQ5Yi1hYjk3MmFlMWY3MGUiLCJzaWduRGF0ZSI6IjIwMTctMDktMTBUMTU6MjM6MzYuMDk0WiIsInVpZCI6bnVsbCwiaXBBbmRQb3J0IjoiMjEyLjExNS4yNTIuMjAyLzQ3ODU4IiwidmVuZG9yUHJvZHVjdElkIjpudWxsLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI4ZmFiNmMwYy1lY2Y4LTQwNjQtYTljYS00NTlhN2E1ODdmYTciLCJhaWQiOiJlZWUwMTA1Ny0zY2UyLTRkZmItOGNhMi1mNWQyN2Q5MGE3MDYiLCJiaVRva2VuIjoiOTdhMzM4NmItMjA1OS0wZGRkLTNlMTgtYmYzMDAxNWQ5ZWRmIiwic2l0ZU93bmVySWQiOiJjNTk5NDA3YS1kYjU1LTQzY2QtYTI0Zi04ZmViYjk2NjQ3YjQifQ',
    'https://progallerycdn.wix.com/_api/pro-gallery-webapp/v1/gallery/8cf721e5-b50c-4951-a38c-51a2eeae0689/35ce318c-8144-2e73-ff56-dfe52774ff31/items/from/0/to/200?instance=wbAnbmLIT9qmauco5uSD6PxUOs7qA8B7t1XeeyF2e5c.eyJpbnN0YW5jZUlkIjoiZWZhYTEyMjctMGEyOS00NDE2LWIxNTItYWQyN2EwYTE4OTQ2IiwiYXBwRGVmSWQiOiIxNDI3MWQ2Zi1iYTYyLWQwNDUtNTQ5Yi1hYjk3MmFlMWY3MGUiLCJzaWduRGF0ZSI6IjIwMTctMDktMTBUMTU6Mjc6MTMuMTY4WiIsInVpZCI6bnVsbCwiaXBBbmRQb3J0IjoiMjEyLjExNS4yNTIuMjAyLzU1MDcyIiwidmVuZG9yUHJvZHVjdElkIjpudWxsLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI4ZmFiNmMwYy1lY2Y4LTQwNjQtYTljYS00NTlhN2E1ODdmYTciLCJhaWQiOiJjYTdhMmU2ZS1hNjZkLTRlZTktODVmYy01OTljNDZjNzY4NTIiLCJiaVRva2VuIjoiYmIxMDVmYTItOTVkMy0wNjQ3LTA2MDQtYWEzNDE0YWJiODEzIiwic2l0ZU93bmVySWQiOiJjNTk5NDA3YS1kYjU1LTQzY2QtYTI0Zi04ZmViYjk2NjQ3YjQifQ',
    'https://progallerycdn.wix.com/_api/pro-gallery-webapp/v1/gallery/60f6633f-c5a7-45aa-9647-e899c6b6d54c/955e725c-3356-133c-5802-0ab51374c153/items/from/0/to/200?instance=aege95UNvVc4sAf0Z6zAxZtrxYjkTu_7M2HZMvo0neM.eyJpbnN0YW5jZUlkIjoiMTY3MGE4Y2ItZTdhOS00YWMxLWI0N2EtOGUzNjcyZTg3MTk4IiwiYXBwRGVmSWQiOiIxNDI3MWQ2Zi1iYTYyLWQwNDUtNTQ5Yi1hYjk3MmFlMWY3MGUiLCJzaWduRGF0ZSI6IjIwMTctMDktMTBUMTU6MzA6NTYuNDE1WiIsInVpZCI6bnVsbCwiaXBBbmRQb3J0IjoiMjEyLjExNS4yNTIuMjAyLzQ1MjkyIiwidmVuZG9yUHJvZHVjdElkIjpudWxsLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI4ZmFiNmMwYy1lY2Y4LTQwNjQtYTljYS00NTlhN2E1ODdmYTciLCJhaWQiOiI4ZDI2ODczMC02ZWM0LTRkMjAtYTI0OC1mYTAxMzZiMmJlYjEiLCJiaVRva2VuIjoiZmIzZTg1ZGEtYzRiNC0wYmVlLTFlOTktMWJiMDAwMGI5YjQ2Iiwic2l0ZU93bmVySWQiOiJjNTk5NDA3YS1kYjU1LTQzY2QtYTI0Zi04ZmViYjk2NjQ3YjQifQ',
]
dwnl_url = 'https://static.wixstatic.com/media/'

bar = progressbar.ProgressBar().start()

for urls in json_urls:
    url = urllib.request.urlopen(urls)
    data = json.loads(url.read().decode())
    print('/full/path/to/pictures/ / at the end required')
    path = input()
    p_iter = 100/data['totalItemsCount']
    try:
        for i in range(data['totalItemsCount']):
            sleep(0.5)
            pict_url = dwnl_url + data['items'][i]['mediaUrl']
            filename = path + data['items'][i]['mediaUrl']
            if os.path.exists(filename) == True:
                print('\n File already exist')
                p_iter = p_iter + 100/data['totalItemsCount']
                bar.update(p_iter)
            else:
                urllib.request.urlretrieve(pict_url, filename)
                p_iter = p_iter + 100/data['totalItemsCount']
                bar.update(p_iter)
    except urllib.error.ContentTooShortError:
        sleep(1)
        pict_url = dwnl_url + data['items'][i]['mediaUrl']
        filename = path + data['items'][i]['mediaUrl']
        urllib.request.urlretrieve(pict_url, filename)
        p_iter = p_iter + 100/data['totalItemsCount']
        bar.update(p_iter)
