def serializar_itens(itens_do_banco):
    itens = [item.to_dict() for item in itens_do_banco]
    return itens 

def validar_dados(data, campos):
    for campo in campos:
        if not data.get(campo):
            return False
        
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


