import statistics


population = {
    'china': 143,
    'india': 136,
    'usa': 32
}

def fetch_population():
    return population

def add_population(country, value):
    population[country]=value
    return population

def remove(country):
    if country not in population:
        return "country not found to remove"
    del population[country]
    return f"Removed {country} available countries dict {population}"

#to check 
def print_individually():
    for country_name, population_count in population.items():
        print(f"country is {country_name} and population is {population_count}")

def get_countries():
    for country_name in population.keys():
        print(f"country is {country_name} ")


#stocks info
stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all_stocks():
    for stock,price_list in stocks.items():
        print(f"stock is {stock} and val is {price_list} and mean {statistics.mean(price_list)}")

def add_stock(stock_name,val):
    if(stock_name in stocks):
        stocks[stock_name].append(val)
    stocks[stock_name]=[val]

def main():
    print(print_all_stocks())
    add_stock('msft',600)
    print(print_all_stocks())
    
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        country = input(f"enter country")
        val = input(f"enter country population")
        print(add_population(country,val))
    elif op.lower() == 'print':
        # print(fetch_population())
        print_individually()
    elif op.lower() == 'remove':
        country = input(f"enter country to remove :")
        print(remove(country))
    elif op.lower() == 'other':
        get_countries()

if __name__ == '__main__':
    main()
    

# let cpudata = (
#     NodeHealthReportEvent
#     | filter TIMESTAMP >= startTime and TIMESTAMP <= endTime
#     | filter (Tenant == "cdb-ms-test51-centralus1-be1") 
#     | where healthPropertyName == "PerfProfileCollectorHealth" and message contains "CollectProfiles: True"
#     | extend Cpu0 = extractall("CPU0,_Total: (-?\\d+(?:\\.\\d+)?), CPU0,_Total: -?\\d+(?:\\.\\d+)?,", message)
#     | extend Cpu1 = extractall("CPU1,_Total: (-?\\d + (?:\\.\\d +)?), CPU1,_Total: -?\\d + (?:\\.\\d +)?,", message)
#     | summarize Cpu0Array = makelist(Cpu0), Cpu1Array = makelist(Cpu1) by bin(TIMESTAMP, 5m), Tenant, RoleInstance);cpuData
#     | mvexpand bagexpansion = bag Cpu0Array
#     | summarize Value = avg(todouble(Cpu0Array)) by TIMESTAMP, Tenant, RoleInstance
#     | where Value > 75
#     | extend NUMANode = 0
#     | union(
#         cpuData | mvexpand bagexpansion = bag Cpu1Array    
#                 | summarize Value = avg(todouble(Cpu1Array)) by TIMESTAMP, Tenant, RoleInstance    
#                 | where Value > 75    
#                 | extend NUMANode = 1)
#     | union(
#         NodeCounter5MRoleInstanceEvent
#         | filter TIMESTAMP >= startTime and TIMESTAMP <= endTime
#         | filter (Tenant == "cdb-ms-test51-centralus1-be1") 
#         | filter CounterName matches regex @"\\Processor Information\(\d+,_Total\)\\\% Processor Time" and SampleCount > 5
#         | summarize max(AverageCounterValue) by bin(TIMESTAMP, 5m), CounterName, RoleInstance, Tenant
#         | extend Value = max_AverageCounterValue| where max_AverageCounterValue > 75
#         | extend NUMANode = extract("\\d", 0, CounterName, typeof(long))
#         | project TIMESTAMP, NUMANode, Tenant, RoleInstance, Value
#         )
#         | summarize CpuValue = max(Value) by TIMESTAMP, Tenant, RoleInstance, NUMANode
#         | order by Tenant, RoleInstance, TIMESTAMP, NUMANode
#         | project Tenant, RoleInstance, TIMESTAMP, CpuValue, NUMANode
# )