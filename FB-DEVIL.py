import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/I8lDwpjr7L1Jql60UhIXep')
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("FB-DEVIL32")
elif fbd=="64bit":
    __import__("FB-DEVIL64")
