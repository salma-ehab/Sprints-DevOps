#usr/bin/bash

echo "Enter the port number you would like SSH to run on"

read port

if ! [[ "$port" =~ ^[0-9]+$ ]];
then
    	echo "The port number has to be an integer."

else
    	if [[ "$port" -ge 1024 && "$port" -le 65535 || "$port" = 22 ]];
    	then
            	sed -i -e "/Port /c\Port $port" /etc/ssh/sshd_config
            	echo "The port number has been changed to $port"

    	else
            	echo "The port number has to be between 1024 and 66535 or 22"
    	fi
fi

sed -i -e "/PermitRootLogin /c\PermitRootLogin no" /etc/ssh/sshd_config
echo "Root Login has been disabled"

while [[ -n $1 ]];
do

    	echo "$1	ALL=(ALL:ALL) ALL" >> /etc/sudoers;
    	shift
done
