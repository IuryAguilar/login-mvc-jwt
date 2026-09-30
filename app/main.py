from fastapi import FastAPI
from pydantic import BaseModel
from app.controllers.auth_controller import AuthController

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str

app = FastAPI()

@app.post("/cadastro")
def cadastro(usuario: Usuario):
    auth_controller = AuthController()

    resposta_cadastro = auth_controller.cadastro_usuario(
        usuario.nome,
        usuario.email,
        usuario.senha
    )

    return resposta_cadastro