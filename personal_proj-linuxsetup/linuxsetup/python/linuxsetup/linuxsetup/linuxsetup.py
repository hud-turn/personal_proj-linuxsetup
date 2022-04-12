import os, subprocess

#Updating the OS
os.system('sudo apt-get update -y')
os.system('sudo apt-get upgrade -y')
os.system('sudo apt-get dist-upgrade -y')
os.system('sudo apt-get autoremove -y')
os.system('sudo apt-get autoclean -y')

#Installing Utilities and Features

#Installing Brave
os.system('sudo apt install apt-transport-https curl')
os.system('sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg')
os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
os.system('sudo apt update')
os.system('sudo apt install -y brave-browser')

#Installing Network Tools
os.system('sudo apt-get install -y net-tools')

#Installing Wireshark
os.system('sudo apt-get install -y wireshark')

#Installing Htop
os.system('sudo apt-get install -y htop')

#Installing Putty
os.system('sudo apt-get install -y putty')

#Installing Open SSH Server
os.system('sudo apt-get install -y openssh-server')
os.system('sudo ufw allow ssh')

#Installing TFTP Server
os.system('sudo apt-get install -y tftpd-hpa')
os.system('sudo systemctl staus tftpd-hpa')
os.system('sudo systemctl stop tftpd-hpa')
os.system('sudo systemctl disable tftpd-hpa')

#Installing RPI Imaging Software
os.system('snap install rpi-imager')

#Installing Git
os.system('sudo apt-get install -y git')

#Installing Nmap
os.system('sudo apt-get install -y nmap')

#Installing Gnome Tweaks
os.system('sudo apt-get install -y gnome-tweaks')
          
#Creating a Putty Bash file for USB Rollover Cables
os.system('mkdir ~/bin')
os.system("echo '#!/bin/bash' > ~/bin/puttyusb.sh")
os.system('echo "sudo putty /dev/ttyUSB0 -serial -sercfg 9600,8,n,1,N" >> ~/bin/puttyusb.sh')
os.system('chmod +x puttyusb.sh')
os.system('cd ~')
input('Install should be complete')

#cf-19 additions

#os.system('sudo apt-get update')
#os.system('mv ./analog-output-speaker.conf /usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf')
#os.system('sudo apt install -y inotify-tools')
#os.system('sudo cp ./redirect-brightness.sh /usr/local/bin/')
#os.system('sudo chmod +x /usr/local/bin/redirect-brightness.sh')
#os.system("clear")
#print ("This Command will need to be inserted into the crontab")
#print("Please do not press [ENTER] until you have copied the following text")
#input ("@reboot sudo /usr/local/bin/redirect-brightness.sh -l")
#os.system("clear")
#input('Now you will need to take this text and insert it in the bottom of the next page')
#os.system('sudo crontab -e')
#os.system('1')

#@reboot sudo redirect-brightness.sh -l
#This command needs to go in the crontab

          
#These Lines are meant for the Raspberry Pi Distro of Linux
#os.system('sudo apt-get-repository -p proposed')
#os.system('sudo apt install linux-raspi')
#os.system('sudo apt-get-repository -r -p proposed')
#os.system('sudo reboot')

os.system('sudo apt autoremove')
