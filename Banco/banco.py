import sqlite3
import pygame
import requests
banco = sqlite3.connect('Finanças.db')
cursor = banco.cursor()
pygame.init()
screen = pygame.display.set_mode((1000, 500))
dinheiro = 0
moeda = 'R$'
lista = lista_nomes = lista2 = []
# cursor.execute('CREATE TABLE dados (Nome text, Senha text, dinheiro BigDecimal, Investimento text)')
# cursor.execute("INSERT INTO dados VALUES ('oi', 'oi', 1, 1)")
cursor.execute('SELECT * FROM dados')
for a in cursor.fetchall():
   lista2 = [a[0], a[1], a[2], a[3]]
   lista.append(lista2)
banco.commit()
pygame.display.set_caption('Banco New Age')
# Título
print(lista)

usuario = ''

conta = pygame.image.load('Botao conta.gif')
voltar = pygame.image.load('seta.gif')
iniciar = pygame.image.load('botao_entrar.gif')
nego = pygame.image.load('fundo negociação.gif')
sair = pygame.image.load('botao sair.gif')
investir = pygame.image.load('investir.gif')
transacao_concluida = pygame.image.load('transação concluida.gif')
bitcoin_imagem = pygame.image.load('bitcoin.png')
dolar_imagem = pygame.image.load('dolar.png')
real_imagem = pygame.image.load('real.gif')
# imagem

criar_1 = pygame.Rect(300, 150, 400, 75)
criar_2 = pygame.Rect(300, 300, 400, 75)
pagar_1 = pygame.Rect(50, 210, 300, 75)
pagar_2 = pygame.Rect(50, 290, 300, 75)
paga_2 = pygame.Rect(100, 400, 200, 75)
x_transacao = pygame.Rect(600, 100, 50, 50)
# retangulos

cor = (0, 0, 255)
# cores
print(dinheiro)
botao_conta = screen.blit(conta, (350, 300))
botao_login = screen.blit(conta, (350, 150))
botao_criar_1 = pygame.draw.rect(screen, cor, criar_1, 3)
botao_criar_2 = pygame.draw.rect(screen, cor, criar_2, 3)
botao_seta = screen.blit(voltar, (10, 10))
b_seta = screen.blit(voltar, (800, 10))
botao_iniciar = screen.blit(iniciar, (700, 400))
botao_pagar = screen.blit(conta, (10, 350))
botao_sair = screen.blit(sair, (360, 200))
botao_escrever = pygame.Rect(50, 230, 300, 75)
botao_transacao = pygame.draw.rect(screen, (0, 255, 0), paga_2)
botao_senha = pygame.draw.rect(screen, (0, 0, 255), pagar_2, 2)
botao_investir = screen.blit(investir, (850, 350))
botao_sair_transacao = pygame.draw.rect(screen, cor, x_transacao)
botao_bitcoin = screen.blit(bitcoin_imagem, (500, 150))
botao_dolar = screen.blit(dolar_imagem, (50, 150))
botao_real = screen.blit(real_imagem, (500, 150))
botao_real2 = screen.blit(real_imagem, (50, 150))
# Botões
fonte = pygame.font.SysFont('Times New Roman', 60)
font = pygame.font.SysFont('Times New Roman', 45)
fon = pygame.font.SysFont('Times New Roman', 30)
titulo = fonte.render('Banco New Age', False, (0, 0, 0))
criar_conta = font.render('Criar Conta', False, (0, 0, 0))
login = font.render('Login', False, (0, 0, 0))
titulo_criar = font.render('Crie sua conta', False, (0, 0, 0))
titulo_login = font.render('Entre na sua conta', False, (0, 0, 0))
nome_criar = font.render('Nome', False, (0, 0, 0))
senha_criar = font.render('Senha', False, (0, 0, 0))
esc_entrar = font.render('Entrar', False, (0, 0, 0))
escr_criar = font.render('Criar', False, (0, 0, 0))
pagar = font.render('Pagar', False, (0, 0, 0))
investir_cifrao = fonte.render('$', False, (0, 0, 0))
transacao_c = fon.render('Transação Concluída', False, (255, 255, 255))
escolha = font.render('Você quer converter seu dinheiro em:', False, (0, 0, 0))
# texto
cont = 0
tela = True
criar = entrar = escrever = escrever2 = conta_entrar = negociacao = escrever_pagar = escrever_pagar2 = transacao = conversao = False
deixar = ''
# Variáveis

