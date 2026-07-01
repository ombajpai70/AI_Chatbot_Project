from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.models import (
    ChatRequest,
    ChatResponse
)
from api.upload import router as upload_router
from services.router import route_question


app = FastAPI(
    title="AI ERP Assistant(OM)",
    version="1.0"
)

app.include_router(upload_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    answer = route_question(
        request.question
    )

    return ChatResponse(
        answer=answer
    )
