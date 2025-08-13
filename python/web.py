server_ip = (192, 168, 1, 1)
allowed_ips = ['192.168.1.10', '192.168.1.20']

def update_allowed_ips(new_ips):
    global allowed_ips
    allowed_ips = new_ips
    print("Allowed IPs updated.")

def show_config():
    print(f"Server IP: {server_ip}")
    print(f"Allowed IPs: {allowed_ips}")

def update_server_ip(new_ip):
    print("Error: server_ip cannot be changed during runtime.")

show_config()
update_allowed_ips(['192.168.1.30', '192.168.1.40'])
update_server_ip((10, 0, 0, 1))
show_config()
