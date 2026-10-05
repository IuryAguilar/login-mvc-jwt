from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import (
    UsuarioNaoEncontradoException,
    UsuarioJaCadastradoException,
    EmailOuSenhaInvalidoException
    )
from app.routers.auth_router import router as auth_router
from app.routers.usuario_router import router as usuario_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(usuario_router)

@app.exception_handler(UsuarioNaoEncontradoException)
def usuario_nao_encontrado_handler(request, exc):
    return JSONResponse(
        status_code = 404,
        content ={
            "detail": str(exc)
        }
    )

@app.exception_handler(UsuarioJaCadastradoException)
def usuario_ja_cadastrado_handler(request, exc):
    return JSONResponse(
        status_code = 400,
        content ={
            "detail": str(exc)
        }
    )

@app.exception_handler(EmailOuSenhaInvalidoException)
def email_ou_senha_invalido_handler(request, exc):
    return JSONResponse(
        status_code = 401,
        content ={
            "detail": str(exc)
        }
    )
