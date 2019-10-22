#!/bin/bash

reboot_required=no
connect_usbsound=no

# Back up config files
cp /boot/config.txt /boot/config.txt$(date +%Y%m%d)
cp /usr/share/alsa/alsa.conf /usr/share/alsa/alsa.conf$(date +%Y%m%d)

# SPI checks
if [ "`raspi-config nonint get_spi`" -eq "0" ]; then
    echo -e "\e[92mSPI seems enabled (reported by raspi-config).\e[39m";
else
    echo -e "\e[91mSPI seems disabled (reported by raspi-config). Enabling now.\e[39m";
    raspi-config nonint do_spi 0
    reboot_required=yes
fi

if [ "`cat /boot/config.txt |grep ^dtparam=spi=on$| wc -l`" -eq "1" ]; then
	echo -e "\e[92mSPI seems enabled (/boot/config.txt)\e[39m";
else
	echo -e "\e[91mSPI seems disabled in /boot/config.txt. Enabling it\e[39m";
	sed -i -e "s/dtparam=spi=off/dtparam=spi=on/g" /boot/config.txt
    reboot_required=yes
fi

if [ "`lsmod | grep spi_bcm2835 | wc -l`" -eq "1" ]; then
	echo -e "\e[92mSPI is already active\e[39m";
else
	echo -e "\e[91mSPI does not seem active yet. If you just enabled it, a reboot is required.\e[39m";
	reboot_required=yes
fi

if [[ -e /dev/spidev0.0 ]]; then
	echo -e "\e[92mSPI kernel device found.\e[39m";
else
	echo -e "\e[91mNo SPI kernel device found.\e[39m";
	reboot_required=yes
fi

# Audio checks
if [ "`cat /boot/config.txt | grep ^dtparam=audio=off$ | wc -l`" -eq "1" ]; then
	echo -e "\e[92mInternal sound card is deactivated.\e[39m";
else
	echo -e "\e[91mInternal sound card still active.\e[39m";
	echo -e "\e[96mDisabling it in /boot/config.txt.\e[39m";
	sed -i -e "s/dtparam=audio=on/dtparam=audio=off/g" /boot/config.txt
    reboot_required=yes
fi

if [ "`cat /proc/asound/modules | wc -l`" -gt "1" ]; then
	echo -e "\e[91mToo many sound cards found. Disable internal sound card in /boot/config.txt. If you just disabled it, please reboot.\e[39m"
	reboot_required=yes
fi

if [ "`cat /proc/asound/modules | grep usb | wc -l`" -eq "1" ]; then
    echo -e "\e[92mUSB soundcard found.\e[39m";
else
	echo -e "\e[91mUSB soundcard not found in /proc/asound/modules. Please connect the USB sound card.\e[39m";
	connect_usbsound=yes
fi

if [ "`cat /proc/asound/cards | grep USB | wc -l`" -gt "1" ]; then
	echo -e "\e[92mUSB soundcard found.\e[39m";
else
	echo -e "\e[91mUSB soundcard not found.\e[39m";
	connect_usbsound=yes
fi


if [ "`cat /usr/share/alsa/alsa.conf | grep 'defaults.ctl.card 1' | wc -l`" -eq "1" ]; then
	echo -e "\e[92mDefault CTL sound card is 1.\e[39m";
else
	echo -e "\e[91mDefault CTL sound card is still 0 in /usr/share/alsa/alsa/alsa.conf.\e[39m";
	echo -e "\e[96mSetting CTL sound card to 1"\e[39m;
	sed -i -e "s/defaults.ctl.card 0/defaults.ctl.card 1/g" /usr/share/alsa/alsa.conf
fi

if [ "`cat /usr/share/alsa/alsa.conf | grep 'defaults.pcm.card 1' | wc -l`" -eq "1" ]; then
    echo -e "\e[92mDefault PCM sound card is 1.\e[39m";
else
    echo -e "\e[91mDefault PCM sound card is still 0 in /usr/share/alsa/alsa.conf\e[39m";
    echo -e "\e[96mSetting PCM sound card to 1\e[39m";
    sed -i -e "s/defaults.pcm.card 0/defaults.pcm.card 1/g" /usr/share/alsa/alsa.conf
fi


package_check() {
	if [ "`dpkg -s $1 | grep Status | grep installed | wc -l`" -eq "1" ]; then
		echo -e "\e[92m$1 is installed\e[39m";
	else
		echo -e "\e[91mPackage $1 is not installed.\e[39m";
		echo -e "\e[96mInstalling now...\e[39m";
		apt install -y $1
	fi
}

# Pillow dependencies
package_check libjpeg-dev
package_check zlib1g-dev

# Pygame dependencies
package_check python-dev
package_check libsdl-image1.2-dev
package_check libsdl-mixer1.2-dev
package_check libsdl-ttf2.0-dev
package_check libsdl1.2-dev
package_check libsmpeg-dev
package_check python-numpy
package_check subversion
package_check libportmidi-dev
package_check ffmpeg
package_check libswscale-dev
package_check libavformat-dev
package_check libavcodec-dev
package_check python3-pip

# Redis Server
package_check redis-server

if [ "`which pip3 | wc -l`" -eq "1" ]; then
        echo -e "\e[92mFound pip3\e[39m";
else
        echo -e "\e[91mpip3 not found\e[39m";
        exit 11
fi

python_check() {
	if [ "`pip3 list --disable-pip-version-check 2>/dev/null | grep $1 | wc -l`" -gt "0" ]; then
		echo -e "\e[92mFound python package $1\e[39m";
	else
		echo -e "\e[91mPython package $1 not found. Installing ...\e[39m";
		pip3 install $1
	fi
}

python_check pygame
python_check numpy
python_check Pillow
python_check luma.led-matrix
python_check luma
python_check luma.core
python_check aioredis
python_check setuptools
python_check aiohttp
python_check jinja2
python_check aiohttp-jinja2
python_check python-socketio
python_check redis

python_import() {
	if python3 -c "import $1" &> /dev/null; then
		echo -e "\e[92mPython import $1 successful\e[39m";
	else
		echo -e "\e[91mPython import $1 failed\e[39m";
		exit 13
	fi
}

python_import PIL
python_import pygame
python_import aiohttp
python_import random
python_import pickle
python_import datetime
python_import threading
python_import signal
python_import time
python_import luma.core
python_import luma.core.virtual
python_import luma.core.render
python_import luma.led_matrix.device
python_import luma.core.legacy.font
python_import luma.core.interface.serial
python_import colorsys
python_import os
python_import jinja2
python_import aiohttp_jinja2
python_import socketio

if [ "$reboot_required" = "yes" ]; then
    echo -e "\e[96mA reboot seems required\e[39m";
    echo -e "\e[91mPlease save open documents and reboot\e[39m"
fi

if [ "$connect_usbsound" = "yes" ]; then
    echo -e "\e[91mThe USB sound card seems not connected. Please connect.\e[39m";
fi

echo "FontAwesome download..."
wget http://use.fontawesome.com/releases/v5.8.1/fontawesome-free-5.8.1-web.zip -O fontawesome-free-web.zip
echo "Unzip Fontawesome"
unzip fontawesome-free-web.zip -d ./static/
echo "Remove downloaded zip file..."
mv ./static/fontawesome-free-5.8.1-web ./static/fontawesome-free-web
rm fontawesome-free-web.zip
cd ..