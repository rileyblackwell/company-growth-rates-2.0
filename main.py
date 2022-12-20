import company_data
import projections
import print_projections

results = projections.load_results(company_data.load_companies('company_data.csv'))

print('Enter companies to create projections: (ex: amd, nvidia, intel)')
for company in results.keys():
    print(f'- {company}')    
print() # Prints an extra new line

company_names_response = input().lower()
company_names_response = set(company_names_response.split(', '))
for company in company_names_response:
    while company not in results:
        print('No data for this company.  Enter a different company: \n' +
              'Enter \'quit\' to exit: ')    
        company = input()
        if company == 'quit':
            raise ValueError('User did not enter a valid company name!')

print('Enter a number of years to view.  Press \'Enter\' to use default of 5 years: ')
years_response = input()
try:
    years = int(years_response)
except ValueError:
    print('Default of 5 years used:\n')  
    years = 5   

print('Enter a comma seperated list of the metrics to be viewed:' + 
      '\n- revenue\n- operating income\n- net income')
metrics = input().lower()
metrics = set(metrics.split(', '))

for company in company_names_response:
    results[company].create_revenue_projections(years)
    print(f'\n{company.upper()}')

    if 'revenue' in metrics:
        print_projections.revenue_projections(company, results)

    if 'operating income' in metrics:
        print_projections.operating_profit_projections(company, results)

    if 'net income' in metrics:
        print_projections.net_profit_projections(company, results)

print('Graph results? y/n')
graph_results_response = input().lower()    