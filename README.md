# Honours-MDT

EVE-NG Topology
---------------
![LAN Topology](/Topology.png)

Configuration Files Folder
---------------------------
Contains config files for all devices within topology.

Devices include:
- Core-R1 + Core-R2
- Dist-Sw1 + Dist-Sw2
- Acc-Sw1 + Acc-Sw2
- MGMT-Sw
- PC1-4
- Monitoring-Server

TICK Stack Folder
-----------------
Contains the docker-compose yml file used to spin up the TICK stack.

Also includes the corresponding telegraf config file used with the TICK stack.

ELK Stack Folder (Delogstashed)
-------------------------------
Contains the docker-compose yml file used to spin up the (Delogstashed) ELK stack.

Also includes the additional config files for telegraf, elasticsearch and kibana with the (Delogstashed) ELK stack.

Advanced Netconf Explorer (ANX) Folder
--------------------------------------
Contains the docker-compose yml file used to run the ANX container.

Also includes all the IOS XE Yang Models extracted from the CSR 1000V routers.

Python Scripts Folder
---------------------
Contains python scripts used within the project.

Python Scripts include:
- Config.py (Contains static variables e.g. Login Information etc)
- MDT.py (Used to automatically inject MDT configuration for a variety of scenarios)
- Routes.py (Used to inject additional routes to provide interesting data when monitored via the telemetry stacks)
