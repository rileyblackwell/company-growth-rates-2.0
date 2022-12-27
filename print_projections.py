import matplotlib.pyplot as plt

prop_cycle = plt.rcParams['axes.prop_cycle']
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['lines.dotted_pattern'] = [1, 8]
plt.rcParams['lines.dashed_pattern'] = [12, 6]
 
def format_projection(projections):
    projections_str = ''
    for projection in projections:
        projections_str += str(round(projection, 2)) + ', '
    return projections_str[:-2] + '\n' # slices off last comma and extra space  

def revenue(company_name, results):
    print(format_projection(results[company_name].get_revenue_projections()))
    
def gross_profit(company_name, results):
    print(format_projection(results[company_name].get_gross_profit_projections()))   

def operating_profit(company_name, results):
    print(format_projection(results[company_name].get_operating_profit_projections()))  

def net_profit(company_name, results):
    print(format_projection(results[company_name].get_net_profit_projections()))           

def graph_projections(years, metrics, companies, results):
    plt.figure()
    
    companies_and_colors = zip(companies, prop_cycle.by_key()['color']) 
    for company_and_color in companies_and_colors:       
        if 'revenue' in metrics:
                plt.plot(years, results[company_and_color[0]].get_revenue_projections(), linestyle='solid', 
                         color =f'{company_and_color[1]}', label=f'{company_and_color[0]} revenue')

        if 'operating income' in metrics:
                plt.plot(years, results[company_and_color[0]].get_operating_profit_projections(), linestyle='dashed', 
                         color =f'{company_and_color[1]}', label=f'{company_and_color[0]} operating income')     

        if 'net income' in metrics:
                plt.plot(years, results[company_and_color[0]].get_net_profit_projections(), linestyle='dotted', 
                         color =f'{company_and_color[1]}', label=f'{company_and_color[0]} net income')     

    plt.xlabel('years')
    plt.ylabel('in billions USD')
    plt.legend(loc='best')
    plt.show()
