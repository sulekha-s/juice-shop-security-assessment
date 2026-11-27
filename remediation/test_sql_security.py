import io
from contextlib import redirect_stdout
import unittest
from sql_security_demo import create_database, secure_search


class TestSQLSecurity(unittest.TestCase):

    def setUp(self):
        self.connection = create_database()

    def tearDown(self):
        self.connection.close()

    def test_normal_search(self):
        result = secure_search(self.connection, "Apple")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Apple Juice")

    def test_apostrophe_search(self):
        result = secure_search(self.connection, "Ben's Juice")
        self.assertEqual(result[0][1], "Ben's Juice")

    def test_no_matching_products(self):
        result = secure_search(self.connection, "80's")
        self.assertEqual(result, [])
    
    def test_database_failure(self):
        self.connection.close()
        result = secure_search(self.connection, "Apple")
        self.assertIsNone(result)

    def test_error_logging(self):
        self.connection.close()

        with self.assertLogs(level="ERROR") as logs:
            secure_search(self.connection, "Apple")

        self.assertIn(
            "Database search failed",
            logs.output[0]
        )
    
    def test_secure_error_message(self):
        self.connection.close()

        output = io.StringIO()

        with redirect_stdout(output):
            secure_search(self.connection, "Apple")

        self.assertEqual(
            output.getvalue().strip(),
            "Unable to complete the search."
        )


if __name__ == "__main__":
    unittest.main()