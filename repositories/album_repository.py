from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        album = Album(result['name'], result['id'])
    
    return album