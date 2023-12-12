from fastapi import FastAPI
from pydantic import BaseModel

class GreetingModel(BaseModel):
    texts: str

app = FastAPI()

@app.post('/send_greetings')
async def send_data(text: GreetingModel):
    print(text.texts)
    return{"status":200} 
    GeneratorExit