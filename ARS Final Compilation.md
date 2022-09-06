```python
# importing the required libraries and functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# importing the datasets
anime = pd.read_csv('anime.csv')
rating = pd.read_csv('rating.csv')
```


```python
anime.rename(columns={'rating':'avg_rating'},inplace=True) # renaming the columns
```


```python
anime # checking the dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28977</td>
      <td>Gintama°</td>
      <td>Action, Comedy, Historical, Parody, Samurai, S...</td>
      <td>TV</td>
      <td>51</td>
      <td>9.25</td>
      <td>114262</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9969</td>
      <td>Gintama&amp;#039;</td>
      <td>Action, Comedy, Historical, Parody, Samurai, S...</td>
      <td>TV</td>
      <td>51</td>
      <td>9.16</td>
      <td>151266</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>12289</th>
      <td>9316</td>
      <td>Toushindai My Lover: Minami tai Mecha-Minami</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.15</td>
      <td>211</td>
    </tr>
    <tr>
      <th>12290</th>
      <td>5543</td>
      <td>Under World</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.28</td>
      <td>183</td>
    </tr>
    <tr>
      <th>12291</th>
      <td>5621</td>
      <td>Violence Gekiga David no Hoshi</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>4</td>
      <td>4.88</td>
      <td>219</td>
    </tr>
    <tr>
      <th>12292</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
    </tr>
    <tr>
      <th>12293</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
    </tr>
  </tbody>
</table>
<p>12294 rows × 7 columns</p>
</div>




```python
rating # checking the dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>anime_id</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>20</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>24</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>79</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>226</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>241</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813732</th>
      <td>73515</td>
      <td>16512</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7813733</th>
      <td>73515</td>
      <td>17187</td>
      <td>9</td>
    </tr>
    <tr>
      <th>7813734</th>
      <td>73515</td>
      <td>22145</td>
      <td>10</td>
    </tr>
    <tr>
      <th>7813735</th>
      <td>73516</td>
      <td>790</td>
      <td>9</td>
    </tr>
    <tr>
      <th>7813736</th>
      <td>73516</td>
      <td>8074</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
<p>7813737 rows × 3 columns</p>
</div>




```python
anime_df = anime.merge(rating, on='anime_id') # joining the two dataframes
```


```python
anime_df # checking missing values
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>152</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>244</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>271</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>278</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813722</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>39532</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813723</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>48766</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813724</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>60365</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813725</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>27364</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813726</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>48766</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>7813727 rows × 9 columns</p>
</div>




```python
anime_df.isna().sum()  # checking missing values
```




    anime_id        0
    name            0
    genre         110
    type            4
    episodes        0
    avg_rating      6
    members         0
    user_id         0
    rating          0
    dtype: int64




```python
len(anime_df) # checking the length of dataframe
```




    7813727




```python
anime_df.dropna(inplace=True) # dropping off all the missing values
```


```python
anime_df.isna().sum() # checking missing values
```




    anime_id      0
    name          0
    genre         0
    type          0
    episodes      0
    avg_rating    0
    members       0
    user_id       0
    rating        0
    dtype: int64




```python
anime_df # checking the cleaned dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>152</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>244</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>271</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>278</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813722</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>39532</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813723</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>48766</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813724</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>60365</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813725</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>27364</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>7813726</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>48766</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 9 columns</p>
</div>




```python
anime_df.groupby('name').count().sort_values('user_id',ascending=False).head(10)['user_id'].describe() # checking for each anime, how many reviewers (user_id) viewed it
```




    count       10.000000
    mean     28172.800000
    std       4436.430116
    min      24283.000000
    25%      25255.250000
    50%      27344.500000
    75%      29117.500000
    max      39340.000000
    Name: user_id, dtype: float64



### On an average, each anime has around 30000 users who rated them


```python
user_rating_count_df = pd.DataFrame(anime_df.groupby('name').count()['user_id']).rename(columns={'user_id':'total_reviews'})  # making a dataframe of anime's name along with number of reviewrs
```


```python
user_rating_count_df # checking the above created dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_reviews</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&amp;quot;0&amp;quot;</th>
      <td>26</td>
    </tr>
    <tr>
      <th>&amp;quot;Aesop&amp;quot; no Ohanashi yori: Ushi to Kaeru, Yokubatta Inu</th>
      <td>2</td>
    </tr>
    <tr>
      <th>&amp;quot;Bungaku Shoujo&amp;quot; Kyou no Oyatsu: Hatsukoi</th>
      <td>782</td>
    </tr>
    <tr>
      <th>&amp;quot;Bungaku Shoujo&amp;quot; Memoire</th>
      <td>809</td>
    </tr>
    <tr>
      <th>&amp;quot;Bungaku Shoujo&amp;quot; Movie</th>
      <td>1535</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>xxxHOLiC Kei</th>
      <td>3413</td>
    </tr>
    <tr>
      <th>xxxHOLiC Movie: Manatsu no Yoru no Yume</th>
      <td>2365</td>
    </tr>
    <tr>
      <th>xxxHOLiC Rou</th>
      <td>1513</td>
    </tr>
    <tr>
      <th>xxxHOLiC Shunmuki</th>
      <td>1974</td>
    </tr>
    <tr>
      <th>◯</th>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>11161 rows × 1 columns</p>
</div>




```python
anime_merged_df = anime_df.merge(user_rating_count_df, on='name') # merging the above created dataframe with the master dataframe
```

## EDA (Exploratory Data Analysis)


```python
anime_merged_df  # checking the master dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>152</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>244</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>271</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>278</td>
      <td>-1</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813606</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>39532</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813607</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>48766</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813608</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>60365</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813609</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>27364</td>
      <td>-1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7813610</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>48766</td>
      <td>-1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 10 columns</p>
</div>




```python
anime_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'] # checking the member base per anime
```




    name
    Death Note                          1013917.0
    Shingeki no Kyojin                   896229.0
    Sword Art Online                     893100.0
    Fullmetal Alchemist: Brotherhood     793665.0
    Angel Beats!                         717796.0
    Code Geass: Hangyaku no Lelouch      715151.0
    Naruto                               683297.0
    Steins;Gate                          673572.0
    Mirai Nikki (TV)                     657190.0
    Toradora!                            633817.0
    Name: members, dtype: float64




```python
anime_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'].plot(kind='bar',figsize=(12,6)) # plotting top 10 animes with highest member base
plt.xlabel('Names')
plt.ylabel('Members')
plt.title('Member base per anime')
```




    Text(0.5, 1.0, 'Member base per anime')




    
![png](output_20_1.png)
    



```python
anime_merged_df.groupby('name').mean().sort_values('total_reviews',ascending=False).head(10)['total_reviews'].plot(kind='bar',figsize=(12,6)) # plotting top 10 animes with highest reviews
plt.xlabel('Names')
plt.ylabel('Total Review Counts')
plt.title('Total Review Counts per Anime')
```




    Text(0.5, 1.0, 'Total Review Counts per Anime')




    
![png](output_21_1.png)
    



```python

```


```python
anime_merged_df.groupby('name').mean().sort_values('total_reviews',ascending=False).head(10)['total_reviews'] # checking top animes with highest review counts
```




    name
    Death Note                          39340.0
    Sword Art Online                    30583.0
    Shingeki no Kyojin                  29584.0
    Code Geass: Hangyaku no Lelouch     27718.0
    Elfen Lied                          27506.0
    Angel Beats!                        27183.0
    Naruto                              25925.0
    Fullmetal Alchemist                 25032.0
    Fullmetal Alchemist: Brotherhood    24574.0
    Toradora!                           24283.0
    Name: total_reviews, dtype: float64




