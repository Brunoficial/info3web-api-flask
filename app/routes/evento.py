from flask import Blueprint, request, jsonify
from ..models import Evento
from ..config.db import db
from ..repositories import eventoRepository
from ..utils import *

eventoBP = Blueprint("evento", __name__, url_prefix="/eventos")

@eventoBP.route("/listar", methods=['GET'])
def listar_eventos():
    eventos_do_banco = eventoRepository.listar_eventos()
    
    eventos = serializar_itens(eventos_do_banco)
    if not eventos:
        return jsonify(""), 204
    
    return jsonify(eventos)

@eventoBP.route("/criar", methods=["POST"])
def criar_eventos():
    data = request.get_json()
    if validar_dados(data, Evento.campos_obrigatorios()) == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    novoEvento = Evento(data)

    eventoRepository.save(novoEvento)
    return jsonify({"message":"Evento criado com sucesso!"}), 200

@eventoBP.route("/deletar", methods=["DELETE"])

@eventoBP.route("/deletar/<int:id>", methods=["DELETE"])
# @jwt_required()
def deletar_evento(id):
    evento = eventoRepository.find_by_id(id)

    if not evento:
        return jsonify({"error": "Nenhum evento encontrado"}), 404
    
    eventoRepository.delete(evento)
    return jsonify({"message": "Evento deletado com sucesso"}), 200



@eventoBP.route("/atualizar/<int:id>", methods=["PATCH"])
# @jwt_required()
def atualizar_evento(id):
    evento = eventoRepository.find_by_id(id)

    if not evento:
        return jsonify({"error": "Nenhum evento encontrado"}), 404
    
    data = request.get_json()
    if validar_dados(data, Evento.campos_obrigatorios()) == False:
        return jsonify({"error": "Preencha os campos obrigatórios"}), 400

    if not editar_dados(Evento.campos_editaveis(), data, evento):
        return {"message": "Evento não alterado"}, 200

    eventoRepository.save(evento)

    return jsonify({"message": "Evento atualizado com sucesso"}), 200

