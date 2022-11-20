class Trainer:

    def_id = 1
    def __init__(self,name:str):
        self.name = name
        self.id = self.def_id
        self.def_id +=1

    @staticmethod
    def get_next_id():
        return Trainer.def_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
