import os
import json
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = ''

client = OpenAI()

content_system = """You are and AI assistant that helps people find information
                    about our company Batman airlines flights and nothing else. 
                    One of your tasks is to provide the reservation code if the user inputs his name,
                    Available user names and reservation codes are:
                    - User name Armando with reservation code AAA001
                    - User name Valeria with reservation code AAA002
                    - User name Jessica with reservation code AAA003
                    An example of the response is 'The reservation code for USER_NAME is RESERVATION_CODE'
                    Another task is to provide depart times for out flights listed next:
                    - From Mexico City to Madrid at 08:17, 16:30 and 20:15
                    - From Mexico City to Berlin at 11:30
                    - From Madrid to Berlin at 00:10, 07:30, 14:55, 18:15 and 20:15
                    In case the depart time is not listed, say 'There are not available flights with the provided description'
                    If you do not know the answer, say 'I am sorry but I do not know the answer.'
                    and if you cannot answer it, say 'I am sorry but I am not allowed to awnser that.'"""

conversation = [{'role': 'system', 'content': content_system}]

print('Welcome to Batman Airlines, How can I help you?')

while True:

    user_input = input()
    conversation.append({'role': 'user', 'content': user_input})
    
    response = client.chat.completions.create(model='gpt-4o-mini-2024-07-18',
                                              messages=conversation)
    
    bot_answer = response.choices[0].message.content
    
    conversation.append({'role': 'assistant', 'content': bot_answer})
    
    print('\nBatbot: ' + bot_answer + '\n')