```python
anime_merged_df.groupby('name').mean().sort_values('members',ascending=False).head(10)['members'] # checking top animes with highest member base
```




    name
    Death Note                          1013917.0
    Shingeki no Kyojin                   896229.0
    Sword Art Online                     893100.0
    Fullmetal Alchemist: Brotherhood     793665.0
    Angel Beats!                         717796.0
    Code Geass: Hangyaku no Lelouch      715151.0
    Naruto                               683297.0
    Steins;Gate                          673572.0
    Mirai Nikki (TV)                     657190.0
    Toradora!                            633817.0
    Name: members, dtype: float64




```python
anime_merged_df # checking the dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>152</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>244</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>271</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>278</td>
      <td>-1</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813606</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>39532</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813607</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>48766</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813608</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>60365</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813609</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>27364</td>
      <td>-1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7813610</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>48766</td>
      <td>-1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 10 columns</p>
</div>




```python
anime_merged_df['members'].describe() # checking the descriptive stats for members
```




    count    7.813611e+06
    mean     1.786234e+05
    std      1.881766e+05
    min      2.900000e+01
    25%      4.403000e+04
    50%      1.104700e+05
    75%      2.442680e+05
    max      1.013917e+06
    Name: members, dtype: float64



### On a median scale, an anime has memeber base of 110470 


```python
anime_merged_df['total_reviews'].describe() # checking the descriptive stats for total review
```




    count    7.813611e+06
    mean     6.596039e+03
    std      6.782732e+03
    min      1.000000e+00
    25%      1.760000e+03
    50%      4.368000e+03
    75%      9.191000e+03
    max      3.934000e+04
    Name: total_reviews, dtype: float64



### On a median scale, an anime has been seen by 4368 users ~ 4500 users

## Finding authentic users


```python
anime_merged_df # checking the dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>152</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>244</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>271</td>
      <td>10</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>278</td>
      <td>-1</td>
      <td>2199</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813606</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>39532</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813607</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>48766</td>
      <td>-1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813608</th>
      <td>6133</td>
      <td>Violence Gekiga Shin David no Hoshi: Inma Dens...</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.98</td>
      <td>175</td>
      <td>60365</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7813609</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>27364</td>
      <td>-1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7813610</th>
      <td>26081</td>
      <td>Yasuji no Pornorama: Yacchimae!!</td>
      <td>Hentai</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.46</td>
      <td>142</td>
      <td>48766</td>
      <td>-1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 10 columns</p>
</div>




```python
# grouping by user_id and taking its count (distinct animes using anime_id) and then renaming
user_count_df = anime_merged_df.groupby('user_id').count()[['anime_id']].rename(columns={'anime_id':'animes_reviewed_by_this_user'}) 
```


```python
user_count_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>153</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>94</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
    </tr>
    <tr>
      <th>5</th>
      <td>467</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>73512</th>
      <td>13</td>
    </tr>
    <tr>
      <th>73513</th>
      <td>33</td>
    </tr>
    <tr>
      <th>73514</th>
      <td>1</td>
    </tr>
    <tr>
      <th>73515</th>
      <td>196</td>
    </tr>
    <tr>
      <th>73516</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>73515 rows × 1 columns</p>
</div>




```python
user_count_df['animes_reviewed_by_this_user'].describe() # checking the descriptive stats for animes reviewed by users
```




    count    73515.000000
    mean       106.285942
    std        153.074216
    min          1.000000
    25%         18.000000
    50%         57.000000
    75%        136.000000
    max      10225.000000
    Name: animes_reviewed_by_this_user, dtype: float64




```python
plt.figure(figsize=(12,6))
sns.histplot(user_count_df, x='animes_reviewed_by_this_user',kde=True)
plt.xlim(0,150)
plt.xlabel('animes reviewed')
plt.ylabel('Number of users')
plt.title('Histogram of count animes being reviewed')
```




    Text(0.5, 1.0, 'Histogram of count animes being reviewed')




    
![png](output_35_1.png)
    


### Extreme left skewed


```python
user_count_df['animes_reviewed_by_this_user'].describe() # checking the descriptive stats for animes reviwed by a particular user
```




    count    73515.000000
    mean       106.285942
    std        153.074216
    min          1.000000
    25%         18.000000
    50%         57.000000
    75%        136.000000
    max      10225.000000
    Name: animes_reviewed_by_this_user, dtype: float64



### On a median scale, one user has rated around 57 animes


```python

```


```python
anime_merged_df = anime_merged_df.merge(user_count_df,on='user_id') # merging the master dataframe with the one with users and total animes reviewed by a user
```


```python
anime_merged_df # checking the master dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
      <td>131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>99</td>
      <td>10</td>
      <td>24574</td>
      <td>131</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>99</td>
      <td>9</td>
      <td>19283</td>
      <td>131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4181</td>
      <td>Clannad: After Story</td>
      <td>Drama, Fantasy, Romance, Slice of Life, Supern...</td>
      <td>TV</td>
      <td>24</td>
      <td>9.06</td>
      <td>456749</td>
      <td>99</td>
      <td>10</td>
      <td>17854</td>
      <td>131</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2904</td>
      <td>Code Geass: Hangyaku no Lelouch R2</td>
      <td>Action, Drama, Mecha, Military, Sci-Fi, Super ...</td>
      <td>TV</td>
      <td>25</td>
      <td>8.98</td>
      <td>572888</td>
      <td>99</td>
      <td>9</td>
      <td>24242</td>
      <td>131</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813606</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>14133</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813607</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>40914</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813608</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>40965</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813609</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>55932</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813610</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>64425</td>
      <td>-1</td>
      <td>2475</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 11 columns</p>
</div>



### Most Credible user


```python
# grouping by user id and checking who had the most review counts
anime_merged_df.groupby('user_id').mean().sort_values('animes_reviewed_by_this_user',ascending=False).head(10)['animes_reviewed_by_this_user'].plot(kind='bar',figsize=(12,6))
```




    <AxesSubplot:xlabel='user_id'>




    
![png](output_43_1.png)
    


### Let's choose only those samples which have a memeber base of more than 110470 and total_reviews more than 4500 and only those users who reviewed more than 57 movies


```python
anime_merged_df_2 = anime_merged_df.copy() # creating a copy of the master dataframe
```


```python
# slicing out the relevant samples on basis of being greater then median number of members, total_reviews and anime_reveiwed by a user
anime_merged_df_2 = anime_merged_df_2[(anime_merged_df_2['members'] > anime_merged_df_2['members'].median()) &
                                      (anime_merged_df_2['total_reviews'] > anime_merged_df_2['total_reviews'].median()) & 
                                      (anime_merged_df_2['animes_reviewed_by_this_user'] > anime_merged_df_2['animes_reviewed_by_this_user'].median()) ]
```


