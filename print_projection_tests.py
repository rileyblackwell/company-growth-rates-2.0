import unittest
import company_data
import projections
import print_projections

class TestOutput(unittest.TestCase):
    def test_revenue_projections(self):
        results = projections.load_results(company_data.load_companies())
        for company_name in results.keys():
            results[company_name].create_revenue_projections(5)
            
        print_projections.graph_revenue_projections(results.keys(), results)
            

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOutput))
    unittest.TextTestRunner(verbosity=2).run(suite)