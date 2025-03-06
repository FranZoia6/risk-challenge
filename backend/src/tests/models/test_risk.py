import unittest
from src.models.RiskModel import Risk

class TestRiskModel(unittest.TestCase):

    def test_risk_initialization(self):
        # Creamos una instancia de la clase Risk
        risk = Risk(1, 'R1', 'High', 'Risk 1', 'Description of risk 1', 'No', '2025-03-06')

        # Verificamos que los atributos se hayan asignado correctamente
        self.assertEqual(risk.id, 1)
        self.assertEqual(risk.cod, 'R1')
        self.assertEqual(risk.impact, 'High')
        self.assertEqual(risk.title, 'Risk 1')
        self.assertEqual(risk.description, 'Description of risk 1')
        self.assertEqual(risk.resolved, 'No')
        self.assertEqual(risk.date, '2025-03-06')

    def test_to_json(self):
        # Creamos una instancia de la clase Risk
        risk = Risk(1, 'R1', 'High', 'Risk 1', 'Description of risk 1', 'No', '2025-03-06')

        # Llamamos al método `to_json` y verificamos el diccionario resultante
        expected_result = {
            'id': 1,
            'cod': 'R1',
            'impact': 'High',
            'title': 'Risk 1',
            'description': 'Description of risk 1',
            'resolved': 'No'
        }
        self.assertEqual(risk.to_json(), expected_result)

if __name__ == '__main__':
    unittest.main()
