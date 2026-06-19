#!/data/data/com.termux/files/usr/bin/bash

#================ COLORS =================#
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
PURPLE='\033[1;35m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
NC='\033[0m'

#================ INSTALL CHECK =================#
install_deps() {

pkgs="figlet toilet ruby git wget curl neofetch cmatrix tty-clock btop"

for p in $pkgs
do
command -v $p >/dev/null 2>&1 || pkg install $p -y
done

command -v lolcat >/dev/null 2>&1 || gem install lolcat
}

#================ BOOT =================#
boot_animation() {

clear

msgs=(
"Loading Neural Engine"
"Initializing Quantum Core"
"Loading System Kernel"
"Scanning Security Layer"
"Activating Dashboard"
"Connecting Terminal"
"Cyber System Ready"
)

for msg in "${msgs[@]}"
do
printf "${GREEN}➜ %s ${NC}" "$msg"

for i in {1..15}
do
printf "■"
sleep 0.03
done

echo " [OK]"
sleep 0.15
done

sleep 1
}

#================ LOADING =================#
loading() {

echo ""

for i in {1..100}
do

printf "\r${CYAN}["

for ((j=0;j<i/2;j++))
do
printf "█"
done

for ((j=i/2;j<50;j++))
do
printf " "
done

printf "] %d%%${NC}" "$i"

sleep 0.01
done

echo ""
}

#================ BANNER =================#
banner() {

clear

figlet -f Bloody "CYBER" | lolcat -a -d 2
figlet -f Bloody "TERMINAL" | lolcat -a -d 2

echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════╗"
echo "║             CYBER TERMINAL PRO V10               ║"
echo "╠════════════════════════════════════════════════════╣"
echo "║ STATUS    : ONLINE                               ║"
echo "║ SECURITY  : ACTIVE                               ║"
echo "║ MODE      : PREMIUM                              ║"
echo "║ POWER     : MAXIMUM                              ║"
echo "╚════════════════════════════════════════════════════╝"
echo -e "${NC}"
}

#================ SYSTEM INFO =================#
sysinfo() {

echo -e "${GREEN}"
echo " USER      : $(whoami)"
echo " DEVICE    : $(getprop ro.product.model 2>/dev/null)"
echo " ANDROID   : $(getprop ro.build.version.release 2>/dev/null)"
echo " KERNEL    : $(uname -r)"
echo " TIME      : $(date '+%H:%M:%S')"
echo -e "${NC}"
}

#================ MATRIX =================#
matrix_mode() {
clear
cmatrix -ab
}

#================ CLOCK =================#
clock_mode() {
clear
tty-clock -cs -C 6
}

#================ SYSTEM MONITOR =================#
monitor_mode() {
clear
btop
}

#================ DASHBOARD =================#
dashboard() {

clear

echo -e "${CYAN}"
echo "╔══════════════════════════════════════╗"
echo "║      CYBER CONTROL DASHBOARD         ║"
echo "╚══════════════════════════════════════╝"
echo ""

echo " USER     : $(whoami)"
echo " DEVICE   : $(getprop ro.product.model 2>/dev/null)"
echo " ANDROID  : $(getprop ro.build.version.release 2>/dev/null)"
echo " KERNEL   : $(uname -r)"
echo " DATE     : $(date)"
echo ""

neofetch

echo ""
read -p "Press Enter..."
}

#================ CUSTOM BANNER =================#
custom_banner() {

clear

read -p "Enter Your Name: " name

cat > ~/.bashrc << EOF
clear

figlet -f Bloody "$name" | lolcat -a -d 2

echo "╔══════════════════════════════════════╗"
echo "║      CYBER TERMINAL PRO              ║"
echo "║      STATUS : ONLINE                 ║"
echo "║      MODE   : PREMIUM                ║"
echo "╚══════════════════════════════════════╝"

echo ""
neofetch
EOF

echo ""
echo "[✓] Custom Banner Installed"
sleep 2
}

#================ DEVELOPER =================#
developer() {

clear

figlet -f slant "Developer" | lolcat

echo ""
echo "══════════════════════════════════════"
echo " Name     : Custom User"
echo " Version  : CYBER TERMINAL PRO V10"
echo " Type     : Dashboard Edition"
echo "══════════════════════════════════════"
echo ""

read -p "Press Enter..."
}

#================ START =================#

install_deps
boot_animation

while true
do

banner
sysinfo

echo ""
echo -e "${YELLOW}[1] Full Setup"
echo -e "${YELLOW}[2] Dashboard"
echo -e "${YELLOW}[3] Matrix Mode"
echo -e "${YELLOW}[4] Digital Clock"
echo -e "${YELLOW}[5] System Monitor"
echo -e "${YELLOW}[6] Custom Banner"
echo -e "${YELLOW}[7] Developer Info"
echo -e "${RED}[0] Exit"
echo ""

read -p "Choose Option : " opt

case $opt in

1)
loading
pkg update -y
pkg upgrade -y
echo ""
echo "[✓] Setup Complete"
sleep 2
;;

2)
dashboard
;;

3)
matrix_mode
;;

4)
clock_mode
;;

5)
monitor_mode
;;

6)
custom_banner
;;

7)
developer
;;

0)
clear
figlet -f slant "GOODBYE" | lolcat
exit
;;

*)
echo "Invalid Option"
sleep 1
;;

esac

done
