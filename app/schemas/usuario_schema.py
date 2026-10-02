from pydantic import BaseModel

class Cadastro(BaseModel):
    nome: str
    email: str
    senha: str

class Login(BaseModel):
    email: str
    senha: str

class Perfil(BaseModel):
    nome: str
    email: str