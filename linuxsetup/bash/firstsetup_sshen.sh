#!/bin/bash

echo -e -e "\n$(date"+%d-%m-%Y --- %T") --- Starting work\n"
#chmod +x  firstsetup_sshen.sh
#update the software currently on the system
apt-get update
apt-get -y upgrade
echo -e "Upgraded packages\n"
pip install -upgrade pip
apt-get -y autoremove
apt-get autoclean -y
#apt-get dist-upgrade -y
#do-release-upgrade
#install custom images that I prefer
echo -e "\n\n\n\n\nInstalling IfConfig"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y net-tools
echo -e "\n\n\n\n\nInstalling Wireshark"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y wireshark
echo -e "\n\n\n\n\nInstalling htop"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y htop
echo -e "\n\n\n\n\nInstalling Nmap"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y nmap
echo -e "\n\n\n\n\nInstalling Putty"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y putty
echo -e "\n\n\n\n\nInstalling a SSH server"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install openssh-server -y
#systemctl stop ssh
#systemctl disable ssh
ufw allow ssh
#note if you want to enable/disable ssh you need to use the command
# to allow the ssh instance through the firewall
#echo -e "Disabled the SSH Server\n\n\n\n\n"
#echo -e "-------------------------------------"
#echo -e "-------------------------------------\n"
echo -e "\n\n\n\n\nInstalling a TFTP server"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt-get install -y tftpd-hpa
systemctl stop tftpd-hpa
systemctl disable tftpd-hpa
echo -e "Disabled a TFTP Server\n\n\n\n\n"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
echo -e "Installing pip\n\n\n\n\n"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
apt install python3-pip -y
pip install -upgrade pip
#this creates a shell file to use with USB roll over cables
echo -e "Creating a Putty USB shell file to run USB Roll Over Cables"
echo -e "-------------------------------------"
echo -e "-------------------------------------\n"
mkdir ~/bin
echo -e "#!/bin/bash" > puttyusb.sh
echo -e "sudo putty /dev/ttyUSB0 -serial -sercfg 9600,8,n,1,N" >> puttyusb.sh
chmod +x  puttyusb.sh
#ending cleanup that tidies everything up
apt-get update
apt-get -y upgrade
pip install -upgrade pip
apt-get -y autoremove
apt-get autoclean
echo -e -e "\n$(date "+%T") \t Script Terminated"