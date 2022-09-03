# Sprints-DevOps
This branch contains the bash script file, the docker file and the files that are passed from Test branch

## Bash script
The user has to enter an integer to be the new port. The integer entered has to be between 1024 and 65535 or 22. The root login gets disabled and some users are granted sudo privileges.

If the number entered wasn't an integer:


![Alt text](/Screenshots/NonIntegers.png)




If the number wasn't in the correct range:



![Alt text](/Screenshots/NotInRange.png)



Altering port number, disabling root login and granting some users sudo privileges:



![Alt text](/Screenshots/Results1.png)



![Alt text](/Screenshots/Results2.png)



![Alt text](/Screenshots/Results3.png)



![Alt text](/Screenshots/Results4.png)



## Docker file
This file was created using image python:3.8, the working directory has been set to /var/src/app and all the files in local directory were copied to the container.

To open Dockerfile:


![Alt text](/Screenshots/openDockerfile.png)


To build:


![Alt text](/Screenshots/buildDockerfile.png)


To run:


![Alt text](/Screenshots/runDockerfile.png)

