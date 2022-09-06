#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required libraries and functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# importing the datasets
anime = pd.read_csv('anime.csv')
rating = pd.read_csv('rating.csv')


# In[3]:


anime.rename(columns={'rating':'avg_rating'},inplace=True) # renaming the columns


# In[4]:


anime # checking the dataframe


# In[5]:


rating # checking the dataframe


# In[6]:


anime_df = anime.merge(rating, on='anime_id') # joining the two dataframes


# In[7]:


anime_df # checking missing values


# In[8]:


anime_df.isna().sum()  # checking missing values


# In[9]:


len(anime_df) # checking the length of dataframe


# In[10]:


anime_df.dropna(inplace=True) # dropping off all the missing values


# In[11]:


anime_df.isna().sum() # checking missing values


# In[12]:


anime_df # checking the cleaned dataframe


# In[13]:


anime_df.groupby('name').count().sort_values('user_id',ascending=False).head(10)['user_id'].describe() # checking for each anime, how many reviewers (user_id) viewed it


# ### On an average, each anime has around 30000 users who rated them

# In[14]:


user_rating_count_df = pd.DataFrame(anime_df.groupby('name').count()['user_id']).rename(columns={'user_id':'total_reviews'})  # making a dataframe of anime's name along with number of reviewrs


# In[15]:


user_rating_count_df # checking the above created dataframe


# In[16]:


anime_merged_df = anime_df.merge(user_rating_count_df, on='name') # merging the above created dataframe with the master dataframe


# ## EDA (Exploratory Data Analysis)

# In[17]:


anime_merged_df  # checking the master dataframe


# In[18]:


anime_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'] # checking the member base per anime


# In[19]:


anime_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'].plot(kind='bar',figsize=(12,6)) # plotting top 10 animes with highest member base
plt.xlabel('Names')
plt.ylabel('Members')
plt.title('Member base per anime')


# In[20]:


anime_merged_df.groupby('name').mean().sort_values('total_reviews',ascending=False).head(10)['total_reviews'].plot(kind='bar',figsize=(12,6)) # plotting top 10 animes with highest reviews
plt.xlabel('Names')
plt.ylabel('Total Review Counts')
plt.title('Total Review Counts per Anime')


# In[ ]:





# In[21]:


anime_merged_df.groupby('name').mean().sort_values('total_reviews',ascending=False).head(10)['total_reviews'] # checking top animes with highest review counts


# In[22]:


anime_merged_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'] # checking top animes with highest member base


# In[23]:


anime_merged_df # checking the dataframe


# In[24]:


anime_merged_df['members'].describe() # checking the descriptive stats for members


# ### On a median scale, an anime has memeber base of 110470 

# In[25]:


anime_merged_df['total_reviews'].describe() # checking the descriptive stats for total review


# ### On a median scale, an anime has been seen by 4368 users ~ 4500 users

# ## Finding authentic users

# In[26]:


anime_merged_df # checking the dataframe


# In[27]:


# grouping by user_id and taking its count (distinct animes using anime_id) and then renaming
user_count_df = anime_merged_df.groupby('user_id').count()[['anime_id']].rename(columns={'anime_id':'animes_reviewed_by_this_user'}) 


# In[28]:


user_count_df


# In[29]:


user_count_df['animes_reviewed_by_this_user'].describe() # checking the descriptive stats for animes reviewed by users


# In[30]:


plt.figure(figsize=(12,6))
sns.histplot(user_count_df, x='animes_reviewed_by_this_user',kde=True)
plt.xlim(0,150)
plt.xlabel('animes reviewed')
plt.ylabel('Number of users')
plt.title('Histogram of count animes being reviewed')


# ### Extreme left skewed

# In[31]:


user_count_df['animes_reviewed_by_this_user'].describe() # checking the descriptive stats for animes reviwed by a particular user


# ### On a median scale, one user has rated around 57 animes

# In[ ]:





# In[32]:


anime_merged_df = anime_merged_df.merge(user_count_df,on='user_id') # merging the master dataframe with the one with users and total animes reviewed by a user


# In[33]:


anime_merged_df # checking the master dataframe


# ### Most Credible user

# In[34]:


# grouping by user id and checking who had the most review counts
anime_merged_df.groupby('user_id').mean().sort_values('animes_reviewed_by_this_user',ascending=False).head(10)['animes_reviewed_by_this_user'].plot(kind='bar',figsize=(12,6))


# ### Let's choose only those samples which have a memeber base of more than 110470 and total_reviews more than 4500 and only those users who reviewed more than 57 movies

# In[35]:


anime_merged_df_2 = anime_merged_df.copy() # creating a copy of the master dataframe


# In[36]:


# slicing out the relevant samples on basis of being greater then median number of members, total_reviews and anime_reveiwed by a user
anime_merged_df_2 = anime_merged_df_2[(anime_merged_df_2['members'] > anime_merged_df_2['members'].median()) &
                                      (anime_merged_df_2['total_reviews'] > anime_merged_df_2['total_reviews'].median()) & 
                                      (anime_merged_df_2['animes_reviewed_by_this_user'] > anime_merged_df_2['animes_reviewed_by_this_user'].median()) ]


