from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from hashlib import new
import uuid
from . import models

from . import models

def hability():
    list_1 = [
        'Coaching e mentoria',
        'Abordagem metódica',
        'Princípios morais e padrões éticos',
        'Trabalho colaborativo',
        ' Tecnologia da informação',
        ' Inteligência social e emocional',
        ' Conhecimento de equipamentos e programas',
        ' Gestão de desempenho',
        ' Técnicas de persuasão',
        ' Crescimento na carreira',
        ' Gestão da mudança',
        ' Controle do estresse',
        ' Alfabetização digital',
        ' Comunicação escrita',
        ' Comunicação verbal',
        ' Compromisso com a excelência',
        ' Compromisso com a excelência do cliente',
        ' Perspicácia nos negócios',
        ' Persuasão e influência sob a equipe',
        ' Gestão de dados',
        ' Planejamento e organização',
        ' Pensamento estruturado',
        ' Pensamento criativo',
        ' Identificação de padrões ou conexões',
        ' Pesquisa e análise',
        ' Planejamento futuro',
        ' Gestão estratégica',
        ' Inovação e desenvoltura',
        ' Resolução de problemas',
        ' Tomada de decisões',
        ' Políticas e planejamento',
        ' Confiabilidade',
        ' Trabalho em equipe',
        ' Formação e desenvolvimento',
        ' Gestão de relacionamento com o cliente',
    ]
    list_2 = [
        'Dar conselhos e cuidar dos mais novos',
        'Verificar a origem das informações',
        'Cumprir e fazer cumprir as normas',
        'Oferecer ajuda e conhecimento ao meu time',
        'Esutdar a evolução da tecnologia',
        'Cuidar meus sentimentos para não ferir outros',
        'Entender como computadores podem ajudar',
        'Listar e controlar os passos de uma tarefa',
        'Argumentar, negociar e convencer',
        'Ser responsável pela minha carreira',
        'Convercer pessoas a aceitar novidades',
        'Controlar meu corpo quando sob pressão',
        'Conhecer aplicativos, e tecnologias de uso pessoal',
        'Redigir cartas, memorandos e comunicados',
        'Dialogar e apresentar ideias',
        'Não aceitar menos que o perfeito',
        'Tratar a todos como clientes',
        'Buscar sempre o melhor resultado',
        'Argumenta, influenciar e convencer',
        'Saber ler o que os dados dizem',
        'Usar o que tenho a minha disposição com inteligencia',
        'Manter o passo a passo das coisas em minha mente',
        'Olhar para onde ninguem está olhando',
        'Encontrar tendências, movimentos e novidades',
        'Dedicar interesse aos dados e fatos',
        'Manter sempre um plano',
        'Pensar de maneira empreededora',
        'Encontrar novas formas de fazer',
        'Procurar soluções para problemas existentes',
        'Tomar decisão com os dados que tenho',
        'Negociar interesses e posições divergentes',
        'Manter a responsabilbilidade sob meus atos',
        'Jogar com o time',
        'Dar aulas ou escrever instruções',
        'Fomentar amizades e relacionamentos',
    ]
    list_3 = [
        'Aconselhar pessoas mais novas',
        'Analisar fatos e dados',
        'Atuar de maneira ética',
        'Colaborar com equipes',
        'Conhecer computação corporativa',
        'Conhecer e controlar emoções',
        'Conhecer sistemas e tecnologias aplicadas',
        'Controlar tarefas',
        'Convencer pessoas',
        'Cuidar do meu desenvolvimento',
        'Cuidar para que mudanças ocorram',
        'Dominar sinais de stress',
        'Dominar tencnologia pessoal',
        'Escrever bem',
        'Falar bem',
        'Fazer trabalhos excelentes',
        'Focar no cliente e em sua experiência',
        'Focar no resultado',
        'Influenciar opiniões de outros',
        'Interpretar dados e informações',
        'Organizar recursos e planejar o uso',
        'Pensar de maneira organizada',
        'Pensar fora da caixa',
        'Perceber o que poucos veem',
        'Pesquisar e analisar resultados',
        'Planejar e executar o plano',
        'Possui visão de negócios',
        'Propor novidades',
        'Resolver problemas',
        'Saber decidir certo e rápido',
        'Saber lidar com cultura e politicas empresariais',
        'Ser responsável',
        'Trabalhar em equipe',
        'Treinar pessoas',
        'Zelar pelo relacionamento com outros',
    ]
    list_4 = [
        'Aconselhar quem precisa',
        'Checar fatos e dados',
        'Seguir normas e regras propostas',
        'Compartilhar o que sei com os meus',
        'Manter-me antenado',
        'Controlar minhas emoções',
        'Estudar inovações e tecnologia',
        'Estruturar formas de fazer as coisas',
        'Negociar e convencer',
        'Cuidar dos meus interesses com protagonismo',
        'Propor novidades e "vender" a que é preciso',
        'Manter a cabeça fria',
        'Aprender novas tecnologias',
        'Escrever',
        'Fazer apresentações',
        'Buscar a excelência no que faço',
        'Entender as necessidades dos outros',
        'Buscar minhas metas',
        'Despertar o interesse de outros sobre o que é preciso',
        'Analisar dados',
        'Fazer melhor uso do que está disponível',
        'Planejar com detalhes',
        'Criar quando algo não existe',
        'Perceber movimentos e padrões',
        'Buscar a verdade dos fatos',
        'Planejar e executar o plano',
        'Criar novas formas de fazer mais rápido e melhor',
        'Inovar mesmo errando',
        'Não me conformar com dificuldades existentes',
        'Decidir rápido',
        'Mediar discussões',
        'Assumir as conseqeuncias dos meus atos',
        'Atuar pelo bem maior',
        'Treinar pessoas e passar conhecimento',
        'Conhecer gente e zelar pela relação',
    ]
    return {
        's1':list_1,
        's2':list_2,
        's3':list_3,
        's4':list_4
    }

