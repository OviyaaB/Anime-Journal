import os
import psycopg2    
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='DMQL_Proj_AnimeDB',
                            user='postgres',
                            password='eucalyptus@09')
    return conn

@app.route("/")
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    #cur.execute("SELECT anime_name FROM anime WHERE anime_id='32281';")
    #cur.execute(("INSERT into likes(user_id, anime_id, rating, review, has_spoilers) values (%s, %s, %s, %s, %s)"), (1, 100, 9, "nice anime goos story", False))
    #books = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    #print(books)
    # return '<h1>Hello, World!</h1>'
    return render_template('index.html')
    
    
@app.route('/new_liked', methods=['GET', 'POST'])
def new_liked():
    if request.method == 'POST':
        return render_template('new_liked.html')
    return render_template('index.html')
    
@app.route('/insert_value', methods=['GET', 'POST'])
def insert_value():
    if request.method == 'POST':
        anime_id = request.form.get("anime_id")
        anime_name = request.form.get("anime_name")
        genre = request.form.get("genre")
        ratings = request.form.get("ratings")
        episodes = request.form.get("episodes")
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(("INSERT into anime(anime_id, anime_name, anime_genre, anime_ratings, anime_episodes) values (%s, %s, %s, %s, %s)"), (anime_id, anime_name, genre, ratings, episodes))
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('index.html')

@app.route('/update_anime', methods=['GET', 'POST'])
def update_anime():
    if request.method == 'POST':
        return render_template('update_anime.html')
        
@app.route('/update_value', methods=['GET', 'POST'])
def update_value():
    if request.method == 'POST':
        anime_id = request.form.get("anime_id")
        episodes = request.form.get("episodes")
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(("UPDATE anime set anime_episodes=%s WHERE anime_id=%s"), (episodes, anime_id))
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('index.html')

@app.route('/remove_user', methods=['GET', 'POST'])
def remove_user():
    if request.method == 'POST':
        return render_template('remove_user.html')
        
@app.route('/remove_value', methods=['GET', 'POST'])
def remove_value():
    if request.method == 'POST':
        user_id = request.form.get("user_id")
        print(user_id)
     
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(("DELETE FROM wish_list WHERE user_id=%s"), (user_id,))
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('index.html')
        
@app.route('/unwatched_anime', methods=['GET', 'POST'])
def unwatched_anime():
    if request.method == 'GET':
    
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("select * from anime where anime_id not in (select distinct(anime_id) from diary) limit 5")
        data = cur.fetchall()
        print("fetching data.................")
        print(data)
        ll = []
        for i in data:
            dt={}
            dt['id'] = i[0]
            dt['name'] = i[1]
            dt['genre'] = i[2]
            dt['rating'] = i[3]
            dt['episodes'] = i[4]
            ll.append(dt)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('analyse.html', data=ll)
        
@app.route('/highest_rated', methods=['GET', 'POST'])
def highest_rated():
    if request.method == 'GET':
    
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("select * from anime where anime_id in (select distinct(anime_id) from scores where overall >= 7) and anime_ratings is NOT NULL order by anime_ratings desc limit 7")
        data = cur.fetchall()
        print("fetching data.................")
        print(data)
        ll = []
        for i in data:
            dt={}
            dt['id'] = i[0]
            dt['name'] = i[1]
            dt['genre'] = i[2]
            dt['rating'] = i[3]
            dt['episodes'] = i[4]
            ll.append(dt)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('analyse.html', data=ll)
        
@app.route('/most_liked', methods=['GET', 'POST'])
def most_liked():
    if request.method == 'GET':
    
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("Select * from anime where anime_id in (select distinct(anime_id) from likes where rating >= 7) and anime_ratings IS NOT NULL order by anime_ratings desc limit 10")
        data = cur.fetchall()
        print("fetching data.................")
        print(data)
        ll = []
        for i in data:
            dt={}
            dt['id'] = i[0]
            dt['name'] = i[1]
            dt['genre'] = i[2]
            dt['rating'] = i[3]
            dt['episodes'] = i[4]
            ll.append(dt)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('analyse.html', data=ll)
        
@app.route('/most_wishlisted', methods=['GET', 'POST'])
def most_wishlisted():
    if request.method == 'GET':
    
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("select * from anime where anime_name in (select anime_name from anime where anime_id in (select anime_id from wish_list group by anime_id limit 5) group by anime_name limit 3)")
        data = cur.fetchall()
        print("fetching data.................")
        print(data)
        ll = []
        for i in data:
            dt={}
            dt['id'] = i[0]
            dt['name'] = i[1]
            dt['genre'] = i[2]
            dt['rating'] = i[3]
            dt['episodes'] = i[4]
            ll.append(dt)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return render_template('analyse.html', data=ll)

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    