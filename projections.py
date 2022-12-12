import numpy as np

class Result(object):
    def __init__(self, company):
        self.company = company
        self.revenues_projection = None

    def create_revenues_projection(self, years):
        """ 
            REQUIRES: years >= 0
            EFFECTS: Creates a np array of projected revenues with len[years + 1]
        """
        if (years < 0):
            raise ValueError
        
        self.revenues_projection = revenue_projection(self.company, years)

    def get_revenues_projection(self):
        """ EFFECTS: Returns a np array"""
        return self.revenues_projection            


def revenue_projection(company, years):
    """ EFFECTS: Returns a np array of projected revenues with len[years + 1]."""
    projected_revenues = [] 
    revenue = company.get_ttm_revenue()
    revenue_growth_rate = company.get_revenue_growth_rate()
    i = 0
    while i <= years:
        projected_revenues.append(revenue)  
        revenue = revenue * revenue_growth_rate    
        i += 1

    return np.array(projected_revenues)


def create_results(companies):
    results = {}
    for company in companies.values():
        results[company.get_name()] = Result(company)
    return results    