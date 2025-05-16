# -*- coding: utf-8 -*-
!pip install google-genai

#importando a chave criada no google Ai Studio
import os

from google.colab import userdata
os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

from google import genai

client = genai.Client()

for model in client.models.list():
  print(model.name)

modelo = "models/gemini-2.0-flash"
response = client.models.generate_content(model=modelo, contents="Qual a empresa responsável pelo Gemini?")

response.text

from google.genai import types

chat_config = types.GenerateContentConfig(system_instruction="Você é um assistente pessoal e você sempre responde de forma sucinta.")
chat = client.chats.create(model=modelo, config=chat_config)
#resposta = chat.send_message("Qual a empresa responsável pelo Gemini?")
#resposta.text

prompt = input("Digite sua pergunta: ")

while prompt	!= "sair":
  resposta = chat.send_message(prompt)
  print(resposta.text)
  prompt = input("Digite sua pergunta: ")

# @title
chat.get_history
