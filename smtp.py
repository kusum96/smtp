import requests
import json


def send_sms(number, message):
	url = 'https://www.fast2sms.com/dev/bulk'
	params={
		'authorization':'MmH1tCQvDuf9ZdKVopYFBqN4yTSiRsWxah6gczL8GPO72A3ejXxKgJy4HqWSfb5vDlEG2sX9iFmMz683',
		'sender_id':'FSTSMS',
		'message': message,
		'language':'english',
		'route':'p',
		'numbers': number
	}

	response=requests.get(url, params=params)
	dic=response.json()
	print(dic)


send_sms("8669192794" , "this is first smtp message")