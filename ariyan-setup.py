#!/bin/bash

#================ COLORS ================#
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
NC='\033[0m'

#================ CHECK DEP =============#
for p in figlet toilet lolcat neofetch git
do
command -v $p >/dev/null 2>&1 || pkg install $p -y
done

#================ ANIMATION =============#
loading() {
echo -e "${CYAN}Starting System..."
for i in {1..25}
do
printf "[%-25s] %d%%\r" "$(printf '#%.0s' $(seq 1 $i))" $((i*4))
sleep 0.05
done
echo ""
}

#================ BANNER ================#
banner() {
clear
echo -e "${RED}"
figlet -f slant "ARIYAN" | lolcat
echo -e "${CYAN}===================================="
echo -e "${GREEN}   ULTRA PREMIUM TERMUX PANEL"
echo -e "${CYAN}====================================${NC}"
}

#================ DASHBOARD ============#
dashboard() {
echo -e "${GREEN}"
echo "User   : $(whoami)"
echo "Phone  : $(getprop ro.product.model)"
echo "Android: $(getprop ro.build.version.release)"
echo "Kernel : $(uname -r)"
echo "Time   : $(date '+%H:%M:%S')"
echo -e "${NC}"
}

#================ MAIN MENU ============#
while true
do
banner
dashboard

echo ""
echo -e "${YELLOW}[1] Full Setup"
echo -e "${YELLOW}[2] Install Tools"
echo -e "${YELLOW}[3] Custom Banner"
echo -e "${YELLOW}[4] System Info"
echo -e "${YELLOW}[5] Update Tool"
echo -e "${RED}[0] Exit"
echo ""

read -p "➤ Choose Option: " opt

case $opt in

1)
loading
pkg update -y && pkg upgrade -y
pkg install python git curl wget figlet toilet ruby neofetch -y
gem install lolcat
echo -e "${GREEN}[✓] FULL SETUP DONE"
sleep 2
;;

2)
loading
pkg install python git curl wget -y
echo -e "${GREEN}[✓] BASIC TOOLS INSTALLED"
sleep 2
;;

3)
read -p "Enter Banner Name: " name
cat > ~/.bashrc << EOF
clear
figlet -f slant "$name" | lolcat
echo "Welcome $name"
EOF
echo -e "${GREEN}[✓] CUSTOM BANNER SET"
sleep 2
;;

4)
clear
neofetch
read -p "Press Enter..."
;;

5)
loading
git pull
echo -e "${GREEN}[✓] TOOL UPDATED"
sleep 2
;;

0)
echo -e "${RED}GOOD BYE!"
exit
;;

*)
echo -e "${RED}INVALID OPTION"
sleep 1
;;

esac
done
