import os
import subprocess

#basic linux commands
def cmd():
    a=True
    while a==True:
        os.system("clear")
        print("""
        \n
        Press 1 : To check present working directory.
        Press 2 : To display your login user
        Press 3 : To display all files 
        Press 4 : To display the file content
        Press 5 : To display ip address
        Press 6 : To display where is the command located
        Press 7 : To install software
        Press 8 : To check status of software
        Press 0 : To return to main menu
        """)
        ch = int(input("Enter your Choice:"))
        if   ch == 1 :
            os.system("pwd")
        elif ch==2:
            os.system("whoami")
        elif ch==3:
            os.system("ls -la")
        elif ch==4:
            vgn=input("Give name of the file(with extention):")
            os.system("cat {}".format(vgn))
        elif ch==5:
            os.system("ifconfig")
        elif ch==6:
            size=input("Enter the executable:")
            os.system("which {}".format(size))
        elif ch==7:
            soft=input("Enter the name of software:")
            os.system("yum install {} -y".format(soft))
        elif ch==8:
            vgn4=input("Enter the name for command(ex: start,stop):")
            lvn2=input("Enter the name of software:")
            os.system("systemctl {} {}".format(vgn4,lvn2))
        elif ch==0:
            print("\t\t\tEXIT")
            a=False
        else:
            print("Not Supported")
        input("\nPlease enter to continue...")
def remotecmd():
    un = input("Enter Username :")
    ip = input("Enter ip address")
    pd = getpass.getpass("Enter password :")	
    a=True
    while a==True:
        os.system("clear")
        print("""
        \n
        Press 1 : To check present working directory.
        Press 2 : To display your login user
        Press 3 : To display all files 
        Press 4 : To display the file content
        Press 5 : To display ip address
        Press 6 : To display where is the command located
        Press 7 : To install software
        Press 8 : To check status of software
        Press 0 : To return to main menu
        """)
        ch = int(input("Enter your Choice:"))
        if   ch == 1 :
	    
	    os.system("ssh -p {} ssh {}@{} pwd".format(pd,un,ip))
        elif ch==2:
	 
	    os.system("ssh -p {} ssh {}@{} whoami".format(pd,un,ip))
        elif ch==3:
	    
	    os.system("ssh -p {} ssh {}@{} la -la".format(pd,un,ip))
        elif ch==4:
	   
            vgn=input("Give name of the file(with extention):")
	    os.system("ssh -p {} ssh {}@{} cat {}".format(pd,un,ip,vgn))
        elif ch==5:
	   
	    os.system("ssh -p {} ssh {}@{} ifconfig enp0s3".format(pd,un,ip))
        elif ch==6:
	    
            size=input("Enter the executable:")
	    os.system("ssh -p {} ssh {}@{} which {}".format(pd,un,ip,size))
            size=input("Enter the executable:")
        elif ch==7:
	    
	    os.system("ssh -p {} ssh {}@{} cal".format(pd,un,ip))
            soft=input("Enter the name of software:")
            os.system("yum install {} -y".format(soft))
        elif ch==8:
	   
	    vgn4=input("Enter the name for command(ex: start,stop):")
            lvn2=input("Enter the name of software:")
	    os.system("ssh -p {} ssh {}@{} systemctl {} {}".format(pd,un,ip,vgn4,lvn2))
        elif ch==0:
            print("\t\t\tEXIT")
            a=False
        else:
            print("Not Supported")
        input("\nPlease enter to continue...")

