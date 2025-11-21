#  LAB-1: Username enumeration via different responses

#### :o: Category: Broken Authentication

#### :dart: Goal: Gain Access to account portal by brute-force attempts

## :large_blue_circle: Methodology

Login portal had no brute-force protection and successive attempts were not blocked so bruteforcing the login was the best choice. To exploit we will identify the correct username first and then the password using the same approach

## :large_blue_circle: Steps

1. Capture the /login POST request in Burp Suite and send it to intruder
2. Select Attack Type as Sniper Attack
3. Place payload points on the Username
4. Use the LAB-1-Username.txt as payload
5. Start attack and with for the 302 response, that is the username
6. Next step is to find password, use the same steps above but change the payoad to LAB-1-Passwords.txt
