from urllib import request


url = r'https://trackerslist.com/all_aria2.txt'


fileOpen = request.urlopen(url)
info = fileOpen.read()

static="bt-tracker="
info=info.decode("utf-8")
info=(static+info)
f=open(r"F:\aria.conf", "x")
f.write(info)
f.close()
