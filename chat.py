#! /bin/env python3
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

message_history = []

def sabumuntonicola(message, history):
    load_dotenv()

    print(message)
    print(history)

    message_history.append(message)
    content_message = "\n".join(message_history)

    chat = ChatOpenAI()

    messages = [
        SystemMessage(
            content="voçê é um chatbot simples que deve ser capaz de inserir frases sintetização de forma contínua, sem precisar reinicializar a aplicação cada vez que precisar inserir uma frase. "
        ),
        HumanMessage(
            content=content_message
        ),
    ]

    return(chat(messages))

def main ():
    chatbeto = gr.ChatInterface(sabumuntonicola)
    chatbeto.launch()

if __name__ == "__main__":
    main()