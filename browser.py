import sys
import os
from _collections import deque
import requests
from bs4 import BeautifulSoup
import colorama

args = sys.argv
dir_name = args[1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

my_stack = deque()
# dir_name = 'test'
# # os.mkdir('test')

user_input = input()
tag_lists = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',  'a', 'ul', 'ol', 'li']
while user_input != 'exit':
    if user_input.find('.') != -1:
        if user_input[:4] != 'back' and user_input[:4] != 'http':
             user_input = 'https://' + user_input
        r = requests.get(user_input)
        soup = BeautifulSoup(r.content, 'html.parser')
        whole_text = ''
        for item in tag_lists:
            tag = soup.find_all(item)
            for i in tag:
                if item == 'ul' or item == 'ol' or item == 'li':
                    print(colorama.Fore.BLUE + i.get_text())
                else:
                    print(i.get_text())
                whole_text += i.get_text() + '\n'

        slash = user_input.find('//')
        dot = user_input.rfind('.')
        file_name = user_input[slash + 2: dot] + '.txt'
        with open(dir_name +'/'+ file_name, 'w', encoding='UTF-8') as file:
            # file.write(r.text)
            file.write(whole_text.rstrip())

        my_stack.append(user_input)

    elif user_input == 'back':
        my_stack.pop()
        user_input = my_stack[-1]
        continue
    else:
        file_name = user_input +'.txt'
        try:
            with open(dir_name + '/' + file_name) as file:
                print(file.read())
        except OSError:
            print('error addtess')

    # else:
    #     print('error address')
    user_input = input()

