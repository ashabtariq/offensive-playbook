### Networking Commands

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ifconfig - Interface details along with IP address
iwconfig - Wireless Interface Details
netstat -ano - All active connections
arp -a: - Physically cvonnected devices or devices to which machine  talking to
route: - Prints out the routing table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Writing to a file

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "TEXT YOU WANT IN FILE" > [FILENAME]  ## A SINGLE '>' IS USED TO WRITE/REPLACE IN A FILE
echo "TEXT YOU WANT IN FILE" >> [FILENAME] ## A DOUBLE '>>' IS USED TO APPEND TO EXISTING FILE
touch [FILENAME]                           # CREATING A NEW FILE BLANK WITHOUT EXTENSION


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Starting and Stopping a service

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

service apache2 start/stop   #STARTING APACHE WEBSERVER
python -m SimpleHTTPServer [PORTNUM] # STARTING A SIMPLE PYTHON WEB SERVER SERVES A DIRECTORY WHICH IT IS STARTED IN
systemctl enable / disable ssh #STARTING  A SERVICE ON BOOT(ANY SERVICE)
systemctl enable postgresql
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Installing & Updating tools

Install most of the softwares to /opt directory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sudo apt-get update
sudo apt-get install [PACKAGENAME]
sudo apt-get upgrade
sudo apt-get dist-upgrade

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### NMAP

##### Flags

~~~bash
-sS: TCP SYN Scan      : Half Open Scan
-sT: TCP Connect Scan  : Full TCP Scan
-sU: UDP Scan          : Works by sending UDP packet to every port
-sN: Null Scan         : TCP Packet with no option set, RST = Closed, No reply is Open
-sn: Ping Sweep        : Only send Ping packet, no port scanning. Determine if host is up
-v : Increase Verbosity:
-t4: Timing Template   : 0:paranoid, 1:snkeay, 2:Polite, 4:aggressive. 5:Insane
-sV: Enumerate         : Probe ports and determine Service numbers
-p : CSV for ports     : List of ports to scan
-oG: Grepable Output   : Redirect output to a text file
-F: Fast Mode          : Only scans a few ports, rather than all default ports
-O: Checks OS          : Try to determine OS
-A: Check OS+          : Detect OS and services
-Pn: Skip Discovery    : Assume Host is up
-script: Use Script
~~~

### Netbios/SMB Scans

~~~bash
ntbscan -r [HOST]                             # Scans for the hosts that have netbios service running
enum4linux -a [HOST]                          # Detailed information for a host in case of SMB Vulnerability 
inmao -C -o 139,445 --script smb-os-discovery # NMAP script for SMB OS doscovery
~~~