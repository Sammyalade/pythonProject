class Entry:

    def __init__(self, id, title, body):
        self.body = body
        self.title = title
        self._id = id

    def get_id(self):
        return self._id
    
    def get_body(self):
        return self.body

    def __repr__(self):
        return f'{self.title} : {self.body}'
