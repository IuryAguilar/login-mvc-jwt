from models.usuario_model import UsuarioModel
from services.auth_service import AuthService

usuario_model = UsuarioModel()
auth_service = AuthService()

usuario = usuario_model.buscar_por_email("joao@email.com")

senha_digitada = "auydqiv"

senha_correta = auth_service.verificar_senha(
    senha_digitada,
    usuario[3]
)

print(senha_correta)