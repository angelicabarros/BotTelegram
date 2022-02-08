import telebot

CHAVE_API = "xxx" #adicionar aqui a sua chave api do telegram

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["dparticipar"])
def dparticipar(mensagem):
    bot.send_message(mensagem.chat.id, "Que bom que você quer fazer parte da nossa equipe docente! Nossas vagas são divulgadas através de edital em nosso site: gegteste.com.br/docente. Acompanhe também as nossas redes sociais!")

@bot.message_handler(commands=["aparticipar"])
def aparticipar(mensagem):
    bot.send_message(mensagem.chat.id, "Que bom que você quer fazer parte da nossa equipe administrativa! Nossas vagas são divulgadas através do site gegteste.com.br/adm. Caso não encontre uma vaga que deseja, se inscreva em nosso banco de talentos!")

@bot.message_handler(commands=["andamento"])
def acompanhar(mensagem):
    bot.send_message(mensagem.chat.id, "Que felicidade ter você participando de um processo nosso! Fique atento ao seu e-mail que encaminhamos todas as novidades e atualizações por lá!")

@bot.message_handler(commands=["sintomas"])
def sintomas(mensagem):
    texto = """
    Você já procurou acompanhamento médico? (Clique em uma opção)
    /sim 
    /nao 
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["contatante"])
def contatante(mensagem):
    texto = """
    Você já procurou acompanhamento médico? (Clique em uma opção)
    /sim 
    /nao 
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["sim"])
def sim(mensagem):
    bot.send_message(mensagem.chat.id, "Que bom! Agora siga as orientações do seu médico, caso seja possível, também faça o teste e nos encaminhe o resultado! Desejamos melhoras!")

@bot.message_handler(commands=["nao"])
def nao(mensagem):
    bot.send_message(mensagem.chat.id, "Não acredito nessa ousadia! Vá procurar um médico agora! Run")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Selecione uma das opções abaixo:
    /dparticipar Quero fazer parte da equipe
    /andamento Quero saber o andamento do processo seletivo que estou participando
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Selecione uma das opções abaixo:
    /aparticipar Quero fazer parte da equipe
    /andamento Quero saber o andamento do processo seletivo que estou participando
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Para agendar uma consulta você deve encaminhar um e-mail para gestaoegente@teste.com")

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """
    Você está com sintomas ou é caso contatante? (Clique em uma opção)
    /sintomas Estou com sintomas
    /contatante Tive contato com alguém que testou positivo para Covid-19
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    bot.send_message(mensagem.chat.id, "Para falar diretamente com a equipe você pode ligar para (83) 2101-0000, encaminhar um e-mail para gestaoegente@teste.com ou aguardar o nosso contato dentro de instantes.")


def verificar(mensagem):
    return True
    
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá, tudo bem? Aqui é o Bot do Gestão e Gente! Clique em uma das opções abaixo para continuar:

    /opcao1 Falar sobre Processo Seletivo Docente
    /opcao2 Falar sobre Processo Seletivo Administrativo
    /opcao3 Falar sobre Marcação de Consulta
    /opcao4 Falar sobre casos de covid
    /opcao5 Falar diretamente com a equipe sobre outro assunto

    Atenção: Selecione alguma das opções ou não irá funcionar!
    """
    bot.reply_to(mensagem,texto)

bot.polling()