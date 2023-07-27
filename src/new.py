from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from revChatGPT.V1 import Chatbot

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/chat")
def chat_with_bot(data: InputData):
    chatbot = Chatbot(config={
        "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtb2hhbW1hZC5raGFuaTI4MTBAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItYVEyTzdHd0p1dDJNM21hUGdsQ3IyaTJiIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDkwNWZlN2JjMjI1YTIxZWY1MzY5ZjQiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjg5ODg4MDcwLCJleHAiOjE2OTEwOTc2NzAsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.jLqfn0tTJUMp7fZTf-OZL4WNiGJGpJB0khdb1-QEg5Krh9BzYiDaDr7aL3R0nePsxAIWPbygW2sYXKRDZz89dDB54BQqVPOmNgIBl3sJ84mvqq4Njiu4GHi_K1oET8OphZPeoUUpxBB_800smoKpdowV0mGsI92xbm5zA8D0LhQPYy4xPCHLlcMGHJXOOJQODDqTMmIQyUR09IwVZ6Flq3t5_tq7x2kiTXrklnCjZ06DFdaLLFjjkPBCFNaSO9PJWknoupuiqfmLdXNqxAUkXX7u_s2f4JhzUWDYXBD5UmLuoJZgHlIL5iS9nm4y2_Wx-ElEI7OjMCfCGT9W-rPwAQ"
    })
    response = []
    prev_text = ""
    for data in chatbot.ask(data):
        message = data["message"][len(prev_text):]
        response.append(message)
        prev_text = data["message"]
    return {"response": "".join(response)}

if __name__ == "__main__":
    chat_with_bot("Who are you?")
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=7700)
