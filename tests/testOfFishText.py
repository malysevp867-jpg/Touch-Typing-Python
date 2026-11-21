import requests
CountOfBUGS = 0
def requireText():
    url = "https://fish-text.ru/get"
    params = {
        "type": "sentence",
        "number": 1,
        "format": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        result = data["text"]
    else:
        print("The server is die or you don't have Internet")
    if "—" in result:
        global CountOfBUGS
        response = requests.get(url, params=params)
        print("BUG")
        CountOfBUGS += 1
for x in range(100):
    requireText()
print("Finished")
print(f"There is {CountOfBUGS} sentences with bug")