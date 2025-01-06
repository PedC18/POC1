import pandas as pd

def Stats(Points,Matches,surface= None,result=None,pt_results= None,serve =None):
    
    if result != None:
        Matches = Matches[Matches['Winner'] == result]
    if surface != None:
        Matches = Matches[Matches['Surface'] == surface]

    data = Points[Points['match_id'].isin(Matches['match_id'])]

    if pt_results != None:
        data = data[data['Victor'] == pt_results]
    
    if serve != None:
        data = data[data['Server'] == serve]

    WinRate = round(data['Winner'].value_counts(normalize=True),4)
    AceRate = round(data['Ace'].value_counts(normalize=True),4)
    DoubleFRate = round(data['Double Fault'].value_counts(normalize=True),4)
    FERate = round(data['Forced Error'].value_counts(normalize=True),4)
    UFERate = round(data['Unforced Error'].value_counts(normalize=True),4)

    print(f'Aces => {float(AceRate[serve])}')
    print(f'Winners => {float(WinRate[True])}')
    print(f'Forced Errors => {float(FERate[True])}')
    print(f'Unforced Errors => {float(UFERate[True])}')
    print(f'Double Faults => {float(DoubleFRate[not pt_results])} \n')
    
    return [float(WinRate[True]),float(AceRate[True]),float(DoubleFRate[True]),float(FERate[True]),float(UFERate[True])]

def KeyPointsData(data):
    GamePoints   = pd.DataFrame()
    BreakPoints  = pd.DataFrame()
    DeucePoints  = pd.DataFrame()

    KP = data[data['Pts'].str.contains('40', na=False)]

    ServingKP = data[data['Server'] == True]
    RecpKP = data[data['Server'] == False]

    GamePoints = pd.concat([GamePoints, ServingKP[ServingKP['Pts'].str.startswith(('40','AD') ,na=False)]], axis=0)
    GamePoints = pd.concat([GamePoints, RecpKP[~RecpKP['Pts'].str.startswith(('40','AD'),na=False)]], axis=0)

    BreakPoints = pd.concat([BreakPoints, ServingKP[~ServingKP['Pts'].str.startswith(('40','AD') ,na=False)]], axis=0)
    BreakPoints = pd.concat([BreakPoints, RecpKP[RecpKP['Pts'].str.startswith(('40','AD'),na=False)]], axis=0)

    GamePoints = GamePoints[GamePoints['Pts'] != '40-40']
    BreakPoints = BreakPoints[BreakPoints['Pts'] != '40-40']
    DeucePoints = KP[KP['Pts'] == '40-40']

    # Dpoints = ['40-40','AD-40','40-AD']
    # Dispute = KP[KP['Pts'].isin(Dpoints)]

    return GamePoints,BreakPoints,DeucePoints

def BuildRally(data,PlayerGames):
    rows = ['Total','1-3','4-6','7-9','10']

    PlayerRallyServe = data[data['server'] == 'Roger Federer'].drop(columns=['server','returner'])
    PlayerRallyServe = PlayerRallyServe[PlayerRallyServe['match_id'].isin(PlayerGames['match_id'].unique())]
    PlayerRallyServe = PlayerRallyServe[~PlayerRallyServe['row'].isin(rows)]
    PlayerRallyServe[['pl1_unforced','pl2_unforced']] = PlayerRallyServe[['pl2_unforced','pl1_unforced']]
    PlayerRallyServe['row'] = PlayerRallyServe['row'].str[:3]
    
    PlayerRallyReturn = data[data['returner'] == 'Roger Federer'].drop(columns=['server','returner'])
    PlayerRallyReturn = PlayerRallyReturn[PlayerRallyReturn['match_id'].isin(PlayerGames['match_id'].unique())]
    PlayerRallyReturn = PlayerRallyReturn[~PlayerRallyReturn['row'].isin(rows)]
    PlayerRallyReturn[['pl1_unforced','pl2_unforced']] = PlayerRallyReturn[['pl2_unforced','pl1_unforced']]
    PlayerRallyReturn['row'] = PlayerRallyReturn['row'].str[:3]

    return PlayerRallyServe,PlayerRallyReturn

def statsDiv(data):
    stats_dic = {}
    for r in data['row'].unique():

        Type = data[data['row'] == r]
        stats_dic[r] = Type
    
    return stats_dic

def AllStats(data,Player):

    DirOutcome = pd.read_csv('BaseData/charting-m-stats-ShotDirOutcomes.csv')
    Overview = pd.read_csv('BaseData/charting-m-stats-Overview.csv')
    NetPoints = pd.read_csv('BaseData/charting-m-stats-NetPoints.csv')
    RallySize = pd.read_csv('BaseData/charting-m-stats-Rally.csv')
    KeyPServe = pd.read_csv('BaseData/charting-m-stats-KeyPointsServe.csv')
    KeyPReturn = pd.read_csv('BaseData/charting-m-stats-KeyPointsReturn.csv')

    DirOutcome = DirOutcome[DirOutcome['player'] == Player]

    Overview = Overview[Overview['player'] == Player]
    Overview.rename(columns={'set':'row'}, inplace=True)
    
    NetPoints = NetPoints[NetPoints['player'] == Player]
    KeyPServe = KeyPServe[KeyPServe['player'] == Player ]
    KeyPReturn = KeyPReturn[KeyPReturn['player'] == Player ]

    ServingRally, ReceivingRally = BuildRally(RallySize,data)

    S_Rally_dic = statsDiv(ServingRally)
    R_Rally_dic = statsDiv(ReceivingRally)
    Shots_dic = statsDiv(DirOutcome)
    Over_dic = statsDiv(Overview)
    Net_dic = statsDiv(NetPoints)
    KPS_dic = statsDiv(KeyPServe)
    KPR_dic = statsDiv(KeyPReturn)

    return S_Rally_dic,R_Rally_dic,Shots_dic,Over_dic,Net_dic,KPS_dic,KPR_dic
