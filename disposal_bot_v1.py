import requests
from time import sleep

url = "https://api.telegram.org/bot739295476:AAHQrEtoLvDjep9giolxCudH9PajKN4hmI0/"


def get_updates_json(request):
	params = {'timeout': 100, 'offset': None}
	response = requests.get(request + 'getUpdates', data=params)
	return response.json()


def last_update(data):
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]


def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id


def send_mess(chta, text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

# версия 1
# chat_id = get_chat_id(last_update(get_updates_json(url)))
# send_mess(chat_id, 'Ypur message goes here')

# версия 2
def main():
	update_id = last_update(get_updates_json(url))['update_id']
	while true:
		if update_id == last_update(get_updates_json(url))['update_id']
		send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
		update_id += 1
	sleep(1)

if __name__ == '__name__':
	main()