import random
import time
import sys
import os

class color:
    RED='\033[91m'
    YELLOW='\033[93m'
    UNDERLINE='\033[4m'
    GREEN='\033[92m'
    BLUE='\033[94m'
    PURPLE='\033[95m'
    BOLD='\033[1m'
    DARKCYAN='\033[36m'
    CYAN = '\033[96m'
    END='\033[0m'

# Function to check if a command exists
def command_exists(cmd):
    return os.system(f"command -v {cmd} >/dev/null 2>&1") == 0

def basic():
  print("\n\nINSTALLING START IN 3 SEC...\n\n")
  time.sleep(3)
  os.system("pkg update -y") # Added -y for non-interactive
  os.system("pkg upgrade -y") # Added -y
  os.system("pkg install python -y")
  os.system("pkg install python2 -y")
  os.system("pkg install python3 -y")
  os.system("pkg install tmux -y") # Changed apt to pkg for Termux consistency
  os.system("pip install requests")
  os.system("pip2 install requests")
  os.system("pip install mechanize")
  os.system("pip2 install mechanize")
  os.system("pip install bs4")
  os.system("pip2 install bs4")
  os.system("pip install rich")
  os.system("pkg install ruby -y")
  os.system("gem install lolcat") # Preferred for Termux for system-wide lolcat
  os.system("pip install yt_dlp")
  # Removed: pip install php (PHP is a system package, not python)
  # Removed: pip install lolcat (Duplicate of gem install lolcat)
  os.system("pip install futures")
  os.system("pip2 install futures")
  os.system("pkg install nano -y")
  os.system("pkg install espeak -y") # Ensure espeak is installed via pkg
  os.system("clear")
  print("""\033[1;32m
 _______  _______ _________          _______ 
(  ____ \\(  ____ \\\\__   __/|\\     /|(  ____ )
| (    \\/| (    \\/   ) (   | )   ( || (    )|
| (_____ | (__       | |   | |   | || (____)|
(_____  )|  __)      | |   | |   | ||  _____)
      ) || (         | |   | |   | || (      
/\\____) || (____/\\   | |   | (___) || )      
\\_______)(_______/   )_(   (_______)|/       
                                                                                 
  ____   ___  _   _ _____ 
 |  _ \\ / _ \\| \\ | | ____|
 | | | | | | |  \\| |  _|  
 | |_| | |_| | |\\  | |___ 
 |____/ \\___/|_| \\_|_____|
                          


""")
  if command_exists("espeak"): # Check if espeak exists before using
      os.system("espeak -a 500 'Setup Done'")
  else:
      print(f"{color.RED}espeak not found. Please install it manually if voice output is desired.{color.END}")

  
