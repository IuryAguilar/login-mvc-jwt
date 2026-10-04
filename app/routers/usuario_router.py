from fastapi import APIRouter, Depends
from app.schemas.usuario_schema import Perfil
from app.dependencies.auth_dependencies import verificar_autenticacao
from app.dependencies.dependencies import obter_auth_controller
from app.controllers.auth_controller import AuthController

router = APIRouter()

@router.get("/perfil", response_model = Perfil)
def perfil(
    usuario: dict = Depends(verificar_autenticacao),
    auth_controller: AuthController = Depends(obter_auth_controller)
    ):
    usuario_id = usuario["sub"]

    perfil_usuario = auth_controller.obter_perfil(usuario_id)

    return perfil_usuario