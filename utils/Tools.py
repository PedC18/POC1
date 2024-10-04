

def ResumePointsStats(data, columns):
    total = len(data)
    for column in columns:
        aux = data[data[column] == True]

        true = len(aux)

        Percentage = true/total

        print(f'{column} percentage : {Percentage}')

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


def ReturnTerrain(data):
    
    Clay = data[data['Surface'] == 'Clay']
    Grass = data[data['Surface'] == 'Grass']
    Hard = data[data['Surface'] == 'Hard']

    return Hard, Clay, Grass
