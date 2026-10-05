from app.exceptions import (
    UsuarioNaoEncontradoException,
    UsuarioJaCadastradoException,
    EmailOuSenhaInvalidoException
    )

class UsuarioService:
    def __init__(self, usuario_model, auth_service):
        self.usuario_model = usuario_model
        self.auth_service = auth_service

    def cadastrar_usuario(self, nome, email, senha):
        usuario = self.usuario_model.buscar_por_email(email)

        if usuario:
            raise UsuarioJaCadastradoException(
                "E-mail já cadastrado."
            )
        
        hash_senha = self.auth_service.gerar_hash_senha(senha)

        self.usuario_model.criar_usuario(
            nome,
            email,
            hash_senha
        )

        return True

    def logar_usuario(self, email, senha):
        usuario = self.usuario_model.buscar_por_email(email)

        if not usuario:
            raise EmailOuSenhaInvalidoException(
                "E-mail ou senha inválidos."
            )

        senha_verificada = self.auth_service.verificar_senha(
            senha,
            usuario[3]
        )

        if not senha_verificada:
            raise EmailOuSenhaInvalidoException(
                "E-mail ou senha inválidos."
            )

        token = self.auth_service.gerar_token(usuario[0])

        return token

    def buscar_usuario_por_id(self, usuario_id):
        usuario = self.usuario_model.buscar_por_id(usuario_id)

        if not usuario:
            raise UsuarioNaoEncontradoException(
                "Usuário não encontrado."
            )

        return usuario