#LVM
def lvm():
    print("\t\t\tLOGICAL VOLUME MANAGEMENT\n")
    print("\t\t\t=========================")
    print("\t\tTotal storage attached to the OS ")
    os.system("fdisk -l")
    print("\t\tfor creating Physical Volume\n")
    pv1=input("\t\tEnter the name of storage 1:")
    os.system("pvcreate {}".format(pv1))
    print("\t\tPhysical volume created")
    os.system("pvdisplay {}".format(pv1))
    pv2=input("\t\tEnter the name of storage 2:")
    os.system("pvcreate {}".format(pv2))
    print("\t\tPhysical volume created")
    os.system("pvdisplay {}".format(pv2))
    print("\n\t\tfor creating Volume Group\n")
    vgn=input("\t\tGive name to the VG:")
    os.system("vgcreate {} {} {}".format(vgn,pv1,pv2))
    print("\t\tVolume group created")
    os.system("vgdisplay {}".format(vgn))
    print("\n\t\tFor creating Logical Volume\n")
    size=input("Enter size for your LV:")
    lvn=input("Give name to your LV:")
    os.system("lvcreate --size {}G  --name {} {}".format(size,lvn,vgn))                      
    print("\n\t\tLogical Volume created\n")
    os.system("lvdisplay")
    print("\n\t\tLV formatted\n")
    os.system("mkfs.ext4  /dev/{}/{}".format(vgn,lvn))
    print("\nNew Logical Storage is ready for use\n")	
    input("\nPress enter to go to main menu...")




def partition():
    print("Total storage device you have in your system:")
    os.system("fdisk -l")
    n = input("enter the hard disk name u want to make partition for:")
    os.system("fdisk {0}".format(n))
    os.system("udevadm settle")
    os.system("fdisk -l")
    c = input("enter the name of newly created partition")
    s = input("enter the folder name:")
    os.system("mkfs.ext4 {0}".format(c))
    os.system("mkdir {0}".format(s))
    os.system("mount {0} {1}".format(c,s))                                 
    print("Partition created.")
#HADOOP FUNCTIONS
def software():
    print("\t\tInstalling jdk")
    os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
    print("\t\tInstalling hadoop")
    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")


def datanode():
    print("\t\t\tDATANODE SETUP")
    software()
    datanode_folder = input("\t\t\tFolder name for datanode:")
    os.system("rm -rf {}".format(datanode_folder))
    os.system("mkdir {}".format(datanode_folder))
    namenode_IP = input("\t\t\tProvide namenode IP: ")
    namenode_port = input("\t\t\tProvide port number of namenode: ")
    file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
	 #data of hdfs of datanode
    hdfs_data_dn =  '''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
    <!-- Put site-specific property overrides in this file. -->
    <configuration>
    <property>v
    <name>dfs.data.dir</name>
    <value>{}</value>
    </property>
    </configuration>\n'''.format(datanode_folder)
    file_hdfs_dn.write(hdfs_data_dn) #writing the data

    file_core_dn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
    core_data_dn = '''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
    <!-- Put site-specific property overrides in this file. -->
    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://{}:{}</value>
    </property>
    </configuration>\n'''.format(namenode_IP,namenode_port)
    file_core_dn.write(core_data_dn) 
    subprocess.getoutput("hadoop-daemon.sh start datanode")  
    subprocess.getoutput("jps")
    print("Datanode Started")


def namenode():
    print("\t\t\tNAMENODE SETUP")
    software()
    namenode_folder = input("\t\t\tFolder name for namenode:")
    os.system("rm -rf {}".format(namenode_folder))
    os.system("mkdir {}".format(namenode_folder))
    os.system("hadoop namenode --format")
    namenode_IP = input("\t\t\tProvide namenode IP: ")
    namenode_port = input("\t\t\tProvide port number of namenode: ")
    file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
	 #data of hdfs of datanode
    hdfs_data_nn =  '''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	 
    <!-- Put site-specific property overrides in this file. -->
    <configuration>
    <property>
    <name>dfs.name.dir</name>
    <value>{}</value>
    </property>
    </configuration>\n'''.format(namenode_folder)   
    file_hdfs_nn.write(hdfs_data_nn) #writing the data

    file_core_nn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
    core_data_nn = '''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->
    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://{}:{}</value>
    </property>
    </configuration>\n'''.format(namenode_IP,namenode_port)
    file_core_nn.write(core_data_nn)   
    subprocess.getoutput("hadoop-daemon.sh start namenode")
    subprocess.getoutput("jps")
    print("Namenode Started")

def client():
    print("\t\t\tCLIENT SETUP")
    software()
    namenode_IP = input("\t\t\tProvide namenode IP: ")
    namenode_port = input("\t\t\tProvide port number of namenode: ")
    file_core_nn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
    core_data_nn = '''<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
    <!-- Put site-specific property overrides in this file. -->
    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://{}:{}</value>
    </property>
    </configuration>\n'''.format(namenode_IP,namenode_port)
    file_core_nn.write(core_data_nn)

