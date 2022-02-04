text = open('ports.txt')

svc_ports = []

data = text.read().splitlines()
for line in data:
    if '/' in line:
       # print(int(line.split('/')[0]))
       svc_ports.append(int(line.split('/')[0]))

with open('clean_svc_ports.txt', 'w') as output:
    output.write(str(svc_ports))



