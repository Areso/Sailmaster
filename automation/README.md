# Automation
## Introduction
Automation provided by Ansible.  
Please, install Ansible first.  
For an example, on Ubuntu 18.04 type this:  
		sudo apt install ansible  
Please, pay attention, to manage your localhost, your localhost must have sshd installed.  
		sudo apt install openssh-server  
Or, you could use local plays.
## Installation of Golang
		ansible-playbook -i "localhost, " -k -K -e "pack_purge=True" -u "root" golang.yml  
		ansible-playbook -K -e "pack_purge=True" local-golang.yml  
## Installation of Docker
		ansible-playbook -i "localhost, " -k -K -e "pack_purge=True" -u "root" docker.yml  
		ansible-playbook -K -e "pack_purge=True" local-docker.yml  
## Installation of Lite IDE*
Lite IDE  is a free and open source golang IDE.  
For now, it is a manual operation:  
https://github.com/visualfc/liteide/releases/latest  
chmod +x  
## Popular erorrs
>fatal: [work]: FAILED! => {"changed": false, "module_stderr": "Shared connection to work closed.\r\n", 
> "module_stdout": "/bin/sh: 1: /usr/bin/python: not found\r\n", "msg": "MODULE FAILURE", "rc": 127}
just add to -e this:   
		ansible_python_interpreter=/usr/bin/python3  
