

def ResumeStats(data, columns):
    for column in columns:
        aux = data[column].value_counts()

        true = aux.iloc[1]
        total = aux.iloc[0] + aux.iloc[1]

        Percentage = true/total

        print(f'{column} percentage : {Percentage}')

# Make a function that calculates the way the point was won

# Make a function that specifically calculates serve stats