def putfile():
    fname=input("\t\tEnter your filename : ")
    st=subprocess.getouput("hadoop fs -put {} /".format(fname))


def delfile():
    fname=input("\t\tEnter your filename : ")
    st=subprocess.getouput("hadoop fs -rm  /{} ".format(fname))

def no_of_datanode():
    st=subprocess.getouput("hadoop dfsadmin report | less")


def files_on_cluster():
    st=subprocess.getouput("hadoop fs ls /")

def read_files_from_cluster():
    fname=input("\t\tEnter your filename")
    st=subprocess.getouput("hadoop fs -cat /{}".format(fname))

def hadoop():
    a=True 
    while a == True:
        os.system("clear")
        print("\t\t\tWELCOME TO MY HADOOP MENU")
        print("""
        \t\tPress 0 : To return to main menu
	\t\tPress 1 : To create name node
    	\t\tPress 2 : To create data node
        \t\tPress 3 : To create client
	\t\tPress 4 : To upload file on cluster
	\t\tPress 5 : To delete file on cluster 
    	\t\tPress 6 : To see all the datanodes on cluster
    	\t\tPress 7 : To see all the files on the cluster 
    	\t\tPress 8 : To read a file from cluster 
        """)
        print("\t\t==================================================")
        ch=int(input("Enter your choice : "))
        if   ch == 1:
            namenode()
        elif ch == 2:
            datanode()
        elif ch == 3:
            client()
        elif ch == 4:
            putfile()
        elif ch == 5:
            delfile()
        elif ch == 6:
            no_of_datanode()
        elif ch == 7:
            files_on_cluster()
        elif ch == 8:
            read_files_from_cluster()
        elif ch == 0:
            print("\t\t\tExit\n")
            a=False
        else :
            print("\t\tNot supported")

#AWS_functions
def ch1() :
        a=True 
        while a==True:
            os.system("clear")
            print("\t\t\tTo see details about services you launched\n")
            print("\t\t\t-------------------------------\n")
            print("""	
            \t\tPress 0 : To return to aws menu	
            \t\tPress 1 : Launched Instances 
            \t\tPress 2 : Key Pairs
            \t\tPress 3 : EBS volume
            \t\tPress 4 : Security Groups
            \t\tPress 5 : S3
            \t\tPress 6 : CloudFront Distributions
            \n""")
            print("\t\t\t--------------------------------\n")
            ch=int(input("\t\t\tEnter your choice : "))
            if ch==0:
                print("\t\t\tExit\n")
                a=False
            elif ch==1:
                dinstance()
            elif ch == 2:	
                dkey()	
            elif ch == 3:
                dvolume()
            elif ch == 4:
                dsecgroup()	
            elif ch == 5:
                ds3()
            elif ch == 6:
                dcf()	
            else:
                print("Wrong choice")
            input("\nPress Enter To Continue....\n")	
                #os.system("clear")		
			
def dkey() :
	print("\n\t\t\tLIST OF KEY PAIRS\n")
	print("\n\t\t\t--------------------------------")
	
	st1=subprocess.getstatusoutput("aws ec2 describe-key-pairs")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])	
	print("\n\t\t\t--------------------------------")

def dinstance() :
	print("\n\t\t\tLaunched Instances\n")
	print("\n\t\t\t--------------------------------")
	
	st1=subprocess.getstatusoutput("aws ec2 describe-instances")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")

def dvolume() :
	print("\n\t\t\tLIST OF EBS VOLUMES\n")
	print("\n\t\t\t--------------------------------")
	
	st1=subprocess.getstatusoutput("aws ec2 describe-volumes")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")

def dsecgroup() :
	print("\n\t\t\tSecurity Groups\n")
	print("\n\t\t\t--------------------------------")
	
	st1=subprocess.getstatusoutput("aws ec2 describe-security-groups")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")

