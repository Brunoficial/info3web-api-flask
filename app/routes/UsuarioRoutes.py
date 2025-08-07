from ..services import UsuarioService
from flask import Blueprint

usuarioBP = Blueprint("usuario", __name__, url_prefix="/usuario")

@usuarioBP.route("/listar", methods=["GET"])
def listar_usuarios():
    return UsuarioService.listar_usuarios()

@usuarioBP.route("/encontrar_por_id/<int:id>", methodos=["GET"])
def encontrar_pelo_id(id):
    return UsuarioService.encontrar_pelo_id(id)

