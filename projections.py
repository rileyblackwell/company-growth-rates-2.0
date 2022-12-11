# import company_data
import numpy as np

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
