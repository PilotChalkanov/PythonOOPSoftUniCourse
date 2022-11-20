class Equipment:
    init_id = 1
    def __init__(self,name:str):
        self.name = name
        self.id = self.init_id
        self.init_id +=1

    @staticmethod
    def get_next_id():
        return Equipment.init_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"