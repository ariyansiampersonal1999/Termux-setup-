#!/bin/bash

#================ COLORS ================#
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
PURPLE='\033[1;35m'
NC='\033[0m'

#================ CHECK DEP =============#
for p in figlet toilet lolcat neofetch git
do
command -v $p >/dev/null 2>&1 || pkg install $p -y
done

#================ LOADING ===============#
loading() {
echo -e "${CYAN}Starting System..."
for i in {1..20}
do
printf "[%-20s] %d%%\r" "$(printf '#%.0s' $(seq 1 $i))" $((i*5))
sleep 0.05
done
echo ""
}

#================ BANNER ================#
banner() {
clear

echo -e "${PURPLE}"
figlet -f slant "Termux Setup" | lolcat

echo -e "${CYAN}"
echo "╔══════════════════════════════════════╗"
echo "║        ⚡ TERMUX SETUP TOOL ⚡       ║"
echo "║           VERSION v6 PRO             ║"
echo "╚══════════════════════════════════════╝"

echo -e "${GREEN}"
echo "➤ Status : ACTIVE"
echo "➤ Mode   : ULTRA PREMIUM"
echo "➤ Power  : MAX PERFORMANCE"
echo -e "${NC}"
}

#================ SYSTEM INFO ===========#
sysinfo() {
echo -e "${GREEN}"
echo "User    : $(whoami)"
echo "Device  : $(getprop ro.product.model)"
echo "Android : $(getprop ro.build.version.release)"
echo "Kernel  : $(uname -r)"
echo "Time    : $(date '+%H:%M:%S')"
echo -e "${NC}"
}

#================ CUSTOM BANNER =========#
set_banner() {
read -p "Enter Your Name: " name

cat > ~/.bashrc << EOF
clear
echo -e "\033[1;31m"
figlet -f slant "$name" | lolcat

echo -e "\033[1;36m"
echo "===================================="
echo "        WELCOME BACK USER"
echo "===================================="

echo -e "\033[1;32m"
echo "User : $name"
echo "Mode : PREMIUM ACTIVE"
echo "===================================="
EOF

echo -e "${GREEN}[✓] CUSTOM HIGH-QUALITY BANNER SET"
sleep 2
}

#================ MENU ================#
while true
do
banner
sysinfo

echo ""
echo -e "${YELLOW}[1] Full Setup"
echo -e "${YELLOW}[2] Install Basic Tools"
echo -e "${YELLOW}[3] Set Custom Banner"
echo -e "${YELLOW}[4] System Info"
echo -e "${YELLOW}[5] Update Tool"
echo -e "${RED}[0] Exit"
echo ""

read -p "➤ Choose Option: " opt

case $opt in

1)
loading
pkg update -y && pkg upgrade -y
pkg install python git wget curl figlet toilet ruby neofetch -y
gem install lolcat
echo -e "${GREEN}[✓] FULL SETUP COMPLETE"
sleep 2
;;

2)
loading
pkg install python git wget curl -y
echo -e "${GREEN}[✓] BASIC TOOLS INSTALLED"
sleep 2
;;

3)
set_banner
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
