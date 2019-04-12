import requests  
import datetime
from time import sleep
token="843678390:AAHGey2kE0Bj-EyLn-CHPCQfk8ehxjTw5fA"

url="https://api.telegram.org/bot{}/".format(token)


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.proxy = {"https":"https://104.248.168.59:8080"}

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        #resp = requests.get(self.api_url + method, params,proxies=self.proxy) # c proxy
        resp = requests.get(self.api_url + method, params)

        result_json = resp.json()['result']
        print("result_json=",result_json)
        print("\n")
    
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        #resp = requests.post(self.api_url + method, params,proxies=self.proxy) # proxy
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
  
        
        print("get_result[len(get_result)=",len(get_result))
       
        if len(get_result) > 0:
            last_update = get_result[-1]
            print("last update>0")

        else:
            last_update = get_result[len(get_result)]
            print("last update !0")

        return last_update




greet_bot = BotHandler(token)
new_offset = None

#while True:
##greet_bot.get_updates(new_offset)
##last_update = greet_bot.get_last_update()
##last_update_id = last_update['update_id']
##new_offset = last_update_id + 1
##greet_bot.get_updates(new_offset)    

#params = {'timeout': 30, 'offset': None}
params = {'timeout': 5 , 'offset': 205428760 }
method = 'getUpdates'
response = requests.get(url + method, params)
result_out_json = response.json()
print("resule_json_1=",result_out_json)

##вопросы
##1 если вызвали функцию и не присвоили значение, то оно все равно сохраняется?
##2 данный кусок кода заменяет предыдущий полностью что ли ? 
## изменения

