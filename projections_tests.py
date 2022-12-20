import unittest
import company_data
import projections

class TestProjections(unittest.TestCase):
    def setUp(self):
        self.company = company_data.Company('intel', 10, 1.1, .3, .2, .1)
        self.result = projections.Result(self.company) 
        
        self.result.create_revenue_projections(3)
    
    def test_result_ctor(self):
        result = projections.Result(self.company)
        self.assertEqual(result.get_name(), 'intel') 
    
    def test_result_get_name(self):
        self.assertEqual(self.result.get_name(), 'intel') 
    
    def test_result_get_revenue_projections(self):
        revenue_projections = self.result.get_revenue_projections()

        self.assertEqual(revenue_projections[0], 10)
        self.assertEqual(revenue_projections[1], 11)
        self.assertEqual(revenue_projections[2], 11 * 1.1)

    def test_result_get_gross_profit_projections(self):
        gross_profit_projections = self.result.get_gross_profit_projections()

        self.assertEqual(gross_profit_projections[0], 10 * self.company.get_gross_margin_percentage())
        self.assertEqual(gross_profit_projections[1], 11 * self.company.get_gross_margin_percentage())
        self.assertEqual(gross_profit_projections[2], 11 * 1.1 * self.company.get_gross_margin_percentage())

    def test_result_get_operating_income_projections(self):
        operating_income_projections = self.result.get_operating_profit_projections()

        self.assertEqual(operating_income_projections[0], 10 * self.company.get_operating_margin_percentage())
        self.assertEqual(operating_income_projections[1], 11 * self.company.get_operating_margin_percentage())
        self.assertEqual(operating_income_projections[2], 11 * 1.1 * self.company.get_operating_margin_percentage())

    def test_result_get_net_income_projections(self):
        net_income_projections = self.result.get_net_profit_projections()

        self.assertEqual(net_income_projections[0], 10 * self.company.get_net_margin_percentage())
        self.assertEqual(net_income_projections[1], 11 * self.company.get_net_margin_percentage())
        self.assertEqual(net_income_projections[2], 11 * 1.1 * self.company.get_net_margin_percentage())    
    
    def test_create_results(self):
        results = projections.load_results(company_data.load_companies('company_data.csv'))
        
        self.assertEqual(results["amd"].get_name(), "amd") 


if __name__ == "__main__":
    unittest.main()