```python
anime_merged_df_2 # checking out the new cleaned master dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>244</td>
      <td>10</td>
      <td>24574</td>
      <td>277</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>244</td>
      <td>10</td>
      <td>19283</td>
      <td>277</td>
    </tr>
    <tr>
      <th>277</th>
      <td>23273</td>
      <td>Shigatsu wa Kimi no Uso</td>
      <td>Drama, Music, Romance, School, Shounen</td>
      <td>TV</td>
      <td>22</td>
      <td>8.92</td>
      <td>416397</td>
      <td>244</td>
      <td>10</td>
      <td>9448</td>
      <td>277</td>
    </tr>
    <tr>
      <th>278</th>
      <td>12355</td>
      <td>Ookami Kodomo no Ame to Yuki</td>
      <td>Fantasy, Slice of Life</td>
      <td>Movie</td>
      <td>1</td>
      <td>8.84</td>
      <td>226193</td>
      <td>244</td>
      <td>9</td>
      <td>7709</td>
      <td>277</td>
    </tr>
    <tr>
      <th>279</th>
      <td>30276</td>
      <td>One Punch Man</td>
      <td>Action, Comedy, Parody, Sci-Fi, Seinen, Super ...</td>
      <td>TV</td>
      <td>12</td>
      <td>8.82</td>
      <td>552458</td>
      <td>244</td>
      <td>9</td>
      <td>13374</td>
      <td>277</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7748647</th>
      <td>6205</td>
      <td>Kämpfer</td>
      <td>Action, Comedy, Ecchi, Romance, School, Shoujo...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.73</td>
      <td>146631</td>
      <td>24918</td>
      <td>7</td>
      <td>6595</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748649</th>
      <td>8861</td>
      <td>Yosuga no Sora: In Solitude, Where We Are Leas...</td>
      <td>Drama, Ecchi, Harem, Romance</td>
      <td>TV</td>
      <td>12</td>
      <td>6.72</td>
      <td>173216</td>
      <td>24918</td>
      <td>6</td>
      <td>6687</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748659</th>
      <td>4975</td>
      <td>ChäoS;HEAd</td>
      <td>Harem, Mystery, Psychological, Sci-Fi, Superna...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.62</td>
      <td>174337</td>
      <td>24918</td>
      <td>8</td>
      <td>7862</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748668</th>
      <td>6682</td>
      <td>11eyes</td>
      <td>Action, Ecchi, Super Power, Supernatural</td>
      <td>TV</td>
      <td>12</td>
      <td>6.49</td>
      <td>133971</td>
      <td>24918</td>
      <td>8</td>
      <td>5846</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748679</th>
      <td>2476</td>
      <td>School Days</td>
      <td>Drama, Harem, Romance, School</td>
      <td>TV</td>
      <td>12</td>
      <td>6.17</td>
      <td>279183</td>
      <td>24918</td>
      <td>7</td>
      <td>12417</td>
      <td>229</td>
    </tr>
  </tbody>
</table>
<p>1449228 rows × 11 columns</p>
</div>



### Highest rated animes by avg_rating

## Initially


```python
# plot of top 10 higest rated anime (using avg_rating)
anime_merged_df.groupby('name').mean().sort_values('avg_rating',ascending=False).head(10)['avg_rating'].plot(kind='bar',figsize=(12,6))
plt.xlabel('Name')
plt.ylabel('Avg Rating')
plt.title('Top Avg rated anime')
```




    Text(0.5, 1.0, 'Top Avg rated anime')




    
![png](output_50_1.png)
    


## After Cleaning


```python
# plot of top 10 higest rated anime (using avg_rating) after cleaning
anime_merged_df_2.groupby('name').mean().sort_values('avg_rating',ascending=False).head(10)['avg_rating'].plot(kind='bar',figsize=(12,6))
plt.xlabel('Name')
plt.ylabel('Avg Rating')
plt.title('Top Avg rated anime')
```




    Text(0.5, 1.0, 'Top Avg rated anime')




    
![png](output_52_1.png)
    


### Let's Create a weighted score on the basis of avg_ratings and memebers


```python
anime_merged_df_2 # checking the dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>244</td>
      <td>10</td>
      <td>24574</td>
      <td>277</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>244</td>
      <td>10</td>
      <td>19283</td>
      <td>277</td>
    </tr>
    <tr>
      <th>277</th>
      <td>23273</td>
      <td>Shigatsu wa Kimi no Uso</td>
      <td>Drama, Music, Romance, School, Shounen</td>
      <td>TV</td>
      <td>22</td>
      <td>8.92</td>
      <td>416397</td>
      <td>244</td>
      <td>10</td>
      <td>9448</td>
      <td>277</td>
    </tr>
    <tr>
      <th>278</th>
      <td>12355</td>
      <td>Ookami Kodomo no Ame to Yuki</td>
      <td>Fantasy, Slice of Life</td>
      <td>Movie</td>
      <td>1</td>
      <td>8.84</td>
      <td>226193</td>
      <td>244</td>
      <td>9</td>
      <td>7709</td>
      <td>277</td>
    </tr>
    <tr>
      <th>279</th>
      <td>30276</td>
      <td>One Punch Man</td>
      <td>Action, Comedy, Parody, Sci-Fi, Seinen, Super ...</td>
      <td>TV</td>
      <td>12</td>
      <td>8.82</td>
      <td>552458</td>
      <td>244</td>
      <td>9</td>
      <td>13374</td>
      <td>277</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7748647</th>
      <td>6205</td>
      <td>Kämpfer</td>
      <td>Action, Comedy, Ecchi, Romance, School, Shoujo...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.73</td>
      <td>146631</td>
      <td>24918</td>
      <td>7</td>
      <td>6595</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748649</th>
      <td>8861</td>
      <td>Yosuga no Sora: In Solitude, Where We Are Leas...</td>
      <td>Drama, Ecchi, Harem, Romance</td>
      <td>TV</td>
      <td>12</td>
      <td>6.72</td>
      <td>173216</td>
      <td>24918</td>
      <td>6</td>
      <td>6687</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748659</th>
      <td>4975</td>
      <td>ChäoS;HEAd</td>
      <td>Harem, Mystery, Psychological, Sci-Fi, Superna...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.62</td>
      <td>174337</td>
      <td>24918</td>
      <td>8</td>
      <td>7862</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748668</th>
      <td>6682</td>
      <td>11eyes</td>
      <td>Action, Ecchi, Super Power, Supernatural</td>
      <td>TV</td>
      <td>12</td>
      <td>6.49</td>
      <td>133971</td>
      <td>24918</td>
      <td>8</td>
      <td>5846</td>
      <td>229</td>
    </tr>
    <tr>
      <th>7748679</th>
      <td>2476</td>
      <td>School Days</td>
      <td>Drama, Harem, Romance, School</td>
      <td>TV</td>
      <td>12</td>
      <td>6.17</td>
      <td>279183</td>
      <td>24918</td>
      <td>7</td>
      <td>12417</td>
      <td>229</td>
    </tr>
  </tbody>
</table>
<p>1449228 rows × 11 columns</p>
</div>




```python
# getting all the required values
v = anime_merged_df_2['total_reviews']
R = anime_merged_df_2['avg_rating']
C = anime_merged_df_2['avg_rating'].mean()
m = anime_merged_df_2['avg_rating'].quantile(0.70) # only those samples whose 'avg_rating' is more than 70 percentile (by value)
```


```python
anime_merged_df_2['weighted_average'] = ((R*v) + (C*m))/ (v+m) # using the formula of weighted avergae
```


```python
from sklearn.preprocessing import MinMaxScaler # importing the normal scaling function
```


```python
sc = MinMaxScaler() # creating scaling function rating
```


```python
animes_scaled_df = sc.fit_transform(anime_merged_df_2[['weighted_average','members']]) # fit and transforming the required columns
animes_scaled_df = pd.DataFrame(anime_merged_df_2, columns=['weighted_average','members']) # creating a new dataframe
animes_scaled_df.head() # checking the scaled dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weighted_average</th>
      <th>members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>9.259561</td>
      <td>793665</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9.169479</td>
      <td>673572</td>
    </tr>
    <tr>
      <th>277</th>
      <td>8.919156</td>
      <td>416397</td>
    </tr>
    <tr>
      <th>278</th>
      <td>8.839051</td>
      <td>226193</td>
    </tr>
    <tr>
      <th>279</th>
      <td>8.819465</td>
      <td>552458</td>
    </tr>
  </tbody>
</table>
</div>




```python
# adding the columns into our master dataframe
anime_merged_df_2['normalized_weight'] = animes_scaled_df['weighted_average'] 
anime_merged_df_2['normalized_members'] = animes_scaled_df['members']
```


```python
# evaluating the score giving 50% prefernce to normalized weight and 50% to normalized memebers
anime_merged_df_2['score'] = anime_merged_df_2['normalized_weight'] * 0.5 + anime_merged_df_2['normalized_members'] * 0.5 
```


```python

