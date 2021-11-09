from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from hashlib import new
import uuid

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
        new_list.append(obj)
        if len(new_list) == 35:
            ikigai_list.append(new_list)
            new_list = []
            count += 1
    return ikigai_list

def calculate_ikigai(my_list):
    amo = my_list[0]
    bom = my_list[1]
    preciso = my_list[2]
    pago = my_list[3]
    data = [] 
    ikigai = [] 
    profissao = [] 
    vocacao = []
    missao = [] 
    paixao  = []
    for num in range(35):
        ikigai.append(int(amo[num]) + int(bom[num]) + int(preciso[num]) + int(pago[num]))
        profissao.append(int(bom[num]) + int(pago[num]))
        vocacao.append(int(preciso[num]) + int(pago[num]))
        missao.append(int(amo[num]) + int(preciso[num]))
        paixao.append(int(bom[num]))
    data.append(ikigai)
    data.append(profissao)
    data.append(vocacao)
    data.append(missao)
    data.append(paixao)
    return data