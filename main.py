# Import Libraries
import speedtest
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Speedtest
st = speedtest.Speedtest(secure=1)

# Humanizing Script
def humansize(nbytes):
  suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
  i = 0
  while nbytes >= 1024 and i < len(suffixes) - 1:
    nbytes /= 1024.
    i += 1
  f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
  return '%s %s' % (f, suffixes[i])

# Ask Mode
print(Fore.BLUE + "1)" + Fore.WHITE + " All")
print(Fore.BLUE + "2)" + Fore.WHITE + " Download Speed")
print(Fore.BLUE + "3)" + Fore.WHITE + " Upload Speed")
print(Fore.BLUE + " ")
option = int(input('''Option: ''' + Fore.BLUE))

# Mode Handeler
if option == 1:
  subprocess.call('reset')
  print(Fore.BLUE + "        .__         _____.__  __             ")
  print(Fore.BLUE + "  _____ |__| ______/ ____|___/  |_ ______    ")
  print(Fore.BLUE + " /     \|  |/  ___\   __\|  \   __/  ___/    ")
  print(Fore.BLUE + "|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
  print(Fore.BLUE + "|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
  print(Fore.BLUE + "      \/        \/                    \/  \/")
  print(Fore.BLUE + " ")
  print(Fore.BLUE + "Powered by Speedtest.net // Created by themisfits.ml")
  print(Fore.BLUE + " ")
  ds = st.download()
  print("Download: " + Fore.BLUE + humansize(ds))
  us = st.upload()
  print("Upload: " + Fore.BLUE + humansize(us))

if option == 2:
  subprocess.call('reset')
  print(Fore.BLUE + "        .__         _____.__  __             ")
  print(Fore.BLUE + "  _____ |__| ______/ ____|___/  |_ ______    ")
  print(Fore.BLUE + " /     \|  |/  ___\   __\|  \   __/  ___/    ")
  print(Fore.BLUE + "|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
  print(Fore.BLUE + "|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
  print(Fore.BLUE + "      \/        \/                    \/  \/")
  print(Fore.BLUE + " ")
  print(Fore.BLUE + "Powered by Speedtest.net // Created by themisfits.ml")
  print(Fore.BLUE + " ")
  ds = st.download()
  print("Download: " + Fore.BLUE + humansize(ds))

if option == 3:
  subprocess.call('reset')
  print(Fore.BLUE + "        .__         _____.__  __             ")
  print(Fore.BLUE + "  _____ |__| ______/ ____|___/  |_ ______    ")
  print(Fore.BLUE + " /     \|  |/  ___\   __\|  \   __/  ___/    ")
  print(Fore.BLUE + "|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
  print(Fore.BLUE + "|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
  print(Fore.BLUE + "      \/        \/                    \/  \/")
  print(Fore.BLUE + " ")
  print(Fore.BLUE + "Powered by Speedtest.net // Created by themisfits.ml")
  print(Fore.BLUE + " ")
  us = st.upload()
  print("Upload: " + Fore.BLUE + humansize(us))
