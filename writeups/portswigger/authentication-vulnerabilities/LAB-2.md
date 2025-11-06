#  LAB-2: Username enumeration via subtly different responses

#### :o: *Category*: Broken Authentication

#### :dart: *Goal*: Gain Access to account portal by brute-force attempts

## :large_blue_circle: Methodology

Login portal had a lockout protection whcih blocks multiple attempts with a 30-Min lockdown period, therefore we used Grep-Extract in the Intruder settings and noticed that the correct username and passowrd did not return any error. 

## :large_blue_circle: Steps

1. Capture the /login POST request in Burp Suite and send it to intruder
2. Select Attack Type as Sniper Attack
3. Place payload points on the Username
4. Under Palyload Settings within Intruder, set the grep extract, by selecting the error message from the response
5. Use the Username.txt as payload
6. Start attack and with for the no error in the  response warning column, that is the username
7. Next step is to find password, use the same steps above but change the payoad to Passwords.txt
