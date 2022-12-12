import pandas as pd

def read_company_data():
    """ EFFECTS: Returns a Pandas dataframe that contains columns of company data.
                Column name- Company name
                Row 1- TTM revenue
                R
    """
    return pd.read_csv("company_data.csv")

class Company(object):
    def __init__(self, name, ttm_revenue, revenue_growth_rate, gross_margin_percentage,
                 operating_margin_percentage, net_margin_percentage):
        self.name = name
        self.ttm_revenue = ttm_revenue
        self.revenue_growth_rate = revenue_growth_rate
        self.gross_margin_percentage = gross_margin_percentage
        self.operating_margin_percentage = operating_margin_percentage
        self.net_margin_percentage = net_margin_percentage

    def get_name(self):
        return self.name

    def get_ttm_revenue(self):
        return self.ttm_revenue 

    def get_revenue_growth_rate(self):
        return self.revenue_growth_rate

    def get_gross_margin_percentage(self):
        return self.gross_margin_percentage

    def get_operating_margin_percentage(self):
        return self.operating_margin_percentage

    def get_net_margin_percentage(self):
        return self.net_margin_percentage                         

def create_companies():
    """ EFFECTS: Returns a dictionary, {[company name] : Company object}"""
    company_df = read_company_data()
    companies = {}

    for company in company_df:
        companies[company] =  Company(company, company_df[company][0], company_df[company][1],
                                      company_df[company][2], company_df[company][3], company_df[company][4])
    
    return companies    
