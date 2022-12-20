import unittest
import company_data

class TestCompanyData(unittest.TestCase):
    def setUp(self):
        self.company = company_data.Company('intel', 55, .05, 1.2, 1.15, 1.1)
    
    def test_company_ctor(self):
        company = company_data.Company('intel', 55, .05, 1.2, 1.15, 1.1)

        self.assertEqual(company.get_name(), 'intel')
    
    def test_read_company_data(self):
        df = company_data.read_company_data('company_data.csv')
        
        self.assertEqual(df.columns[0], 'amd')
        self.assertEqual(df.columns[1], 'nvidia') 

    def test_company_get_name(self):
        self.assertEqual(self.company.get_name(), 'intel')

    def test_company_get_ttm_revenue(self):
        self.assertEqual(self.company.get_ttm_revenue(), 55)

    def test_company_get_revenue_growth_rate(self):
        self.assertEqual(self.company.get_revenue_growth_rate(), .05)

    def test_company_get_gross_margin_percentage(self):
        self.assertEqual(self.company.get_gross_margin_percentage(), 1.2)

    def test_company_get_operating_margin_percentage(self):
        self.assertEqual(self.company.get_operating_margin_percentage(), 1.15)     

    def test_company_get_net_margin_percentage(self):
        self.assertEqual(self.company.get_net_margin_percentage(), 1.1)

    def test_load_companies(self):
        companies = company_data.load_companies('company_data.csv')
        
        self.assertEqual(companies["amd"].get_name(), "amd")      
        

if __name__ == "__main__":
    unittest.main()