import unittest
import company_data
import projections

class TestProjections(unittest.TestCase):
    def test_result(self):
        results = projections.Result(company_data.Company("intel", 10, 1.1, 1.2, 1.15, 1.1))
        results.create_revenues_projection(2)
        revenue_projections = results.get_revenues_projection()

        self.assertEqual(revenue_projections[0], 10)
        self.assertEqual(revenue_projections[1], 11)
        self.assertEqual(revenue_projections[2], 11 * 1.1)

    def test_revenue_projection(self):
        company = company_data.Company("intel", 10, 1.1, 1.2, 1.15, 1.1)
        
        revenue_projections = projections.revenue_projection(company, 2)
        
        self.assertEqual(revenue_projections[0], 10)
        self.assertEqual(revenue_projections[1], 11)
        self.assertEqual(revenue_projections[2], 11 * 1.1)

    def test_create_results(self):
        companies = company_data.create_companies()
        results = projections.create_results(companies)
        results["amd"].create_revenues_projection(2)
        revenue_projections = results["amd"].get_revenues_projection()

        ttm_revenue = companies["amd"].get_ttm_revenue()
        growth_rate = companies["amd"].get_revenue_growth_rate()
        self.assertEqual(revenue_projections[0], ttm_revenue)
        self.assertEqual(revenue_projections[1], ttm_revenue * growth_rate)
        self.assertEqual(revenue_projections[2], (ttm_revenue * growth_rate) * growth_rate)




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestProjections))
    unittest.TextTestRunner(verbosity=2).run(suite)