# In[37]:


anime_merged_df_2 # checking out the new cleaned master dataframe


# ### Highest rated animes by avg_rating

# ## Initially

# In[38]:


# plot of top 10 higest rated anime (using avg_rating)
anime_merged_df.groupby('name').mean().sort_values('avg_rating',ascending=False).head(10)['avg_rating'].plot(kind='bar',figsize=(12,6))
plt.xlabel('Name')
plt.ylabel('Avg Rating')
plt.title('Top Avg rated anime')


# ## After Cleaning

# In[39]:


# plot of top 10 higest rated anime (using avg_rating) after cleaning
anime_merged_df_2.groupby('name').mean().sort_values('avg_rating',ascending=False).head(10)['avg_rating'].plot(kind='bar',figsize=(12,6))
plt.xlabel('Name')
plt.ylabel('Avg Rating')
plt.title('Top Avg rated anime')


# ### Let's Create a weighted score on the basis of avg_ratings and memebers

# In[40]:


anime_merged_df_2 # checking the dataframe


# In[41]:


# getting all the required values
v = anime_merged_df_2['total_reviews']
R = anime_merged_df_2['avg_rating']
C = anime_merged_df_2['avg_rating'].mean()
m = anime_merged_df_2['avg_rating'].quantile(0.70) # only those samples whose 'avg_rating' is more than 70 percentile (by value)


# In[42]:


anime_merged_df_2['weighted_average'] = ((R*v) + (C*m))/ (v+m) # using the formula of weighted avergae


# In[43]:


from sklearn.preprocessing import MinMaxScaler # importing the normal scaling function


# In[44]:


sc = MinMaxScaler() # creating scaling function rating


# In[45]:


animes_scaled_df = sc.fit_transform(anime_merged_df_2[['weighted_average','members']]) # fit and transforming the required columns
animes_scaled_df = pd.DataFrame(anime_merged_df_2, columns=['weighted_average','members']) # creating a new dataframe
animes_scaled_df.head() # checking the scaled dataframe


# In[46]:


# adding the columns into our master dataframe
anime_merged_df_2['normalized_weight'] = animes_scaled_df['weighted_average'] 
anime_merged_df_2['normalized_members'] = animes_scaled_df['members']


# In[47]:


# evaluating the score giving 50% prefernce to normalized weight and 50% to normalized memebers
anime_merged_df_2['score'] = anime_merged_df_2['normalized_weight'] * 0.5 + anime_merged_df_2['normalized_members'] * 0.5 


# In[ ]:





# In[48]:


anime_merged_df_2


# In[ ]:





# In[49]:


anime_merged_df_2.groupby('name').mean().sort_values('score',ascending=False)[['score']] # checking animes with the top and bottom'score'


# ## Collaborative Filtering Using KNN

# In[50]:


# creating a pivot table having user_id as column and anime name as index with the value being rating
anime_pivot_table = anime_merged_df_2.pivot_table(index='name',columns='user_id',values='rating').fillna(0) 


# In[51]:


anime_pivot_table


# In[52]:


# comverting array matrix to sparse matrix because NearestNeighbors function can only work on csr matrix
from scipy.sparse import csr_matrix 
anime_featrures_df_matrix = csr_matrix(anime_pivot_table.values)


# In[54]:


from sklearn.neighbors import NearestNeighbors # importing NearestNeighbors function to find the cosine distances


# In[97]:


model_knn = NearestNeighbors(metric='cosine',algorithm='auto') # creating the instance of NearestNeighbors 


# In[98]:


model_knn.fit(anime_featrures_df_matrix) # fitting the knn model on the training set


# In[99]:


anime_featrures_df_matrix.shape


# In[100]:


# testing on a random sample point
query_index = np.random.choice(anime_pivot_table.shape[0]) # getting a random query_index in the range (0,405)
print(query_index)
distances, indices = model_knn.kneighbors(anime_pivot_table.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 10) # calculating distances and indices using our model on the query_index (set randomly)


# In[101]:


distances[0]


# In[102]:


for i in range(0, len(distances.flatten())): # in the range of flattened distances array (2D converted to 1D)
    if i == 0: # if the distance == 0 or if the name is the same name
        print(f'Recommendations for {anime_pivot_table.index[query_index]}:\n') 
    else:
        print(f'{i}: {anime_pivot_table.index[indices.flatten()[i]]}, with distance of {distances.flatten()[i]}:') # all the other anime names whose distance is greater than 0


# In[ ]:





# In[110]:


def anime_recommendation(title):
    '''
    Function which takes in anime name as title and gives out the recommended anime names
    '''
    distances, indices = model_knn.kneighbors(anime_pivot_table[anime_pivot_table.index == title].values.reshape(1, -1), n_neighbors = 10)
    for i in range(0, len(distances.flatten())):
        if i == 0:
            print(f'Recommendations for {title}:\n')
        else:
            print(f'{i}: {anime_pivot_table.index[indices.flatten()[i]]}, with cosine distance of {distances.flatten()[i]}:')


