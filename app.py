import pandas as pd, numpy as np, re, openai, os, json
from sklearn.metrics.pairwise import cosine_similarity
from flask import request, Flask, render_template, jsonify
import requests

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        ## USED THE API KEYS OF OPENAI API HERE. HIDING BECAUSE OF SAFETY PURPOSES

        
        CHUNKSIZE = 1000  # number of lines to read at a time
        dataframes = []
        with open('Final_File_for_ARS.json', 'r') as f:
            for chunk in pd.read_json(f, lines=True, chunksize=CHUNKSIZE):
                dataframes.append(chunk)

        df_rec = pd.concat(dataframes)
        
        def give_anime_recommendation_final_app(name,df=df_rec):

            def string_cleaner(s):
                s = s.lower()
                s = re.sub(r'[.,"\'-?:!;_|/><]', '', s)
                return s.strip()

            
            cleaned_name = string_cleaner(name)
            #name_lower = name.lower()
            if name in  df['Name'].unique():
                required_embedding = df[df['Name']==name]['embedding'].values[0]

            elif name in  df['English name'].unique():
                required_embedding = df[df['English name']==name]['embedding'].values[0]

            elif cleaned_name in  df['Name_cleaned'].unique():
                required_embedding = df[df['Name_cleaned']==cleaned_name]['embedding'].values[0]

            elif cleaned_name in  df['English_name_cleaned'].unique():
                required_embedding = df[df['English_name_cleaned']==cleaned_name]['embedding'].values[0]

            else:
                #def name_finder(name,df=df_rec.copy()):
                def string_cleaner(s):
                    s = s.lower()
                    s = re.sub(r'[.,"\'-?:!;_|/><]', '', s)
                    return s.strip()

                def get_embedding(text):
                    result = openai.Embedding.create(model='text-embedding-ada-002', input=text)

                    return result['data'][0]['embedding']

                cleaned_name = string_cleaner(name)
                cleaned_name_embed = get_embedding(cleaned_name)

                name_dist = []
                for index, row in df.iterrows():
                    name_dist.append(cosine_similarity(np.asarray(row['Final_name_embedding']).reshape(1,-1), np.array(cleaned_name_embed).reshape(1,-1))[0][0])


                df['name_embed_similarity'] = name_dist

                print(f"The name you entered is not in the list, but I believe you meant this anime: {df[df['name_embed_similarity']==df['name_embed_similarity'].max()]['Name'].values[0]}\n\n")
                required_embedding = df[df['name_embed_similarity']==df['name_embed_similarity'].max()]['embedding'].values[0]


            cos_dist = []
            for index, row in df.iterrows():
                cos_dist.append(cosine_similarity(np.asarray(row['embedding']).reshape(1,-1), np.array(required_embedding).reshape(1,-1))[0][0])
            df['cos_similarity'] = cos_dist
            #df['anime_score'] = df['cos_similarity'] * df['weighted_score_norm']
            #return df.sort_values('cos_similarity',ascending=False)[['Name','English name','cos_similarity','Type','Genres','Popularity','Score','Members', 'Final_name']].head(10)[1:].sort_values('Members',ascending=False).head(10)[['Name','English name']].values  
            return df.sort_values('cos_similarity',ascending=False)[['Name','English name','Members','cos_similarity']].head(15)[1:].sort_values('Members',ascending=False).head(10)[['Name','English name']].values
        
        
        anime_name = request.form['anime_name']
        #recommendations = give_anime_recommendation_final_app(anime_name)
        
        recs = give_anime_recommendation_final_app(anime_name)
        recommendations = []
        for i in recs:
            for a in i:
                recommendations.append(a)

        jap_names = recommendations[::2]
        eng_names = recommendations[1::2]
        #print(jap_names)
        #print(eng_names)

        fin_name = []
        for i in range(len(jap_names)):
            fin_name.append(f"Name: {jap_names[i]} OR English name: {eng_names[i]}")
        fin_name
        
        pred_name_1 = fin_name[0]
        pred_name_2 = fin_name[1]
        pred_name_3 = fin_name[2]
        pred_name_4 = fin_name[3]
        pred_name_5 = fin_name[4]
        pred_name_6 = fin_name[5]
        pred_name_7 = fin_name[6]
        pred_name_8 = fin_name[7]
        pred_name_9 = fin_name[8]
        pred_name_10 = fin_name[9]
        
        return render_template('index.html', anime_name=anime_name, pred_name_1 = pred_name_1, pred_name_2 = pred_name_2, pred_name_3 = pred_name_3, pred_name_4 = pred_name_4,
                              pred_name_5 = pred_name_5, pred_name_6 = pred_name_6, pred_name_7 = pred_name_7, pred_name_8 = pred_name_8, pred_name_9 = pred_name_9,
                              pred_name_10 = pred_name_10)
    else:
        print('NO RESPONSE')
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
