FILENAME=server
sudo socat openssl-listen:443,reuseaddr,fork,cert=hackingwithpentesterlab.link.crt,cafile=GandiStandardSSLCA2.pem,key=hackingwithpentesterlab.link.key,verify=0 -
