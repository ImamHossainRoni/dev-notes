install_docker() {
    echo "Let's install latest version of docker!"
    # First, update your existing list of packages
    sudo apt update

    # Next, install a few prerequisite packages
    sudo apt install apt-transport-https ca-certificates curl software-properties-common

    # Then add the GPG key for the official Docker repository to your system
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    # Add the Docker repository to APT sources
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

    # Next, update the package database with the Docker packages from the newly added repo
    sudo apt update

    # Make sure you are about to install from the Docker repo instead of the default Ubuntu repo
    apt-cache policy docker-ce

    # Finally, Lets install Docker :)
    sudo apt install docker-ce

    # Docker should now be installed, Let's check docker status :)
    sudo systemctl status docker
    sudo systemctl status docker.service
    lets_do_some_fun

}

lets_do_some_fun() {
    sudo apt install sl
    sl
}

remove_docker() {
    # To identify what installed package actually I have
    dpkg -l | grep -i docker

    sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock

    echo "Docker is now completely uninstalled :("
}


check_is_outdated() {
    pat="^$1/"
    if [ -z "$(apt list --upgradable | grep -e $pat)" ]; then
        lets_do_some_fun
        echo "You have latest version of $1 :)"

    else
        echo "Lets uninstall old version of docker first"
        remove_docker
        echo "Lets install latest version of docker :)"
        install_docker

    fi
}

# If the docker version is outdated then it will install new version of docker
check_is_outdated docker
