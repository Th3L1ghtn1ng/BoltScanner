import socket

a = """

  ____        _ _   ____                                  
 | __ )  ___ | | |_/ ___|  ___ __ _ _ __  _ __   ___ _ __ 
 |  _ \ / _ \| | __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |_) | (_) | | |_ ___) | (_| (_| | | | | | | |  __/ |   
 |____/ \___/|_|\__|____/ \___\__,_|_| |_|_| |_|\___|_|   
a tool for Http/Https & SSH & Telnet port scanning made by @d.cestaro                                                          
"""
print(a)
# Specificare l'intervallo di indirizzi IP da scansionare
start_ip = "192.168.1.1"
end_ip = "192.168.1.254"

# Convertire gli indirizzi IP in numeri interi
start_int = int(start_ip.split(".")[3])
end_int = int(end_ip.split(".")[3])

# Creare una lista di indirizzi IP da scansionare
ip_list = [start_ip.split(".")[0] + "." + start_ip.split(".")[1] + "." + start_ip.split(".")[2] + "." + str(i) for i in range(start_int, end_int+1)]

# Scansionare gli indirizzi IP alla ricerca di server HTTP o HTTPS
for ip in ip_list:
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, 80))
    if result == 0:
      print(f"Found server HTTP on address {ip}")
    sock.close()
  except:
    pass

  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, 443))
    if result == 0:
      print(f"Found server HTTPS on address {ip}")
    sock.close()
  except:
    pass
    
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, 22))
    if result == 0:
      print(f"Found server SSH on address {ip}")
    sock.close()
  except:
    pass
    
    try:
    	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    	sock.settimeout(0,5)
    	result = sock.connect_ex((ip,23))
    	if result == 0:
    		print("Found server TELNET on address {ip}")
    		sock.close()
    except:
    	pass