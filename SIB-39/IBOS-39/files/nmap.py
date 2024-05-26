import nmap3

nmap = nmap3.Nmap()
result = nmap.nmap_version_detection("192.168.31.135")
for i in result["192.168.31.135"]["ports"]:
	print(i["protocol"], i["portid"], i["state"], i["service"]["name"], i["service"]["version"])