def ds3() :
	print("\n\t\t\tS3\n")
	print("\n\t\t\t--------------------------------")
	print("List of buckets : ")
	
	st1=subprocess.getstatusoutput("aws s3api list-buckets")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")	

def dcf() :
	print("\n\t\t\tLIST OF DISTRIBUTIONS : \n")
	print("\n\t\t\t--------------------------------")
	
	st1=subprocess.getstatusoutput("aws cloudfront list-distributions")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")	


#choice 2
def ch2() :
	print("\t\t\tTo Launch an Instance\n")
	print("\t\t\t-------------------------------\n")
	
	st1=subprocess.getstatusoutput("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --security-group-ids sg-0d84b1831ae8a257a --key-name mykeyhadoop1122 --count 1 ")
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\t\t\t--------------------------------\n")
	print("\n Instance Launched...")
	print("\n\t\t\t--------------------------------")


#choice 3
def ch3() :
	print("\t\t\tTo start an Instance\n")
	print("\t\t\t-------------------------------\n")
	id=input("Enter Instance id : ")
		
	st1=subprocess.getstatusoutput("aws ec2 start-instances --instance-ids {}".format(id))
	if st1[0] == 0 :
		print(st1[1])
		print("\t\t\t--------------------------------\n")
		print("Instance started.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")


#choice 4
def ch4() :
	print("\t\t\tTo login to an instance\n")
	print("\t\t\t-------------------------------\n")
	
	keyn=input("Enter Key-Pair name : ")
	
	usern=input("Enter username : ")
	
	ipadd=input("Enter public ip os instance : ")
	
	st1=subprocess.getstatusoutput("ssh -i {} {}@{}".format(keyn,usern,ipadd))
	if st1[0] == 0 :
		print(st1[1])
		print("\t\t\t--------------------------------\n")
		print("Logged out.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")


#choice 5
def ch5() :
	print("\t\t\tTo stop an Instance\n")
	print("\t\t\t-------------------------------\n")
	id=input("Enter Instance id : ")
	
	st1=subprocess.getstatusoutput("aws ec2 stop-instances --instance-ids {}".format(id))
	if st1[0] == 0 :
		print(st1[1])
		print("\t\t\t--------------------------------\n")	
		print("Instance stopped.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")


#choice 6
def ch6() :
	print("\t\t\tTo terminate an Instance\n")
	print("\t\t\t-------------------------------\n")
	id=input("Enter Instance id : ")
	
	st1=subprocess.getstatusoutput("aws ec2 terminate-instances --instance-ids {}".format(id))
	if st1[0] == 0 :
		print(st1[1])
		print("\t\t\t--------------------------------\n")	
		print("Instance terminated.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")


#choice 7
def ch7():
	print("\t\t\tTo create a Key pair in aws cloud\n")
	print("\t\t\t-------------------------------\n")
	key=input("Enter new Key-pair name : ")
	
	st1=subprocess.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(key))
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")
	print("{} is created.\n".format(key))
	print("\n\t\t\t--------------------------------")


