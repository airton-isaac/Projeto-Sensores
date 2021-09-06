
# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  config.vm.provider "virtualbox" do |v|
    v.memory = 1536
    v.cpus = 2
  end
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  
#  config.vm.provision "shell",inline: "apt-get update"
#  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.network "forwarded_port", guest: 5000, host: 5000  # Linka a porta 5000 da MV com o computador local
  config.vm.provision "ansible_local" do |a|
    a.verbose  = true
	a.install  = true
    a.playbook = "provisioning/setup_dev.yml"
  end
end
