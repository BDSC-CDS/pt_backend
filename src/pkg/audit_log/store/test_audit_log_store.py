import unittest
from unittest.mock import patch, MagicMock
from src.pkg.audit_log.store.postgres import AuditLogStore
from src.pkg.audit_log.model.audit_log import AuditLog

class TestAuditLogStore(unittest.TestCase):
    @patch('src.pkg.audit_log.store.postgres.sessionmaker')
    def test_log_event(self, mock_sessionmaker):
        # Setup mock session
        mock_session = MagicMock()
        mock_sessionmaker.return_value.return_value = mock_session

        # Assume execute returns a mock result with an ID
        mock_session.execute.return_value.fetchone.return_value = [1]

        db = MagicMock()
        store = AuditLogStore(db)
        log = AuditLog(userid=1, service='test_service', action='test_action', body='test_body', response='test_response', error=False, created_at='2023-03-21')
        result = store.log_event(log)

        self.assertEqual(result.id, 1)


if __name__ == '__main__':
    unittest.main()
