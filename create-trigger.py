#"""
#Looks up a host based on its name, and then adds an item to it
#"""

from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

from variables import *

# The hostname at which the Zabbix web interface is available
#ZABBIX_SERVER = 'https://zabbix.example.com'

user_name = sys.argv[1]
user_pass =sys.argv[2]
zapi = ZabbixAPI(sys.argv[3])

# Login to the Zabbix API
zapi.login(user_name, user_pass)

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        trigger = zapi.trigger.create(
            description="Domain "+ str(new_domain) +" expire",
            priority=4,
            expression='{'+str(host_name)+':domain["'+ str(new_domain) +'"].last()}<30'
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    #print("Added item with triggerid {0} to host: {1}".format(trigger["triggerid"][0], host_name))
    print("Trigger addded")
else:
    print("No hosts found")


