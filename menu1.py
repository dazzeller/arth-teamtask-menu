import  os
import  getpass

def linuxCmd(cmd):
	while(True):
		os.system("clear")
		print("""\n\t\t
			Press 1: to see date
			Press 2: to see calendar
			Press 3: to see all the partitions 
			Press 4: to see all the mountpoints or dirves
			Press 5: to list any folder
			Press 6: to create directory
			Press 7: to create file
			Press 8: to change directry
			Press 9: to open file in vi editor
			Press 10: to see IP
			Press 11: to delete file
			Press 12: to delete folder
			PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
		if(ch == 1):
			os.system("{}  date".format(cmd))
		elif(ch == 2):
			os.system("{}  cal".format(cmd))
		elif(ch == 3):
			os.system("{} sudo lsblk".format(cmd))
		elif(ch == 4):
			os.system("{} sudo df -hT".format(cmd))
		elif(ch == 5):
			fol=input("\tEnter your desired location:  ")
			os.system("{} sudo ls  {}".format(cmd,fol))
		elif(ch == 6):
			folder=input("\n\tGive folder name:  ")
			location=input("\n\tGive location where you whant to create folder:  ")
			os.system("{} sudo mkdir {}/{} ".format(cmd,location,folder))
		elif(ch == 7):
			File=input("\n\tEnter file name:  ")
			loc=input("\n\tGive location where you whant to create file:  ")
			os.system("{} sudo touch {}/{} ".format(cmd,loc,File))
		elif(ch == 8):
			fol=input("\n\tEnter lcoation where you want land:  ")
			os.system("{} sudo cd  {}".format(cmd,fol))
		elif(ch == 9):
			File=input("\n\tEnter file name with loction which you want to open:  ")
			os.system("{} sudo vi {} ".format(cmd,File))
		elif(ch == 10):
			os.system("{} ifconfig".format(cmd))
		elif(ch == 11):
			fi=input("\n\tEnter file name with location:  ")
			os.system("{} sudo  rm  {}".format(cmd,fi))
		elif(ch == 12):
			fol=input("\n\tEnter folder name with location:  ")
			os.system("{} sudo  rmdir  {}".format(cmd,fol))
		elif(ch == 0):
			break
		else:
			print("\n\tNo valid choice....")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")


def webserver(cmd,ip):
	while(True):
		os.system("clear")
		print("""\n\t\t
			Press 1: to install httpd software
			Press 2: to copy pages in root document
			Press 3: to start service 
			Press 4: to see status of service
			Press 5: to make service permanent
			Press 6: to stop the service
			Press 7: to restart the service
			Press 8: to copy pages in root document for remote{Exception}
			PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
		if(ch == 1):
			os.system("{} sudo dnf  install  httpd".format(cmd))
		elif(ch == 2):
			os.system("tput setaf 2")
			loc = input("\n\nEnter location of file which you want to copy in webserver:   ")
			os.system("tput setaf 7")
			os.system("{} sudo cat {} > /var/www/html/index.html ".format(cmd,loc))  
		elif(ch == 5):
			os.system("{} sudo systemctl  enable  httpd".format(cmd))
		elif(ch == 3):
			os.system("{} sudo systemctl  start  httpd".format(cmd))
		elif(ch == 4):
			os.system("{} sudo systemctl  status  httpd".format(cmd))
		elif(ch == 7):
			os.system("{} sudo systemctl  restart  httpd".format(cmd))
		elif(ch == 6):
			os.system("{} sudo systemctl  stop  httpd".format(cmd))
		elif(ch == 8):
			os.system("tput setaf 2")
			loc = input("\n\nEnter location of file which you want to copy in webserver:   ")
			os.system("tput setaf 7")
			os.system("scp {} root@{}:/var/www/html/".format(loc,ip))
		elif(ch == 0):
			print("Ending loop...")
			break
		else:
			print("\n\tInvalid choice..., retry")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")



def partitions(cmd,ip):
	while(True):
		os.system("clear")
		print("""\n\t\t
			Press 1: to make static partition
			Press 2: to do format
			Press 3: to  link or mount 
			Press 4: to create LVM dynamic partition
			Press 5: to display PV(Physical Volume)
			Press 6: to display VG(Volume Group)
			Press 7: to display LV(Logical Volume)
			Press 8: to extend LV by increasing the size of VG with adding new PV 
			Press 9: to extend LV without increasing size of VG
			Press 10: to reduce LV size
			Press 11: to unmount or remove link form the mountpoint
			PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
		if(ch == 1):
			hd_name=input("\n\tEnter Hard Disk name to create partition: ")
			os.system("{}{} sudo fdisk  {} ".format(cmd,ip,hd_name))
			os.system("{}{} sudo udevadm settle ".format(cmd,ip))
		elif(ch == 2):
			part_name=input("\n\tEnter partition which you want to  format:  ")
			os.system("{}{} sudo mkfs.ext4  {} ".format(cmd,ip,part_name))
		elif(ch == 3):
			part_name=input("\n\tEnter partition to which you want to mount:  ")
			fol=input("\n\tEnter  folder which you want to mount:  ")
			os.system("{}{} sudo mount  {}  {} ".format(cmd,ip,part_name,fol))
		elif(ch == 4):
			pv_name=input("\n\tEnter partition name you want to create physical volume:  ")
			vg_name=input("\n\tEnter VG name you want to give:  ")
			lv_name=input("\n\tEnter LV name you want to give:  ")
			size=input("\n\tEnter size of LV you want to create but must be less than size of VG:  ")
			os.system("{}{} sudo pvcreate  {} ".format(cmd,ip,pv_name))
			os.system(" {}{} sudo vgcreate  {}  {} ".format(cmd,ip,vg_name,pv_name))
			os.system("{}{} sudo lvcreate  --size {}G  --name  {}  {} ".format(cmd,ip,size,lv_name,vg_name))			
		elif(ch == 5):
			pv_name=input("\n\tEnter partition name or PRESS ENTER to see all the PVs:  ")
			os.system("{}{} sudo pvdisplay  {} ".format(cmd,ip,pv_name))
		elif(ch == 6):
			vg_name=input("\n\tEnter VG name or PRESS ENTER to see all the VGs:  ")
			os.system("{}{} sudo vgdisplay  {} ".format(cmd,ip,vg_name))
		elif(ch == 7):
			vg_name=input("\n\tEnter VG name:  ")
			lv_name=input("\n\tEnter LV name:  ")
			os.system("{}{} sudo lvdisplay  {}/{} ".format(cmd,ip,vg_name,lv_name))
		elif(ch == 8):
			Npv_name=input("\n\tEnter another partition name to create new  physical volume to extend VG:  ")
			vg_name=input("\n\tEnter VG name want to extend:  ")
			lv_name=input("\n\tEnter LV name you want to extend:  ")
			nsz=input("\n\tEnter the Size by which you want to increase:  ")
			os.system("{}{} sudo pvcreate  {} ".format(cmd,ip,Npv_name))
			os.system("{}{} sudo vgextend {} {}".format(cmd,ip,vg_name,Npv_name))									
			os.system("{}{} sudo lvextend  --size +{}G  /dev/mapper/{}-{} ".format(cmd,ip,nsz,vg_name,lv_name))
			os.system("{}{}  sudo e2fsck -fy  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
			os.system("{}{} sudo resize2fs  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
		elif(ch == 9):
			vg_name=input("\n\tEnter VG name want to extend:  ")
			lv_name=input("\n\tEnter LV name you want to extend:  ")
			nsz=input("\n\tEnter the Size by which you want to increase:  ")
			os.system("{}{} sudo lvextend  --size +{}G  /dev/mapper/{}-{} ".format(cmd,ip,nsz,vg_name,lv_name))
			os.system("{}{}  sudo e2fsck -fy  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
			os.system("{}{} sudo resize2fs  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
		elif(ch == 10):
			vg_name=input("\n\tEnter VG name want to extend:  ")
			lv_name=input("\n\tEnter LV name you want to extend:  ")
			nsz=input("\n\tEnter the Size by which you want to decrease:  ")
			os.system("{}{} sudo lvreduce  --size -{}G  /dev/mapper/{}-{} ".format(cmd,ip,nsz,vg_name,lv_name))
			os.system("{}{}  sudo e2fsck -fy  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
			os.system("{}{} sudo resize2fs  /dev/{}/{} ".format(cmd,ip,vg_name,lv_name))
			
		elif(ch == 11):
			ufol=input("\n\tEnter folder with location you want to unmount ")
			os.system("{}{} sudo umount -f {}".format(cmd,ip,ufol))

		elif(ch == 0):
			break
		else:
			print("Invalid choice....  ")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")

		
def Docker(cmd,ip):
	while(True):
		os.system("clear")
		print("""\n\t\t
			Press 1: to install docker
			Press 2: to start docker service
			Press 3: to see status of docker service
			Press 4:  to do permanent docker service
			Press 5: to restart docker serivce
			Press 6: to pull docker image
			Press 7: to launch container with interactive terminal in attach mode
			Press 8: to launch container with interactive terminal in detach mode 
			Press 9: to launch container without interactive terminal to run one or more programs in single go and come out from container 
			Press 10: to see  currently all the running containers
			Press 11: to list all the containers, stopped and runnng both
			Press 12: to list all the docker images
			Press 13: to see logs of any container
			Press 14: to copy file from base OS to docker container
			Press 15: to copy file from container to base OS
			Press 16: to search  docker images from the docker hub 
			Press 17: to delete particular container
			Press 18: to delete all the container
			Press 19: to stop particular container
			Press 20: to start  particular container
			Press 21: to attach particular container 
			PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
		
		if ch == 1:
			os.system("scp /teamTask1/docker.repo root@{}:/etc/yum.repos.d/ ".format(ip))
			os.system("{} sudo dnf install docker-ce --nobest  -y ".format(cmd))
		elif ch == 2:
			os.system("{} sudo systemctl  start  docker".format(cmd))
		elif ch == 3:
			os.system("{} sudo systemctl  status  docker".format(cmd))
		elif ch == 4:
			os.system("{} sudo systemctl  enable  docker".format(cmd))
		elif ch == 5:
			os.system("{} sudo systemctl  restart  docker".format(cmd))
		elif ch == 6:
			ImgNm=input("\n\tEnter  docker image name:  ")
			os.system("{} sudo docker pull {} ".format(cmd,ImgNm))
		elif ch == 7:
			conNm=input("\n\tEnter  docker container name:  ")
			ImgNm=input("\n\tEnter  docker image name:  ")
			os.system("{} sudo docker run  -it --name {} {} ".format(cmd,conNm,ImgNm))
		elif ch == 8:
			conNm=input("\n\tEnter  docker container name:  ")
			ImgNm=input("\n\tEnter  docker image name:  ")
			os.system("{} sudo docker run  -dit --name {} {} ".format(cmd,conNm,ImgNm))
		elif ch == 9:
			ImgNm=input("\n\tEnter  docker image name:  ")
			prog=input("\n\tEnter program you want to run")
			os.system("{} sudo docker run -i {} {}".format(cmd,ImgNm,prog))
		elif ch == 10:
			os.system("{} sudo docker ps".format(cmd))
		elif ch == 11:
			os.system("{} sudo docker ps -a".format(cmd))
		elif ch == 12:
			os.system("{} sudo docker images".format(cmd))
		elif ch == 13:
			conNm=input("\n\tEnter  container whom you want to see logs:  ")
			os.system("{} sudo docker logs {}".format(cmd,conNm))
		elif ch == 14:
			bsFile=input("\n\tEnter file with location there in base OS you want to copy:  ")
			conFile=input("\n\tEnter file with location where you want to copy in container os:  ")
			conNm=input("\n\tEnter  docker container name:  ")
			os.system("{} sudo docker cp {}  {}:{} ".format(bsFile,conFile,conNm))
		elif ch == 15:
			bsFile=input("\n\tEnter file with location where in base OS you want to copy:  ")
			conFile=input("\n\tEnter file with location  you want to copy there in container os:  ")
			conNm=input("\n\tEnter  docker container name:  ")
			os.system("{} sudo docker cp  {}:{}   {} ".format(conNm,conFile,bsFile))
		elif ch == 16:
			imgNm=input("\n\tEnter  docker image which you want to search:  ")
			os.system("{} sudo docker search {}".format(cmd,imgNm))
		elif ch == 17:
			conNm=input("\n\tEnter container name you want to delete")
			os.system("{} sudo docker rm  -f  {}".format(cmd,conNm))
		elif ch == 18:
			os.system("{} sudo docker rm `docker ps -a -q`".format(cmd))
		elif ch == 19:
			conNm=input("\n\tEnter  docker container name:  ")
			os.system("{} sudo docker stop {}".format(cmd,conNm))
		elif ch == 20:
			conNm=input("\n\tEnter  docker container name:  ")
			os.system("{} sudo docker start {}".format(cmd,conNm))
		elif ch == 21:
			conNm=input("\n\tEnter  docker container name:  ")
			os.system("{} sudo docker attach {}".format(cmd,conNm))
		elif ch == 0:
			break
		else:
			print("Invalid choice....  ")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")
def awsCli(cmd):
	while(True):
		os.system("clear")
		print("""\n\t\t
		Press 1: Login To AWS Cloud
		Press 2: Create a key Pair
		Press 3: Create a Security Group
		Press 4: Set Up Inbound Rule 
		Press 5: Launch an EC2 Instance
		Press 6: Create an EBS Volume
		Press 7: Attach EBS Volume to EC2 Instance
		Press 8: Configure A Webserver Inside EC2 Instance
		Press 9: Static Partitioning & Mounting Document Root(/var/www/html) To EBS  
		Press 10: Create S3 Bucket 
		Press 11: Upload the Content to S3 Bucket
		Press 12cle: Create Cloud Front Distribution
		Press 13: Delete A Key pair
		Press 14: Detach EBS Volume from  EC2 Insatnce
		Presss 15: Shut Down EC2 Instance
		Press 16: Terminate EC2 Instance
		Press 20: Start EC2 Instance after shut down
		Press 17: Delete Content From S3 Bucket
		Press 18: Delete S3 Bucket
		Press 19: Delete Security Group
		Press 21: To run some aws commands
		PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")

		if ch == 1:
			os.system("{} aws configure".format(cmd))
			print("\n\t\t\t----Sucessfully Logged In AWS Cloud---")
		elif ch == 2:
			key = input("\n\tEnter Key Name : ")
			os.system('{0} aws ec2 create-key-pair --key-name {1} --query "KeyMaterial" > {1}.pem'.format(cmd,key))
			os.system('{} chmod 0400 {}.pem'.format(cmd,key))
			print("\n\tSucessfully Created the Key Pair")
 
		elif ch == 3:
			sg = input("\n\tEnter Security Group Name : ")
			desSg = input("\n\tGive Description of Security Group : ")
			os.system('{} aws ec2 create-security-group --group-name {} --description "{}"'.format(cmd,sg,desSg))
			print("\n\tSecurity Group Created....")

		elif ch == 4:    
			print("\n\tcustomize Security Group according to your wish ...")
			sgId = input("\n\tEnter Your Security Group ID : ")
			port = input("\n\tEnter Port No : ")
			protocol = input("\n\tEnter Protocol Name : ")
			cidr = input("\n\tEnter CIDR Block Value : " )
			os.system('{0} aws ec2 authorize-security-group-ingress --group-id {1} --protocol {2} --port {3} --cidr {4}'.format(cmd,sgId,protocol,port,cidr))
			print("\n\tSucessfully Set Up The Inbound Rule ......") 

		elif ch == 5:
			sgId = input("Enter Your Security Group ID :")
			instanceType = input("Enter Your Instance Type :")
			key = input("\n\tEnter Your Key Name :")
			ami = input("\n\tEnter AMI ID means image flavour: ")
			count= input("\n\tHow many Instances You want To Launch? :")
			os.system("{} aws ec2 run-instances --security-group-ids {} --instance-type {} --image-id {}  --key-name {} --count {} ".format(cmd,sgId,instanceType,ami, key,count))
			print("\n\tSucessfully Launched Instance ......")
		
		elif ch == 6:
			volType = input("\n\tEnter Your Volume Type(gp2/io1/io2/sc1/st1/standard) :")
			volSize = input("\n\tHow Much Amount of EBS You want :")
			az = input("\n\tEnter Your Availability Zone :")
			os.system('{} aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(cmd,volType,volSize,az))
			print("\n\tSucessfully Launched EBS Volume ......")

		elif ch == 7:
			volId = input("\n\tEnter Your Volume ID :")
			instanceId = input("\n\tEnter Your Instance ID :")
			HDname = input("\n\tEnter Hard DisK name")
			os.system('{} aws ec2 attach-volume --volume-id {} --instance-id {} --device {}'.format(cmd,volId,instanceId,HDname))
			print("\n\tSucessfully attached EBS Volume ......")

		elif ch == 8:
			ip = input("\n\tEnter Your Instance Public IP :")
			key = input("\n\tEnter Key Location where you stored key to login: ")
			os.system('{} ssh ec2-user@{} -i {}.pem sudo yum install httpd -y'.format(cmd,ip,key))
			os.system('{} ssh ec2-user@{} -i {}.pem sudo systemctl start httpd'.format(cmd,ip,key))
			os.system('{} ssh ec2-user@{} -i {}.pem sudo systemctl enable httpd '.format(cmd,ip,key))
			os.system('{} ssh ec2-user@{} -i {}.pem sudo systemctl status httpd '.format(cmd,ip,key))
			print("\n\t\tWebserever Configured Sucessfully .....")

		elif int(ch) == 9:
			ip = input("\n\tEnter Public IP of EC2 : ")
			key = input("\n\tEnter Key Location where you stored key to login: ")
			os.system('{} ssh ec2-user@{} -i {}.pem sudo fdisk -l'.format(cmd,ip,key))
			part = input("\n\tEnter Partition Name To be Mounted on /var/www/html : ")
			os.system('{} ssh ec2-user@{} -i {}.pem sudo mkfs.ext4 {}'.format(cmd,ip,key))
			os.system('{} ssh ec2-user@{} -i {}.pem sudo mount {}  /var/www/html'.format(cmd,ip,key,part))
			print("*****************************************")
			os.system('{} ssh ec2-user@{} -i {}.pem sudo df -hT'.format(cmd,ip,key))
			print("\n\tEBS Volume Mounted Sucessfully.....")
		
		elif int(ch) == 10:
			bucket = input("Give Name to Your S3 Bucket : ")
			region = input("Enter Your Region Name : ")
			os.system('{0} aws s3api create-bucket --bucket {1} --region {2} --create-bucket-configuration LocationConstraint={2}'.format(cmd,bucket,region)) 
			print("**************************************")	

		elif ch == 11:    
			print("\n\tProvide The Details Given Below To Upload Your Content In S3 Bucket")
			fiLoc = input("\n\tEnter Your File/Folder/Images location that You want to Uplaod :")
			bucket = input("\n\tEnter your S3 Bucket Name : ")
			permission = input("\n\tEnter the permissions for your content in S3 : ")
			os.system('{} aws s3 cp  {}  s3://{}/  --acl {} '.format(cmd,fiLoc,bucket,permission))
			print("**************************************")

		elif ch == 12:
			bucket = input("\n\tEnter Your S3 Bucket Name : ")
			os.system('{} aws cloudfront create-distribution  --origin-domain-name {}.s3.amazonaws.com --query Distribution.DomainName '.format(cmd,bucket))
			print("**************************************")

		elif ch == 14:
			volId = input("\n\tEnter ID of EBS To be Detached : ")
			os.system('{} aws ec2 detach-volume --volume-id {}'.format(cmd,volId))
			print("\n\tEBS Volume Detached Sucessfully........")

		elif ch == 15:
			instanceId = input("\n\tEnter ID of EC2 Instance To be shut down: ")
			os.system('{} aws ec2 stop-instances --instance-ids {} '.format(cmd,instanceId))
			print("\n\tShut down.....")

		elif ch == 16:
			instanceId = input("\n\tEnter ID of EC2 Instance To be Terminated : ")
			os.system('{} aws ec2 terminate-instances --instance-ids {} '.format(cmd,instanceId))
			print("\n\tTerminated.....")

		elif ch == 17:
			obj = input("\n\tEnter The Name of Object(file) You want to Delete from S3 :")
			bucket = input("\n\tEnter S3 Bucket Name : ")
			os.system('{} aws s3 rm s3://{}/{}'.format(cmd,bucket,obj))
			print("\n\tDeleted.....")

		elif ch == 18:
			bucket = input("\n\tEnter S3 Bucket Name that You want To Delete :   ")
			region = input("\n\tEnter Your Region where  s3 bucket is there:  ")
			os.system('{} aws s3api delete-bucket --bucket {} --region {} '.format(cmd,bucket,region))

		elif ch == 19:
			sg = input("Enter ID of Security Group that you want to Delete : ")
			os.system('{} aws ec2 delete-security-group --group-id {} '.format(cmd,sg))

		elif ch == 20:
			instanceId = input("\n\tEnter ID of EC2 Instance To be started: ")
			os.system('{} aws ec2 start-instances --instance-ids {} '.format(cmd,instanceId))
			print("\n\tStarted.....")

		elif ch == 21:
			command=input("\n\t Enter any aws command:  ")
			os.system("{} {}".format(cmd,command))

		elif ch == 0:
			break

		else:
			print("Invalid choice....  ")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")
def Hadoop():
	while True:
		os.system("clear")
		print("\n\n********************")
		print("""\n\t\t
		Press 1: Install Hadoop Requirements
		Press 2: Configure Name Node
		Press 3: Configure Data Node
		Press 4: Configure Hadoop Client
		Press 5: Upload Data To Hadoop Cluster
		Press 6: Read Client Data from Hadoop Cluster
		Press 7: Delete Client Data
		Press 8: Start Name Node
		Press 9: Start Data Node
		PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
       
		if ch == 1:
			n=input("\n\tIf don't have sotftware and want to copy Press YES:   ")
			ip=input("\n\tEnter IP where you want to install:  ")
			user=input("\n\tEnter username of the Node:  ")
			if n == "YES":
				os.system("scp /root/jdk-8u171-linux-x64.rpm {}@{}:/root".format(user,ip))
				os.system("scp /root/hadoop-1.2.1-1.x86_64.rpm {}@{}:/root".format(user,ip))
			os.system('ssh {}@{} sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(user,ip))
			os.system('ssh {}@{} sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force'.format(user,ip))
			print("\n\tHadoop Requirements Sucessfully Installed")
           
		elif ch == 2:
			ip=input("\n\tEnter IP of Namenode:  ")
			user=input("\n\tEnter username of the NameNode:  ")
			Dir = input("\n\t\tEnter your NameNode directory name : ")
			print("\t\t\t\tConfiguring hdfs-site.xml file ............")
			os.system(" echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			os.system(' echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
			os.system(' echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(Dir))
			os.system(' echo -e "</property>" >> /root/hdfs-site.xml')
			os.system(' echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			os.system('scp  /root/hdfs-site.xml  {}@{}:/etc/hadoop/ '.format(user,ip))
			os.system('rm -rf /root/hdfs-site.xml')
			print("\n\tFormatting the Name Node ........")
			os.system('ssh {}@{} sudo hadoop namenode -format'.format(user,ip))
			print("\n\t\t\t\tConfiguring core-site.xml file ...........")
			os.system(" echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			os.system(' echo -e "\n<configuration>" >> /root/core-site.xml')
			os.system(' echo -e "\n<property>" >> /root/core-site.xml')
			os.system(' echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(ip))
			os.system('echo -e "</property>" >> /root/core-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
			os.system('scp  /root/core-site.xml  {}@{}:/etc/hadoop/ '.format(user,ip))
			os.system('rm -rf /root/core-site.xml')
			print("\n\t-------------------------------------------")
			print("\n\t Starting Hadoop Name Node Service..........")
			os.system('ssh {}@{} sudo hadoop-daemon.sh start namenode '.format(user,ip)) 
			os.system('ssh {}@{} sudo jps'.format(user,ip))

		elif ch == 3:
			ip=input("\n\tEnter IP of DataNode:  ")
			IP=input("\n\tEnter IP of NameNode:  ")
			user=input("\n\tEnter username of the DataNode:  ")
			Dir = input("\n\t\tEnter your DataNode directory name : ")
			print("\t\t\t\tConfiguring hdfs-site.xml file ............")
			os.system(" echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
			os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
			os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
			os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
			os.system(' echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
			os.system(' echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(Dir))
			os.system(' echo -e "</property>" >> /root/hdfs-site.xml')
			os.system(' echo -e "\n</configuration>" >> /root/hdfs-site.xml')
			os.system('scp  /root/hdfs-site.xml  {}@{}:/etc/hadoop/ '.format(user,ip))
			os.system('rm -rf /root/hdfs-site.xml')
			print("\n\t\t\t\tConfiguring core-site.xml file ...........")
			os.system(" echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			os.system(' echo -e "\n<configuration>" >> /root/core-site.xml')
			os.system(' echo -e "\n<property>" >> /root/core-site.xml')
			os.system(' echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(IP))
			os.system('echo -e "</property>" >> /root/core-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
			os.system('scp  /root/core-site.xml  {}@{}:/etc/hadoop/ '.format(user,ip))
			os.system('rm -rf /root/core-site.xml')
			print("\n\t-------------------------------------------")
			print("\n\t Starting Hadoop DataNode Service..........")
			os.system('ssh {}@{} sudo hadoop-daemon.sh start datanode '.format(user,ip)) 
			os.system('ssh {}@{} sudo jps'.format(user,ip))

			print("\n\t------------------------------------")
			print("\n\t Showing Hadoop Cluster Report .....")
			os.system('ssh {}@{} sudo hadoop dfsadmin -report '.format(user,ip))

      
		elif ch == 4:
			ip=input("\n\tEnter IP of ClientNode:  ")
			IP=input("\n\tEnter IP of NameNode:  ")
			user=input("\n\tEnter username of the ClientNode:  ")
			print("\n\t\t\t\tConfiguring core-site.xml file ...........")
			os.system(" echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
			os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
			os.system(' echo -e "\n<configuration>" >> /root/core-site.xml')
			os.system(' echo -e "\n<property>" >> /root/core-site.xml')
			os.system(' echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
			os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(IP))
			os.system('echo -e "</property>" >> /root/core-site.xml')
			os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
			os.system('scp  /root/core-site.xml  {}@{}:/etc/hadoop/ '.format(user,ip))
			os.system('rm -rf /root/core-site.xml')
			print("\n\t-------------------------------------")
			print("\n\t Showing Hadoop Cluster Report ......")
			os.system('ssh {}@{} sudo hadoop dfsadmin -report '.format(user,ip))

			print("\t\tHadoop Client Sucessfully Configured.........")

 
		elif ch == 5:
			ip = input("\t\tEnter Client IP : ")
			fi = input("\t\tEnter The Name of File You want to upload in Hadoop Cluster : ")
			user=input("\n\tEnter username of the ClientNode:  ")
			os.system('ssh {}@{} sudo hadoop fs -put {} / '.format(user,ip,fi))
			print("\t\t\tFile Sucessfully Uploaded .......................")
			os.system('ssh {}@{} sudo hadoop fs -ls /'.format(user,ip))
       
		elif ch == 6:
			ip = input("\t\tEnter Client IP : ")
			fi = input("\t\tEnter The Name of File You want to Read in Hadoop Cluster : ")
			user=input("\n\tEnter username of the ClientNode:  ")
			os.system('ssh {}@{} sudo hadoop fs -cat /{} '.format(user,ip,fi))

		elif ch == 7:
			ip = input("\t\tEnter Client IP : ")
			fi = input("\t\tEnter The Name of File You want to Delete in Hadoop Cluster : ")
			user=input("\n\tEnter username of the ClientNode:  ")
			os.system('ssh {}@{} sudo  hadoop fs -rm /{} '.format(user,ip,fi))
			print("\t\tSucessfully Deleted File {} ".format(fi))
       
		elif ch == 8:
			ip=input("\n\tEnter IP of Namenode:  ")
			user=input("\n\tEnter username of the NameNode:  ")
			os.system('ssh {}@{} sudo hadoop-daemon.sh start namenode '.format(user,ip)) 
			os.system('ssh {}@{} sudo jps'.format(user,ip))
		elif ch == 9:
			ip=input("\n\tEnter IP of Damenode:  ")
			user=input("\n\tEnter username of the DameNode:  ")
			os.system('ssh {}@{} sudo hadoop-daemon.sh start datanode '.format(user,ip)) 
			os.system('ssh {}@{} sudo jps'.format(user,ip))
		elif ch == 0:
			break

		else:
			print("Invalid choice....  ")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")
       
def hadoopRem(cmd):
	while True:
		os.system("clear")
		print("\n\n********************")
		print("""\n\t\t
		Press 1: Upload Data To Hadoop Cluster
		Press 2: List any File
		Press 3: Read Client Data from Hadoop Cluster
		Press 4: Delete Client Data
		Press 5: To see report of cluster
		Press 6: Stop  Node
		PRESS 0: TO COME OUT""")
		os.system("tput setaf 2")
		ch=int(input("\n\n\t\tEnter choice:  "))
		os.system("tput setaf 7")
		if ch == 1:
			fi = input("\t\tEnter The Name of File location You want to Upload in Hadoop Cluster : ")
			os.system('{} sudo hadoop fs -put {} / '.format(cmd,fi))
			print("\t\t\tFile Sucessfully Uploaded .......................")
		elif ch == 2:
			os.system('{} sudo hadoop fs -ls /'.format(cmd))
       
		elif ch == 3:
			fi = input("\t\tEnter The Name of File You want to Read in Hadoop Cluster : ")
			os.system('{} sudo hadoop fs -cat /{} '.format(cmd,fi))

		elif ch == 4:
			fi = input("\t\tEnter The Name of File You want to Delete in Hadoop Cluster : ")
			os.system('{} sudo  hadoop fs -rm /{} '.format(cmd,fi))
			print("\t\tSucessfully Deleted File {} ".format(fi))
       
		elif ch == 5:
			os.system("{}  sudo hadoop  dfsadmin  -report".format(cmd))
		elif ch == 6:
			node=input("\n\t\tEnter datanode/namenode")
			os.system('{} sudo hadoop-daemon.sh start datanode '.format(cmd)) 
			os.system('{} sudo jps'.format(cmd))
		elif ch == 0:
			break

		else:
			print("Invalid choice....  ")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")
       

os.system("tput  setaf  3")
print("\t\t\tWelcome to Menu !!!")
os.system("tput  setaf  7")
print("\t\t\t----------")
password=getpass.getpass("Enter password:  ")

if(password != "Vishal"):
	print("\n\t\tWrong password....")
else:
	while True:
		os.system("clear")
		os.system("tput  setaf  6")
		choice = input("\n\t\tEnter remote/local/exit:  ")
		os.system("tput  setaf  7")
		if(choice == "local"): 
			while(True):
				os.system("sudo clear")
				print("""\t\t
				Press 1 to run some linux commands
				Press 2 to see Instace details in AWS
				Press 3 to Configure Webserver
				Press 4 to do partition related stuff
				Press 5 to do docker related stuff
				Press 6 to do AWS cloud related stuff
				Press 7 to set up Hadoop Cluster
				PRESS 0: TO COME OUT""")
				os.system("tput  setaf  5")
				cmd=int(input("\n\t\tEnter choice: "))
				os.system("tput  setaf  7")
				if(cmd==1):
					command=linuxCmd("")
					os.system("{}".format(command))
				elif(cmd==2):
					os.system("aws  ec2  describe-instances")
				elif(cmd==3):
					webserver("","")
				elif(cmd==4):
					partitions("","")
				elif(cmd==5):
					Docker("","")
				elif(cmd==6):
					awsCli("")
				elif(cmd==7):
					Hadoop()
				elif(cmd==0):
					os.system("clear")
					break
				else:
					print("\n\t\tInvalid choice...")
				os.system("tput setaf 5")
				input("\n\n\t\tEnter to continue...")
				os.system("tput setaf 7")
		elif choice == "remote":
			os.system("clear")
			ip=input("Enter IP Address:  ")
			while(True):
				os.system("clear")
				print("""\t\t
				Press 1 to run some linux commands
				Press 2 to see Aws instnace details
				Press 3  To configure webserver
				Press 4 to do partition related stuff
				Press 5 to do docker related stuff
				Press 6 to do AWS cloud related stuff
				Press 7 to run  Hadoop related commands 
				PRESS 0: TO COME OUT""")
				os.system("tput  setaf  5")
				cmd=int(input("\n\tEnter choice:  "))
				os.system("tput  setaf  7")
				if(cmd==1):
					linuxCmd("ssh  root@{}".format(ip))
				elif(cmd==2):
					os.system("ssh  root@{} aws ec2 describe-instances".format(ip))  
				elif(cmd==3):
					webserver("ssh  root@{}".format(ip),ip)
				elif(cmd==4):
					partitions("ssh  root@",ip)
				elif(cmd==5):
					Docker("ssh  root@{}".format(ip),ip)
				elif(cmd==6):
					awsCli("ssh  root@{}".format(ip))
				elif(cmd==7):
					hadoopRem("ssh  root@{}".format(ip))
				elif(cmd==0):
					os.system(" clear")
					break
				else:
					print("\n\t\tInvalid choice...")
				os.system("tput setaf 5")
				input("\n\n\t\tEnter to continue...")
				os.system("tput setaf 7")
		elif choice ==  "exit":
			os.system(" clear")
			exit()
		else:
			print("\n\t\tInvalid choice....")
		os.system("tput setaf 5")
		input("\n\n\t\tEnter to continue...")
		os.system("tput setaf 7")