def generate_key():
    verify = True
    my_key = str(uuid.uuid4()).replace('-', '')
    '''while verify is True:
        my_key = str(uuid.uuid4()).replace('-', '')
        verify = verify_key(my_key)'''
    return my_key

def verify_key(key):
    if models.Client.objects.filter(key=key).exists():
        return True
    else:
        return False

def rank_responses(ikigai):
    for i in range(4):
        del ikigai[0]
    count = 0
    new_list = []
    ikigai_list = []
    count = 0
    for obj in ikigai:
        new_list.append('x' if obj == '1' else '0')
        if len(new_list) == 35:
            ikigai_list.append(new_list)
            new_list = []
            count += 1
    return ikigai_list

def concatenate(data):
    string_list = []
    for my_list in data:
        my_string = ''
        for i in my_list:
            my_string += str(i)
        string_list.append(my_string)
    return string_list

def desconcatenate(data):
    new_list = []
    for string in data:
        string_list = []
        for char in string:
            string_list.append(char)
        new_list.append(string_list)
    return new_list

def save_data(name, email, key, data):
    string_list = concatenate(data)
    db = models.Client(
        name=name, 
        email=email,
        key=key,
        profissao=string_list[0],
        vocacao=string_list[1],
        missao=string_list[2],
        paixao=string_list[3],
    )
    db.save()

def get_client(key):
    query = models.Client.objects.get(key=key)
    return {
        'name':query.name,
        'email':query.email,
        'key':query.key,
        'profissao':query.profissao,
        'vocacao':query.vocacao,
        'missao':query.missao,
        'paixao':query.paixao,
    }

