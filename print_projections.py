import matplotlib.pyplot as plt

def format_projection(projections):
    projections_str = ''
    for projection in projections:
        projections_str += str(round(projection, 2)) + ', '
    return projections_str[:-2] + '\n' # slices off last comma and extra space  

def revenue_projections(company_name, results):
    print(format_projection(results[company_name].get_revenue_projections()))
    
def gross_profit_projections(company_name, results):
    print(format_projection(results[company_name].get_gross_profit_projections()))   

def operating_profit_projections(company_name, results):
    print(format_projection(results[company_name].get_operating_profit_projections()))  

def net_profit_projections(company_name, results):
    print(format_projection(results[company_name].get_net_profit_projections()))           

def graph_projections(metrics, companies, results):
    plt.figure()
    for company_name in companies:
        revenue_projections = results[company_name].get_revenue_projections()
        years = []
        year = 1
        for _ in revenue_projections:
            years.append(year)
            year += 1
       
        plt.plot(years, revenue_projections, label=f'{company_name}')
        
    plt.xlabel('years')
    plt.ylabel('revenue in billions USD')
    plt.legend(loc='best')
    plt.show()