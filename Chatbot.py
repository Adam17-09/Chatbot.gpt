import openai

openai.api_key = "sua-chave-da-OpenAI"

def chatbot(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}]
    )
    return resposta.choices[0].message.content.strip()

pergunta = input("Você: ")
print("Bot:", chatbot(pergunta))
