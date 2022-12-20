import numpy as np

class Result(object):
    def __init__(self, company):
        self.company = company
        self.revenue_projections = np.array([])

    def get_name(self):
        return self.company.get_name()
    
    def create_revenue_projections(self, years):
        """ 
            REQUIRES: years >= 0
            EFFECTS: Creates a np array of projected revenues with len[years]
        """
        if (years < 0):
            raise ValueError
      
        revenue = self.company.get_ttm_revenue()
        revenue_growth_rate = self.company.get_revenue_growth_rate()
        projected_revenues = [] 
        i = 0
        while i < years:
            projected_revenues.append(revenue)  
            revenue = revenue * revenue_growth_rate    
            i += 1
        
        self.revenue_projections = np.array(projected_revenues)

    def get_revenue_projections(self):
        """ EFFECTS: Returns a np array"""
        return self.revenue_projections

    def get_gross_profit_projections(self):
        """ EFFECTS: Returns a np array"""
        return self.get_revenue_projections() * self.company.get_gross_margin_percentage()

    def get_operating_profit_projections(self):
        """ EFFECTS: Returns a np array"""
        return self.get_revenue_projections() * self.company.get_operating_margin_percentage()

    def get_net_profit_projections(self):
        """ EFFECTS: Returns a np array"""
        return self.get_revenue_projections() * self.company.get_net_margin_percentage()            
    
def load_results(companies):
    results = {}
    for company in companies.values():
        results[company.get_name()] = Result(company)
    return results    