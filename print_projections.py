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

def graph_projections(years, metrics, companies, results):
    plt.figure()

    if 'revenue' in metrics:
        for company_name in companies:
            plt.plot(years, results[company_name].get_revenue_projections(), '.', label=f'{company_name} revenue')
      
    if 'operating income' in metrics:
         for company_name in companies:
            plt.plot(years, results[company_name].get_operating_profit_projections(), '-', label=f'{company_name} operating income')     

    if 'net income' in metrics:
        for company_name in companies:
            plt.plot(years, results[company_name].get_net_profit_projections(), '+', label=f'{company_name} net income')     
                         
            
    plt.xlabel('years')
    plt.ylabel('in billions USD')
    plt.legend(loc='best')
    plt.show()