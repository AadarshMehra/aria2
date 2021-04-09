from urllib import request


url = r'https://trackerslist.com/all_aria2.txt'

fileOpen = request.urlopen(url)
info = fileOpen.read()

static="dir=/content/drive/Shareddrives/Movies/Movies/
always-resume=true
max-concurrent-downloads=10
enable-rpc=true
rpc-listen-all=true
max-connection-per-server=16
user-agent=qBittorrent/4.3.3
peer-agent=qbittorrent/4.3.3
peer-id-prefix=-qB4330-
disk-cache=0
file-allocation=none
seed-ratio=1.5
bt-tracker="
info=info.decode("utf-8")
info=(static+info)
f=open(r"/home/.aria2/aria2.conf", "x")
f.write(info)
f.close()
