#"""
#Looks up a host based on its name, and then adds an item to it
#"""

# The hostname at which the Zabbix web interface is available
#ZABBIX_SERVER = 'https://zabbix.example.com'


from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

user_name = sys.argv[1]
user_pass = sys.argv[2]

zapi = ZabbixAPI(sys.argv[3])

var = sys.argv[2]

from variables import *

# Login to the Zabbix API
zapi.login(user_name, user_pass)

#host_application = zapi.application.get(filter={"applicationids": host_application})
print(sys.argv[3])

if  sys.argv[3] == "https://zabbix.example.com" :
   if str(host_name) == "IMPORTANT Domains":
      host_application = ["12345"]
   elif str(host_name) == "OTHER Domains":
       host_application = ["67890"]
else:
   if  sys.argv[3] == "https://zabbix-2.example.com" :
      if str(host_name) == "IMPORTANT Domains":  
         host_application = ["11121"]
      elif str(host_name) == "OTHER Domains":
          host_application = ["31415"]
      else:
        print("Could not find true expression")

print(host_application)

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        item = zapi.item.create(
            hostid=host_id,
            name='Check name ',
            key_='domain["'+ str(new_domain) +'"]',
            type=10,
            value_type=3,
            interfaceid=hosts[0]["interfaces"][0]["interfaceid"],
            applications=host_application,
            delay="86400s;h11m50"
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    print("Added item with itemid {0} to host: {1}".format(item["itemids"][0], host_name))
else:
    print("No hosts found")


