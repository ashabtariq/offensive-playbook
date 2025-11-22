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