def full():
  print("\n\nSETUP START IN 3 SEC...\n\n")
  time.sleep(3)
  os.system("pkg update -y")
  os.system("pkg upgrade -y")
  os.system("pkg install python -y")
  os.system("pkg install python2 -y")
  os.system("pkg install python3 -y")
  os.system("pkg install wget -y")
  os.system("pkg install python-pip -y")
  os.system("pkg install fish -y")
  os.system("pkg install ruby -y")
  # os.system("pkg install help") # Removed: not a package
  os.system("pkg install dnsutils -y")
  os.system("pkg install php -y")
  os.system("pkg install perl -y")
  os.system("pkg install lua -y")
  os.system("pkg install parallel -y")
  os.system("pkg install nmap -y")
  os.system("pkg install bash -y")
  os.system("pkg install clang -y")
  os.system("pkg install nano -y")
  os.system("pkg install w3m -y")
  os.system("pkg install hydra -y")
  os.system("pkg install figlet -y")
  os.system("pkg install cowsay -y")
  os.system("pkg install curl -y")
  os.system("pkg install tar -y")
  os.system("pkg install zip -y")
  os.system("pkg install unzip -y")
  os.system("pkg install tor -y")
  os.system("pkg install net-tools -y")
  os.system("pkg install sudo -y")
  os.system("pkg install wireshark -y")
  os.system("pkg install tmux -y") # Consistent with pkg install
  os.system("pkg install crunch -y")
  # os.system("pkg install wgetrc") # Removed: not a package
  os.system("pkg install wcalc -y")
  os.system("pkg install openssl -y")
  os.system("pkg install openssl-tool -y")
  os.system("pkg install bmon -y")
  os.system("pkg install vpn -y") # Placeholder, specific VPN tools would be better
  os.system("pkg install unrar -y")
  os.system("pkg install toilet -y")
  os.system("pkg install proot -y")
  os.system("pkg install vim -y")
  os.system("pkg install vim-python -y")
  # os.system("pkg install ired") # Removed: not a common Termux package
  os.system("pkg install goaccess -y")
  os.system("pkg install golang -y")
  # os.system("pkg install kibi") # Removed: not a common Termux package
  os.system("pkg install tsu -y")
  os.system("pkg install mtools -y")
  os.system("pkg install file -y")
  os.system("pkg install vis -y")
  os.system("pkg install pass -y")
  os.system("pkg install pick -y")
  os.system("pkg install chroot -y")
  os.system("pkg install macchanger -y")
  os.system("pkg install ninja -y")
  os.system("pkg install elixir -y")
  os.system("pkg install swift -y")
  os.system("pkg install xmlstarlet -y")
  os.system("pkg install fakeroot -y")
  os.system("pkg install texinfo -y")
  os.system("pkg install netcat -y")
  os.system("pkg install wren -y")
  # os.system("pkg install gatling") # Removed: not a common Termux package
  os.system("pkg install cvs -y")
  os.system("pkg install ffmpeg -y")
  os.system("pkg install screen -y")
  os.system("pkg install neofetch -y")
  os.system("pkg install mariadb -y")
  os.system("pkg install picolisp -y")
  os.system("pkg install cmatrix -y")
  os.system("pkg install dropbear -y")
  os.system("pkg install openssh -y")
  os.system("pkg install espeak -y") # Ensure espeak is installed via pkg

  # Python pip installations
  os.system("pip install yt_dlp")
  # Removed: pip2 install wget (wget is system package)
  os.system("pip install bs4")
  os.system("pip2 install bs4")
  os.system("pip install requests")
  os.system("pip2 install requests")
  os.system("pip install mechanize")
  os.system("pip2 install mechanize")
  # Removed: pip install php, pip2 install php (PHP is a system package)
  os.system("gem install lolcat") # Consistent lolcat install
  os.system("pip install espeak") # Install espeak python binding (though pkg install is primary)

  os.system("clear")
  print("""\033[1;32m
 _______  _______ _________          _______ 
(  ____ \\(  ____ \\\\__   __/ |\\     /|(  ____ )
| (    \\/| (    \\/   ) (   | )   ( || (    )|
| (_____ | (__       | |   | |   | || (____)|
(_____  )|  __)      | |   | |   | ||  _____)
      ) || (         | |   | |   | || (      
/\\____) || (____/\\   | |   | (___) || )      
\\_______)(_______/   )_(   (_______)|/       
                                             
 ____   ___  _   _ _____ 
|  _ \\ / _ \\| \\ | | ____|
| | | | | | |  \\| |  _|  
| |_| | |_| | |\\  | |___ 
|____/ \\___/|_| \\_|_____|
                                    
	
	
""")
  if command_exists("espeak"): # Check if espeak exists before using
      os.system("espeak -a 500 'Setup Done'")
  else:
      print(f"{color.RED}espeak not found. Please install it manually if voice output is desired.{color.END}")

