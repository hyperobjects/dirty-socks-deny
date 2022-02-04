#Step 1:  get second column of listening service ports and save to text file<br>
cat /etc/services | awk '{print $2}'> ports.txt  <br> <br>

#Step 2: run get_ports.py to clean list of ports <br>
python3 get_ports.py <br> <br>

#Step 3: run deny_socks.py to turn string of ports into a list of ports, then close using ufw <br>
python3 deny_socks.py <br><br>
