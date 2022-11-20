import math

class PhotoAlbum:
    def __init__(self,pages:int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.photos_per_page = 4
        self.current_page = 1

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label:str) -> str:
        if self.photos_per_page ==0 and  self.current_page == self.pages:
            return "No more free slots"
        elif self.photos_per_page > 0 :
            self.photos_per_page -= 1
            self.photos[self.current_page-1].append(label)
            return  f"{label} photo added successfully on page {self.current_page} slot {len(self.photos[self.current_page-1])}"
        else:
            self.current_page += 1
            self.photos_per_page = 4
            self.photos_per_page -= 1
            self.photos[self.current_page - 1].append(label)
            return f"{label} photo added successfully on page {self.current_page} slot {len(self.photos[self.current_page - 1])}"


    def display(self):
        output_result = f"-----------\n"
        for page in range(len(self.photos)):
            if self.photos[page]:
                output_result += f"{' '.join(['[]' for _ in range(len(self.photos[page]))])}\n"
            else:
                output_result += '\n'
            output_result += "-----------\n"
        return output_result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())










