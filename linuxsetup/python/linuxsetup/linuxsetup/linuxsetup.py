import os, subprocess, time

#Updating the OS
os.system('clear')
os.system('sudo apt-get update -y')
os.system('sudo apt-get upgrade -y')
os.system('sudo apt-get dist-upgrade -y')
os.system('sudo apt-get autoremove -y')
os.system('sudo apt-get autoclean -y')

#Installing Utilities and Features

#Installing Brave
os.system('sudo apt install apt-transport-https curl')
os.system('sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg')
os.system('sudo echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
os.system('sudo apt update')
os.system('sudo apt install -y brave-browser')

#Installing CUPS (Print Utility)
os.system('sudo apt-get install -y cups')
os.system('sudo service cups start')

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
os.system('clear')

#Installing IDLE Python IDE
os.system('sudo apt install -y idle')
os.system("clear")

#cf-19 additions
cfsystemlow = input(print("Are you on a CF laptop?"))
cfsystem = cfsystemlow.lower()

if "y" in cfsystem:
          os.system('sudo apt-get update')
          os.system('sudo mv ./analog-output-speaker.conf /usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf')
          os.system('sudo apt install -y inotify-tools')
          os.system('sudo cp ./redirect-brightness.sh /usr/local/bin/')
          os.system('sudo chmod +x /usr/local/bin/redirect-brightness.sh')
          os.system("clear")
          print ("This Command will need to be inserted into the crontab")
          print("Please do not press [ENTER] until you have copied the following text")
          input ("@reboot sudo /usr/local/bin/redirect-brightness.sh -l")
          os.system("clear")
          input('Now you will need to take this text and insert it in the bottom of the next page')
          os.system('sudo crontab -e')
          os.system('clear')
          
          #@reboot sudo redirect-brightness.sh -l
          #This command needs to go in the crontab

          
#These Lines are meant for the Raspberry Pi Distro of Linux
rpisystemlow = input(print("Are you on a Raspberry Pi System?"))
rpisystem = rpisystemlow.lower()

if "y" in rpisystem:
          os.system('sudo apt-get-repository -p proposed')
          os.system('sudo apt install linux-raspi -y')
          os.system('sudo apt-get-repository -r -p proposed')
          input('You will likely want to reboot after applying these updates')
          os.system('clear')

#Cleaning up after the installs
print('Install should be complete, the next step will clean the computer of unnecessary repos')
time.sleep(5)   
os.system('sudo apt autoremove -y')
os.system('clear')

rebootsystemlow = input(print("Do you want to reboot your machine?"))
rebootsystem = rebootsystemlow.lower()

if "y" in rebootsystem:
          input("The computer will reboot once you hit [ENTER], please make sure you save any work before hitting enter.")
          os.system('sudo reboot')
quit()
