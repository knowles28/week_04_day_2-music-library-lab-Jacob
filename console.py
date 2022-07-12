import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()

artist1 = Artist("Kanye West")
artist2 = Artist("Queen")
artist_repository.save(artist1)
artist_repository.save(artist2)

album1 = Album("Graduation", "rap", artist1)
album_repository.save(album1)
album2 = Album("Greatest Hits", "pop", artist2)

print(album_repository.select_by_artist(artist1))

# test = artist_repository.select(10)

# print(test.__dict__)
# # for artists in artist_repository:
# #     print(artist_repository.__dict__)
    
pdb.set_trace()