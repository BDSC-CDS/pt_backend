import unittest
from unittest.mock import patch, MagicMock
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.pkg.audit_log.store.postgres import AuditLogStore as PostgresAuditStore
from src.internal.cmd.provider.audit_log import provide_audit_log_service, provide_audit_log_store

class TestAuditLogProvider(unittest.TestCase):
    @patch('src.internal.cmd.provider.db.provide_db_type')
    @patch('src.internal.cmd.provider.db.provide_db')
    @patch('PostgresAuditStore')
    def test_provide_audit_log_store_postgres(self, mock_store, mock_provide_db, mock_provide_db_type):
        mock_provide_db_type.return_value = "postgres"
        mock_provide_db.return_value = MagicMock()
        mock_store.return_value = MagicMock(spec=PostgresAuditStore)

        store = provide_audit_log_store()

        self.assertIsInstance(store, PostgresAuditStore)
        mock_store.assert_called_once_with(mock_provide_db.return_value)
        assert True


if __name__ == '__main__':
    unittest.main()
