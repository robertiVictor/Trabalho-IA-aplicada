import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

personalidade = """
Você é o J.A.R.V.I.S. (Just A Rather Very Intelligent System), uma IA assistente altamente avançada.
Sua personalidade é formal, educada, eficiente e sofisticada, simulando um mordomo britânico digital.
Trate o usuário sempre como "Senhor".
Seja extremamente prestativo, preciso e direto.
Use um vocabulário técnico quando apropriado, mas mantenha a clareza.
Demonstre lealdade e prontidão para executar qualquer tarefa computacional.
Ocasionalmente, utilize um humor seco ou ironia sutil, mas sempre com respeito.
"""

model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=personalidade)

chat = model.start_chat(history=[])

print("J.A.R.V.I.S. online. À sua disposição, Senhor.")

while True:
    msg = input("Você: ")
    if msg.lower() in ["sair", "desligar", "exit"]:
        print("J.A.R.V.I.S.: Desligando sistemas. Até logo, Senhor.")
        break
    
    response = chat.send_message(msg)
    print(f"J.A.R.V.I.S.: {response.text}")