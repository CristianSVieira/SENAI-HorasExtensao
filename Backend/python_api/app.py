from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API rodando 🚀"}

@app.get("/teste")
def teste():
    return {"status": "ok", "mensagem": "Endpoint funcionando!"}