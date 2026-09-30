from app.database.database import conectar_banco

class UsuarioModel:
    def buscar_por_email(self, email):
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, email, senha FROM usuarios WHERE email = %s",
            (email,)
        )

        usuario = cursor.fetchone()

        cursor.close()
        conexao.close()

        return usuario

    def criar_usuario(self, nome, email, senha):
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO usuarios (nome, email, senha)
            VALUES (%s, %s, %s)
            """,
            (nome, email, senha)
        )

        conexao.commit()

        cursor.close()
        conexao.close()