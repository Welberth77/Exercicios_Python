def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita vários)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num) / len(num)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
        
    return r

help(notas)
resp = notas(1, 2, 6, sit=True)
print(resp)
