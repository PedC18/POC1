import pandas as pd
   

# Pega todos os pontos dos jogos onde o jogador participou
# e divide em Won e Lost 
def PlayerPoints(player_name, points_data, player_matches):

    WonPoints = pd.DataFrame()
    LostPoints = pd.DataFrame()

    player_game_id = player_matches['match_id']
    
    for id in player_game_id:
        game = points_data[points_data['match_id'] == id]
        player_info = player_matches[player_matches['match_id'] == id]
        Player1 = player_info['Player 1'].unique()

        if(Player1 == player_name):
            PointsWon = game[game['PtWinner'] == 1]
            PointsLost = game[game['PtWinner'] == 2]
        else:
            PointsWon = game[game['PtWinner'] == 2]
            PointsLost = game[game['PtWinner'] == 1]
        
        WonPoints = pd.concat([WonPoints,PointsWon])
        LostPoints = pd.concat([LostPoints,PointsLost])
    
    return WonPoints.reset_index(drop=True), LostPoints.reset_index(drop=True)


    
# Pega todos os pontos dos jogos onde o jogador participou, 
# e retorna, divididos, os saques e as recepções

def PlayerServes(player_name, points_data, player_matches):
    
    Serves = pd.DataFrame()
    Receives = pd.DataFrame()

    player_game_id = player_matches['match_id']

    for id in player_game_id:
        game = points_data[points_data['match_id'] == id]
        player_info = player_matches[player_matches['match_id'] == id]
        Player1 = player_info['Player 1'].unique()

        if (Player1 == player_name):
            Serving = game[game['Svr'] == 1]
            Receiving = game[game['Svr'] == 2]
        else:
            Serving = game[game['Svr'] == 2]
            Receiving = game[game['Svr'] == 1]
        
        Serves = pd.concat([Serves,Serving])
        Receives = pd.concat([Receives,Receiving])
    
    return Serves.reset_index(drop=True), Receives.reset_index(drop=True)

