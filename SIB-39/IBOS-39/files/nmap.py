import nmap3

nmap = nmap3.Nmap()
result = nmap.nmap_version_detection("127.0.0.1")
for i in result["127.0.0.1"]["ports"]:
	print(i["protocol"], i["portid"], i["state"], i["service"]["name"], i["service"]["version"])