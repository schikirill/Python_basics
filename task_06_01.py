with open('nginx_logs.txt', 'r') as f:
    parsed_data = []
    for line in f:
        parsed_data.append((line.replace('"','').split()[0], line.replace('"','').split()[5], line.replace('"','').split()[6]))
print(parsed_data)