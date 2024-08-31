from fastapi import FastAPI
from social_network_simulation.modules.schemas import Message


app = FastAPI(title="API de simulação de rede social")


@app.get("/", response_model=Message)
async def root():
    print("ASD")
    return {"message": "Olá mundo!"}
