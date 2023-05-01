import uuid 

class Basic:
    def __init__(self, id, tag):
        self.id = id
        self.name = tag
        
class fighterpilot(Basic):
    def __init__(self,id,tag,jet):
        super().__init__(self,id,tag)
        self.jet = jet
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag}"



































