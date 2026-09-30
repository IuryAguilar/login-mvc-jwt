from app.models.usuario_model import UsuarioModel
from app.services.auth_service import AuthService

class AuthController:
    def __init__(self):
        self.usuario_model = UsuarioModel()
        self.auth_service = AuthService()
    

    def cadastro_usuario(self, nome, email, senha):
        usuario = self.usuario_model.buscar_por_email(email)

        if usuario:
            return {
                "sucesso": False,
                "mensagem": "E-mail já cadastrado."
            }
        else:
            hash_senha = self.auth_service.gerar_hash_senha(senha)

            self.usuario_model.criar_usuario(
                nome,
                email,
                hash_senha
            )

            return {
                "sucesso": True,
                "mensagem": "Usuaário cadastrado com sucesso."
            }