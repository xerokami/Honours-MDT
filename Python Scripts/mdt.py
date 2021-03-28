import paramiko
import time
import config

print("Which device do you want to configure MDT for? ")
ip_addr = input("[r1] or [r2] ")

if ip_addr.lower() == "r1":
    ip_addr = config.r1
elif ip_addr.lower() == "r2":
    ip_addr = config.r2

print("SSH connection established with ", ip_addr)
print("Which MDT stack do you want to use? ")
mdt = input("[TICK] or [ELK] ")

if mdt.lower() == "tick":
    mdt = config.mdt_tick
elif mdt.lower() == "elk":
    mdt = config.mdt_elk

user = config.user
secret = config.secret
yang_xpath = config.yang_xpath

pm = paramiko.SSHClient()
pm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pm.connect(hostname = ip_addr, username = user, password = secret)
c = pm.invoke_shell()

def global_config(c):
    c.send("conf t\n")

def device_health(c, option, mdt, ip_addr, yang_xpath):
    if option.lower() == "create":
        print("Creating telemetry subscriptions...")
        c.send("telemetry ietf sub 101\n")
        c.send(yang_xpath[0])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
        c.send("telemetry ietf sub 102\n")
        c.send(yang_xpath[1])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
    elif option.lower() == "remove":
        print("Removing telemetry subscriptions...")
        c.send("no telemetry ietf sub 101\n")
        c.send("no telemetry ietf sub 102\n")

def int_statistics(c, option, mdt, ip_addr, yang_xpath):
    if option.lower() == "create":
        print("Creating telemetry subscriptions...")
        c.send("telemetry ietf sub 111\n")
        c.send(yang_xpath[2])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
        c.send("telemetry ietf sub 112\n")
        c.send(yang_xpath[3])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
    elif option.lower() == "remove":
        print("Removing telemetry subscriptions...")
        c.send("no telemetry ietf sub 111\n")
        c.send("no telemetry ietf sub 112\n")

def ospf_statistics(c, option, mdt, ip_addr, yang_xpath):
    if option.lower() == "create":
        print("Creating telemetry subscriptions...")
        c.send("telemetry ietf sub 121\n")
        c.send(yang_xpath[4])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
    elif option.lower() == "remove":
        print("Removing telemetry subscriptions...")
        c.send("no telemetry ietf sub 121\n")

def bgp_statistics(c, option, mdt, ip_addr, yang_xpath):
    if option.lower() == "create":
        print("Creating telemetry subscriptions...")
        c.send("telemetry ietf sub 131\n")
        c.send(yang_xpath[5])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
        c.send("telemetry ietf sub 132\n")
        c.send(yang_xpath[6])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
    elif option.lower() == "remove":
        print("Removing telemetry subscriptions...")
        c.send("no telemetry ietf sub 131\n")
        c.send("no telemetry ietf sub 132\n")

def mdt_statistics(c, option, mdt, ip_addr, yang_xpath):
    if option.lower() == "create":
        print("Creating telemetry subscriptions...")
        c.send("telemetry ietf sub 141\n")
        c.send(yang_xpath[7])
        c.send(mdt.strip() + "\n")
        c.send("source-address {0}\n".format(ip_addr))
        time.sleep(0.5)
    elif option.lower() == "remove":
        print("Removing telemetry subscriptions...")
        c.send("no telemetry ietf sub 141\n")

def exit(c):
    c.send("end\n")
    c.send("exit\n")

while True:
    print("What would you like to do? ")
    option = input("[create] or [remove] MDT subscription or [quit]? ")
    time.sleep(0.5)

    if option == "quit":
        print("Closing SSH session with ", ip_addr)
        exit(c)
        time.sleep(1) 
        c.close
        break

    print(""" What do you want to configure?: \n
        [1]Device health statistics
        [2]Interface statistics
        [3]OSPF device statistics 
        [4]BGP device statistics
        [5]MDT subscription statistics
        """)
    choice = int(input("Enter your choice: "))
    time.sleep(0.5)

    global_config(c)
    if choice == 1:
        device_health(c, option, mdt, ip_addr, yang_xpath)
    elif choice == 2:
        int_statistics(c, option, mdt, ip_addr, yang_xpath)
    elif choice == 3:
        ospf_statistics(c, option, mdt, ip_addr, yang_xpath)
    elif choice == 4:
        bgp_statistics(c, option, mdt, ip_addr, yang_xpath)
    elif choice == 5:
        mdt_statistics(c, option, mdt, ip_addr, yang_xpath)
    else:
        print("Invalid choice!")