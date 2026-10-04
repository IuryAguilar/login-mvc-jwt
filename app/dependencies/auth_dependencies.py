from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.auth_service import AuthService

bearer_scheme = HTTPBearer()

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