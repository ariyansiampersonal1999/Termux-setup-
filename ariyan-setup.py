#!/data/data/com.termux/files/usr/bin/bash

#================ COLORS =================#
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
PURPLE='\033[1;35m'
NC='\033[0m'

#================ DEPENDENCY CHECK =================#
check_deps() {

pkgs="figlet toilet ruby git wget curl neofetch"

for pkg in $pkgs
do
command -v $pkg >/dev/null 2>&1 || pkg install -y $pkg
done

command -v lolcat >/dev/null 2>&1 || gem install lolcat

}

#================ LOADING =================#
loading() {

clear

echo -e "${CYAN}Initializing System...${NC}"

for i in {1..100}
do
printf "\r${GREEN}["
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
sleep 1
}

#================ BANNER =================#
banner() {

clear

figlet -f slant "TERMUX" | lolcat
figlet -f slant "SETUP TOOL" | lolcat

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════╗"
echo "║          TERMUX SETUP TOOL PRO              ║"
echo "║          CUSTOM BANNER EDITION              ║"
echo "╚══════════════════════════════════════════════╝"
echo -e "${NC}"

}

#================ SYSTEM INFO =================#
system_info() {

clear

echo -e "${GREEN}"
echo "User      : $(whoami)"
echo "Device    : $(getprop ro.product.model 2>/dev/null)"
echo "Android   : $(getprop ro.build.version.release 2>/dev/null)"
echo "Kernel    : $(uname -r)"
echo "Time      : $(date)"
echo -e "${NC}"

echo ""
neofetch

read -p "Press Enter..."
}

#================ FULL SETUP =================#
full_setup() {

loading

pkg update -y
pkg upgrade -y

pkg install -y \
python \
python-pip \
git \
curl \
wget \
nano \
vim \
figlet \
toilet \
ruby \
neofetch

gem install lolcat

echo ""
echo -e "${GREEN}[✓] Full Setup Completed${NC}"

sleep 2
}

#================ BASIC TOOLS =================#
basic_tools() {

loading

pkg install -y \
python \
git \
curl \
wget \
nano

echo ""
echo -e "${GREEN}[✓] Basic Tools Installed${NC}"

sleep 2
}

#================ CUSTOM BANNER =================#
custom_banner() {

clear

figlet -f slant "CUSTOM" | lolcat
figlet -f slant "BANNER" | lolcat

echo ""

read -p "Enter Your Name : " uname

cat > ~/.bashrc << EOF

clear

echo -e "\033[1;32m"

figlet -f slant "$uname" | lolcat

echo -e "\033[1;36m"
echo "╔════════════════════════════════════════════╗"
echo "║           CYBER TERMUX SYSTEM             ║"
echo "╠════════════════════════════════════════════╣"
echo "║ USER      : $uname"
echo "║ STATUS    : ONLINE"
echo "║ SECURITY  : ACTIVE"
echo "║ MODE      : PREMIUM"
echo "╚════════════════════════════════════════════╝"

echo ""

neofetch

echo ""
echo " Welcome Back $uname"
echo ""

EOF

echo ""
echo -e "${GREEN}[✓] Banner Installed Successfully${NC}"

sleep 2
}

#================ REMOVE BANNER =================#
remove_banner() {

echo "" > ~/.bashrc

echo -e "${GREEN}[✓] Banner Removed${NC}"

sleep 2
}

#================ UPDATE TOOL =================#
update_tool() {

loading

git pull

echo -e "${GREEN}[✓] Tool Updated${NC}"

sleep 2
}

#================ DEVELOPER =================#
developer_info() {

clear

figlet -f slant "DEVELOPER" | lolcat

echo ""
echo -e "${CYAN}══════════════════════════════════════"
echo "Name      : Your Name"
echo "Tool      : Termux Setup Tool Pro"
echo "Version   : 1.0"
echo "Platform  : Termux"
echo "══════════════════════════════════════${NC}"

echo ""

read -p "Press Enter..."
}

#================ START =================#
check_deps

while true
do

banner

echo ""
echo -e "${YELLOW}[1] Full Termux Setup"
echo -e "${YELLOW}[2] Install Basic Tools"
echo -e "${YELLOW}[3] Create Custom Banner"
echo -e "${YELLOW}[4] Remove Banner"
echo -e "${YELLOW}[5] System Information"
echo -e "${YELLOW}[6] Update Tool"
echo -e "${YELLOW}[7] Developer Info"
echo -e "${RED}[0] Exit"
echo ""

read -p "Choose Option : " opt

case $opt in

1)
full_setup
;;

2)
basic_tools
;;

3)
custom_banner
;;

4)
remove_banner
;;

5)
system_info
;;

6)
update_tool
;;

7)
developer_info
;;

0)
clear
figlet -f slant "GOOD BYE" | lolcat
exit
;;

*)
echo -e "${RED}Invalid Option${NC}"
sleep 1
;;

esac

done
