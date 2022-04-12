#!/bin/bash

echo -e "\n$(date"+%d-%m-%Y --- %T") --- Starting work\n"

chmod +x  firsttimesetup.sh

#update the software currently on the system
apt-get -y update
apt-get -y upgrade
echo "Upgraded packages\n"
pip install -upgrade pip
apt-get -y autoremove
apt-get autoclean -y
apt-get dist-upgrade -y
do-release-upgrade

#install custom images that I prefer
echo "\n\n\n\n\nInstalling IfConfig"
echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y net-tools

echo "\n\n\n\n\nInstalling Wireshark"
echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y wireshark

echo "\n\n\n\n\nInstalling htop"

echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y htop

echo "\n\n\n\n\nInstalling Nmap"
echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y nmap

echo "\n\n\n\n\nInstalling Putty"

echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y putty

echo "\n\n\n\n\nInstalling a SSH server"

echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install openssh-server -y
systemctl stop ssh
systemctl disable ssh
#ufw allow/disable ssh
#note if you want to enable/disable ssh you need to use the command
# to allow the ssh instance through the firewall

echo "Disabled the SSH Server\n\n\n\n\n"

echo "-------------------------------------"
echo "-------------------------------------\n"

echo "\n\n\n\n\nInstalling a TFTP server"

echo "-------------------------------------"
echo "-------------------------------------\n"
apt-get install -y tftpd-hpa

systemctl stop tftpd-hpa
systemctl disable tftpd-hpa

echo "Disabled a TFTP Server\n\n\n\n\n"
echo "-------------------------------------"
echo "-------------------------------------\n"


echo "Installing pip\n\n\n\n\n"
echo "-------------------------------------"
echo "-------------------------------------\n"
apt install python3-pip -y
pip install -upgrade pip

#this creates a shell file to use with USB roll over cables
echo "Creating a Putty USB shell file to run USB Roll Over Cables"
echo "-------------------------------------"
echo "-------------------------------------\n"
mkdir ~/bin
echo "#!/bin/bash" > puttyusb.sh
echo "sudo putty /dev/ttyUSB0 -serial -sercfg 9600,8,n,1,N" >> puttyusb.sh 
chmod +x  puttyusb.sh

#ending cleanup that tidies everything up
apt-get update
apt-get -y upgrade
pip install -upgrade pip
apt-get -y autoremove
apt-get autoclean

echo -e "\n$(date "+%T") \t Script Terminated"