def banner_tool():
    print(f"\n{color.CYAN}Installing requirements for banner...{color.END}")
    time.sleep(1)
    os.system("pkg update -y")
    os.system("pkg upgrade -y")
    os.system("pkg install espeak figlet -y")
    os.system("pip install lolcat")

    user = input(f"{color.YELLOW}Enter your name for banner (e.g., studentname): {color.END}")
    
    banner_art = r"""
██╗ ██████╗███████╗███████╗
██║██╔════╝██╔════╝██╔════╝
██║██║     ███████╗█████╗  
██║██║     ╚════██║██╔══╝  
██║╚██████╗███████║██║     
╚═╝ ╚═════╝╚══════╝╚═╝
"""
    
    bashrc_path = os.path.expanduser("~/.bashrc")
    
    with open(bashrc_path, "a") as bashrc:
        bashrc.write(f"\nclear\nfiglet {user} | lolcat\necho '{banner_art}' | lolcat\necho 'welcome~{user}'\n")
    
    print(f"{color.GREEN}✅ Banner successfully added! Restart Termux to see it.{color.END}")
    if command_exists("espeak"): # Check if espeak exists before using
        os.system("espeak 'Banner has been set'")
    else:
        print(f"{color.RED}espeak not found. Voice notification skipped.{color.END}")


# Main program flow
logo = (f"""{color.GREEN}
██╗░█████╗░░██████╗███████╗
██║██╔══██╗██╔════╝██╔════╝
██║██║░░╚═╝╚█████╗░█████╗░░
██║██║░░██╗░╚═══██╗██╔══╝░░
██║╚█████╔╝██████╔╝██║░░░░░
╚═╝░╚════╝░╚═════╝░╚═╝░░░░░

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚╚═╝░░░░ {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}DEVELOPER{color.END}     {color.BOLD}:{color.END}  {color.GREEN} SOMSER {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}GITHUB{color.END}        {color.BOLD}:{color.END}  {color.GREEN} Somser SA {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}VERSION{color.END}       {color.BOLD}:{color.END}  {color.GREEN} 1.0 {color.END}
{color.BLUE}[{color.END}{color.BOLD}{color.PURPLE}={color.END}{color.BLUE}]{color.END}  {color.YELLOW}TOOL'S NAME{color.END}   {color.BOLD}:{color.END}  {color.GREEN} ICSF SETUP{color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
{color.BLUE}[{color.END}{color.PURPLE}01/A{color.END}{color.BLUE}]{color.END} {color.GREEN} Basic Setup {color.END}
{color.BLUE}[{color.END}{color.PURPLE}02/B{color.END}{color.BLUE}]{color.END} {color.GREEN} Full Setup {color.END}
{color.BLUE}[{color.END}{color.PURPLE}03/C{color.END}{color.BLUE}]{color.END} {color.GREEN} Termux Banner Setup {color.END}
{color.BLUE}[{color.END}{color.PURPLE}04/D{color.END}{color.BLUE}]{color.END} {color.GREEN} Admin Info {color.END}
{color.BLUE}[{color.END}{color.PURPLE}{color.RED}05/X{color.END}{color.BLUE}]{color.END} {color.GREEN} {color.RED}Exit Programme {color.END}
{color.BOLD}{color.BLUE}==============================================={color.END}
""")

if __name__ == "__main__":
    os.system("clear")
    
  
    for i in logo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0001) 

    while True:
        user_input=input(f"{color.BLUE}{color.BOLD}[{color.GREEN}>{color.BLUE}]{color.END} {color.GREEN}CHOOSE: ")
        user_input=user_input.replace(' ','')
        if user_input == "01" or user_input == "a" or user_input == "A" or user_input == "1":
           basic()
        elif user_input == "02" or user_input == "b" or user_input == "B" or user_input == "2":
           full()
        elif user_input == "03" or user_input == "c" or user_input == "C" or user_input == "3":
           banner_tool()
        elif user_input == "04" or user_input == "d" or user_input == "D" or user_input == "4":
           os.system("xdg-open https://sasomserhacker.staticrun.app")
        elif user_input ==  "05" or user_input == "x" or user_input == "X" or user_input == "5":
           sys.exit()
        else:
           print(f"{color.RED}Invalid Input!!! {color.END}")
