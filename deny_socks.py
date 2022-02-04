import subprocess
ports_list = []

file = open('clean_svc_ports.txt', 'r')
data = file.read()
data1 = data.replace('[', '').replace(']', '')

for line in data1.split(','):
    ports_list.append(int(line))


for l in ports_list:
    deny = subprocess.run(['ufw', 'deny',f'{l}'], capture_output=True)
    print(deny)


print(len(ports_list), 'ports denied!')
