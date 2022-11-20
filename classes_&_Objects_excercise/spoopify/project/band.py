from project.album import Album
from project.song import Song

class Band:
    def __init__(self,name):
        self.name = name
        self.albums = []

    def add_album(self,album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
    def remove_album(self, album_name: str):
        for el in self.albums:
            if el.name == album_name and el.published:
                return "Album has been published. It cannot be removed."
            elif el.name == album_name and not el.published:
                self.albums.remove(el)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."
    def details(self):
        info = f"Band {self.name}"
        for el in self.albums:
            info += f"\n{el.details()}"
        return info

# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, True)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())