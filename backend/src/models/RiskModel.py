class Risk():
     # Constructor que inicializa los atributos del riesgo.
    def __init__(self, id, cod, impact, title, description, resolved):
        self.id = id
        self.cod = cod  
        self.impact = impact
        self.title = title
        self.description = description
        self.resolved = resolved

    # Método que convierte los datos del riesgo a un formato JSON.
    def to_json(self):
        return {
            'id': self.id,
            'cod': self.cod, 
            'impact': self.impact,
            'title': self.title,
            'description': self.description,
            'resolved': self.resolved,
        }
