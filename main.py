import requests, json

token = 'secret_MgcEqo3nB76F2qvDBZJYX4mq1nXmItk5mkS28N3R1z4'

databaseId = '3b25c883c14948f38fe47a64cb3069db'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers, verify = False)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

def updatePage(pageId, headers):
    print(headers)
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {
          "Status": {
            "status": {
              "name": "done",  
              "color": "green"            
            }
          },   
        }
    }

    data = json.dumps(updateData)
    print(data)
    response = requests.patch(url=updateUrl, headers=headers, data=data, verify = False)

    print(response.status_code)
    print(response.text)


updatePage("912963d6-c9f7-48b5-b1f6-952544b782d7", headers)