from project.song import Song
class Album:
    def __init__(self,name,*args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = [x for x in args]

    def add_song(self,song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        in_album = False
        for el in self.songs:
            if el.name == song_name:
                in_album = True
        if self.published:
            return "Cannot remove songs. Album is published."
        elif not in_album:
            return "Song is not in the album."
        else:
            for el in self.songs:
                if el.name == song_name:
                    self.songs.remove(el)
                    return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        info = f"Album {self.name}"
        for el in self.songs:
            info += f"\n== {el.get_info()}"
        return info

