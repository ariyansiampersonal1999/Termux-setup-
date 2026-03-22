#!/bin/bash

#================= COLOR =================#
red='\033[1;31m'
green='\033[1;32m'
cyan='\033[1;36m'
yellow='\033[1;33m'
white='\033[1;37m'

#================= START =================#
while true
do
clear

# Main Banner
toilet -f slant "ARIYAN TOOL" | lolcat

# RED BANNER
echo -e "${red}"
figlet "SETUP TOOLS"
echo -e "${white}"

echo -e "${cyan}=================================="
echo -e "${green} Developer : ARIYAN"
echo -e "${yellow} Version   : 3.0"
echo -e "${cyan}=================================="

echo ""
echo -e "${green}[1] Full Termux Setup"
echo -e "${green}[2] Install Basic Packages"
echo -e "${green}[3] Set Custom Banner"
echo -e "${green}[4] Show System Info"
echo -e "${green}[5] Update Tool"
echo -e "${green}[0] Exit"
echo ""

read -p "Choose Option: " opt

#================= OPTION 1 =================#
if [ "$opt" == "1" ]
then
    clear
    echo -e "${yellow}[+] Updating System..."
    pkg update -y && pkg upgrade -y

    echo -e "${yellow}[+] Installing Packages..."
    pkg install python git wget curl figlet toilet ruby neofetch -y
    gem install lolcat

    echo -e "${green}[✓] Full Setup Completed!"
    sleep 2

#================= OPTION 2 =================#
elif [ "$opt" == "2" ]
then
    clear
    pkg install python git wget curl -y
    echo -e "${green}[✓] Basic Packages Installed!"
    sleep 2

#================= OPTION 3 =================#
elif [ "$opt" == "3" ]
then
    clear
    echo -e "${yellow}Set Your Custom Banner"

    read -p "Enter Your Name: " name

cat > ~/.bashrc << EOF
clear
toilet -f slant "$name" | lolcat
echo "Welcome $name"
EOF

    echo -e "${green}[✓] Banner Set Successfully for $name!"
    sleep 2

#================= OPTION 4 =================#
elif [ "$opt" == "4" ]
then
    clear
    neofetch
    read -p "Press Enter to continue..."

#================= OPTION 5 =================#
elif [ "$opt" == "5" ]
then
    clear
    echo -e "${yellow}Updating Tool..."
    git pull
    echo -e "${green}[✓] Tool Updated!"
    sleep 2

#================= EXIT =================#
elif [ "$opt" == "0" ]
then
    echo -e "${red}Goodbye Boss 😎"
    exit

#================= INVALID =================#
else
    echo -e "${red}Invalid Option!"
    sleep 1
fi

done
