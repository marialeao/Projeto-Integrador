def add_tarefa(codigo, tarefa):
    tarefas.update({codigo, tarefa})
    
tarefas = {1: 'prova de matemática', 2: 'tarefa de português'}
resposta = 0

while resposta != '4':
    print('-='*15)
    print('[1] Adicionar nova tarefa')
    print('[2] Mostrar tarefas')
    print('[3] Excluir tarefa')
    print('[4] Sair')
    
    resposta = input('O que deseja fazer? ')

    if resposta == '1':
        tarefa = input('Nome da tarefa: ')
        codigo = input('Código da tarefa: ')
        add_tarefa(codigo, tarefa)
    elif resposta == '2':
        print(tarefas)
    elif resposta == '3':
        delete = input ('Digite o código da tarefa que deseja deletar: ')
        del(tarefas[int(delete)])
    elif resposta == '4':
        print('Programa finalizado com suceso :)')