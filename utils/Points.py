import pandas as pd
   

# Pega todos os pontos dos jogos onde o jogador participou, 
# e retorna apenas os pontos do próprio jogador

def PlayerPoints(player_name, points_data, player_matches_data):
    
    Player_Points_Won = pd.DataFrame()
    Player_Points_Lost = pd.DataFrame()

    for _,row in player_matches_data.iterrows():
        Player1 = row['Player 1']
        game_points_data = points_data[points_data['match_id'] == row['match_id']]

        if(Player1 == player_name):
            Player_points_data_won = game_points_data[game_points_data['PtWinner'] == 1]
            Player_points_data_lost= game_points_data[game_points_data['PtWinner'] == 2]
        else:
            Player_points_data_won  = game_points_data[game_points_data['PtWinner'] == 2]
            Player_points_data_lost  = game_points_data[game_points_data['PtWinner'] == 1]
        
        Player_Points_Won = pd.concat([Player_Points_Won,Player_points_data_won])
        Player_Points_Lost = pd.concat([Player_Points_Lost,Player_points_data_lost])
    

    return Player_Points_Won,Player_Points_Lost

        
        
