from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import uuid

from . import models

def arguments():
    questions = [
        'Em cada ação, pergunte-se se deu o seu melhor',
        'Opinião, cada um tem a sua. Fatos são únicos.',
        'Conhecimento deve ser colocado em prática',
        'Motivação só pode vir de dentro do coração e da mente',
        'Tudo pode ser melhorado',
        'Somos os unicos responsáveis pelo nosso sucesso',
        'Eu cedo, você cede e no meio nos encontramos',
        'O entendimento depende de se colocar no lugar do outro',
        'Sem dados, o que temos é opinião',
        'Os fatos são como são. A diferença é o que se faz com eles',
        'Controlando os sentimentos, controlamos o ambiente',
        'Se foi prometido para hoje, então faça hoje',
        'Ao final, pergunte se poderia fazer melhor',
        'O ambiente define o comportamento',
        'Empatia e argumentação resolvem qualquer divergência',
        'Disciplina faz as coisas acontecerem, mesmo sem motivação',
        'Resolver problemas envolve mais a causa que o sintoma',
        'Todas as pessoas com quem nos relacionamos são clientes',
        'Tudo tem causa e efeito. Sem um não se entende o outro',
        'Respeitar a visão do outro é o primeiro passo para o entendimento',
        'Cada um tem um estilo próprio de entender as coisas',
        'Meu valor depende da minha contribuição para com o coletivo',
        'Não se trata de ser mais forte. Se tarta de adaptação',
        'Sem objetivos, não se faz nada',
        'Quando em grupo, compartilhe o que sabe e pergunte sobre o que ignora',
        'Todo problema tem solução',
        'O pensamento é livre. O comportamento é regulado.',
        'Dados e informações definem a história',
        'Qualquer lugar é lugar para atuar',
        'Quando em dúvida, pergunte',
        'Cabe ao indivíduo o oficio da atualização',
        'O que o outro entende é mais importante que o que eu falo',
        'Toda tradição um dia foi inovação',
        'Sozinho se vai rápido, junto se vai longe',
        'Novidades sempre acontecem. É preciso encontrar a harmonia',
        'Tudo tem consequências. É preciso medir antecipadamente',
        'Para entender é preciso se afastar e ver o todo',
        'Sabendo como o coletivo funciona, defino minhas ações',
    ]
    return questions

def profile_category(myList, key):
    args = myList[2:]
    arguments_category = [
        'CA',
        'AG',
        'AD',
        'PR',
        'MO',
        'CC',
        'CR',
        'CR',
        'EM',
        'MO',
        'PR',
        'AD',
        'NE',
        'NE',
        'PC',
        'AG',
        'CC',
        'EM',
        'VG',
        'CI',
        'PC',
        'AC',
        'EE',
        'TE',
        'TE',
        'AC',
        'SP',
        'SP',
        'CO',
        'CO',
        'CI',
        'EE',
        'MB',
        'DE',
        'MB',
        'CA',
        'DE',
        'VG'
    ]
    i = 0
    myComp = myEmpr = myTecn = myLid = myOrg = myInfra = 0
    for arg in args:
        if arg ==  'Não tenho opinião':
            count = -1
        elif arg == 'Discordo em parte':
            count = 1
        elif arg == 'Concordo':
            count = 2
        elif arg == 'Concordo totalmente':
            count = 3
        else:
            count = 0
        
        if arguments_category[i] == 'CA':
            myComp += count
            myEmpr += count
            myTecn += count
            myLid += count
        elif arguments_category[i] == 'AG':
            myOrg += count
            myComp += count
            myEmpr += count
            myInfra += count
        elif arguments_category[i] == 'AD':
            myOrg += count
            myComp += count
        elif arguments_category[i] == 'PR':
            myOrg += count
            myTecn += count
            myComp += count
        elif arguments_category[i] == 'MO':
            myOrg += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'CC':
            myOrg += count
            myComp += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'CR':
            myOrg += count
            myTecn += count
        elif arguments_category[i] == 'EM':
            myOrg += count
            myComp += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'NE':
            myOrg += count
            myTecn += count
            myComp += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'PC':
            myOrg += count
            myTecn += count
            myLid += count
        elif arguments_category[i] == 'VG':
            myOrg += count
            myComp += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'CI':
            myOrg += count
            myTecn += count
            myComp += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'AC':
            myTecn += count
            myComp += count
            myLid += count
        elif arguments_category[i] == 'EE':
            myOrg += count
            myComp += count
            myEmpr += count
            myInfra += count
        elif arguments_category[i] == 'TE':
            myOrg += count
            myComp += count
        elif arguments_category[i] == 'SP':
            myOrg += count
            myTecn += count
            myEmpr += count
            myInfra += count
            myLid += count
        elif arguments_category[i] == 'CO':
            myOrg += count
            myTecn += count
            myLid += count
        elif arguments_category[i] == 'MB':
            myTecn += count
            myComp += count
            myLid += count
        elif arguments_category[i] == 'DE':
            myOrg += count
            myTecn += count 
            myComp += count 
            myEmpr += count
            myInfra += count
        i+=1
    total = ((myOrg + myTecn + myComp + myEmpr + myInfra + myLid)/444)*100
    myOrg= (myOrg/(6*16))*100
    myTecn = (myTecn/(6*11))*100
    myComp = (myComp/(6*14))*100
    myEmpr = (myEmpr/(6*11))*100
    myInfra = (myInfra/(6*10))*100
    myLid = (myLid/(6*12))*100
    insert_client([myList[0], myList[1], myOrg, myTecn, myComp, myEmpr, myInfra, myLid, total], key)
    return [myList[0], myList[1], myOrg, myTecn, myComp, myEmpr, myInfra, myLid, total]


