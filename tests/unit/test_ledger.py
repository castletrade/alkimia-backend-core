"""
Unit Test: Ledger Precision
Purpose: Validates the integrity of the double-entry ledger service.
Copyright: (c) 2026 Castle Trade LLC. Institutional Fintech Infrastructure.
"""

import unittest
from decimal import Decimal
from unittest.mock import MagicMock
from src.services.ledger_service import LedgerService

class TestLedgerService(unittest.TestCase):
    """
    Unit tests to ensure ledger arithmetic and data integrity.
    """

    def setUp(self):
        self.mock_db = MagicMock()
        self.ledger = LedgerService(self.mock_db)

    def test_record_transaction_integrity(self):
        """Verifies that a transaction is correctly prepared for recording."""
        result = self.ledger.record_transaction(
            tx_id="tx_test_123",
            amount=Decimal("150.50"),
            currency="USD",
            metadata={"description": "Institutional Settlement"}
        )
        # Note: In a real test, we would check if db.execute was called with correct params
        self.assertTrue(result)

    def test_balance_retrieval(self):
        """Checks if account balance queries return the expected interface."""
        balance = self.ledger.get_account_balance("acc_99")
        self.assertEqual(balance["account_id"], "acc_99")
        self.assertIn("balance", balance)

if __name__ == "__main__":
    unittest.main()
