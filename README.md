# Game supermarket war based on clustering Real-time Kmeans  
Project Supermarket war game (Promotion and marketing Analytic game)  
**Objective :**  
The objective of this game is Create games to help segment players who play the game accordingly.
Player's preferences according to the promotion category that the player chooses in the game.  
  
**Benefit :**  
- Help in Clustering before Segmentation customers according to customer interest (Interest) Benefits
Can be used in retail businesses that want to sell products that meet the needs of a more precise group  
- Save on cost acquisition  
- Help in making Product Recommendation can be more direct to the group, Cross sell, Upsales, Send promotion directly to the group, saving costs in sending Promotion to people who don't use it.  
- to divide the target audience before placing the the position of the brand of the product or service itself (Positioning) and and sell to that target group (Targeting)  
  
**Technique :**  
- Clustering Real-time by Cluster.Kmeans  
  
**Dataset :**  
Real-time data from the person at that moment.  
Feature  

        
        A0) Position in X axis => position X [1, 2, 3, 2, 1] / 5  
        A1) Position in Y axis => position Y [200, 150, 130, 170] / 4  
        A2) Number of Upselling count  
        A3) Number of Cross selling count  
        A4) Number of Discount count  
        A5) Number of Member count  
        A6) Number of Upselling count / Number of Upselling created  
        A7) Number of Cross selling count / Number of Cross selling created  
        A8) Number of Discount count / Number of Discount created  
        A9) Number of Member count / Number of Member created  
        
Promotion and enemy character in game :  
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.1.png" width="450" height="300" />   
  
Collect data every 1 second  
example :  
10 variable data  
First second : 570.60, 400.85, 7, 7, 7, 8, 0.63, 0.63, 0.63  
Seconds later: 572.12, 401.79, 7, 7, 8, 8, 0.63, 0.63, 0.66  
Find difference first and seconds : 1.52, 0.94, 0, 0, 1 ,0, 0, 0, 0, 0.03
  
  
## **Data achitecture**  
From the picture on the left, players will come to play games to get their favorite promotions. Player data is sent to netpie for analytic using scikit multiflow for real-time clustering using kmean. After analytic is done it is sent to netpie and sent to shop.  
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.2.png" width="450" height="300" />  
  
  
## **Predict**  
Use K-mean for 4 group Clustering   
labels[0]: 'Promotion Upselling',  
labels[1]: 'Promotion Cross selling',  
labels[2]: 'Promotion Discounts',  
labels[3]: 'Promotion For member',  
  
          def prediction_user_type(level, keyX_pressed_count, keyY_pressed_count, respawn_enemy_count, respawn_coin_count):
              global A0, A1
              a0 = statistics.mean(A0) if len(A0) else 0
              a1 = statistics.mean(A1) if len(A1) else 0
              a2 = destroyed_Upselling_count
              a3 = destroyed_Crossselling_count
              a4 = destroyed_Discount_count
              a5 = destroyed_Member_count
              a6 = respawn_UpsellPro_count
              a7 =  respawn_Crosssell_count
              a8 = respawn_Discount_count
              a9 = respawn_Member_count
              a10 = respawn_coin_count
              # a11 = a3/a9
              # a12 = a2/a10
              X = [[a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]]

              X_scale = dt_scaler.transform(X)
              y = decision_tree.predict(X_scale)[0]
              return LABELS.get(y)
  
  
Find Most User Type  
Rank by mean  
A2) Number of Upselling count  
A3) Number of Cross selling count  
A4) Number of Discount count  
A5) Number of Member count  

        def Fine_most_user_type(collect_somthing,PLAYER_NAME):
            import pandas as pd
            import numpy as np

            Total_df = pd.DataFrame (collect_somthing, columns = ['Name','A0','A1','A2','A3','A4','A5','A6','A7','A8','A9','y'])

            predict_user_type = Total_df.loc[Total_df['Name'] == PLAYER_NAME ].groupby('y').count()
            # print(predict_user_type)
            index_group = predict_user_type.index.values.tolist()


            mean_upsell = list(Total_df.groupby(['y']).mean()['A2'])
            mean_crossell = list(Total_df.groupby(['y']).mean()['A3'])
            mean_discount = list(Total_df.groupby(['y']).mean()['A4'])
            mean_member = list(Total_df.groupby(['y']).mean()['A5'])

            sorted_index_upsell = np.argsort(mean_upsell).tolist()[::-1]
            sorted_index_crossell = np.argsort(mean_crossell).tolist()[::-1]
            sorted_index_discount = np.argsort(mean_discount).tolist()[::-1]
            sorted_index_member = np.argsort(mean_member).tolist()[::-1]
            
## How to play the game  
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.3.png" width="450" height="300" /> <img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.4.png" width="450" height="300" />  
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.5.png" width="450" height="300" /> <img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.6.png" width="450" height="300" /> 
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.7.png" width="450" height="300" /> <img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.8.png" width="450" height="300" /> 




