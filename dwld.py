from urllib import request


url = r'https://trackerslist.com/all_aria2.txt'

fileOpen = request.urlopen(url)
info = fileOpen.read()

static="dir=/content/drive/Shareddrives/Movies\nalways-resume=true\nmax-concurrent-downloads=50\ncontinue=true\ncheck-integrity=true\nmax-connection-per-server=16\nuser-agent=qBittorrent/4.3.3\npeer-agent=qbittorrent/4.3.3\npeer-id-prefix=-qB4330-\ndisk-cache=0\nfile-allocation=none\nseed-ratio=0.0\nbt-tracker="
info=info.decode("utf-8")
info=(static+info)
f=open(r"/home/.aria2/aria2.conf", "x")
f.write(info)
f.close()
