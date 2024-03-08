from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from use_ai import main

app = FastAPI()

class Item(BaseModel):
    answer : bool
    chat : str

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/chat/")
async def chat(item:Item):
    prompt = item.chat

    if item.answer == True:
    # 会話履歴を読み込み、ユーザーのプロンプトを追加
        with open(f"./use_ai/chat_history.pickle", 'rb') as f:
            messages = pickle.load(f)
        messages.append({"role": "user", "content": prompt})
    elif item.answer == False:
        # 新しい会話を開始
        messages = [{"role": "system", "content": "あなたは優秀なAIアシスタントです。"},
                {"role": "user", "content": prompt}
    ]

    response = main.chat(messages)
    return {"Ai",response}
    