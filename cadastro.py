alunos = []
notas = []
opção = 0
while True:
    print('{:^31}'.format('=== MENU DO SISTEMA ==='))
    print('-' * 31)
    print('[1] CADASTRAR NOVO ALUNO')
    print('[2] LISTAR ALUNOS CADASTRADOS')
    print('[3] VER MÉDIA GERAL DA TURMA')
    print('[4] VER APROVADOS E REPROVADOS')
    print('[5] SAIR')
    print('-' * 31)
    opção = int(input('Escolha uma opção: '))
    print('-' * 31)
    if opção == 1:
        while True:
            print('{:^31}'.format('=== CADASTRO DE ALUNO ==='))
            nome = str(input('Digite o nome do aluno: ')).strip().upper()
            idade = int(input('Digite a idade do aluno: '))
            nota = float(input('Digite a nota do aluno: '))
            alunos.append([nome, idade, nota])
            print('-' * 31)
            continuar = ' '
            while continuar not in 'SN':
                continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                print('-' * 31)
            if continuar == 'N':
                break
    if opção == 2:
        i = 0
        while i < len(alunos):
            print(f'Nome: {alunos[i][0]}')
            i += 1
            print('-' * 31)
    if opção == 3:
        if len(alunos) == 0:
            print('Nenhum aluno cadastrado ainda.')
            print('-' * 31)
        else:
            i = 0
            soma = 0
            while i < len(alunos):
                soma += alunos[i][2]
                i += 1
            media = soma / len(alunos)
            print(f'A média geral da turma é: {media:.2f}')
            print('-' * 31)
    if opção == 4:
        print('LISTA DE ALUNOS APROVADOS')
        i = 0
        while i < len(alunos):
            if alunos[i][2] >= 7:
                print(f'Nome: {alunos[i][0]}\nNota: {alunos[i][2]}')
            i += 1
        print('-' * 31)
        print('LISTA DE ALUNOS REPROVADOS')
        c = 0
        while c < len(alunos):
            if alunos[c][2] < 7:
                print(f'Nome: {alunos[c][0]}\nNota: {alunos[c][2]}')
            c += 1
        print('-' * 31)
    if opção == 5:
        break
