import unittest
from unittest.mock import MagicMock
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.pkg.audit_log.model.audit_log import AuditLog

class TestAuditLogService(unittest.TestCase):
    def setUp(self):
        # Create a mock for the audit_log_store
        self.mock_audit_log_store = MagicMock()
        self.audit_log_service = AuditLogService(self.mock_audit_log_store)

    def test_log_event(self):
        mock_log = MagicMock(spec=AuditLog)
        self.audit_log_service.log_event(mock_log)
        # Verify log_event method of audit_log_store was called with mock_log
        self.mock_audit_log_store.log_event.assert_called_once_with(mock_log)

    def test_get_logs(self):
        offset = 0
        limit = 10
        # Setup mock return value for get_logs method of mock_audit_log_store
        self.mock_audit_log_store.get_logs.return_value = ['log1', 'log2']
        result = self.audit_log_service.get_logs(offset, limit)
        self.mock_audit_log_store.get_logs.assert_called_once_with(offset, limit)
        self.assertEqual(result, ['log1', 'log2'])

    def test_get_logs_for_user(self):
        identifier = '2'
        offset = 0
        limit = 10
        self.mock_audit_log_store.get_logs_for_user.return_value = ['log1', 'log2']
        result = self.audit_log_service.get_logs_for_user(identifier, offset, limit)
        self.mock_audit_log_store.get_logs_for_user.assert_called_once_with(identifier=identifier, offset=offset, limit=limit)
        self.assertEqual(result, ['log1', 'log2'])

if __name__ == '__main__':
    unittest.main()
