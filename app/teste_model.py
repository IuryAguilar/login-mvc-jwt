from models.usuario_model import UsuarioModel

usuario_model = UsuarioModel()

resultado = usuario_model.buscar_por_email("teste@email.com")

print(resultado)