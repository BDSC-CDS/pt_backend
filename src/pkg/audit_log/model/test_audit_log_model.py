import unittest
from src.pkg.audit_log.model.audit_log import AuditLog

class TestAuditLogModel(unittest.TestCase):
    def test_to_dict(self):
        log = AuditLog(userid=1, service='test_service', action='test_action', body='test_body', response='test_response', error=False, created_at='01-01-2024')
        expected = {
            'userid': 1,
            'service': 'test_service',
            'action': 'test_action',
            'body': 'test_body',
            'response': 'test_response',
            'error': False,
            'created_at': '01-01-2024',
            'id': None,
        }
        self.assertEqual(log.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
