import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def delete_message(self , chat_id , MID):
        #https://api.telegram.org/botTOKEN/deleteMessage?chat_id=CID&message_id=MID
        params = {'chat_id': chat_id, 'message_id': MID}
        method = 'deleteMessage'
        resp = requests.post(self.api_url + method ,params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler("337200725:AAFbDoHN6Do7nZyW7F3X2EEYcLKh358gWDA")
#greetings = ('hello', 'hi', 'greetings', 'sup')
#now = datetime.datetime.now()


def main():
    new_offset = None
    #today = now.day
    #hour = now.hour


    greet_bot.get_updates(new_offset)

    last_update = greet_bot.get_last_update()

    last_update_id = last_update['update_id']
    #print(last_update_id)
    last_message_id = last_update['message']['message_id']
    print(last_message_id)
    last_chat_text = last_update['message']['text']
    print(last_chat_text)
    last_chat_id = last_update['message']['chat']['id']
    print(last_chat_id)
    last_chat_name = last_update['message']['from']['first_name']
    print(last_chat_name)
    #greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
    last_entity_type = last_update ['message']['entities'][0]['type']
    if last_entity_type=='url' :
        print('ok')
        greet_bot.delete_message(last_chat_id, last_message_id)
    print(greet_bot.delete_message(last_chat_id , last_message_id))
    #greet_bot.delete_message(last_chat_id, last_message_id)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
