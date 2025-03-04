class Risk():
    def __init__(self, id, impact, title, description):
        self.id = id
        self.impact = impact
        self.title = title
        self.description = description
    
    def to_json(self):
        return {
            'id': self.id,
            'impact': self.impact,
            'title': self.title,
            'description': self.description
        }
