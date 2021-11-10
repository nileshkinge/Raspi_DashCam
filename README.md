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
* [To Do](#to-do)

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
* [Memory card](https://www.amazon.com/Micro-Center-Class-Memory-Adapter/dp/B07K81Z6DF/)

## Software
* [Raspberry Pi Imager](https://www.raspberrypi.com/software/) or [balenaEtcher](https://www.balena.io/etcher/)
* [Putty](https://www.ssh.com/academy/ssh/putty/windows/install)
	
## Setup
1)  Install latest [Raspberry Pi OS](https://www.raspberrypi.com/software/).
2)  Add ssh and wpa_supplicant file. This will allow us to access [Pi headless](https://pimylifeup.com/headless-raspberry-pi-setup/).
3)  Login to Pi using [Putty](https://www.ssh.com/academy/ssh/putty/windows/install). Default login credentioals - login:pi password:raspberry.
4)  Confirm if Git is installed
    ```
    git --version
    ```
    Git comes pre installed in Raspberry Pi OS. If git is not installed, [install git](https://projects.raspberrypi.org/en/projects/getting-started-with-git/3) before moving on to next step.
5)  Download dashcam repository from Github.
    ```
    cd /home/pi/
    git clone https://github.com/nileshkinge/Raspi_DashCam
    cd /Raspi_DashCam/code/
    ```
6)  Run setup.sh file.
    ```
    sudo chmod +x setup.sh
    sudo bash setup.sh
    ```
    This will install the neccessary packages, web app, also create a access point named dashcam adn password dashcam.
7) Restart
    ```
    sudo reboot
    ```
## TO DO
* add instruction for interactions/inputs on setup.sh run.