# In[111]:


anime_recommendation('Naruto')


# In[112]:


anime_recommendation('Death Note')


# In[113]:


anime_recommendation('One Punch Man')


# In[114]:


anime_recommendation('Kuroko no Basket')


# ### I was expecting more sports anime in this list

# ## Let's Try using Content based filtering

# In[68]:


anime_merged_df


# In[69]:


anime_merged_df_2['number_of_genre'] = anime_merged_df['genre'].apply(lambda x: len(x.split(','))) # checking the count of each genre for each row


# In[70]:


anime_merged_df_2 


# In[71]:


anime_merged_df_2['number_of_genre'].describe() 


# #### On an average an anime has 5 genre

# In[72]:


anime_merged_df_2


# ### We can use TFidf on genre for this

# In[73]:


from sklearn.feature_extraction.text import TfidfVectorizer # importing the tfidf function


# In[74]:


tfidf = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode", analyzer="word",token_pattern=r"\w{1,}", ngram_range=(1, 3), stop_words = "english") # creating tfidf instance


# In[76]:


vec_df = anime_merged_df.copy() # making a copy of the master anime dataframe


# In[77]:


vec_df.drop_duplicates(subset ="name", keep = "first", inplace = True) # dropping duplicates from the 'name' columns and keeps only the first instance


# In[78]:


vec_df.reset_index(drop=True,inplace=True) # resetting and dropping the index


# In[79]:


vec_df


# ### Implementing weighted average score for final sorting of the recommended list purpose

# In[80]:


# getting all the required values
v = vec_df['total_reviews']
R = vec_df['avg_rating']
C = vec_df['avg_rating'].mean()
m = vec_df['avg_rating'].quantile(0.70) # only those samples whose 'veot_avergae' is more than 70 percentile (by value)
vec_df['weighted_average'] = ((R*v) + (C*m))/ (v+m) # using the formula for weighted average


# In[81]:


from sklearn.preprocessing import MinMaxScaler  # importing the function
sc = MinMaxScaler() # creating the scaling function instance
animes_scaled_df = sc.fit_transform(vec_df[['weighted_average','members']]) # fit and transform the required column
animes_scaled_df = pd.DataFrame(vec_df, columns=['weighted_average','members']) # creating the dataframe containing normalized weight and memebers

vec_df['normalized_weight'] = animes_scaled_df['weighted_average'] # adding the column for normalized weight
vec_df['normalized_members'] = animes_scaled_df['members'] # adding the column for normalized members
vec_df['score'] = vec_df['normalized_weight'] * 0.5 + vec_df['normalized_members'] * 0.5 # final score gives 50% weightage to normalized weight and normalized memebers


# In[ ]:





# In[82]:


genre_anime = vec_df["genre"].str.split(", | , | ,").astype(str) # splitting out into a list of  different genres contained in the genre column of the vec_df dataframe


# In[134]:


genre_anime


# In[83]:


tfidf_matrix = tfidf.fit_transform(genre_anime) # creating a sparse matrix for tfidf vectorized 'genre'


# In[85]:


tfidf_matrix.shape 


# In[86]:


tfidf_matrix


# ### We need the output for each sample to be in the range(0,1), so we'll use sigmoid function

# In[87]:


from sklearn.metrics.pairwise import sigmoid_kernel # importing the sigmoid_kernel function 


# In[88]:


sig = sigmoid_kernel(tfidf_matrix, tfidf_matrix) # compute the sigmoid kernel


# In[89]:


sig[0]


# In[119]:


indices = pd.Series(vec_df.index, index=vec_df['name']).drop_duplicates() # reverse mapping of indices and movie titles


# In[120]:


indices


# In[129]:


def give_anime_recommendation(title, sig = sig):
    
    idx = indices[title] # Getting index corresponding to original_title

    sig_score = list(enumerate(sig[idx]))  # Getting pairwsie similarity scores 
    sig_score = sorted(sig_score, key=lambda x: x[1], reverse=True)
    sig_score = sig_score[1:11]
    anime_indices = [i[0] for i in sig_score]
     
    # Top 10 most similar movies
    rec_dic = { "Anime Name" : vec_df["name"].iloc[anime_indices].values,"Rating" : vec_df["avg_rating"].iloc[anime_indices].values, 'Genre': vec_df["genre"].iloc[anime_indices].values,
              'Scaled Score': vec_df['score'].iloc[anime_indices].values}
    rec_df = pd.DataFrame(data = rec_dic)
    rec_df = rec_df.sort_values(by=['Scaled Score', 'Rating'],ascending=False)
    rec_df.index = np.arange(1,11)
    
    print(f"Recommendations for {title} viewers :\n")
    
    return rec_df


# In[130]:


give_anime_recommendation('Naruto')


# In[131]:


give_anime_recommendation('Kuroko no Basket')


# ### A lot of 'relevant' sports animes

# In[132]:


give_anime_recommendation('Death Note')


# In[133]:


give_anime_recommendation('Dragon Ball')


# # Conclusion:
# ### The content based filtering method outperformed the collabrative filtering (based on KNN).

# In[ ]:




