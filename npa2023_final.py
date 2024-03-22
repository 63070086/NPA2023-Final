import requests
import json
import time
import netconf_final

accessToken = "Bearer MzE0YjcyMjktMGRmZC00MGFkLTg2ZWUtMWVmMWUxYzExZDc0ZWEyMzVkMTgtYjgy_P0A1_a61a0b2b-feba-43a3-8a20-e8cc10a43c9a"

roomIdToGetMessages = (
    "Y2lzY29zcGFyazovL3VzL1JPT00vZjBkZjY0NDAtYWU5Yi0xMWVlLTg5MGMtMGQzNjUwOTJlMmUy"
)

# room test
#Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzVmNGE1YjAtZTdhZC0xMWVlLWIyNjEtNDczYWNhMmVjYzEy

#room NPA
#Y2lzY29zcGFyazovL3VzL1JPT00vZjBkZjY0NDAtYWU5Yi0xMWVlLTg5MGMtMGQzNjUwOTJlMmUy

while True:
    time.sleep(1)

    getParameters = {"roomId": roomIdToGetMessages, "max": 1}

    getHTTPHeader = {"Authorization": accessToken}

    r = requests.get(
        "https://webexapis.com/v1/messages",
        params=getParameters,
        headers=getHTTPHeader,
    )

    if not r.status_code == 200:
        raise Exception(
            "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
        )

    json_data = r.json()

    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")

    messages = json_data["items"]

    message = messages[0]["text"]
    print("Received message: " + message)

    if message.find("/") == 0:

        # extract the command
        command = message[message.find(" ")+1:]
        print(command)

        if command == "create":
            responseMessage =  netconf_final.create()
        elif command == "delete":
            responseMessage =  netconf_final.delete()
        elif command == "enable":
                responseMessage =  netconf_final.enable()
        elif command == "disable":
            responseMessage =  netconf_final.disable()
        elif command == "status":
            responseMessage =  netconf_final.status()
        else:
            responseMessage = "Error: No command or unknown command"

        postHTTPHeaders = HTTPHeaders = {"Authorization": accessToken, "Content-Type": "application/json"}

        postData = {"roomId": roomIdToGetMessages, "text": responseMessage}

        r = requests.post(
            "https://webexapis.com/v1/messages",
            data=json.dumps(postData),
            headers=postHTTPHeaders,
        )