escrita_retangulo_1 = escrita_retangulo_2 = escrita_pagar = escrita_pagar2 = ''
# escrita
url_bitcoin = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response_bitcoin = requests.get(url_bitcoin)
data_bitcoin = response_bitcoin.json()
cotacao_bitcoin = data_bitcoin["bitcoin"]["usd"]

url_usd = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response_usd = requests.get(url_usd)
data_usd = response_usd.json()

cotacao_dolar = float(data_usd["USDBRL"]["bid"])
cotacao_real = 1/cotacao_dolar
while tela:
    pygame.time.delay(50)
    screen.fill((255, 255, 255))
    bem_vindo = font.render(f'Bem vindo {usuario}!', False, (0, 0, 0))
    if moeda == 'BTC':
        saldo = font.render(f'Saldo: {moeda} {dinheiro:.10f}', False, (0, 0, 0))
    else:
        saldo = font.render(f'Saldo: {moeda} {dinheiro:.2f}', False, (0, 0, 0))
    mostrar_cot_usd = font.render(f'U$ {cotacao_dolar:.2f}', False, (0, 0, 0))
    mostrar_cot_rs = font.render(f'R$ {cotacao_real:.2f}', False, (0, 0, 0))
    if moeda == 'R$':
        mostrar_cot_btc = font.render(f'BTC {cotacao_bitcoin*cotacao_dolar:.2f}', False, (0, 0, 0))
    else:
        mostrar_cot_btc = font.render(f'BTC {cotacao_bitcoin:.2f}', False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tela = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botao_conta.collidepoint(event.pos) and criar is False and entrar is False:
                criar = True
            if botao_login.collidepoint(event.pos) and entrar is False and criar is False:
                entrar = True
            if botao_criar_1.collidepoint(event.pos):
                escrever = True
                escrever2 = False
            if botao_criar_2.collidepoint(event.pos):
                escrever2 = True
                escrever = False
            if botao_seta.collidepoint(event.pos):
                if conta_entrar:
                    criar_conta = False
                if criar:
                    criar = False
                if entrar:
                    entrar = False
            if botao_iniciar.collidepoint(event.pos) and conta_entrar is False:
                if criar is True or entrar is True:
                    if criar:
                        for c in lista:
                            if escrita_retangulo_1 == c[0]:
                                deixar += 'S'
                            else:
                                deixar += 'N'
                        print(deixar)
                        if 'S' in deixar:
                            print('ja tem')
                        else:
                            if len(escrita_retangulo_2) > 5 and len(escrita_retangulo_1) > 5:
                                cursor.execute(f'INSERT INTO dados VALUES ("{escrita_retangulo_1}", "{escrita_retangulo_2}", 0, "{moeda}")')
                                lista_nomes = [escrita_retangulo_1, escrita_retangulo_2, 0, moeda]
                                lista.append(lista_nomes)
                                print(lista)
                                banco.commit()
                                criar = False
                    if entrar:

                        for b in lista:
                            if cont < len(lista):
                                cont += 1
                            tudo = escrita_retangulo_1 + escrita_retangulo_2
                            tudo2 = b[0] + b[1]
                            if tudo == tudo2:
                                print(cont)
                                cursor.execute('SELECT * FROM dados')
                                dinheiro = lista[cont - 1][2]
                                moeda = lista[cont - 1][3]
                                usuario = escrita_retangulo_1
                                conta_entrar = True
            if botao_pagar.collidepoint(event.pos) and conta_entrar is True:
                negociacao = True
            if b_seta.collidepoint(event.pos) and conta_entrar is True and negociacao is False:
                if conversao is False:
                    conta_entrar = False
                if conversao is True:
                    conversao = False
            if botao_sair.collidepoint(event.pos) and negociacao is True:
                negociacao = False
            if botao_escrever.collidepoint(event.pos) and negociacao is True:
                escrever_pagar = True
                escrever_pagar2 = False
            if botao_senha.collidepoint(event.pos) and negociacao is True:
                escrever_pagar2 = True
                escrever_pagar = False
            if botao_transacao.collidepoint(event.pos) and negociacao is True:
                if escrita_pagar2.replace(',', '', 1).isdigit() or escrita_pagar2.replace('.', '', 1).isdigit():
                    print('etapa1')
                    if ',' in escrita_pagar2:
                        escrita_pagar2 = escrita_pagar2.replace(',', '.')
                    transacao = float(escrita_pagar2)
                    if transacao <= dinheiro:
                        for d in lista:
                            cont += 1
                            if escrita_pagar == d[0]:
                                moeda_receptor = d[3]
                                if moeda == 'USD':
                                    dinheiro -= transacao
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro - {transacao} WHERE Nome = "{usuario}"')
                                    transacao = transacao * cotacao_dolar
                                elif moeda == 'BTC':
                                    dinheiro -= transacao
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro - {transacao} WHERE Nome = "{usuario}"')
                                    transacao = transacao * (cotacao_dolar * cotacao_bitcoin)
                                else:
                                    dinheiro -= transacao
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro - {transacao} WHERE Nome = "{usuario}"')
                                if moeda_receptor == 'R$':
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro + {transacao} WHERE Nome = "{d[0]}"')
                                if moeda_receptor == 'USD':
                                    transacao = transacao/cotacao_dolar
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro + {transacao} WHERE Nome = "{d[0]}"')
                                if moeda_receptor == 'BTC':
                                    transacao = transacao / cotacao_bitcoin * cotacao_dolar
                                    cursor.execute(f'UPDATE dados SET dinheiro = dinheiro + {transacao} WHERE Nome = "{d[0]}"')
                                banco.commit()
                                negociacao = False
                                transacao = True
            if botao_investir.collidepoint(event.pos) and conta_entrar is True and negociacao is False:
                conversao = True
            if botao_sair_transacao.collidepoint(event.pos):
                transacao = False
            if botao_dolar.collidepoint(event.pos) and conversao is True and moeda != 'USD':
                if moeda == 'R$':
                    dinheiro = dinheiro/cotacao_dolar
                else:
                    dinheiro = dinheiro * cotacao_bitcoin
                moeda = 'USD'
                cursor.execute(f'UPDATE dados SET dinheiro = {dinheiro} WHERE Nome = "{usuario}"')
                cursor.execute(f'UPDATE dados SET Investimento = "{moeda}" WHERE Nome = "{usuario}"')
                banco.commit()
                conversao = False
            if botao_bitcoin.collidepoint(event.pos) and conversao is True and moeda != 'BTC':
                if moeda == 'USD':
                    dinheiro = dinheiro / cotacao_bitcoin
                else:
                    dinheiro = dinheiro / (cotacao_bitcoin * cotacao_dolar)
                moeda = 'BTC'
                cursor.execute(f'UPDATE dados SET dinheiro = {dinheiro} WHERE Nome = "{usuario}"')
                cursor.execute(f'UPDATE dados SET Investimento = "{moeda}" WHERE Nome = "{usuario}"')
                banco.commit()
                conversao = False
            if conversao is True and moeda != 'R$':
                if botao_real.collidepoint(event.pos) or botao_real2.collidepoint(event.pos):
                    if moeda == 'USD':
                        dinheiro = dinheiro * cotacao_dolar
                    else:
                        dinheiro = dinheiro * (cotacao_dolar * cotacao_bitcoin)
                    moeda = 'R$'
                    cursor.execute(f'UPDATE dados SET dinheiro = {dinheiro} WHERE Nome = "{usuario}"')
                    cursor.execute(f'UPDATE dados SET Investimento = "{moeda}" WHERE Nome = "{usuario}"')
                    banco.commit()
                    conversao = False
        if escrever:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    escrita_retangulo_1 = escrita_retangulo_1[0:-1]
                else:
                    if len(escrita_retangulo_1) <= 10:
                        escrita_retangulo_1 += event.unicode
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            escrita_retangulo_1 = escrita_retangulo_1[0:-1]
        if escrever_pagar:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    escrita_pagar = escrita_pagar[0:-1]
                else:
                    if len(escrita_pagar) <= 10:
                        escrita_pagar += event.unicode
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            escrita_pagar = escrita_pagar[0:-1]

        if escrever_pagar2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    escrita_pagar2 = escrita_pagar2[0:-1]
                else:
                    if len(escrita_pagar2) <= 10:
                        escrita_pagar2 += event.unicode
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            escrita_pagar2 = escrita_pagar2[0:-1]
        if escrever2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    escrita_retangulo_2 = escrita_retangulo_2[0:-1]
                else:
                    if len(escrita_retangulo_2) <= 10:
                        escrita_retangulo_2 += event.unicode
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            escrita_retangulo_2 = escrita_retangulo_2[0:-1]
    if criar is False and entrar is False and conta_entrar is False and conversao is False:
        screen.blit(titulo, (300, 0))
        screen.blit(conta, (350, 300))
        screen.blit(conta, (350, 150))
        screen.blit(criar_conta, (375, 325))
        screen.blit(login, (430, 170))
    if criar is True or entrar is True and conta_entrar is False and conversao is False:
        escrita1 = font.render(escrita_retangulo_1, False, (0, 0, 0))
        escrita2 = font.render(escrita_retangulo_2, False, (0, 0, 0))
        screen.blit(escrita1, (310, 150))
        screen.blit(escrita2, (310, 300))
        screen.blit(voltar, (10, 10))
        pygame.draw.rect(screen, cor, criar_1, 3)
        screen.blit(nome_criar, (300, 100))
        screen.blit(senha_criar, (300, 250))
        pygame.draw.rect(screen, cor, criar_2, 3)
        screen.blit(iniciar, (700, 400))
        if criar:
            screen.blit(titulo_criar, (300, 10))

            screen.blit(escr_criar, (740, 410))
            entrar = False
        if entrar:
            screen.blit(esc_entrar, (730, 410))
            criar = False
            screen.blit(titulo_login, (300, 10))
    if criar is False and entrar is False:
        escrita_retangulo_1 = ''
        escrita_retangulo_2 = ''
    deixar = ''
    if negociacao is False:
        escrita_pagar = ''
        escrita_pagar2 = ''
    if conta_entrar is True and conversao is False:
        screen.blit(bem_vindo, (10, 10))
        screen.blit(saldo, (10, 100))
        screen.blit(conta, (10, 350))
        screen.blit(pagar, (80, 370))
        screen.blit(investir, (850, 350))
        screen.blit(investir_cifrao, (885, 360))
    if conta_entrar is True or conversao is True:
        screen.blit(voltar, (800, 10))
    if conversao is True:
        screen.blit(escolha, (10, 10))
        if moeda == 'R$':
            screen.blit(mostrar_cot_btc, (500, 100))
            screen.blit(mostrar_cot_usd, (100, 100))
            screen.blit(dolar_imagem, (50, 150))
            screen.blit(bitcoin_imagem, (500, 150))
        if moeda == 'USD':
            screen.blit(mostrar_cot_rs, (100, 100))
            screen.blit(mostrar_cot_btc, (500, 100))
            screen.blit(bitcoin_imagem, (500, 150))
            screen.blit(real_imagem, (50, 150))
        if moeda == 'BTC':
            screen.blit(mostrar_cot_usd, (100, 100))
            screen.blit(real_imagem, (500, 150))
            screen.blit(dolar_imagem, (50, 150))
            screen.blit(mostrar_cot_rs, (500, 100))
    if negociacao is True and conversao is False:
        quanto_pagar = font.render(escrita_pagar, False, (255, 255, 255))
        quanto_pagar2 = font.render(escrita_pagar2, False, (255, 255, 255))
        screen.blit(nego, (10, 200))
        screen.blit(sair, (360, 200))
        pygame.draw.rect(screen, (42, 79, 240), pagar_1, 2)
        screen.blit(quanto_pagar, (60, 210))
        pygame.draw.rect(screen, (42, 79, 240), paga_2)
        pygame.draw.rect(screen, (42, 79, 240), pagar_2, 2)
        screen.blit(quanto_pagar2, (60, 290))
        screen.blit(pagar, (135, 400))
    if transacao is True and conversao is False:
        pygame.draw.rect(screen, cor, x_transacao)
        screen.blit(transacao_concluida, (360, 100))
        screen.blit(transacao_c, (380, 220))
    cont = 0
    pygame.display.flip()
pygame.quit()

