import unittest
from parser import rule_engine

class TestRuleEngine(unittest.TestCase):
    def test_compliance_check_pass(self):
        rule = {
            "compliance_check": [
                {"field": "scope_1_2_emissions", "must_exist": True}
            ]
        }
        report = {"scope_1_2_emissions": 1500}
        result = rule_engine.validate(report, rule)[0]
        self.assertTrue(result["compliant"])

    def test_compliance_check_fail(self):
        rule = {
            "compliance_check": [
                {"field": "scope_1_2_emissions", "must_exist": True}
            ]
        }
        report = {"other_field": 999}
        result = rule_engine.validate(report, rule)[0]
        self.assertFalse(result["compliant"])

if __name__ == "__main__":
    unittest.main()
