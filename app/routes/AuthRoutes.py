from flask import request, Blueprint
from ..services import AuthService

authBP = Blueprint("auth", __name__, url_prefix="/auth")

@authBP.route("/login", methods=["POST"])
def login():
    dados = AuthService.login(request.get_json())
    return dados


@authBP.route("/registro", methods=["POST"])
def registro():
    dados = AuthService.registro(request.get_json())
    return dados