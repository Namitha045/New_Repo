#############################################################################################################################
import requests
import json
import time
#############################################################################################################################

my_url = requests.get('https://formulae.brew.sh/api/formula.json')
data_str = my_url.json()
results = []
for package in data_str:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    get_package_data = requests.get(package_url)
    package_data = get_package_data.json()
    installs_30 = package_data['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_data['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_data['analytics']['install_on_request']['365d'][package_name]
    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365
        }
    }
    results.append(data)
    time.sleep(get_package_data.elapsed.total_seconds())
    if len(results) == 10:
        break
with open('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)
    

