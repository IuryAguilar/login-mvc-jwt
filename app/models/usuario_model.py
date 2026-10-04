from app.database.database import conectar_banco

class UsuarioModel:
    def buscar_por_email(self, email):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha FROM usuarios WHERE email = %s",
                    (email,)
                )

                usuario = cursor.fetchone()

        return usuario

    def criar_usuario(self, nome, email, senha):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO usuarios (nome, email, senha)
                    VALUES (%s, %s, %s)
                    """,
                    (nome, email, senha)
                )

                conexao.commit()

    def buscar_por_id(self, usuario_id):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:

                cursor.execute(
                    "SELECT nome, email FROM usuarios WHERE id= %s",
                    (usuario_id,)
                    )
                
                usuario = cursor.fetchone()

        return usuario
