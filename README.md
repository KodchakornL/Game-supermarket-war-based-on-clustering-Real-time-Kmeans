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
  
**Technique :**  
- Clustering Real-time by Cluster.Kmeans  


**Data achitecture**  
From the picture on the left, players will come to play games to get their favorite promotions. Player data is sent to netpie for analytic using scikit multiflow for real-time clustering using kmean. After analytic is done it is sent to netpie and sent to shop.  


**Predict**  
Use K-mean for 4 group Clustering   
labels[0]: 'Promotion Upselling',  
labels[1]: 'Promotion Cross selling',  
labels[2]: 'Promotion Discounts',  
labels[3]: 'Promotion For member',  

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
