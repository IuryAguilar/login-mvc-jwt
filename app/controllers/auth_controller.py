from app.models.usuario_model import UsuarioModel
from app.services.auth_service import AuthService
from app.schemas.usuario_schema import Perfil
from app.exceptions import UsuarioNaoEncontradoException

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
                "mensagem": "Usuário cadastrado com sucesso."
            }

    def login_usuario(self, email, senha):
        usuario = self.usuario_model.buscar_por_email(email)

        if not usuario:
            return {
                "sucesso": False,
                "mensagem": "E-mail ou senha inválidos."
            }

        senha_verificada = self.auth_service.verificar_senha(
            senha,
            usuario[3]
        )

        if not senha_verificada:
            return {
                "sucesso": False,
                "mensagem": "E-mail ou senha inválidos."
            }

        token = self.auth_service.gerar_token(usuario[0])

        return {
            "sucesso": True,
            "token": token,
            "mensagem": "Login bem-sucedido"
        }

    def obter_perfil(self, usuario_id):
        perfil_usuario = self.usuario_model.buscar_por_id(usuario_id)

        if not perfil_usuario:
            raise UsuarioNaoEncontradoException(
                "Usuário não encontrado."
            )

        perfil = Perfil(
            nome = perfil_usuario[0],
            email = perfil_usuario[1]
        )

        return perfil