user = "jamie"
secret = "cisco"

r1 = "192.168.11.10"
r1_bgp = 11
r1_ospf = 12

r2 = "192.168.11.11"
r2_bgp = 13
r2_ospf = 14

localhost = "192.168.11.12"

mdt_tick = "encoding encode-kvgpb\nstream yang-push\nupdate-policy periodic 1000\nsource-vrf Management\nreceiver ip add 192.168.11.12 57500 protocol grpc-tcp\n"
mdt_elk = "encoding encode-kvgpb\nstream yang-push\nupdate-policy periodic 1000\nsource-vrf Management\nreceiver ip add 192.168.11.12 57555 protocol grpc-tcp\n"

yang_xpath = ["filter xpath /memory-ios-xe-oper:memory-statistics/memory-statistic\n", 
              "filter xpath /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization\n",
              "filter xpath /interfaces-ios-xe-oper:interfaces/interface/statistics\n",
              "filter xpath /cdp-ios-xe-oper:cdp-neighbor-details\n",
              "filter xpath /ospf-ios-xe-oper:ospf-oper-data/ospfv2-instance/ospfv2-area/ospfv2-interface/ospfv2-neighbor\n",
              "filter xpath /bgp-ios-xe-oper:bgp-state-data/neighbors/neighbor\n",
              "filter xpath /bgp-ios-xe-oper:bgp-state-data/address-families/address-family\n",
              "filter xpath /mdt-oper:mdt-oper-data/mdt-subscriptions/base\n"]