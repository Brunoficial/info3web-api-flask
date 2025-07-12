from flask import session, g
from .repositories import UsuarioRepository

def serializar_itens(itens_do_banco):
    itens = [item.to_dict() for item in itens_do_banco]
    return itens 

def validar_dados(data, campos):
    for campo in campos:
        if not data.get(campo):
            return False
    return True
        
def editar_dados(campos, data, objeto):
    novos_valores=[]
    valores_antigos=[]
    for campo in campos:
        novo_valor = data.get(campo)
        novos_valores.append(novo_valor)

        valor_antigo = getattr(objeto, campo)
        valores_antigos.append(valor_antigo)
        
        if novo_valor != valor_antigo:
            setattr(objeto, campo, novo_valor)
    
    if novos_valores == valores_antigos:
        return False

    return True

def get_usuario_logado():
    usuario_id = session.get('usuario_id')

    if usuario_id == None:
        g.user = None
    else: 
        g.user = UsuarioRepository.find_by_id(usuario_id)



