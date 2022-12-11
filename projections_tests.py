import unittest
import company_data
import projections

class TestProjections(unittest.TestCase):
    def test_revenue_projection(self):
        company = company_data.Company("intel", 10, 1.1)
        
        projected_revenues = projections.revenue_projection(company, 2)
        
        self.assertEqual(projected_revenues[0], 10)
        self.assertEqual(projected_revenues[1], 11)
        self.assertEqual(projected_revenues[2], 11 * 1.1)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestProjections))
    unittest.TextTestRunner(verbosity=2).run(suite)