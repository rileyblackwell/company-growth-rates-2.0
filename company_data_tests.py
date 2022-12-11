import unittest
import company_data


class TestCompanyData(unittest.TestCase):
    def test_read_company_data(self):
        df = company_data.read_company_data()
        
        self.assertEqual(df.columns[0], "amd")
        self.assertEqual(df.columns[1], "nvidia")

    def test_company(self):
        company = company_data.Company("intel", 55, .05)

        self.assertEqual(company.get_name(), "intel")
        self.assertEqual(company.get_ttm_revenue(), 55)
        self.assertEqual(company.get_revenue_growth_rate(), .05)

    def test_create_companies(self):
        companies = company_data.create_companies()
        
        self.assertEqual(companies["amd"].get_name(), "amd")
        self.assertEqual(companies["nvidia"].get_name(), "nvidia")
        

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCompanyData))
    unittest.TextTestRunner(verbosity=2).run(suite)