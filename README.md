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
<img src="https://github.com/KodchakornL/Project-Supermarket-war-game/blob/main/slide_ppt/picture_No.1.png" width="450" height="250" />   
  
**Technique :**  
- Clustering Real-time by Cluster.Kmeans  


**Data achitecture**  
From the picture on the left, players will come to play games to get their favorite promotions. Player data is sent to netpie for analytic using scikit multiflow for real-time clustering using kmean. After analytic is done it is sent to netpie and sent to shop.  


