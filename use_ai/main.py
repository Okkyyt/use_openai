
import pickle
from openai import OpenAI
client = OpenAI()

def chat(messages):
    # OpenAIのAPIを呼び出し、与えられたメッセージに対する応答を取得
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    response = completion.choices[0].message.content
    # 応答を保存
    save_chat(messages=messages, new_message={'role':'assistant', 'content':response})
    return response

def save_chat(messages, new_message):
    # 新しいメッセージを追加し、チャット履歴をファイルに保存
    messages.append(new_message)
    with open(f"./use_ai/chat_history.pickle", "wb") as f:
        pickle.dump(messages, f)