from os import system as terminal
from time import sleep
from datetime import datetime as date

terminal('clear && printf "\e[1;96m"')
terminal('''printf " ___            _ _
|_ _|_ ____   _(_) |_ ___ _ __
 | || '_ \ \ / / | __/ _ \ '__|
 | || | | \ V /| | ||  __/ |
|___|_| |_|\_/ |_|\__\___|_|\nСоздатель >> @Dently (Telegram)"''')
terminal('printf "\e[1;91m\n"')

from pyrogram import Client as client, idle as idle
from pyrogram.raw.functions.messages import GetAllChats as GetAllChats

app = client('invite')
app.start()
terminal('printf "\e[1;95m"')

chats = app.send(GetAllChats(except_ids=[777000])).chats
num = 0
ids = []
terminal('echo "\e[1;95mВыберите чат, с которого брать участников"')
for chat in chats:
	num += 1
	terminal('printf "\e[1;92m"')
	terminal('printf "[{}]" '.format(num))
	terminal('printf "\e[1;93m"') 
	ids.append(chat['id'])
	terminal('printf " {}\n"'.format(chat['title']))

option = ''
while not option:
	terminal('printf "\e[1;95m"')
	try:
		option = int(input('>> '))
		if option > num:
			option = ''
	except:
		option = ''
	
terminal('printf "\e[1;93mЗагрузка участников..."')
members = app.iter_chat_members(int(str(f'-100{ids[option-1]}')))

num = 0
print()
terminal('echo "\e[1;95mВыберите чат, куда добавлять участников"')
for chat in chats:
	num += 1
	terminal('printf "\e[1;92m"')
	terminal('printf "[{}]" '.format(num))
	terminal('printf "\e[1;93m"') 
	ids.append(chat['id'])
	terminal('printf " {}\n"'.format(chat['title']))

option = ''
while not option:
	terminal('printf "\e[1;95m"')
	try:
		option = int(input('>> '))
		if option > num:
			option = ''
	except:
		option = ''
		
for member in members:
	if f'{member.user.id}' != 'None':
		try:
			sleep(0.15)
			app.add_chat_members(int(str(f'-100{ids[option-1]}')), member.user.id)
			terminal(f"echo '\e[1;92m{member.user.id} успешно добавлен'")
		except Exception as exc:
			sleep(0.15)
			terminal(f"echo '\e[1;91m{member.user.id} не удалось добавить'")
	
idle()
