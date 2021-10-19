import abc


def arguments():
    list_arguments = [
        'Ninguém aguenta mais o termo "cringe"',
        'Volta Domingão do Faustão',
        'Tio Zuck espião',
        'Flamengo é melhor time',
        'Velozes e furiosos perdeu a graça',
        'The Walking Dead precisa acabar',
        'Sofrencia é bom',
    ]
    return list_arguments

def profile_category(info, args):
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
        if arg ==  'Não tenho opnião':
            count = -1
        elif arg == 'Discordo em parte':
            count = 1
        elif arg == 'Concordo':
            count = 2
        elif arg == 'Concordo Totalmente':
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

    myOrg= (myOrg/(6*16))*100
    myTecn = (myTecn/(6*11))*100
    myComp = (myComp/(6*14))*100
    myEmpr = (myEmpr/(6*11))*100
    myInfra = (myInfra/(6*10))*100
    myLid = (myLid/(6*12))*100
    total = ((myOrg + myTecn + myComp + myEmpr + myInfra + myLid)/444)*100

    print('''
        Organizacional: %d,
        Técncicas: %i,
        Comportamental: %i,
        Empreendedorismo: %i,
        Intraempreendedorismo: %i,
        Liderança: %i,
        Geral: %i
    '''%(myOrg, myTecn, myComp, myEmpr, myInfra, myLid, total))

    return [myOrg, myTecn, myComp, myEmpr, myInfra, myLid, total]

def update_data():
    pass

def send_mail():
    pass

