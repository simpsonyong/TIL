site = list(input().split('/'))
print(f'protocol: {site[0][:len(site[0])-1]}')
print(f'host: {site[2]}')
print(f'others: {site[3]}')
