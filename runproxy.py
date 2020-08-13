import os

# pip3 install  mitmproxy

os.system("mitmdump.exe -p 8888 -s record.py")
#os.system("mitmdump -p 8888   -w wireless-login")