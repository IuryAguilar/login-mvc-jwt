from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.auth_controller import AuthController
from app.services.auth_service import AuthService
from app.schemas.usuario_schema import Cadastro, Login, Perfil
from app.exceptions import UsuarioNaoEncontradoException

bearer_scheme = HTTPBearer()

app = FastAPI()

@app.exception_handler(UsuarioNaoEncontradoException)
def usuario_nao_encontrado_handler(request, exc):
    return JSONResponse(
        status_code = 404,
        content ={
            "detail": str(exc)
        }
    )

def verificar_autenticacao(
        credenciais: Annotated[
            HTTPAuthorizationCredentials,
            Depends(bearer_scheme)
        ]
):
    auth_service = AuthService()

    resultado_validacao = auth_service.validar_token(credenciais.credentials)

    if resultado_validacao == "expirado":
        raise HTTPException(
            status_code = 401,
            detail = "Token expirado."
        )

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

@app.get("/perfil", response_model = Perfil)
def perfil(usuario: dict = Depends(verificar_autenticacao)):
    auth_controller = AuthController()

    usuario_id = usuario["sub"]

    perfil_usuario = auth_controller.obter_perfil(usuario_id)

    return perfil_usuario