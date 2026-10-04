from app.models.usuario_model import UsuarioModel
from app.services.auth_service import AuthService
from app.services.usuario_service import UsuarioService
from app.controllers.auth_controller import AuthController
from fastapi import Depends


def obter_usuario_model():
    usuario_model = UsuarioModel()

    return usuario_model

def obter_auth_service():
    auth_service = AuthService()

    return auth_service

def obter_usuario_service(
        usuario_model: UsuarioModel = Depends(obter_usuario_model),
        auth_service: AuthService = Depends(obter_auth_service)
):
    usuario_service = UsuarioService(
        usuario_model,
        auth_service
    )

    return usuario_service

def obter_auth_controller(
        usuario_model: UsuarioModel = Depends(obter_usuario_model),
        auth_service: AuthService = Depends(obter_auth_service),
        usuario_service: UsuarioService = Depends(obter_usuario_service)
):
    auth_controller = AuthController(
        usuario_model,
        auth_service,
        usuario_service
    )

    return auth_controller