from unittest.mock import patch, MagicMock
import unittest
from src.services.RiskService import RiskService
from src.utils.Logger import Logger

class TestRiskService(unittest.TestCase):
    
    @patch('src.services.RiskService.get_connection')  
    def test_post_risk_success(self, mock_get_connection):

        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulamos el resultado que devolvería el `fetchall`
        mock_cursor.fetchall.return_value = [
            (1, 'R1', 'High', 'Risk 1', 'Description of risk 1', 'No', '2025-03-06')
        ]
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.post_risk("Risk 1 High")
        
        mock_cursor.fetchall.assert_called_once()  
        
        expected_result = [ 
            { 
                'id': 1,  
                'cod': 'R1', 
                'impact': 'High', 
                'title': 'Risk 1', 
                'description': 'Description of risk 1', 
                'resolved': 'No'
            }
        ]
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)  

    @patch('src.services.RiskService.get_connection')  
    def test_post_risk_text(self, mock_get_connection):
        
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.post_risk("")
        
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)  
        
    @patch('src.services.RiskService.get_connection')  
    def test_post_risk_no_results(self, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulamos que la consulta no devuelve resultados
        mock_cursor.fetchall.return_value = []
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.post_risk("Non-existent risk")
        
        mock_cursor.fetchall.assert_called_once()
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)

    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_success(self, mock_add_to_log, mock_get_connection):
        mock_get_connection.side_effect = Exception("Database connection failed")
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.post_risk("Risk 1 High")
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)

    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log') 
    def test_post_risk_connection_failed(self,mock_add_to_log, mock_get_connection):
        mock_get_connection.return_value = None
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.post_risk("Risk 1 High")
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)
    
    @patch('src.services.RiskService.get_connection')  
    def test_get_risk_no_results(self, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulamos que la consulta no devuelve resultados
        mock_cursor.fetchall.return_value = []
        
        # Llamamos al método que estamos probando
        risk_service = RiskService()
        result = risk_service.get_risk()
        
        mock_cursor.fetchall.assert_called_once()
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)




if __name__ == '__main__':
    unittest.main()
