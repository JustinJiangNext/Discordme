import requests
import json

class Account:
     def __init__(self:str, token):
          self.token:str = token

     #If message is sent successful, the return is the sent message ID, if failed it will return a message starting with "False" + the reason why it failed
     def send_message(self, message: str, channel_ID:str) -> str:
          message_data:dict = {"content": message, "tts": "false"}
          sentStatus:str = "NULL"
          header_data:dict = { 
               "content-type": "application/json", 
               "user-agent": "chrome", 
               "authorization": self.token, 
               "host": "discord.com", 
               "referer": channel_ID
          }
  
          try: 
               #myconn = self.get_connection()
               #myconn.request("POST", f"/api/v9/channels/{channel_ID}/messages", json.dumps(message_data), header_data) 
               #resp = myconn.getresponse() 

               resp = requests.post(f"https://discord.com/api/v9/channels/{channel_ID}/messages", 
                                   headers = header_data, 
                                   data = json.dumps(message_data))

               if 199 < resp.status_code < 300: 
                    sentStatus = resp.json()["id"]
               else:
                    sentStatus = f"False Received HTTP {resp.status_code}: {resp.reason}\n"


          except Exception as e: 
               sentStatus = f"False other error: {str(e)}"

          return sentStatus
     

