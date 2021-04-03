from urllib import request


url = r'https://trackerslist.com/all_aria2.txt'


fileOpen = request.urlopen(url)
info = fileOpen.read()

static="bt-tracker="
info=info.decode("utf-8")
info=(static+info)
f=open(r"/home/.aria2/aria2.conf", "x")
f.write(info)
f.close()
