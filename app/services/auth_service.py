import bcrypt

class AuthService:
    def gerar_hash_senha(self, senha):
        senha_bytes = senha.encode("utf-8")

        hash_senha = bcrypt.hashpw(
            senha_bytes,
            bcrypt.gensalt()
        )

        return hash_senha.decode("utf-8")

    def verificar_senha(self, senha, hash_senha):
        senha_bytes = senha.encode("utf-8")
        hash_bytes = hash_senha.encode("utf-8")

        return bcrypt.checkpw(senha_bytes, hash_bytes)