```


```python
anime_merged_df_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
      <th>weighted_average</th>
      <th>normalized_weight</th>
      <th>normalized_members</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>244</td>
      <td>10</td>
      <td>24574</td>
      <td>277</td>
      <td>9.259561</td>
      <td>9.259561</td>
      <td>793665</td>
      <td>396837.129781</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>244</td>
      <td>10</td>
      <td>19283</td>
      <td>277</td>
      <td>9.169479</td>
      <td>9.169479</td>
      <td>673572</td>
      <td>336790.584740</td>
    </tr>
    <tr>
      <th>277</th>
      <td>23273</td>
      <td>Shigatsu wa Kimi no Uso</td>
      <td>Drama, Music, Romance, School, Shounen</td>
      <td>TV</td>
      <td>22</td>
      <td>8.92</td>
      <td>416397</td>
      <td>244</td>
      <td>10</td>
      <td>9448</td>
      <td>277</td>
      <td>8.919156</td>
      <td>8.919156</td>
      <td>416397</td>
      <td>208202.959578</td>
    </tr>
    <tr>
      <th>278</th>
      <td>12355</td>
      <td>Ookami Kodomo no Ame to Yuki</td>
      <td>Fantasy, Slice of Life</td>
      <td>Movie</td>
      <td>1</td>
      <td>8.84</td>
      <td>226193</td>
      <td>244</td>
      <td>9</td>
      <td>7709</td>
      <td>277</td>
      <td>8.839051</td>
      <td>8.839051</td>
      <td>226193</td>
      <td>113100.919526</td>
    </tr>
    <tr>
      <th>279</th>
      <td>30276</td>
      <td>One Punch Man</td>
      <td>Action, Comedy, Parody, Sci-Fi, Seinen, Super ...</td>
      <td>TV</td>
      <td>12</td>
      <td>8.82</td>
      <td>552458</td>
      <td>244</td>
      <td>9</td>
      <td>13374</td>
      <td>277</td>
      <td>8.819465</td>
      <td>8.819465</td>
      <td>552458</td>
      <td>276233.409733</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7748647</th>
      <td>6205</td>
      <td>Kämpfer</td>
      <td>Action, Comedy, Ecchi, Romance, School, Shoujo...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.73</td>
      <td>146631</td>
      <td>24918</td>
      <td>7</td>
      <td>6595</td>
      <td>229</td>
      <td>6.731527</td>
      <td>6.731527</td>
      <td>146631</td>
      <td>73318.865764</td>
    </tr>
    <tr>
      <th>7748649</th>
      <td>8861</td>
      <td>Yosuga no Sora: In Solitude, Where We Are Leas...</td>
      <td>Drama, Ecchi, Harem, Romance</td>
      <td>TV</td>
      <td>12</td>
      <td>6.72</td>
      <td>173216</td>
      <td>24918</td>
      <td>6</td>
      <td>6687</td>
      <td>229</td>
      <td>6.721519</td>
      <td>6.721519</td>
      <td>173216</td>
      <td>86611.360759</td>
    </tr>
    <tr>
      <th>7748659</th>
      <td>4975</td>
      <td>ChäoS;HEAd</td>
      <td>Harem, Mystery, Psychological, Sci-Fi, Superna...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.62</td>
      <td>174337</td>
      <td>24918</td>
      <td>8</td>
      <td>7862</td>
      <td>229</td>
      <td>6.621397</td>
      <td>6.621397</td>
      <td>174337</td>
      <td>87171.810698</td>
    </tr>
    <tr>
      <th>7748668</th>
      <td>6682</td>
      <td>11eyes</td>
      <td>Action, Ecchi, Super Power, Supernatural</td>
      <td>TV</td>
      <td>12</td>
      <td>6.49</td>
      <td>133971</td>
      <td>24918</td>
      <td>8</td>
      <td>5846</td>
      <td>229</td>
      <td>6.492061</td>
      <td>6.492061</td>
      <td>133971</td>
      <td>66988.746031</td>
    </tr>
    <tr>
      <th>7748679</th>
      <td>2476</td>
      <td>School Days</td>
      <td>Drama, Harem, Romance, School</td>
      <td>TV</td>
      <td>12</td>
      <td>6.17</td>
      <td>279183</td>
      <td>24918</td>
      <td>7</td>
      <td>12417</td>
      <td>229</td>
      <td>6.171184</td>
      <td>6.171184</td>
      <td>279183</td>
      <td>139594.585592</td>
    </tr>
  </tbody>
</table>
<p>1449228 rows × 15 columns</p>
</div>




```python

```


```python
anime_merged_df_2.groupby('name').mean().sort_values('score',ascending=False)[['score']] # checking animes with the top and bottom'score'
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Death Note</th>
      <td>506962.854921</td>
    </tr>
    <tr>
      <th>Shingeki no Kyojin</th>
      <td>448118.769918</td>
    </tr>
    <tr>
      <th>Sword Art Online</th>
      <td>446553.915017</td>
    </tr>
    <tr>
      <th>Fullmetal Alchemist: Brotherhood</th>
      <td>396837.129781</td>
    </tr>
    <tr>
      <th>Angel Beats!</th>
      <td>358902.194934</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>Trinity Blood</th>
      <td>56899.220437</td>
    </tr>
    <tr>
      <th>Golden Boy</th>
      <td>56524.024927</td>
    </tr>
    <tr>
      <th>Kara no Kyoukai 5: Mujun Rasen</th>
      <td>55541.339401</td>
    </tr>
    <tr>
      <th>Fate/stay night Movie: Unlimited Blade Works</th>
      <td>55495.290292</td>
    </tr>
    <tr>
      <th>Asu no Yoichi!</th>
      <td>55377.510696</td>
    </tr>
  </tbody>
</table>
<p>405 rows × 1 columns</p>
</div>



## Collaborative Filtering Using KNN


```python
# creating a pivot table having user_id as column and anime name as index with the value being rating
anime_pivot_table = anime_merged_df_2.pivot_table(index='name',columns='user_id',values='rating').fillna(0) 
```


```python
anime_pivot_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>user_id</th>
      <th>5</th>
      <th>7</th>
      <th>17</th>
      <th>38</th>
      <th>43</th>
      <th>46</th>
      <th>54</th>
      <th>123</th>
      <th>129</th>
      <th>139</th>
      <th>...</th>
      <th>73417</th>
      <th>73422</th>
      <th>73457</th>
      <th>73460</th>
      <th>73476</th>
      <th>73491</th>
      <th>73499</th>
      <th>73502</th>
      <th>73503</th>
      <th>73507</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>07-Ghost</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>-1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11eyes</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>-1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>-1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Absolute Duo</th>
      <td>2.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Accel World</th>
      <td>3.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>-1.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Afro Samurai</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Zero no Tsukaima: Princesses no Rondo</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Zetsuen no Tempest</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Zoku Natsume Yuujinchou</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>-1.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>ef: A Tale of Memories.</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>xxxHOLiC</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
<p>405 rows × 9909 columns</p>
</div>




```python
# comverting array matrix to sparse matrix because NearestNeighbors function can only work on csr matrix
from scipy.sparse import csr_matrix 
anime_featrures_df_matrix = csr_matrix(anime_pivot_table.values)
```


```python
from sklearn.neighbors import NearestNeighbors # importing NearestNeighbors function to find the cosine distances
```


```python
model_knn = NearestNeighbors(metric='cosine',algorithm='auto') # creating the instance of NearestNeighbors 
```


