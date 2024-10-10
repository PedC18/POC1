import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ResumePointsStats(data, columns):
    total = len(data)
    result = []
    for column in columns:
        aux = data[data[column] == True]

        true = len(aux)

        Percentage = true/total
        Percentage = round(Percentage,2)

        result.append(Percentage)
    
    return result

# Make a function that calculates the way the point was won

# Make a function that specifically calculates serve stats

def ResumeServeStats(data):
    FirstIn = data[data['1stIn'] == True]
    FirstOut = data[data['1stIn'] == False]

    
    SecondIn = FirstOut[FirstOut['2ndIn'] == True]

   
    FirstIn_Percent = len(FirstIn)/len(data)
    SecondIn_Percent = len(SecondIn)/len(FirstOut)


    print(f'1stIn percentage : {FirstIn_Percent}')
    print(f'2ndIn percentage : {SecondIn_Percent}')


def PlotGraph(data,surface, columns, won):

    Federer_Clay_Points = data[0][data[0]['Surface'] == surface]
    Djokovic_Clay_Points = data[1][data[1]['Surface'] == surface]
    Nadal_Clay_Points = data[2][data[2]['Surface'] == surface]

    FedererStats = ResumePointsStats(Federer_Clay_Points,columns)
    DjokovicStats = ResumePointsStats(Djokovic_Clay_Points,columns)
    NadalStats = ResumePointsStats(Nadal_Clay_Points,columns)

    PtCodes = ['Ace', 'Unreturned', 'Winners','Forced Error', 'Unforced Error', 'Double Fault']

    barWidth = 0.25
    br1 = np.arange(len(FedererStats)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2]
    
    plt.subplots(figsize =(8, 4))
    plt.bar(br1, FedererStats, color= 'blue', alpha = 0.7,
            width = barWidth)
    plt.bar(br2, DjokovicStats, color= 'green', alpha = 0.7,
            width = barWidth)
    plt.bar(br3, NadalStats, color= 'red', alpha = 0.7,
            width = barWidth)
    
    plt.xticks([r + barWidth for r in range(len(FedererStats))], 
            PtCodes)
    
    plt.ylabel("Percentages")
    plt.title(f"Result of Points {won} in {surface} by the Big 3")
    plt.legend(['Federer','Djokovic','Nadal'])

    plt.show()

