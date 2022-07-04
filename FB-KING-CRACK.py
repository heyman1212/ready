import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    os.system('git pull')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Assalamu alaikum\n Congratulations ! Your Device Support this Tools")
    print(' Join our Facebook Group For Any Help 🙋 thanks ')
    os.system('xdg-open https://www.facebook.com/groups/351076900316263/?ref=share');time.sleep(3)
    from FIRE import Subscraption
    Subscraption()