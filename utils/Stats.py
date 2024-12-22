

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

    print(f'Aces => {float(AceRate[True])}')
    print(f'Winners => {float(WinRate[True])}')
    print(f'Forced Errors => {float(FERate[True])}')
    print(f'Unforced Errors => {float(UFERate[True])}')
    print(f'Double Faults => {float(DoubleFRate[True])} \n')
    
    return [float(WinRate[True]),float(AceRate[True]),float(DoubleFRate[True]),float(FERate[True]),float(UFERate[True])]