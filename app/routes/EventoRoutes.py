from flask import Blueprint, request
from ..services import EventoService
from flask_jwt_extended import jwt_required

eventoBP = Blueprint("evento", __name__, url_prefix="/eventos")

@eventoBP.route("/listar", methods=['GET'])
@jwt_required()
def listar_eventos():
    return EventoService.listar_eventos()

@eventoBP.route("/criar", methods=["POST"])
@jwt_required()
def criar_eventos():
    return EventoService.criar_eventos(request.get_json())

@eventoBP.route("/deletar/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar_evento(id):
    return EventoService.deletar_evento(id)

@eventoBP.route("/editar/<int:id>", methods=["PATCH"])
@jwt_required()
def editar_evento(id):
    return EventoService.editar_evento(id, request.get_json())

