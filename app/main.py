from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.auth_controller import AuthController
from app.services.auth_service import AuthService

bearer_scheme = HTTPBearer()

class Cadastro(BaseModel):
    nome: str
    email: str
    senha: str

class Login(BaseModel):
    email: str
    senha: str

app = FastAPI()

def verificar_autenticacao(
        credenciais: Annotated[
            HTTPAuthorizationCredentials,
            Depends(bearer_scheme)
        ]
):
    auth_service = AuthService()

    resultado_validacao = auth_service.validar_token(credenciais.credentials)

    if not resultado_validacao:
        raise HTTPException(
            status_code = 401,
            detail = "Token inválido."
        )

    return resultado_validacao

@app.post("/cadastro")
def cadastro(usuario: Cadastro):
    auth_controller = AuthController()

    resposta_cadastro = auth_controller.cadastro_usuario(
        usuario.nome,
        usuario.email,
        usuario.senha
    )

    return resposta_cadastro

@app.post("/login")
def login(usuario: Login):
    auth_controller = AuthController()

    resposta_login = auth_controller.login_usuario(
        usuario.email,
        usuario.senha
    )

    return resposta_login

@app.get("/perfil")
def perfil(usuario: dict = Depends(verificar_autenticacao)):
    return usuario