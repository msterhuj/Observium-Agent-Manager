#!/bin/bash

###
### This script is not a official script
### Base of script by Observium Edited By MsterHuj
### https://github.com/msterhuj
###

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function agentinstall {
    echo -e "${GREEN}Update packages...${NC}"
    apt-get update
    echo -e "${GREEN}Installing additional packages...${NC}"
    apt-get -qq install -y xinetd snmpd libwww-perl
    cp /opt/observium/scripts/observium_agent_xinetd /etc/xinetd.d/observium_agent_xinetd
    service xinetd restart
    cp /opt/observium/scripts/observium_agent /usr/bin/observium_agent
    mkdir -p /usr/lib/observium_agent
    mkdir -p /usr/lib/observium_agent/scripts-available
    mkdir -p /usr/lib/observium_agent/scripts-enabled
    cp -r /opt/observium/scripts/agent-local/* /usr/lib/observium_agent/scripts-available
    chmod +x /usr/bin/observium_agent
    ln -sf /usr/lib/observium_agent/scripts-available/dmi /usr/lib/observium_agent/scripts-enabled
    cp /opt/observium/scripts/distro /usr/bin/distro
    chmod +x /usr/bin/distro
    echo -e "${GREEN}Reconfiguring local snmpd${NC}"
    echo "agentAddress  udp:161" > /etc/snmp/snmpd.conf
    snmpcommunity="$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-15};echo;)"
    echo "rocommunity $snmpcommunity" >> /etc/snmp/snmpd.conf
    echo "extend .1.3.6.1.4.1.2021.7890.1 distro /usr/bin/distro" >> /etc/snmp/snmpd.conf
    service snmpd restart
   echo -e "${GREEN}DONE! UNIX-agent is installed and this server is now ready for Observium${NC}"

}

if [[ $EUID -ne 0 ]]; then
  echo -e "${RED}ERROR: You must be a root user${NC}" 2>&1
  exit 1
fi

ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')

if [ -f /etc/lsb-release ]; then
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    OS=Debian  # XXX or Ubuntu??
    VER=$(cat /etc/debian_version)
else
    OS=$(uname -s)
    VER=$(uname -r)
fi

if [[ !$OS =~ ^(Ubuntu|Debian)$ ]]; then
    echo -e "${RED} [*] ERROR: This installscript does not support this distro, only Debian or Ubuntu supported.${NC}"
    echo -e "${RED} [*] ERROR: If this a error create a issues on my repo github${NC}"
    exit 1
fi

cat << "EOF"
  ___  _                         _
 / _ \| |__  ___  ___ _ ____   _(_)_   _ _ __ ___
| | | | '_ \/ __|/ _ \ '__\ \ / / | | | | '_ ` _ \
| |_| | |_) \__ \  __/ |   \ V /| | |_| | | | | | |
 \___/|_.__/|___/\___|_|    \_/ |_|\__,_|_| |_| |_|
EOF
echo -a ""
echo -e "${GREEN}Welcome to Observium automatic agent installscript"
echo -e ""
echo -e "${RED}(Unofficial Script By MsterHuj)${NC}"
echo -e ""
echo -e "Please choose which verision of Observium you would like to install${NC}"
echo -e ""
echo "1. Install the UNIX-Agent (snmpd-config will be overwritten)"
echo "3. Quit"
echo -n "(1-2):"
read -n 1 observ_ver
if [ $observ_ver = 1 ]; then
   echo ""
   echo -e "${GREEN} [*] Downloading Observium CE and unpacking...${NC}"
   wget -nv http://www.observium.org/observium-community-latest.tar.gz -O /opt/observium-community-latest.tar.gz
   cd /opt/
   tar zxf observium-community-latest.tar.gz
   agentinstall
   rm /opt/observium-community-latest.tar.gz
   exit 1
fi
