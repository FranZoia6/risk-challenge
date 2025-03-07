from unittest.mock import patch, MagicMock
import unittest
from src.services.RiskService import RiskService
from src.utils.Logger import Logger

class TestRiskService(unittest.TestCase):
    
    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_success(self, mock_add_to_log, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = [
            (1, 'R1', 'High', 'Risk 1', 'Description of risk 1', 'No', '2025-03-06')
        ]
        
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
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_text(self, mock_add_to_log, mock_get_connection):
        risk_service = RiskService()
        result = risk_service.post_risk("")
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)  

    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_no_results(self, mock_add_to_log, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        mock_cursor.fetchall.return_value = []
        
        risk_service = RiskService()
        result = risk_service.post_risk("Non-existent risk")
        
        mock_cursor.fetchall.assert_called_once()
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)

    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_success_exception(self, mock_add_to_log, mock_get_connection):
        mock_get_connection.side_effect = Exception("Database connection failed")
        
        risk_service = RiskService()
        result = risk_service.post_risk("Risk 1 High")
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)

    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_post_risk_connection_failed(self, mock_add_to_log, mock_get_connection):
        mock_get_connection.return_value = None
        
        risk_service = RiskService()
        result = risk_service.post_risk("Risk 1 High")
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)
    
    @patch('src.services.RiskService.get_connection')  
    @patch.object(Logger, 'add_to_log')  
    def test_get_risk_no_results(self, mock_add_to_log, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulamos que la consulta no devuelve resultados
        mock_cursor.fetchall.return_value = []
        
        risk_service = RiskService()
        result = risk_service.get_risk()
        
        mock_cursor.fetchall.assert_called_once()
        
        expected_result = []
        
        # Verificamos si el resultado coincide con el esperado
        self.assertEqual(result, expected_result)

    @patch('src.services.RiskService.get_connection')
    @patch.object(Logger, 'add_to_log')  
    def test_update_risk_success(self, mock_add_to_log, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        
        # Simulamos una actualización exitosa
        mock_cursor.callproc.return_value = None
        mock_cursor.fetchone.return_value = (1,) 

        risk_data = {
            "id": 1,
            "cod": "R1",
            "impact": "High",
            "title": "Updated Risk",
            "description": "Updated description",
            "resolved": "1"
        }

        risk_service = RiskService()
        success, message = risk_service.update_risk(risk_data)

        mock_cursor.callproc.assert_called_once_with(
            'sp_updateRisks',
            [1, "R1", "High", "Updated Risk", "Updated description", 1]
        )

        # Verificamos si la actualización fue exitosa
        self.assertTrue(success)
        self.assertEqual(message, "Risk updated successfully")
    
    @patch('src.services.RiskService.get_connection')
    @patch.object(Logger, 'add_to_log')  
    def test_update_risk_failed_connection(self, mock_add_to_log, mock_get_connection):
        mock_get_connection.return_value = None

        risk_data = {
            "id": 1,
            "cod": "R1",
            "impact": "High",
            "title": "Updated Risk",
            "description": "Updated description",
            "resolved": "1"
        }

        risk_service = RiskService()
        success, message = risk_service.update_risk(risk_data)

        # Verificamos si la conexión falló
        self.assertFalse(success)
        self.assertEqual(message, "Database connection failed")

    @patch('src.services.RiskService.get_connection')
    @patch.object(Logger, 'add_to_log')  
    def test_add_risk_success(self, mock_add_to_log, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        # Simulamos una inserción exitosa
        mock_cursor.callproc.return_value = None
        mock_cursor.fetchone.return_value = (2,)  

        risk_data = {
            "cod": "R2",
            "impact": "Medium",
            "title": "New Risk",
            "description": "Description of new risk",
            "resolved": "0"
        }

        risk_service = RiskService()
        success, new_id = risk_service.add_risk(risk_data)

        mock_cursor.callproc.assert_called_once_with(
            'sp_addRisks',
            ["R2", "Medium", "New Risk", "Description of new risk", 0]
        )

        # Verificamos si el riesgo fue agregado correctamente
        self.assertTrue(success)
        self.assertEqual(new_id, 2)
    
    @patch('src.services.RiskService.get_connection')
    @patch.object(Logger, 'add_to_log')  
    def test_add_risk_failed_connection(self, mock_add_to_log, mock_get_connection):
        mock_get_connection.return_value = None

        risk_data = {
            "cod": "R2",
            "impact": "Medium",
            "title": "New Risk",
            "description": "Description of new risk",
            "resolved": "0"
        }

        risk_service = RiskService()
        success, message = risk_service.add_risk(risk_data)

        # Verificamos si la conexión falló
        self.assertFalse(success)
        self.assertEqual(message, "Database connection failed")


if __name__ == '__main__':
    unittest.main()
