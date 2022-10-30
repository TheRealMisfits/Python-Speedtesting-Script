# Import Libraries
import speedtest
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Speedtest
st = speedtest.Speedtest(secure=1)

# Humanizing Script
def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# Print Logo
print(Fore.BLUE+"        .__         _____.__  __             ")
print(Fore.BLUE+"  _____ |__| ______/ ____|___/  |_ ______    ")
print(Fore.BLUE+" /     \|  |/  ___\   __\|  \   __/  ___/    ")
print(Fore.BLUE+"|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
print(Fore.BLUE+"|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
print(Fore.BLUE+"      \/        \/                    \/  \/")
print(Fore.BLUE+" ")
print(Fore.BLUE+"Powered by Speedtest.net // Created by themisfits.ml")
print(Fore.BLUE+" ")

# Download Speed
ds = st.download()
print("Download: " + Fore.BLUE + humansize(ds))

# Upload Speed
us = st.upload()
print("Upload: " + Fore.BLUE + humansize(us))