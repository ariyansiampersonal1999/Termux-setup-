#!/bin/bash

#================ COLORS ================#
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
PURPLE='\033[1;35m'
NC='\033[0m'

#================ DEP CHECK =============#
for p in figlet toilet lolcat neofetch git
do
command -v $p >/dev/null 2>&1 || pkg install $p -y
done

#================ LOADING ===============#
loading() {
echo -e "${CYAN}Booting Dark System..."
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

echo -e "${GREEN}"
figlet -f slant "Termux Setup" | lolcat

echo -e "${CYAN}"
echo "╔══════════════════════════════════════╗"
echo "║       ⚡ DARK ELITE SYSTEM ⚡        ║"
echo "║        TERMUX CONTROL PANEL          ║"
echo "╚══════════════════════════════════════╝"

echo -e "${GREEN}"
echo "➤ STATUS : ONLINE"
echo "➤ MODE   : DARK PREMIUM"
echo "➤ POWER  : MAXIMUM"
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

echo -e "\033[1;30m"
clear

echo -e "\033[1;32m"
figlet -f slant "$name" | lolcat

echo -e "\033[1;36m"
echo "╔══════════════════════════════════╗"
echo "║        DARK ELITE MODE           ║"
echo "║     PREMIUM TERMINAL ACTIVE      ║"
echo "╚══════════════════════════════════╝"

echo -e "\033[1;32m"
echo "USER   : $name"
echo "STATUS : ONLINE"
echo "MODE   : DARK ELITE"
echo "POWER  : MAXIMUM"
echo ""
EOF

echo -e "${GREEN}[✓] CUSTOM DARK BANNER SET SUCCESS"
sleep 2
}

#================ DEVELOPER INFO ========#
dev_info() {
clear

echo -e "${RED}"
figlet -f slant "Developer" | lolcat

echo -e "${CYAN}"
echo "╔══════════════════════════════════════╗"
echo "║          👨‍💻 DEVELOPER INFO          ║"
echo "╚══════════════════════════════════════╝"

echo -e "${GREEN}"
echo "Name     : ARIYAN"
echo "Tool     : Termux Setup Tool"
echo "Version  : 6.0 DARK PREMIUM"
echo "Platform : Termux (Android)"
echo "Type     : Automation Tool"

echo ""
echo -e "${YELLOW}FEATURES:"
echo "- Auto Setup"
echo "- Dark UI System"
echo "- Custom Banner"
echo "- System Info Dashboard"
echo "- Fast Installer"

echo ""
echo -e "${CYAN}⚠️ EDUCATIONAL USE ONLY"
echo -e "${NC}"

read -p "Press Enter..."
}

#================ MENU ================#
while true
do
banner
sysinfo

echo ""
echo -e "${YELLOW}[1] Full Setup"
echo -e "${YELLOW}[2] Install Basic Tools"
echo -e "${YELLOW}[3] Set Custom Banner (Dark Premium)"
echo -e "${YELLOW}[4] System Info"
echo -e "${YELLOW}[5] Update Tool"
echo -e "${YELLOW}[6] Developer Info"
echo -e "${RED}[0] Exit"
echo ""

read -p "➤ Choose Option: " opt

case $opt in

1)
loading
pkg update -y && pkg upgrade -y
pkg install python git wget curl figlet toilet ruby neofetch -y
gem install lolcat
echo -e "${GREEN}[✓] FULL DARK SETUP COMPLETE"
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

6)
dev_info
;;

0)
echo -e "${RED}GOOD BYE DARK USER!"
exit
;;

*)
echo -e "${RED}INVALID OPTION"
sleep 1
;;

esac
done
