# Automation
## Introduction
Automation provided by Ansible.  
Please, install Ansible first.  
For an example, on Ubuntu 18.04 type this:  
		sudo apt install ansible  
Please, pay attention, to manage your localhost, your localhost must have sshd installed.  
		sudo apt install openssh-server  
Or, you could use local plays.
# Installation of Golang
		ansible-playbook -i "localhost, " -k -K -e "gopurge=True" golang.yml  
		ansible-playbook -K -e "gopurge=True" local-golang.yml  
# Installation of Lite IDE*
Lite IDE  is a free and open source golang IDE.  
For now, it is a manual operation:  
https://github.com/visualfc/liteide/releases/latest  
chmod +x  
