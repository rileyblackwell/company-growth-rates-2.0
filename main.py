import company_data
import projections
import print_projections


results = projections.create_results(company_data.create_companies())

print('Enter a company to create a projection: ')
company_name = input()
while company_name not in results:
    print('No data for this company.  Enter a different company: \n' +
          'Enter \'quit\' to exit: ')    
    company_name = input()
    if company_name == 'quit':
        raise ValueError('User did not enter a valid company name!')

print('Enter the number of years to view.  Press \'Enter\' to use default of 5 years: ')
years_str = input()
try:
    years = int(years_str)
except ValueError:
    print('Default of 5 years used:\n')  
    years = 5   

results[company_name].create_revenue_projections(years)

print('Enter a comma seperated list of the metrics to be viewed (revenue, operating income, net income):')
metrics = input()
metrics = set(metrics.split(', '))

print(f'\n{company_name.upper()}')

if 'revenue' in metrics:
    print_projections.revenue_projections(company_name, results)

if 'operating income' in metrics:
    print_projections.operating_profit_projections(company_name, results)

if 'net income' in metrics:
    print_projections.net_profit_projections(company_name, results)