#choice 8
def ch8():
	print("\t\t\tTo delete a Key pair in aws cloud\n")
	print("\t\t\t-------------------------------\n")
	print("\n\t\t\tLIST OF KEY PAIRS\n")
	print("\n\t\t\t--------------------------------")
	os.system("aws ec2 describe-key-pairs")
	print("\n\t\t\t--------------------------------")
	id=input("Enter Key-pair id to be deleted : ")
	
	st=subprocess.getstatusoutput("aws ec2 delete-key-pair --key-pair-id {}".format(id))
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("Deleted.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 9
def ch9():
	print("\t\t\tTo create a security group in aws cloud\n")
	print("\t\t\t-------------------------------\n")
	des=input("Enter description for group : ")
	grp=input("Enter security group name : ")
	print("\t\t\t-------------------------------\n")
	st1=subprocess.getstatusoutput()
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("Security group  created.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 10
def ch10():
	print("\t\t\tTo delete a security group\n")
	print("\t\t\t-------------------------------\n")
	print("\n\t\t\tLIST OF SECURITY GROUPS\n")
	print("\n\t\t\t--------------------------------")
	os.system("aws ec2 describe-security-groups")
	print("\n\t\t\t--------------------------------")
	id=input("Enter security group id to be deleted : ")
	st=subprocess.getstatusoutput("aws ec2 delete-security-group --group-id {}".format(id))
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("Security group  deleted.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 11
def ch11() :
	print("\t\tTo create an EBS volume in AWS\n")
	print("\t\t\t-------------------------------\n")
	azc=input("Enter Availability-zone code : ")
	print()
	size=input("Enter size of volume(in GiB) : ")
	st=subprocess.getstatusoutput("aws ec2 create-volume --availability-zone {} --size {}".format(azc,size))
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("Volume created.\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 12
def ch12() : 
	print("\t\tTo attach EBS volume to aws instance\n")
	print("\n\t\t\t--------------------------------")	
	volid=input("Enter volume id to be attached : ")
	iid=input("Enter instance id : ")	
	st=subprocess.getstatusoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,iid))
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("volume attached\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 13
def ch13() :
	print("\t\tTo detach EBS volume to aws instance\n")
	print("\t\t\t-------------------------------\n")
	volid=input("Enter volume id to be attached : ")
	iid=input("Enter instance id : ")
	st=subprocess.getstatusoutput("aws ec2 detach-volume --volume-id <Volume_id> --instance-id <Instance_id> --device /dev/sdf")
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("volume detached\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 14
def ch14():
	print("\t\tTo delete EBS volume to aws instance\n")
	print("\t\t\t-------------------------------\n")
	volid=input("Enter volume id to be attached : ")
	st=subprocess.getstatusoutput("aws ec2 delete-volume --volume-id {}".format(volid))
	if st1[0] == 0 :
		print(st1[1])
		print("\n\t\t\t--------------------------------")
		print("volume deleted\n")
	else :
		print("ERROR : ")
		print(st1[1])
	
	print("\n\t\t\t--------------------------------")


#choice 15
def ch15():
	print("\t\tTo create a s3 bucket\n")
	print("\t\t\t-------------------------------\n")
	bn=input("Enter bucket Name : ")
	rn=input("Enter Region Name : ")
	st=subprocess.getstatusoutput("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={} --acl public-read".format(bn,rn,rn))
	print("\n\t\t\t--------------------------------")
	if st[0] == 0 :
		print("\t\tBucket created\n")
	else :
		print("Bucket name already exist.\n")
		print("\t\tTry once more!!")
		ch15()	
	print("\n\t\t\t--------------------------------")
	q=input("do you Want to add some objects(y/n) :")
	if q=='y':
		ch16()
		
#choice 16
def ch16():
	print("\t\tTo add an object to s3 object\n")
	print("\t\t\t-------------------------------\n")
	fn=input("Enter file Name : ")
	bn=input("Enter Bucket Name : ")
	on=input("Enter object file name : ")
	st=subprocess.getstatusoutput("aws s3 cp {} s3://{}/{} --acl public-read".format(fn,bn,on))
	print("\n\t\t\t--------------------------------")
	if st[0] == 0 :
		print("Object Added\n")	
		print(st[1])
	else:
		print("ERROR : \n")
		print(st[1])
		print("\t\tTry once more!!")
		ch16()	
	print("\n\t\t\t--------------------------------")


#choice 17
def ch17():
	print("\t\tTo delete an object from s3\n")
	print("\t\t\t-------------------------------\n")
	bn=input("Enter Bucket Name")
	on=input("Enter object file name : ")

	st1=subprocess.getstatusoutput()
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\n\t\t\t--------------------------------")
	print("Object Deleted\n")	
	print("\n\t\t\t--------------------------------")


#choice 18
def ch18():
	print("\t\tTo delete a bucket from s3\n")	
	print("\t\t\t-------------------------------\n")
	bn=input("Enter Bucket Name : ")
	
	st1=subprocess.getstatusoutput("aws s3api delete-bucket --bucket {}".format(bn))
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\t\t\t-------------------------------\n")
	print("Bucket Deleted\n")
	print("\n\t\t\t--------------------------------")


#choice 19
def ch19():
	print("\t\tTo create cloudfront distribution\n")
	print("\t\t\t-------------------------------\n")
	odn=input("Enter origin domain name(Bucket name) : ")
	
	st1=subprocess.getstatusoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(odn))
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\t\t\t-------------------------------\n")
	print("Cloudfront Distribution\n")
	print("\n\t\t\t-------------------------------\n")


#choice 20
def ch20():
	print("To delete a cloudfront distribution")
	print("\t\t\t-------------------------------\n")
	cid=input("Enter id of the distribution to be deleted : ")
	
	st1=subprocess.getstatusoutput("aws cloudfront delete-distribution --id {}".format(cid))
	if st1[0] == 0 :
		print(st1[1])
	else :
		print("ERROR : ")
		print(st1[1])
	print("\t\t\t-------------------------------\n")
	print("Cloudfront Distribution\n")
	print("\n\t\t\t--------------------------------")

def aws():
    
    a=True

    print("AWS Configuration")
    os.system("aws configure")
    while a == True:
        os.system("clear")
		#print("\t\t\tAWS")
		#print("AWS Configuration")
		#os.system("aws configure")
        print("\n\tWelcomE To AWS MenU")
        print("""
        Press 0:To return to main menu	
	Press 1:To see details about services
	Press 2:To launch AWS instance
	Press 3:To start a AWS instance
	Press 4:To login to an instance
	Press 5:To stop a AWS instance
	Press 6:To terminate an instance
	Press 7:To create a Key pair in aws cloud
	Press 8:To delete a Key Pair
	Press 9:To create a security group in AWS cloud
	Press 10:To delete a security group
	Press 11:To create an EBS volume in AWS
	Press 12:To attach EBS volume to aws instance
	press 13:To detach an EBS volume
	press 14:To delete an EBS volume 
	Press 15:To create a s3 bucket
	Press 16:To add an object to s3 bucket
	Press 17:To delete an object from s3
	Press 18:TO delete s3 bucket
	Press 19:To create cloudfront distribution
	Press 20:To delete a cloudfront distribution
        """)
        ch=int(input("Enter Your choice : "))
        if ch == 0 :
            print("\tExit")
            a=False
        elif ch == 1:
            ch1()
        elif ch == 2:
            ch2()
        elif ch == 3:
            ch3()
        elif ch == 4:
            ch4()
        elif ch == 5:
            ch5()
        elif ch == 6:
            ch6()
        elif ch == 7:
            ch7()
        elif ch == 8:
            ch8()
        elif ch == 9:
            ch9()
        elif ch == 10:
            ch10()
        elif ch == 11:
            ch11()
        elif ch == 12:
            ch12()
        elif ch == 13:
            ch13()
        elif ch == 14:
            ch14()
        elif ch == 15:
            ch15()
        elif ch == 16:
            ch16()
        elif ch == 17:
            ch17()
        elif ch == 18:
            ch18()
        elif ch == 19:
            ch19()
        elif ch == 20:
            ch20()
        else :
            print("WRONG CHOICE!!")
        input("\nPress Enter To Continue....\n")
    #os.system("cls")	

def docker():
    a=True
    while a == True:
        os.system("clear")
        print("\t\t****************************************")
        print("""
	\t\tPress 0 :Exit
	\t\tpress 1 :To launch a new os
	\t\tpress 2 :To see the existing image
	\t\tpress 3 :To see the running os
	\t\tpress 4 :To see all the launched os
	\t\tpress 5 :To start a container
	\t\tpress 6 :To stop a container
	\t\tpress 7 :To delete a image
	\t\tpress 8 :To remove a container
	\t\tpress 9:To remove a running container forcefully
	\t\tpress 10:To remove all containers
	\t\tpress 11:To see manual of docker
	""")
        print("\t\t*****************************************")
        ch=int(input("Enter your choice : "))
        if ch == 1:
            print("Launch a new os")
            print("\t\t******************************************")
            name=input("Enter your container name :")
            print("\t\t******************************************")
            print("""
            Image available:
            """)
            print("\t\t******************************************")
            os.system("docker images")
            print("\t\t******************************************")
            image=input("Select Image (image:version) : ")
            os.system("docker run --name {0} {1}".format(name,image))
            print("\t\t******************************************")
            print("{} container launched!!".format(name))
            print("\t\t******************************************")
        elif ch == 2:
            print("Available Images :")
            print("\t\t******************************************")
            os.system("docker images")
            print("\t\t******************************************")
        elif ch == 3:
            print("To see the running container : ")
            print("\t\t******************************************")
            os.system("docker ps")
            print("\t\t******************************************")
        elif ch == 4:
            print("To see all the launched container: ")
            print("\t\t******************************************")
            os.system("docker ps -a")
            print("\t\t******************************************")
        elif ch == 5:
            print("To start a container")
            print("\t\t******************************************")
            print("List of containers")
            os.system("docker ps -a")
            print("\t\t******************************************")
            name=input("select a container name : ")
            os.system("docker start {}".format(name))
            print("{} started!!".format(name))
            print("\t\t******************************************")
        elif ch == 6:
            print("To stop a container")
            print("\t\t******************************************")
            print("List of running containers")
            os.system("docker ps")
            print("\t\t******************************************")
            name=input("select a container name : ")
            os.system("docker stop {}".format(name))
            print("{} stopped!!".format(name))
            print("\t\t******************************************")
        elif ch == 7:
            print("To delete an image")
            print("\t\t******************************************")
            print("Available Images :")
            os.system("docker images")
            print("\t\t******************************************")
            image=input("Select Image (image:version) : ")
            os.system("docker rmi {}".format(image))
            print("{} removed!!".format(image))
            print("\t\t******************************************")
        elif ch == 8:
            print("To remove a container")
            print("\t\t******************************************")
            print("List of container: ")
            os.system("docker ps -a")
            osname=input("Enter container name to be removed: ")
            print("\t\t******************************************")
            os.system("docker rm {}".format(osname))
            print("{} removed!!".format(osname))
            print("\t\t******************************************")
        elif ch == 9:
            print("To remove a running container forcefully")
            print("\t\t******************************************")
            print("List of running containers: ")
            os.system("docker ps ")
            osname=input("Enter container name to be removed: ")
            print("\t\t******************************************")
            os.system("docker rm {} -f".format(osname))
            print("{} removed!!".format(osname))
            print("\t\t******************************************")
        elif ch == 10:
            print("To remove all containers")
            print("\t\t******************************************")
            os.system("docker rm `docker ps -a -q`")
            print("All containers are removed")
            print("\t\t******************************************")
        elif ch == 11:
            print("Docker manual")
            print("\t\t******************************************")
            os.system("man docker")
            print("\t\t******************************************")
        elif ch == 0 :
            print("\t\tEXIT")
            a=False
        else :
            print("Wrong Choice")				
        input("Press enter to continue...")
		

#MAIN MENU
print("\t\t\tWelcome to my tools")

r=input("Where do you want to run this menu(remote/local):")
if r.lower() == "local" :
	while True :
                os.system("clear")
                os.system("tput setaf 3")
                print("\t\tWELCOME TO MY AUTOMATION WORLD")

                print("\t\t\t\t MENU")

                print("\t\t\tPress 1 : LINUX COMMANDS")

                print("\t\t\tPress 2 : LVM")

                print("\t\t\tPress 3 : PARTITION")

                print("\t\t\tPress 4 : HADOOP")

                print("\t\t\tPress 5 : AWS")

                print("\t\t\tPress 6 : DOCKER")

                print("\t\t\tPress 0 : EXIT")
                ch=int(input("\t\tENTER YOUR CHOICE : "))
                if ch == 1:
                    cmd()
                elif ch == 2:
                    lvm()
                elif ch == 3:
                    partition()
                elif ch == 4:
                    hadoop()
                elif ch == 5:
                    aws()
                elif ch == 6:
                    docker()
		#elif ch == 7:
                     #partition()	
                elif ch == 0:
                    print("Have A Nice Day!!!THANKYOU... ")                    
                    exit()
                else:
                   print("Not Supported")
elif r.lower() == "remote" : 		
	 print("\t\tWELCOME TO MY AUTOMATION WORLD")
	 remotecmd()
else :
    print("Not Supported")			

			



