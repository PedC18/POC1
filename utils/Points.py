import pandas as pd
from utils.Tools import Translate
   
def DivisionSets(Points,ids):
    SetPerMatches = {}
    for id in ids:
        Match = Points[Points['match_id'] == id]
        Sets_Matrix = []
        size = int(max(Match['Set#']))

        for i in Match['Set#'].unique():
            Set = Match[Match['Set#'] == i]

            Rallys = []
            for _,row in Set.iterrows():
            
                if(row['2nd'] == 'False'):
                    Rallys.append(row['1st'])
                else:
                    Rallys.append(row['2nd']) 
                    
            Sets_Matrix.append(Rallys)
        
        SetPerMatches[id] = Sets_Matrix
    
    return SetPerMatches

def DivisionGames(Points,ids):
    GamesPerMatches = {}
    for id in ids:
        Match = Points[Points['match_id'] == id]
        
        Games_Matrix = []
        size = int(max(Match['Gm#']))
        
        for i in Match['Gm#'].unique():
            Game = Match[Match['Gm#'] == i]

            Rallys = []
            for _,row in Game.iterrows():
            
                if(row['2nd'] == 'False'):
                    Rallys.append(row['1st'])
                else:
                    Rallys.append(row['2nd'])

            Games_Matrix.append(Rallys)
        
        GamesPerMatches[id] = Games_Matrix
    
    return GamesPerMatches

def RallyParsing(s,dic):
    Sequence = []
    text = Translate(s=s)
    serve = text[0]
    rally = text[1:len(text)-1]
    end = text[-1]
    
    
    if(len(text) == 2):
        Sequence.append(dic[serve])
        
        if(end == '*'):
            Sequence.append('Ace')
        else:
            Sequence.append(dic[end])

        return Sequence

    Sequence.append(dic[serve])

    if rally != '':
        rallyShots = rally[::2]
        rallyDir = rally[1::2]
        for i in range(len(rallyShots)):
            if(i == len(rallyDir)):
                Sequence.append(dic[rallyShots[i]])
            else:
                Sequence.append(dic[rallyShots[i]] + dic[rallyDir[i]])

    Sequence.append(dic[end])
    return Sequence

