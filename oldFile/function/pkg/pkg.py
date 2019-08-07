import wget
import tarfile
from typing import Optional

apt = ["debian", "ubuntu"]
yum = ["centos"]

packager = None


# return packager type (apt, yum, pacman)
def getPackagerType(dist_name: str) -> Optional[str]:
    if dist_name in apt:
        return "apt"
    elif dist_name in yum:
        return "yum"
    else:
        return None


def installAgent() -> bool:
    print("Downloading Observium CE...")
    wget.download("http://www.observium.org/observium-community-latest.tar.gz", "/opt/observium-community-latest.tar.gz")  # TODO Make a check if need to redownload the file
    print("\nExtract tar file...")
    file = tarfile.open("/opt/observium-community-latest.tar.gz")
    file.extractall("/opt/")
    #print("Install agent dependence")
    #if pkg_apt():
    #    print(GREEN + "Update apt source" + YELLOW)
    #    os.system("apt-get update")
    #    print(GREEN + "Install dependence" + YELLOW)
    #    os.system("apt-get -qq install -y xinetd snmpd libwww-perl")
    #    print(GREEN + "")
    #    flm.copy("/opt/observium/scripts/observium_agent_xinetd", "/etc/xinetd.d/observium_agent_xinetd")
    #    os.system("service xinetd restart")
    #    flm.copy("/opt/observium/scripts/observium_agent", "/usr/bin/observium_agent")
    #    os.mkdir("/usr/lib/observium_agent")
    #    os.mkdir("/usr/lib/observium_agent/scripts-available")
    #    os.mkdir("/usr/lib/observium_agent/scripts-enabled")
    #    # flm.copy("/opt/observium/scripts/agent-local/*", "/usr/lib/observium_agent/scripts-available")
    #    # os.system("chmod +x /usr/bin/observium_agent")
    #    # os.system("ln -sf /usr/lib/observium_agent/scripts-available/dmi /usr/lib/observium_agent/scripts-enabled")
    #    flm.copy("/opt/observium/scripts/distro", "/usr/bin/distro")
    #    os.system("chmod +x /usr/bin/distro")
    #    print("FIN DE LA BASE DU TEST")
    #    end_program()
    #else:
    #    print(RED + "Intern script error report this to repo github" + GREEN)