```python
model_knn.fit(anime_featrures_df_matrix) # fitting the knn model on the training set
```




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>NearestNeighbors(metric=&#x27;cosine&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">NearestNeighbors</label><div class="sk-toggleable__content"><pre>NearestNeighbors(metric=&#x27;cosine&#x27;)</pre></div></div></div></div></div>




```python
anime_featrures_df_matrix.shape
```




    (405, 9909)




```python
# testing on a random sample point
query_index = np.random.choice(anime_pivot_table.shape[0]) # getting a random query_index in the range (0,405)
print(query_index)
distances, indices = model_knn.kneighbors(anime_pivot_table.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 10) # calculating distances and indices using our model on the query_index (set randomly)
```

    98
    


```python
distances[0]
```




    array([0.        , 0.32623005, 0.33665935, 0.34018487, 0.3491304 ,
           0.35886086, 0.36181589, 0.36182458, 0.3707989 , 0.37679528])




```python
for i in range(0, len(distances.flatten())): # in the range of flattened distances array (2D converted to 1D)
    if i == 0: # if the distance == 0 or if the name is the same name
        print(f'Recommendations for {anime_pivot_table.index[query_index]}:\n') 
    else:
        print(f'{i}: {anime_pivot_table.index[indices.flatten()[i]]}, with distance of {distances.flatten()[i]}:') # all the other anime names whose distance is greater than 0
```

    Recommendations for Death Parade:
    
    1: Kiseijuu: Sei no Kakuritsu, with distance of 0.32623004580589365:
    2: Tokyo Ghoul, with distance of 0.33665935342834163:
    3: Zankyou no Terror, with distance of 0.340184871270369:
    4: One Punch Man, with distance of 0.34913039730012174:
    5: Shingeki no Kyojin, with distance of 0.358860863113611:
    6: No Game No Life, with distance of 0.3618158902706964:
    7: Noragami, with distance of 0.361824578330345:
    8: Boku dake ga Inai Machi, with distance of 0.3707988984486834:
    9: Psycho-Pass, with distance of 0.3767952768613363:
    


```python

```


```python
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
```


```python
anime_recommendation('Naruto')
```

    Recommendations for Naruto:
    
    1: Death Note, with cosine distance of 0.3046531344408395:
    2: Code Geass: Hangyaku no Lelouch, with cosine distance of 0.3457773789281512:
    3: Bleach, with cosine distance of 0.3480387656001078:
    4: Sword Art Online, with cosine distance of 0.34919609451324063:
    5: Fullmetal Alchemist: Brotherhood, with cosine distance of 0.35603728410993407:
    6: Ao no Exorcist, with cosine distance of 0.3560441566742101:
    7: Fullmetal Alchemist, with cosine distance of 0.3572021701958408:
    8: Shingeki no Kyojin, with cosine distance of 0.3603843207800872:
    9: Code Geass: Hangyaku no Lelouch R2, with cosine distance of 0.36261057343126013:
    


```python
anime_recommendation('Death Note')
```

    Recommendations for Death Note:
    
    1: Code Geass: Hangyaku no Lelouch, with cosine distance of 0.20585709659451812:
    2: Code Geass: Hangyaku no Lelouch R2, with cosine distance of 0.22533968014006944:
    3: Elfen Lied, with cosine distance of 0.2527642921503126:
    4: Fullmetal Alchemist: Brotherhood, with cosine distance of 0.2557929357999871:
    5: Shingeki no Kyojin, with cosine distance of 0.26298337558906015:
    6: Angel Beats!, with cosine distance of 0.2640831833363818:
    7: Toradora!, with cosine distance of 0.27694131348626694:
    8: Sword Art Online, with cosine distance of 0.28351301599309797:
    9: Fullmetal Alchemist, with cosine distance of 0.28842798687025906:
    


```python
anime_recommendation('One Punch Man')
```

    Recommendations for One Punch Man:
    
    1: Shingeki no Kyojin, with cosine distance of 0.29432723459783017:
    2: No Game No Life, with cosine distance of 0.297258184426928:
    3: Kiseijuu: Sei no Kakuritsu, with cosine distance of 0.3142797513228084:
    4: Boku dake ga Inai Machi, with cosine distance of 0.31704609482045354:
    5: Tokyo Ghoul, with cosine distance of 0.324214812594119:
    6: Boku no Hero Academia, with cosine distance of 0.3336931850327056:
    7: Sword Art Online, with cosine distance of 0.33528366842805124:
    8: Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka, with cosine distance of 0.3362893053698144:
    9: Shokugeki no Souma, with cosine distance of 0.3396129643912251:
    


```python
anime_recommendation('Kuroko no Basket')
```

    Recommendations for Kuroko no Basket:
    
    1: Kuroko no Basket 2nd Season, with cosine distance of 0.12130801081342546:
    2: Kuroko no Basket 3rd Season, with cosine distance of 0.27016576760399413:
    3: Haikyuu!!, with cosine distance of 0.3372156225170534:
    4: Shingeki no Kyojin, with cosine distance of 0.40290269136501544:
    5: Ao no Exorcist, with cosine distance of 0.4123780962939658:
    6: Sword Art Online, with cosine distance of 0.4251277258969045:
    7: Tonari no Kaibutsu-kun, with cosine distance of 0.43181441694506106:
    8: Noragami, with cosine distance of 0.43644095176182607:
    9: Magi: The Labyrinth of Magic, with cosine distance of 0.44220925533865063:
    

### I was expecting more sports anime in this list

## Let's Try using Content based filtering


```python
anime_merged_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
      <td>131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>99</td>
      <td>10</td>
      <td>24574</td>
      <td>131</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>99</td>
      <td>9</td>
      <td>19283</td>
      <td>131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4181</td>
      <td>Clannad: After Story</td>
      <td>Drama, Fantasy, Romance, Slice of Life, Supern...</td>
      <td>TV</td>
      <td>24</td>
      <td>9.06</td>
      <td>456749</td>
      <td>99</td>
      <td>10</td>
      <td>17854</td>
      <td>131</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2904</td>
      <td>Code Geass: Hangyaku no Lelouch R2</td>
      <td>Action, Drama, Mecha, Military, Sci-Fi, Super ...</td>
      <td>TV</td>
      <td>25</td>
      <td>8.98</td>
      <td>572888</td>
      <td>99</td>
      <td>9</td>
      <td>24242</td>
      <td>131</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7813606</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>14133</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813607</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>40914</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813608</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>40965</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813609</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>55932</td>
      <td>10</td>
      <td>2475</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7813610</th>
      <td>1639</td>
      <td>Boku no Pico</td>
      <td>Hentai, Yaoi</td>
      <td>OVA</td>
      <td>1</td>
      <td>5.13</td>
      <td>57355</td>
      <td>64425</td>
      <td>-1</td>
      <td>2475</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>7813611 rows × 11 columns</p>
</div>




```python
anime_merged_df_2['number_of_genre'] = anime_merged_df['genre'].apply(lambda x: len(x.split(','))) # checking the count of each genre for each row
```


```python
anime_merged_df_2 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
      <th>weighted_average</th>
      <th>normalized_weight</th>
      <th>normalized_members</th>
      <th>score</th>
      <th>number_of_genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>244</td>
      <td>10</td>
      <td>24574</td>
      <td>277</td>
      <td>9.259561</td>
      <td>9.259561</td>
      <td>793665</td>
      <td>396837.129781</td>
      <td>7</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>244</td>
      <td>10</td>
      <td>19283</td>
      <td>277</td>
      <td>9.169479</td>
      <td>9.169479</td>
      <td>673572</td>
      <td>336790.584740</td>
      <td>2</td>
    </tr>
    <tr>
      <th>277</th>
      <td>23273</td>
      <td>Shigatsu wa Kimi no Uso</td>
      <td>Drama, Music, Romance, School, Shounen</td>
      <td>TV</td>
      <td>22</td>
      <td>8.92</td>
      <td>416397</td>
      <td>244</td>
      <td>10</td>
      <td>9448</td>
      <td>277</td>
      <td>8.919156</td>
      <td>8.919156</td>
      <td>416397</td>
      <td>208202.959578</td>
      <td>5</td>
    </tr>
    <tr>
      <th>278</th>
      <td>12355</td>
      <td>Ookami Kodomo no Ame to Yuki</td>
      <td>Fantasy, Slice of Life</td>
      <td>Movie</td>
      <td>1</td>
      <td>8.84</td>
      <td>226193</td>
      <td>244</td>
      <td>9</td>
      <td>7709</td>
      <td>277</td>
      <td>8.839051</td>
      <td>8.839051</td>
      <td>226193</td>
      <td>113100.919526</td>
      <td>2</td>
    </tr>
    <tr>
      <th>279</th>
      <td>30276</td>
      <td>One Punch Man</td>
      <td>Action, Comedy, Parody, Sci-Fi, Seinen, Super ...</td>
      <td>TV</td>
      <td>12</td>
      <td>8.82</td>
      <td>552458</td>
      <td>244</td>
      <td>9</td>
      <td>13374</td>
      <td>277</td>
      <td>8.819465</td>
      <td>8.819465</td>
      <td>552458</td>
      <td>276233.409733</td>
      <td>7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7748647</th>
      <td>6205</td>
      <td>Kämpfer</td>
      <td>Action, Comedy, Ecchi, Romance, School, Shoujo...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.73</td>
      <td>146631</td>
      <td>24918</td>
      <td>7</td>
      <td>6595</td>
      <td>229</td>
      <td>6.731527</td>
      <td>6.731527</td>
      <td>146631</td>
      <td>73318.865764</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7748649</th>
      <td>8861</td>
      <td>Yosuga no Sora: In Solitude, Where We Are Leas...</td>
      <td>Drama, Ecchi, Harem, Romance</td>
      <td>TV</td>
      <td>12</td>
      <td>6.72</td>
      <td>173216</td>
      <td>24918</td>
      <td>6</td>
      <td>6687</td>
      <td>229</td>
      <td>6.721519</td>
      <td>6.721519</td>
      <td>173216</td>
      <td>86611.360759</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7748659</th>
      <td>4975</td>
      <td>ChäoS;HEAd</td>
      <td>Harem, Mystery, Psychological, Sci-Fi, Superna...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.62</td>
      <td>174337</td>
      <td>24918</td>
      <td>8</td>
      <td>7862</td>
      <td>229</td>
      <td>6.621397</td>
      <td>6.621397</td>
      <td>174337</td>
      <td>87171.810698</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7748668</th>
      <td>6682</td>
      <td>11eyes</td>
      <td>Action, Ecchi, Super Power, Supernatural</td>
      <td>TV</td>
      <td>12</td>
      <td>6.49</td>
      <td>133971</td>
      <td>24918</td>
      <td>8</td>
      <td>5846</td>
      <td>229</td>
      <td>6.492061</td>
      <td>6.492061</td>
      <td>133971</td>
      <td>66988.746031</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7748679</th>
      <td>2476</td>
      <td>School Days</td>
      <td>Drama, Harem, Romance, School</td>
      <td>TV</td>
      <td>12</td>
      <td>6.17</td>
      <td>279183</td>
      <td>24918</td>
      <td>7</td>
      <td>12417</td>
      <td>229</td>
      <td>6.171184</td>
      <td>6.171184</td>
      <td>279183</td>
      <td>139594.585592</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>1449228 rows × 16 columns</p>
</div>




```python
anime_merged_df_2['number_of_genre'].describe() 
```




    count    1.449228e+06
    mean     4.750052e+00
    std      1.507469e+00
    min      2.000000e+00
    25%      4.000000e+00
    50%      5.000000e+00
    75%      6.000000e+00
    max      1.000000e+01
    Name: number_of_genre, dtype: float64



#### On an average an anime has 5 genre


```python
anime_merged_df_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
      <th>weighted_average</th>
      <th>normalized_weight</th>
      <th>normalized_members</th>
      <th>score</th>
      <th>number_of_genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>244</td>
      <td>10</td>
      <td>24574</td>
      <td>277</td>
      <td>9.259561</td>
      <td>9.259561</td>
      <td>793665</td>
      <td>396837.129781</td>
      <td>7</td>
    </tr>
    <tr>
      <th>276</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>244</td>
      <td>10</td>
      <td>19283</td>
      <td>277</td>
      <td>9.169479</td>
      <td>9.169479</td>
      <td>673572</td>
      <td>336790.584740</td>
      <td>2</td>
    </tr>
    <tr>
      <th>277</th>
      <td>23273</td>
      <td>Shigatsu wa Kimi no Uso</td>
      <td>Drama, Music, Romance, School, Shounen</td>
      <td>TV</td>
      <td>22</td>
      <td>8.92</td>
      <td>416397</td>
      <td>244</td>
      <td>10</td>
      <td>9448</td>
      <td>277</td>
      <td>8.919156</td>
      <td>8.919156</td>
      <td>416397</td>
      <td>208202.959578</td>
      <td>5</td>
    </tr>
    <tr>
      <th>278</th>
      <td>12355</td>
      <td>Ookami Kodomo no Ame to Yuki</td>
      <td>Fantasy, Slice of Life</td>
      <td>Movie</td>
      <td>1</td>
      <td>8.84</td>
      <td>226193</td>
      <td>244</td>
      <td>9</td>
      <td>7709</td>
      <td>277</td>
      <td>8.839051</td>
      <td>8.839051</td>
      <td>226193</td>
      <td>113100.919526</td>
      <td>2</td>
    </tr>
    <tr>
      <th>279</th>
      <td>30276</td>
      <td>One Punch Man</td>
      <td>Action, Comedy, Parody, Sci-Fi, Seinen, Super ...</td>
      <td>TV</td>
      <td>12</td>
      <td>8.82</td>
      <td>552458</td>
      <td>244</td>
      <td>9</td>
      <td>13374</td>
      <td>277</td>
      <td>8.819465</td>
      <td>8.819465</td>
      <td>552458</td>
      <td>276233.409733</td>
      <td>7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7748647</th>
      <td>6205</td>
      <td>Kämpfer</td>
      <td>Action, Comedy, Ecchi, Romance, School, Shoujo...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.73</td>
      <td>146631</td>
      <td>24918</td>
      <td>7</td>
      <td>6595</td>
      <td>229</td>
      <td>6.731527</td>
      <td>6.731527</td>
      <td>146631</td>
      <td>73318.865764</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7748649</th>
      <td>8861</td>
      <td>Yosuga no Sora: In Solitude, Where We Are Leas...</td>
      <td>Drama, Ecchi, Harem, Romance</td>
      <td>TV</td>
      <td>12</td>
      <td>6.72</td>
      <td>173216</td>
      <td>24918</td>
      <td>6</td>
      <td>6687</td>
      <td>229</td>
      <td>6.721519</td>
      <td>6.721519</td>
      <td>173216</td>
      <td>86611.360759</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7748659</th>
      <td>4975</td>
      <td>ChäoS;HEAd</td>
      <td>Harem, Mystery, Psychological, Sci-Fi, Superna...</td>
      <td>TV</td>
      <td>12</td>
      <td>6.62</td>
      <td>174337</td>
      <td>24918</td>
      <td>8</td>
      <td>7862</td>
      <td>229</td>
      <td>6.621397</td>
      <td>6.621397</td>
      <td>174337</td>
      <td>87171.810698</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7748668</th>
      <td>6682</td>
      <td>11eyes</td>
      <td>Action, Ecchi, Super Power, Supernatural</td>
      <td>TV</td>
      <td>12</td>
      <td>6.49</td>
      <td>133971</td>
      <td>24918</td>
      <td>8</td>
      <td>5846</td>
      <td>229</td>
      <td>6.492061</td>
      <td>6.492061</td>
      <td>133971</td>
      <td>66988.746031</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7748679</th>
      <td>2476</td>
      <td>School Days</td>
      <td>Drama, Harem, Romance, School</td>
      <td>TV</td>
      <td>12</td>
      <td>6.17</td>
      <td>279183</td>
      <td>24918</td>
      <td>7</td>
      <td>12417</td>
      <td>229</td>
      <td>6.171184</td>
      <td>6.171184</td>
      <td>279183</td>
      <td>139594.585592</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>1449228 rows × 16 columns</p>
</div>



### We can use TFidf on genre for this


```python
from sklearn.feature_extraction.text import TfidfVectorizer # importing the tfidf function
```


```python
tfidf = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode", analyzer="word",token_pattern=r"\w{1,}", ngram_range=(1, 3), stop_words = "english") # creating tfidf instance
```


```python
vec_df = anime_merged_df.copy() # making a copy of the master anime dataframe
```


```python
vec_df.drop_duplicates(subset ="name", keep = "first", inplace = True) # dropping duplicates from the 'name' columns and keeps only the first instance
```


```python
vec_df.reset_index(drop=True,inplace=True) # resetting and dropping the index
```


```python
vec_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>anime_id</th>
      <th>name</th>
      <th>genre</th>
      <th>type</th>
      <th>episodes</th>
      <th>avg_rating</th>
      <th>members</th>
      <th>user_id</th>
      <th>rating</th>
      <th>total_reviews</th>
      <th>animes_reviewed_by_this_user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32281</td>
      <td>Kimi no Na wa.</td>
      <td>Drama, Romance, School, Supernatural</td>
      <td>Movie</td>
      <td>1</td>
      <td>9.37</td>
      <td>200630</td>
      <td>99</td>
      <td>5</td>
      <td>2199</td>
      <td>131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5114</td>
      <td>Fullmetal Alchemist: Brotherhood</td>
      <td>Action, Adventure, Drama, Fantasy, Magic, Mili...</td>
      <td>TV</td>
      <td>64</td>
      <td>9.26</td>
      <td>793665</td>
      <td>99</td>
      <td>10</td>
      <td>24574</td>
      <td>131</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9253</td>
      <td>Steins;Gate</td>
      <td>Sci-Fi, Thriller</td>
      <td>TV</td>
      <td>24</td>
      <td>9.17</td>
      <td>673572</td>
      <td>99</td>
      <td>9</td>
      <td>19283</td>
      <td>131</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4181</td>
      <td>Clannad: After Story</td>
      <td>Drama, Fantasy, Romance, Slice of Life, Supern...</td>
      <td>TV</td>
      <td>24</td>
      <td>9.06</td>
      <td>456749</td>
      <td>99</td>
      <td>10</td>
      <td>17854</td>
      <td>131</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2904</td>
      <td>Code Geass: Hangyaku no Lelouch R2</td>
      <td>Action, Drama, Mecha, Military, Sci-Fi, Super ...</td>
      <td>TV</td>
      <td>25</td>
      <td>8.98</td>
      <td>572888</td>
      <td>99</td>
      <td>9</td>
      <td>24242</td>
      <td>131</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11156</th>
      <td>33266</td>
      <td>Nanocore</td>
      <td>Sci-Fi</td>
      <td>ONA</td>
      <td>10</td>
      <td>6.17</td>
      <td>163</td>
      <td>42790</td>
      <td>-1</td>
      <td>1</td>
      <td>284</td>
    </tr>
    <tr>
      <th>11157</th>
      <td>31972</td>
      <td>Tang Lang Bu Chan</td>
      <td>Historical</td>
      <td>Movie</td>
      <td>1</td>
      <td>5.90</td>
      <td>112</td>
      <td>49322</td>
      <td>9</td>
      <td>1</td>
      <td>301</td>
    </tr>
    <tr>
      <th>11158</th>
      <td>33484</td>
      <td>Shiroi Zou</td>
      <td>Action, Historical, Kids</td>
      <td>Movie</td>
      <td>1</td>
      <td>4.71</td>
      <td>45</td>
      <td>69497</td>
      <td>10</td>
      <td>1</td>
      <td>202</td>
    </tr>
    <tr>
      <th>11159</th>
      <td>30173</td>
      <td>Fruity Samurai</td>
      <td>Action, Comedy, Historical, Samurai</td>
      <td>TV</td>
      <td>13</td>
      <td>5.52</td>
      <td>134</td>
      <td>62710</td>
      <td>8</td>
      <td>1</td>
      <td>47</td>
    </tr>
    <tr>
      <th>11160</th>
      <td>9304</td>
      <td>Happy Day</td>
      <td>Hentai</td>
      <td>OVA</td>
      <td>1</td>
      <td>4.94</td>
      <td>172</td>
      <td>23745</td>
      <td>-1</td>
      <td>1</td>
      <td>48</td>
    </tr>
  </tbody>
</table>
<p>11161 rows × 11 columns</p>
</div>



### Implementing weighted average score for final sorting of the recommended list purpose


```python
# getting all the required values
v = vec_df['total_reviews']
R = vec_df['avg_rating']
C = vec_df['avg_rating'].mean()
m = vec_df['avg_rating'].quantile(0.70) # only those samples whose 'veot_avergae' is more than 70 percentile (by value)
vec_df['weighted_average'] = ((R*v) + (C*m))/ (v+m) # using the formula for weighted average
```


```python
from sklearn.preprocessing import MinMaxScaler  # importing the function
sc = MinMaxScaler() # creating the scaling function instance
animes_scaled_df = sc.fit_transform(vec_df[['weighted_average','members']]) # fit and transform the required column
animes_scaled_df = pd.DataFrame(vec_df, columns=['weighted_average','members']) # creating the dataframe containing normalized weight and memebers

vec_df['normalized_weight'] = animes_scaled_df['weighted_average'] # adding the column for normalized weight
vec_df['normalized_members'] = animes_scaled_df['members'] # adding the column for normalized members
vec_df['score'] = vec_df['normalized_weight'] * 0.5 + vec_df['normalized_members'] * 0.5 # final score gives 50% weightage to normalized weight and normalized memebers
```


```python

```


```python
genre_anime = vec_df["genre"].str.split(", | , | ,").astype(str) # splitting out into a list of  different genres contained in the genre column of the vec_df dataframe
```


```python
genre_anime
```




    0           ['Drama', 'Romance', 'School', 'Supernatural']
    1        ['Action', 'Adventure', 'Drama', 'Fantasy', 'M...
    2                                   ['Sci-Fi', 'Thriller']
    3        ['Drama', 'Fantasy', 'Romance', 'Slice of Life...
    4        ['Action', 'Drama', 'Mecha', 'Military', 'Sci-...
                                   ...                        
    11156                                           ['Sci-Fi']
    11157                                       ['Historical']
    11158                     ['Action', 'Historical', 'Kids']
    11159        ['Action', 'Comedy', 'Historical', 'Samurai']
    11160                                           ['Hentai']
    Name: genre, Length: 11161, dtype: object




```python
tfidf_matrix = tfidf.fit_transform(genre_anime) # creating a sparse matrix for tfidf vectorized 'genre'
```


```python
tfidf_matrix.shape 
```




    (11161, 1525)




```python
tfidf_matrix
```




    <11161x1525 sparse matrix of type '<class 'numpy.float64'>'
    	with 80262 stored elements in Compressed Sparse Row format>



### We need the output for each sample to be in the range(0,1), so we'll use sigmoid function


```python
from sklearn.metrics.pairwise import sigmoid_kernel # importing the sigmoid_kernel function 
```


```python
sig = sigmoid_kernel(tfidf_matrix, tfidf_matrix) # compute the sigmoid kernel
```


```python
sig[0]
```




    array([0.76186941, 0.76160057, 0.76159416, ..., 0.76159416, 0.76159416,
           0.76159416])




```python
indices = pd.Series(vec_df.index, index=vec_df['name']).drop_duplicates() # reverse mapping of indices and movie titles
```


```python
indices
```




    name
    Kimi no Na wa.                            0
    Fullmetal Alchemist: Brotherhood          1
    Steins;Gate                               2
    Clannad: After Story                      3
    Code Geass: Hangyaku no Lelouch R2        4
                                          ...  
    Nanocore                              11156
    Tang Lang Bu Chan                     11157
    Shiroi Zou                            11158
    Fruity Samurai                        11159
    Happy Day                             11160
    Length: 11161, dtype: int64




```python
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
```


```python
give_anime_recommendation('Naruto')
```

    Recommendations for Naruto viewers :
    
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Anime Name</th>
      <th>Rating</th>
      <th>Genre</th>
      <th>Scaled Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Naruto: Shippuuden Movie 4 - The Lost Tower</td>
      <td>7.53</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>42267.264215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsu...</td>
      <td>7.50</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>41761.249300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Boruto: Naruto the Movie</td>
      <td>8.03</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>37349.011752</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Naruto Soyokazeden Movie: Naruto to Mashin to ...</td>
      <td>7.11</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>12590.553446</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Naruto x UT</td>
      <td>7.58</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>11736.286886</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Boruto: Naruto the Movie - Naruto ga Hokage ni...</td>
      <td>7.68</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>8437.829060</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Naruto Shippuuden: Sunny Side Battle</td>
      <td>7.26</td>
      <td>Action, Comedy, Martial Arts, Shounen, Super P...</td>
      <td>6510.624207</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ranma ½: Akumu! Shunmin Kou</td>
      <td>7.70</td>
      <td>Action, Comedy, Martial Arts, Shounen, Superna...</td>
      <td>3535.838690</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Battle Spirits: Ryuuko no Ken</td>
      <td>4.89</td>
      <td>Action, Comedy, Martial Arts, Shounen</td>
      <td>856.514330</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Kyutai Panic Adventure!</td>
      <td>5.21</td>
      <td>Action, Martial Arts, Shounen, Super Power</td>
      <td>352.789606</td>
    </tr>
  </tbody>
</table>
</div>




```python
give_anime_recommendation('Kuroko no Basket')
```

    Recommendations for Kuroko no Basket viewers :
    
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Anime Name</th>
      <th>Rating</th>
      <th>Genre</th>
      <th>Scaled Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Kuroko no Basket</td>
      <td>8.46</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>169161.729405</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kuroko no Basket 2nd Season</td>
      <td>8.58</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>121666.789116</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Diamond no Ace</td>
      <td>8.25</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>40696.121145</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kuroko no Basket: Tip Off</td>
      <td>8.07</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>20884.032292</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Diamond no Ace: Second Season</td>
      <td>8.50</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>19269.741998</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Area no Kishi</td>
      <td>7.38</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>19158.687379</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kuroko no Basket NG-shuu</td>
      <td>7.84</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>16111.416837</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Kuroko no Basket: Baka ja Katenai no yo!</td>
      <td>7.75</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>13396.371294</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Kuroko no Basket: Oshaberi Shiyokka</td>
      <td>7.42</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>11972.207229</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Kuroko no Basket: Mou Ikkai Yarimasen ka</td>
      <td>7.86</td>
      <td>Comedy, School, Shounen, Sports</td>
      <td>10202.423664</td>
    </tr>
  </tbody>
</table>
</div>



### A lot of 'relevant' sports animes


```python
give_anime_recommendation('Death Note')
```

    Recommendations for Death Note viewers :
    
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Anime Name</th>
      <th>Rating</th>
      <th>Genre</th>
      <th>Scaled Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Higurashi no Naku Koro ni</td>
      <td>8.17</td>
      <td>Horror, Mystery, Psychological, Supernatural, ...</td>
      <td>179751.084548</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Monster</td>
      <td>8.72</td>
      <td>Drama, Horror, Mystery, Police, Psychological,...</td>
      <td>123785.358309</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Higurashi no Naku Koro ni Kai</td>
      <td>8.41</td>
      <td>Mystery, Psychological, Supernatural, Thriller</td>
      <td>109054.704271</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mousou Dairinin</td>
      <td>7.74</td>
      <td>Drama, Mystery, Police, Psychological, Superna...</td>
      <td>68847.369022</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Higurashi no Naku Koro ni Rei</td>
      <td>7.56</td>
      <td>Comedy, Mystery, Psychological, Supernatural, ...</td>
      <td>49735.279223</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Death Note Rewrite</td>
      <td>7.84</td>
      <td>Mystery, Police, Psychological, Supernatural, ...</td>
      <td>44353.418801</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Shigofumi</td>
      <td>7.62</td>
      <td>Drama, Fantasy, Psychological, Supernatural, T...</td>
      <td>27003.807893</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Himitsu: The Revelation</td>
      <td>7.42</td>
      <td>Mystery, Police, Psychological, Sci-Fi, Shoujo</td>
      <td>5884.189982</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Hikari to Mizu no Daphne</td>
      <td>6.87</td>
      <td>Comedy, Drama, Mystery, Police, Psychological,...</td>
      <td>4441.431014</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bloody Night</td>
      <td>4.26</td>
      <td>Horror, Psychological, Supernatural, Thriller</td>
      <td>648.315427</td>
    </tr>
  </tbody>
</table>
</div>




```python
give_anime_recommendation('Dragon Ball')
```

    Recommendations for Dragon Ball viewers :
    
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Anime Name</th>
      <th>Rating</th>
      <th>Genre</th>
      <th>Scaled Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Dragon Ball Z</td>
      <td>8.32</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>187835.159626</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Dragon Ball Kai</td>
      <td>7.95</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>58419.973766</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dragon Ball Z Movie 14: Kami to Kami</td>
      <td>7.62</td>
      <td>Action, Adventure, Fantasy, Martial Arts, Shou...</td>
      <td>33239.308804</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragon Ball Z Movie 10: Kiken na Futari! Super...</td>
      <td>7.11</td>
      <td>Action, Adventure, Comedy, Demons, Fantasy, Ma...</td>
      <td>27477.054398</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragon Ball Z Movie 11: Super Senshi Gekiha!! ...</td>
      <td>6.28</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>24977.640271</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragon Ball Kai (2014)</td>
      <td>8.01</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>21336.999012</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragon Ball Z Movie 15: Fukkatsu no F</td>
      <td>7.55</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>20529.272473</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Dragon Ball GT: Goku Gaiden! Yuuki no Akashi w...</td>
      <td>6.75</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>16429.874596</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Dragon Ball Z: Atsumare! Gokuu World</td>
      <td>6.76</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>5025.378277</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Dragon Ball Z: Summer Vacation Special</td>
      <td>7.05</td>
      <td>Action, Adventure, Comedy, Fantasy, Martial Ar...</td>
      <td>2129.010234</td>
    </tr>
  </tbody>
</table>
</div>



# Conclusion:
### The content based filtering method outperformed the collabrative filtering (based on KNN).


```python

```
