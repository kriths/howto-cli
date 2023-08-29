#!/usr/bin/env python3
import sys
from getpass import getpass
from os import path

import requests

API_KEY_FILE_NAME = "API_KEY"
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-3.5-turbo"


messages = [
    {
        "role": "system",
        "content": "You are an AI assistant called from the command line of a computer. Most likely, the user will have a technical question and expects a technical response.",
    },
]


def get_api_key_file_path() -> str:
    script_dir = path.dirname(path.realpath(__file__))
    return path.join(script_dir, API_KEY_FILE_NAME)


def read_api_key() -> str:
    api_key_path = get_api_key_file_path()
    assert path.isfile(api_key_path), f"Missing \"{API_KEY_FILE_NAME}\" file in project directory"
    with open(api_key_path, "r") as api_key_file:
        return api_key_file.read().strip()


def send_message_for_response(message: str) -> str:
    messages.append({
        "role": "user",
        "content": message,
    })

    api_key = read_api_key()
    body = {
        "model": OPENAI_MODEL,
        "messages": messages
    }
    resp = requests.post(OPENAI_ENDPOINT,
                         headers={"Authorization": f"Bearer {api_key}"},
                         json=body)
    response_text = resp.json()["choices"][0]["message"]["content"]
    messages.append({
        "role": "assistant",
        "content": response_text
    })

    return response_text


def start_session():
    messages.append({
        "role": "system",
        "content": "Answer concisely, without introduction and only provide an explanation when asked.",
    })
    while True:
        try:
            question = input("» ")
            response = send_message_for_response(question)
            print(f"« {response}")
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)


def set_api_key():
    api_key = getpass("Enter API key (masked): ").strip()
    with open(get_api_key_file_path(), "w") as f:
        f.write(api_key)
        print("API key stored")


def send_single_question_for_response(query: str):
    messages.append({
        "role": "system",
        "content": "You must answer as concisely as possible. Answer only with the requested command without any introduction or explanation.",
    })
    question = f"On Arch Linux, what is the command line command to {query}?"
    print(f"» {question}")
    response = send_message_for_response(question)
    print(f"« {response}")


if __name__ == "__main__":
    query = " ".join(sys.argv[1:])
    if query == "-i":
        start_session()
    elif query == "-c":
        set_api_key()
    else:
        send_single_question_for_response(query)
