from app.exceptions import UsuarioJaCadastradoException

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