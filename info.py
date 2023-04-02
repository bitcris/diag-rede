import subprocess
import json


def app(interface):
    getInfo = subprocess.run(['ip','-j','addr','show',interface], capture_output=True)
    bdata = getInfo.stdout.decode('utf-8')
    jsd = json.loads(bdata)
    global dat0, datIpv4, datIpv6
    dat0 = jsd[0]
    dat1 = dat0["addr_info"]

    if len(dat1) >1:
        datIpv4 = dat1[0]
        datIpv6 = dat1[1]
    else:
        datIpv4 = dat1[0]
        datIpv6 = "IPv6 Indidponível"
    

#VERIFICADOR DE PLATAFORMA 

def desktop(out):
    del out[0]
    del out[0]
    del out[0]
    interface = out[1]
    app(interface)



def mobile(out):
    del out[0]
    interface = out[1]
    app(interface)




cmd = subprocess.run(['ip', 'route', 'show'], capture_output=True)
out = cmd.stdout.decode('utf-8').split()

if out[0] == 'default':
    desktop(out)
else:
    mobile(out)
