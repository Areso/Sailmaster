# Automation
## Introduction
Automation provided by Ansible.  
Please, install Ansible first.  
For an example, on Ubuntu 18.04 type this:  
        sudo apt install ansible  
Please, pay attention, to manage your localhost, your localhost must have sshd installed.  
        sudo apt install openssh-server  
Or, you could use local plays 
# Installation of Golang
		ansible-playbook -i "localhost, " -k -K -e "purge=True" golang.yml  
		ansible-playbook -K -e "purge=True" local-golang.yml  
# Installation of Lite IDE*
Lite ID  is a free and open source golang IDE