def calculate_profile(data, option):
    profiles = {
        'vocação':{
            'name':'Vocação',
            'text':'Qual a minha vocação',
            'value':'xx'
        },
        'profissão':{
            'name':'Profissão',
            'text':'Qual minha profissão ideal',
            'value':'xx',
        },
        'missão':{
            'name':'Missão',
            'text':'Qual a base de minha missão',
            'value':'xx',
        },
        'paixão':{
            'name':'Paixão',
            'text':'O que eu faço com paixão',
            'value':'xx',
        },
        'razão':{
            'name':'Razão',
            'text':'Qual minha razão de ser',
            'value':'xxxx', 
        }
    }
    info = [
        'Coaching e mentoria',
        'Abordagem metódica',
        'Princípios morais e padrões éticos',
        'Trabalho colaborativo',
        ' Tecnologia da informação',
        ' Inteligência social e emocional',
        ' Conhecimento de equipamentos e programas',
        ' Gestão de desempenho',
        ' Técnicas de persuasão',
        ' Crescimento na carreira',
        ' Gestão da mudança',
        ' Controle do estresse',
        ' Alfabetização digital',
        ' Comunicação escrita',
        ' Comunicação verbal',
        ' Compromisso com a excelência',
        ' Compromisso com a excelência do cliente',
        ' Perspicácia nos negócios',
        ' Persuasão e influência sob a equipe',
        ' Gestão de dados',
        ' Planejamento e organização',
        ' Pensamento estruturado',
        ' Pensamento criativo',
        ' Identificação de padrões ou conexões',
        ' Pesquisa e análise',
        ' Planejamento futuro',
        ' Gestão estratégica',
        ' Inovação e desenvoltura',
        ' Resolução de problemas',
        ' Tomada de decisões',
        ' Políticas e planejamento',
        ' Confiabilidade',
        ' Trabalho em equipe',
        ' Formação e desenvolvimento',
    ]
    preciso = data[0]
    bom = data[1]
    pago = data[2]
    amo = data[3]
    my_profile = []
    if profiles['vocação']['text'] == option:
        for i in range(35):
            result = preciso[i] + pago[i]
            if result == profiles['vocação']['value']:
                my_profile.append(info[i])
    elif profiles['profissão']['text'] == option:
        for i in range(35):
            result = bom[i] + pago[i]
            if result == profiles['profissão']['value']:
                my_profile.append(info[i])
    elif profiles['missão']['text'] == option:
        for i in range(35):
            result = amo[i] + preciso[i]
            if result == profiles['missão']['value']:
                my_profile.append(info[i])
    elif profiles['paixão']['text'] == option:
        for i in range(35):
            result = amo[i] +  bom[i]
            if result == profiles['paixão']['value']:
                my_profile.append(info[i])
    elif profiles['razão']['text'] == option:
        for i in range(35):
            result = amo[i] + bom[i] + preciso[i] + pago[i]
            if result == profiles['razão']['value']:
                my_profile.append(info[i])
    return my_profile


def send_mail(my_list):
    import smtplib
    from email.message import EmailMessage
    port = 465
    
    my_mail = 'theus0197@gmail.com'
    my_pass = 'Tiube@0504'
    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.ehlo()
        server.login(my_mail, my_pass)
        msg = MIMEMultipart('alternative')

        html = '''
        <h1 style='font-family:Arial'>Olá <span style='color:#00E88F;'><b>{}</b></span></h1>\n
        <p style='font-family:Arial'>Segue o resultado do seus forms:</p>\n
            <span style='font-family:Arial'><b>Geral:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Habilidades organizacionai:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Competências técnicas:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Comportamentos:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Nível de empreendedorismo:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Nível de intraempreededorismo:</b> {:.2f}%</span><br>\n
            <span style='font-family:Arial'><b>Perfil de liderança:</b> {:.2f}%</span><br>\n
        <br>
        <p style='font-family:Arial'>Segue o link, para futuras consultas: <a href='http://127.0.0.1:8000/ikigai/charts/{}'>http://127.0.0.1:8000/atratividade/charts/{}</a></p><br>\n
        <span style='font-family:Arial'>Atenciosamente,</span>\n
        <p style='font-family:Arial'>Equipe <a href='https://descomplica.com.br/' style='color:#00E88F; text-decoration:none'><b>Descomplica</b></a>.</p>
        '''.format(
            my_list[0],
            float(my_list[2]),
            float(my_list[3]),
            float(my_list[4]),
            float(my_list[5]),
            float(my_list[6]),
            float(my_list[7]),
            float(my_list[8]),
            my_list[10],
            my_list[10],
        )
        msg['Subject'] = 'Avaliação Atratividade Mercado'
        msg['From'] = "my_mail"
        msg['To'] = my_list[1]
        part = MIMEText(html, 'html')
        msg.attach(part)

        server.sendmail(msg['From'],  msg['To'], msg.as_string())
        server.quit()