def generate_key():
    verify = True
    while verify is True:
        my_key = str(uuid.uuid4()).replace('-', '')
        verify = verify_key(my_key)
    return my_key

def verify_key(key):
    if models.Client.objects.filter(key=key).exists():
        return True
    else:
        return False


def send_mail(my_list):
    import smtplib
    from email.message import EmailMessage
    port = 465
    
    my_mail = 'faladescomplica@gmail.com'
    my_pass = 'Tiube@2083'
    host = 'http://'+my_list[11]+'/atratividades/charts/'+my_list[10]
    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.ehlo()
        server.login(my_mail, my_pass)
        msg = MIMEMultipart('alternative')

        html = '''
        <h1 style='font-family:Arial; color:#000'>Parabéns, Você completou o seu Questionário: Atratividade no Mercado!</h1>\n
        <br>\n
        <p style='font-family:Arial'>Agora você conhece um pouco mais sobre que tipo de profissional você é e como o Mercado enxerga o seu perfil!</p>\n
        <p style='font-family:Arial'>A gente mandou esse email pra você saber exatamente onde encontrar os seus resultados caso você precise deles de novo.</p>\n
        <p style='font-family:Arial'>Link: <a href='{}'>{}</a></p><br>\n
        <p style='font-family:Arial'>Esse link vai ficar disponível por 3 meses. Por isso a gente recomenda que você salve ou imprima uma versão dele. Você pode fazer isso direto do seu navegador mesmo.</p>\n
        <p style='font-family:Arial'>Depois de salvar, não esquece de continuar no conteúdo de Orientação de Carreira. Os próximos passos são essenciais para você entender melhor como criar um plano a partir do seu resultado no Questionário.</p>\n
        <span style='font-family:Arial'>Atenciosamente,</span>\n
        <br>\n
        <p style='font-family:Arial'>Equipe <a href='https://descomplica.com.br/' style='color:#00E88F; text-decoration:none'><b>Descomplica</b></a>.</p>
        <img src='https://s3-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/485/400/resized/LogoDescomplica.png?1602169648'>
        '''.format(
            host,
            host
        )
        msg['Subject'] = 'Resultado | Questionário: Atratividade no Mercado'
        msg['From'] = "falacomigo@descomplica.com.br"
        msg['To'] = my_list[1]
        part = MIMEText(html, 'html')
        msg.attach(part)

        server.sendmail(msg['From'],  msg['To'], msg.as_string())
        server.quit()

def insert_client(my_list, key):
    p = models.Client(
        key = key,
        name = my_list[0],
        email = my_list[1],
        organizacao = float(my_list[3]),
        tecnica = float(my_list[4]),
        comportamento = float(my_list[5]),
        empreendedorismo =  float(my_list[6]),
        intraempreendedorismo = float(my_list[7]),
        lideranca = float(my_list[8]),
        geral = float(my_list[2])
    )
    p.save()

def get_client(key):
    query = models.Client.objects.get(key=key)
    return [
        query.name,
        query.email,
        query.organizacao,
        query.tecnica,
        query.comportamento,
        query.empreendedorismo,
        query.intraempreendedorismo,
        query.lideranca,
        query.geral,
        query.key
    ]

    