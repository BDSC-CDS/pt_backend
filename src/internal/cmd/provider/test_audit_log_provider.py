import unittest
from unittest.mock import patch, MagicMock
from src.internal.cmd.provider.audit_log import provide_audit_log_service, provide_audit_log_store

class TestAuditLogProvider(unittest.TestCase):
    @patch('src.internal.cmd.provider.audit_log.provide_db_type')
    @patch('src.internal.cmd.provider.audit_log.provide_db')
    def test_provide_audit_log_store_with_postgres(self, mock_provide_db, mock_provide_db_type):
        # Set up mocks
        mock_provide_db_type.return_value = 'postgres'
        mock_db_instance = MagicMock()
        mock_provide_db.return_value = mock_db_instance

        store = provide_audit_log_store()

        self.assertIsNotNone(store)
        mock_provide_db.assert_called_once()
        mock_provide_db_type.assert_called_once()

    @patch('src.internal.cmd.provider.audit_log.provide_audit_log_store')
    def test_provide_audit_log_service(self, mock_provide_audit_log_store):
        # Set up mocks
        mock_store_instance = MagicMock()
        mock_provide_audit_log_store.return_value = mock_store_instance

        # Execute the function under test
        service = provide_audit_log_service()

        # Verify the service is correctly instantiated
        self.assertIsNotNone(service)
        mock_provide_audit_log_store.assert_called_once()

    def test_provide_audit_log_store_raises_not_implemented_error(self):
        # Set up the environment for the test
        with patch('src.internal.cmd.provider.audit_log.provide_db_type') as mock_provide_db_type:
            mock_provide_db_type.return_value = 'unsupported_db'

            # Verify that calling the function with an unsupported db type raises an error
            with self.assertRaises(NotImplementedError):
                provide_audit_log_store()

if __name__ == '__main__':
    unittest.main()
