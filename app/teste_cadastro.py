from models.usuario_model import UsuarioModel
from services.auth_service import AuthService


usuario_model = UsuarioModel()
auth_service = AuthService()

senha = "123456"

hash_senha = auth_service.gerar_hash_senha(senha)

usuario_model.criar_usuario(
    "João",
    "joao@email.com",
    hash_senha
)

print("Usuário cadastrado!")