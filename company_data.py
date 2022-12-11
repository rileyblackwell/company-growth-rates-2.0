import pandas as pd

def read_company_data():
    """ EFFECTS: Returns a Pandas dataframe that contains columns of company data.
                Column name- Company name
                Row 1- TTM revenue
                R
    """
    return pd.read_csv("company_data.csv")

class Company(object):
    def __init__(self, name, ttm_revenue, revenue_growth_rate):
        self.name = name
        self.ttm_revenue = ttm_revenue
        self.revenue_growth_rate = revenue_growth_rate

    def get_name(self):
        return self.name

    def get_ttm_revenue(self):
        return self.ttm_revenue 

    def get_revenue_growth_rate(self):
        return self.revenue_growth_rate       

def create_companies():
    """ EFFECTS: Returns a dictionary, {[company name] : Company object}"""
    company_df = read_company_data()
    companies = {}

    for company in company_df:
        companies[company] =  Company(company, company_df[company][0], company_df[company][1])
    
    return companies    
