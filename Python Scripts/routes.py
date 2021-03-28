import paramiko
import time
import config

print("Which device do you want to send data to? ")
ip_addr = input("[r1] or [r2] ")

if ip_addr == "r1":
    ip_addr = config.r1
    network_bgp = config.r1_bgp
    network_ospf = config.r1_ospf
elif ip_addr == "r2":
    ip_addr = config.r2
    network_bgp = config.r2_bgp
    network_ospf = config.r2_ospf

routes = int(input("Enter the no of routes to add/remove: "))
protocol = input("[bgp] or [ospf] ")

if protocol == "bgp":
    protocol_num = 64512
else:
    protocol_num = 1

print("Select a choice ")
choice = int(input("[1] Inject routes [2] Remove routes ")) 

pm = paramiko.SSHClient()
pm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pm.connect(hostname = ip_addr, username = config.user, password = config.secret)

print("SSH connection established with ", ip_addr)

c = pm.invoke_shell()

def global_config(c):
    c.send("conf t\n")

def route_inject_static_bgp(c, routes, network_bgp):
    for i in range(1, (routes + 1)):
        print("Injecting route no: " + str(i))
        c.send("ip route {0}.0.0.{1} 255.255.255.255 null0\n".format(network_bgp, i))
        time.sleep(0.5)

def route_injector_bgp(c, routes, protocol, protocol_num, network_bgp):
    c.send("router {0} {1}\n".format(protocol, protocol_num))
    for i in range(1, (routes + 1)):
        print("Adding route no: " + str(i) + " to {0} {1}".format(protocol, protocol_num))
        c.send("network {0}.0.0.{1} mask 255.255.255.255\n".format(network_bgp, i))
        time.sleep(0.5)

def route_remove_static_bgp(c, routes, network_bgp):
    for i in range(1, (routes + 1)):
        print("Removing route no: " + str(i))
        c.send("no ip route {0}.0.0.{1} 255.255.255.255 null0\n".format(network_bgp, i))
        time.sleep(0.5)

def route_remover_bgp(c, routes, protocol, protocol_num, network_bgp):
    c.send("router {0} {1}\n".format(protocol, protocol_num))
    for i in range(1, (routes + 1)):
        print("Removing route no: " + str(i) + " from {0} {1}".format(protocol, protocol_num))
        c.send("no network {0}.0.0.{1} mask 255.255.255.255\n".format(network_bgp, i))
        time.sleep(0.5)

def route_inject_static_ospf(c, routes, network_ospf):
    for i in range(1, (routes + 1)):
        print("Injecting route no: " + str(i))
        c.send("ip route {0}.0.0.{1} 255.255.255.255 null0\n".format(network_ospf, i))
        time.sleep(0.5)

def route_injector_ospf(c, routes, protocol, protocol_num, network_ospf):
    c.send("router {0} {1}\n".format(protocol, protocol_num))
    for i in range(1, (routes + 1)):
        print("Adding route no: " + str(i) + " to {0} {1}".format(protocol, protocol_num))
        c.send("network {0}.0.0.{1} 0.0.0.0 area 0\n".format(network_ospf, i))
        time.sleep(0.5)
    c.send("redis static subnet\n")

def route_remove_static_ospf(c, routes, network_ospf):
    for i in range(1, (routes + 1)):
        print("Removing route no: " + str(i))
        c.send("no ip route {0}.0.0.{1} 255.255.255.255 null0\n".format(network_ospf, i))
        time.sleep(0.5)

def route_remover_ospf(c, routes, protocol, protocol_num, network_ospf):
    c.send("router {0} {1}\n".format(protocol, protocol_num))
    for i in range(1, (routes + 1)):
        print("Removing route no: " + str(i) + " from {0} {1}".format(protocol, protocol_num))
        c.send("no network {0}.0.0.{1} 0.0.0.0 area 0\n".format(network_ospf, i))
        time.sleep(0.5)
    c.send("no redis static subnet\n")

def exit(c):
    c.send("end\n")
    c.send("exit\n")

global_config(c)
if choice == 1 and protocol == "bgp":
    route_inject_static_bgp(c, routes, network_bgp)
    route_injector_bgp(c, routes, protocol, protocol_num, network_bgp)
elif choice == 2 and protocol == "bgp":
    route_remove_static_bgp(c, routes, network_bgp)
    route_remover_bgp(c, routes, protocol, protocol_num, network_bgp)
elif choice == 1 and protocol == "ospf":
    route_inject_static_ospf(c, routes, network_ospf)
    route_injector_ospf(c, routes, protocol, protocol_num, network_ospf)
elif choice == 2 and protocol == "ospf":
    route_remove_static_ospf(c, routes, network_ospf)
    route_remover_ospf(c, routes, protocol, protocol_num, network_ospf)
else:
    print("Invalid choice!")
exit(c)

time.sleep(1)
print("Closing SSH session with ", ip_addr) 
c.close