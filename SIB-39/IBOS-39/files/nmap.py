import nmap3


scan = nmap3.NmapScanTechniques()
result = scan.nmap_syn_scan('127.0.0.1')
print(result)