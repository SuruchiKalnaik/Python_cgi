#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess

form = cgi.FieldStorage()

cmd = form.getvalue("c")

if ("date" in cmd) or ("day" in cmd) or ("time" in cmd):
	output = subprocess.getstatusoutput("date")
	if output[0] == 0:
		print("Here is your date..<br />")
		print(output[1])
elif ("calendar" in cmd):
	output = subprocess.getstatusoutput("cal")
	if output[0] == 0:
		print("Here is your calendar..<br />")
		print(output[1])
elif ("storage" in cmd) or ("space" in cmd):
	output = subprocess.getstatusoutput("free -m")
	if output[0] == 0:
		print("This is your system storage..")
		print("<br />")
		print(output[1])
elif ("ip" in cmd) or ("address" in cmd):
	output = subprocess.getstatusoutput("ifconfig enp0s3")
	if output[0] == 0:
		print("This is your system IP address..<br />")
		print(output[1])
elif (("list" in cmd) or ("show" in cmd) or ("display" in cmd)) and (("file" in cmd) or ("folder" in cmd) or ("directory" in cmd)):
	output = subprocess.getstatusoutput("ls")
	if output[0] == 0:
		print("List of all files and folders in your system..<br />")
		print(output[1])
elif (("list" in cmd) or ("show" in cmd) or ("display" in cmd)) and (("process" in cmd) or ("activity" in cmd) or ("operation" in cmd)):
	output = subprocess.getstatusoutput("ps -aux")
	if output[0] == 0:
		print("Here is your all process running in the system..<br />") 
		print(output[1])
elif (("configure" in cmd) or ("set" in cmd)) and (("yum" in cmd) or ("dnf" in cmd)):
	output = subprocess.getstatusoutput("cd /etc/yum.repos.d/")
	if output[0] == 0:
		output = subprocess.getstatusoutput("sudo touch /etc/yum.repos.d/rhel8.repo")
		output = subprocess.getstatusoutput("sudo chmod a+rwx rhel8.repo")
		if output[0] == 0:
			output = subprocess.getstatusoutput("sudo echo [dvd1] >> rhel8.repo")
			output = subprocess.getstatusoutput("sudo echo baseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream >> rhel8.repo")
			output = subprocess.getstatusoutput("sudo echo gpgcheck = 0 >> rhel8.repo")
			output = subprocess.getstatusoutput("sudo echo [dvd2] >> rhel8.repo")
			output = subprocess.getstatusoutput("sudo echo baseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS >> rhel8.repo")
			output = subprocess.getstatusoutput("sudo echo gpgcheck = 0 >> rhel8.repo")
			if output[0] == 0:
				print("Yum has been configure successfully")
elif (("install" in cmd) or ("configure" in cmd)) and ("docker" in cmd):
	output = subprocess.getstatusoutput("cd /etc/yum.repos.d/")
	if output[0] == 0:
		output = subprocess.getstatusoutput("sudo touch /etc/yum.repos.d/docker.repo")
		if output[0] == 0:
			output = subprocess.getstatusoutput("sudo echo [docker] > docker.repo")
			output = subprocess.getstatusoutput("sudo echo baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/ >> docker.repo")
			output = subprocess.getstatusoutput("sudo echo gpgcheck = 0 >> docker.repo")
			if output[0] == 0:
				output = subprocess.getstatusoutput("sudo yum install docker-ce --nobest")
				if output[0] == 0:
					output = subprocesss.getstatusoutput("sudo systemctl start docker")
					if output[0] == 0:
						print("Docker has been install properly")
elif (("configure" in cmd) or ("setup" in cmd)) and (("web" in cmd) or ("server" in cmd)):
	output = subprocess.getstatusoutput("sudo dnf install httpd")
	if output[0] == 0:
		output = subprocess.getstatusoutput("sudo systemctl start httpd")
		if output[0] == 0:
			print("Webserver has been configure properly..<br />")
			print("Now you can create your web pages in /var/www/html/ folder..")
elif ("quit" in cmd) or ("exit" in cmd):
	print("Goodbye! Have a nice day..")
else:
	print("Your system does not support..")
 		 
