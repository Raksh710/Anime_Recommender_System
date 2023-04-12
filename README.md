# Anime_Recommender_System
Recommends Anime using Content based filtering. <br>

Built Anime Recommender System using Content-based filtering and then finding the top 10 recommendations, sorted using Weighted Hybrid technique modelled on total reviews, review sentiment and average rating. <br>
OpenAI API was used for creating “embeddings” which was performed on string column which concatenated ‘Synopsis’ and ‘Genre’ column and on this basis, similarity was calculated using cosine similarity on the embedding vector. <br>
The model was deployed using Salesforce Heroku. Also, built its docker image and pushed it to DockerHub


Link to my Kaggle Notebook: https://www.kaggle.com/raksh710/content-based-filtering-sorted-by-weighted-average <br>
The link to the Kaggle Dataset: https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database?datasetId=571 <br>

**Assessing the performance of the recommender system.**
[This link could be helpful](https://analyticsindiamag.com/how-to-measure-the-success-of-a-recommendation-system/#:~:text=your%20business%20goal.-,Common%20Metrics%20Used,evaluation%20metrics%20for%20recommender%20systems.)

As per the above mentioned source, getting data on CTR (Click Through Rate) we can assess the system.
<br>

<img src="Demo Pic of the final Product.jpg">

<br>
<img src="static/poster.jpg">
