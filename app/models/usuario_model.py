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

    def buscar_por_id(self, usuario_id):
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT nome, email FROM usuarios WHERE id= %s",
            (usuario_id,)
            )
        
        usuario = cursor.fetchone()

        cursor.close()
        conexao.close()

        return usuario
