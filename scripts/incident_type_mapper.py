name= incident.name
incidenttypelist=[]
if name.find("VPN")!=-1:
  incidenttypelist.append('VPN')
if name.find("leak")!=-1:
  incidenttypelist.append('Dataleak')
if name.find("SQL Injection")!=-1:
  incidenttypelist.append('SQL Injection')
if name.find("Port Scan")!=-1:
  incidenttypelist.append('Port Scan')  
if incidenttypelist==[]:
  incidenttypelist.append('Basic Incident')

incident["incident_type_ids"]=incidenttypelist  
# python version: 2
