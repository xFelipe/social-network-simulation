from fastapi import FastAPI
from social_network_simulation.schemas.utils import Message
from social_network_simulation.core.deps import setup_logging
from social_network_simulation.routes.v1 import router as v1_router

import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="API de simulação de rede social")
app.include_router(v1_router)


@app.get("/", response_model=Message)
async def root():
    logger.info("Olá mundo!!! :)")
    return {"message": "Olá mundo!"}
