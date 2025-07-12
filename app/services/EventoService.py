from flask import jsonify
from ..models import Evento
from ..repositories import EventoRepository
from ..utils import *

def listar_eventos():
    try:
      eventos_do_banco = EventoRepository.listar_eventos()

      if not eventos_do_banco:
          return jsonify({"detail": "Não existem eventos registrados no momento"}), 204
      
      eventos = serializar_itens(eventos_do_banco)
      return jsonify(eventos)
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao listar eventos: {e}"}), 500
        
def criar_eventos(data):
    try:
      if validar_dados(data, Evento.campos_obrigatorios()) == False:
        return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

      novoEvento = Evento(data)
      EventoRepository.save(novoEvento)

      return jsonify({"detail":"Evento criado com sucesso!"}), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao criar evento: {e}"}), 500

def deletar_evento(id):
    try:
      evento = EventoRepository.find_by_id(id)

      if not evento:
          return jsonify({"detail": "Nenhum evento encontrado"}), 404
        
      EventoRepository.delete(evento)
      return jsonify({"detail": "Evento deletado com sucesso"}), 200
    except Exception as e:
        return jsonify({"detail": f"Erro desconhecido ao deletar evento: {e}"}), 500

def editar_evento(id, data):
    try:
      evento = EventoRepository.find_by_id(id)
      if not evento:
          return jsonify({"detail": "Nenhum evento encontrado"}), 404

      if not validar_dados(data, Evento.campos_obrigatorios()):
          return jsonify({"detail": "Preencha os campos obrigatórios"}), 400

      if not editar_dados(Evento.campos_editaveis(), data, evento):
          return {"detail": "Evento não alterado"}, 200

      EventoRepository.save(evento)

      return jsonify({"detail": "Evento atualizado com sucesso"}), 200
    except Exception as e:
      return jsonify({"detail": f"Erro desconhecido ao atualizar evento: {e}"}), 500

