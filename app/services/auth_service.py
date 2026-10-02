import bcrypt
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime, timedelta, timezone

load_dotenv()

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

    def gerar_token(self, usuario_id):
        secret = os.getenv("JWT_SECRET")
        algorithm = os.getenv("JWT_ALGORITHM")
        agora = datetime.now(timezone.utc)
        expiracao = agora + timedelta(minutes = 30) 

        payload = {
            "sub": str(usuario_id),
            "iat": agora,
            "exp": expiracao
        }

        token = jwt.encode(
            payload,
            secret,
            algorithm
        )

        return token

    def validar_token(self, token):
        secret = os.getenv("JWT_SECRET")
        algorithm = os.getenv("JWT_ALGORITHM")

        try:
            token_validado = jwt.decode(
                token,
                secret,
                [algorithm]
            )
            return token_validado

        except jwt.ExpiredSignatureError:
            return "expirado"
        
        except jwt.InvalidTokenError:
            return False