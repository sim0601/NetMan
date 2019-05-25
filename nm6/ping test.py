import subprocess

#iplist=["198.51.100.1","10.10.10.1", "11.11.11.1"]
iplist = ["8.8.8.8", "127.0.0.1"]
for ip in iplist:
    #p = subprocess.Popen('ping '+ip)
    p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)
    # the stdout=subprocess.PIPE will hide the output of the ping command
    p.wait()
    if p.poll():
        print (ip+" is down")
    else:
        print (ip+" is up")

# add code to ssh before pinging
