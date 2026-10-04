from app.schemas.usuario_schema import Perfil
from app.exceptions import UsuarioNaoEncontradoException

class AuthController:
    def __init__(self, usuario_model, auth_service, usuario_service):
        self.usuario_model = usuario_model
        self.auth_service = auth_service
        self.usuario_service = usuario_service
    
    def cadastro_usuario(self, nome, email, senha):
        resultado = self.usuario_service.cadastrar_usuario(
            nome,
            email,
            senha
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