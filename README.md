<h1 align="center">
  <img src="https://github.com/nileshkinge/Raspi_DashCam/blob/main/code/web/public/img/logos/logo-256.png" width="224px"/><br/>
  Raspberry Pi Dashcam
</h1>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Hardware](#hardware)
* [Software](#software)
* [Setup](#setup)

## General info
A Daschcam built using Raspberry-pi zero W.
	
## Technologies
Project is created with:
* [Python](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/en/)

## Hardware
* [Raspberry pi zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
* [Rasperry pi camera](https://www.raspberrypi.com/products/camera-module-v2/)
* [Power Supply](https://www.raspberrypi.com/products/micro-usb-power-supply/)
* [pi zero case](https://www.aliexpress.com/item/32861638369.html)
* Memory card, using 32 gb micro SD card.

## Software
* [Raspberry Pi Imager](https://www.raspberrypi.com/software/) or [balenaEtcher](https://www.balena.io/etcher/)
* [Putty](https://www.ssh.com/academy/ssh/putty/windows/install)
	
## Setup
1)  Install latest [Raspberry Pi OS](https://www.raspberrypi.com/software/).
2)  Add ssh and wpa_supplicant file. This will allow us to access [Pi headless](https://pimylifeup.com/headless-raspberry-pi-setup/).
3)  Login to Pi using [Putty](https://www.ssh.com/academy/ssh/putty/windows/install). Default login credentioals - login:pi password:raspberry.
3)  Confirm if Git is installed
    ```
    git --version
    ```
    Git comes pre installed in Raspberry Pi OS. If git is not installed, [install git](https://projects.raspberrypi.org/en/projects/getting-started-with-git/3) before moving on to next step.
5)  Change directotry to home/pi, you might already be in this directory. 
    ```
    cd /home/pi/
    ```
6)  Download dashcam repository from Github.
    ```
    git clone https://github.com/nileshkinge/Raspi_DashCam
    ```
7)  Change to below directory in the downloaded repository.
    ```
    cd /Raspi_DashCam/code/
    ```
8) sudo chmod +x setup.sh
9) sudo bash setup.sh
10) sudo chmod -x apSetup.sh
11) sudo bash apSetup.sh ["your password"]
12) install node if not already installed
    curl -o node-v9.7.1-linux-armv6l.tar.gz https://nodejs.org/dist/v9.7.1/node-v9.7.1-linux-armv6l.tar.gz
    tar -xzf node-v9.7.1-linux-armv6l.tar.gz
    sudo cp -r node-v9.7.1-linux-armv6l/* /usr/local/

    kill -15 $(lsof -t -i:3000)

13) cd web/
14) npm install   
15) sudo reboot

To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## ⚡️ Quick start
#clone git repo
git clone https://github.com/nileshkinge/Raspi_DashCam

cd /home/pi/Raspi_DashCam/code/

sudo chmod +x setup.sh

sh setup.sh

sudo reboot

install raspberry pi imager or balena ethcher
    1) install latest os.
    2) add ssh and wpa_supplicant file
    3) git --version
    5) cd /home/pi/
    6) git clone https://github.com/nileshkinge/Raspi_DashCam
    7) cd /Raspi_DashCam/code/
    8) sudo chmod +x setup.sh
    9) sudo bash setup.sh
   10) sudo chmod -x apSetup.sh
   11) sudo bash apSetup.sh ["your password"]
   12) install node if not already installed
        curl -o node-v9.7.1-linux-armv6l.tar.gz https://nodejs.org/dist/v9.7.1/node-v9.7.1-linux-armv6l.tar.gz
        tar -xzf node-v9.7.1-linux-armv6l.tar.gz
        sudo cp -r node-v9.7.1-linux-armv6l/* /usr/local/

        kill -15 $(lsof -t -i:3000)

   13) cd web/
   14) npm install   
   15) sudo reboot
