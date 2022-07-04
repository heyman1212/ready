import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    os.system('git pull')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print(' Join Over Facebook Group For Any Help 😍 ')
    os.system('xdg-open https://www.facebook.com/groups/blackmafiax.pamming.squad/?ref=share');time.sleep(3)
    from V4 import Main
    Main()