#  LAB-4: Broken brute-force protection, IP block

#### :o: *Category*: Broken Authentication

#### :dart: *Goal*: Gain Access to account portal by brute-force attempts

## :large_blue_circle: Methodology

Due to IP block we were unable to run the brute-force method as the ip was blocked after certain amount of requests, but there was a catch, once we entered the correct credentials the restriction was removed and the counter was reset. So th approach was to modify the username and password file in a way that it alternately used the correct credential so that the requests are not blocked.

## :large_blue_circle: Steps

1. Modify the username file and add given username(carlos), and the correct user (wiener), carlos should be repeated at-least 100 time and the wiener should be after every 10 occurences.
2. Modify the password file and add the user wiener password (peter) after every password, make sure the posision aligns with the username file like wiener:peter
3. Capture the /login POST request in Burp Suite and send it to intruder
4. Select Attack Type as Pitch-Fork Attack
5. From the resource pool, select ma concurent request to 1
6. Place payload positions on the Username and Password
7. Select user-LAB-4.txt file as username 
8. For payload position 2, use the password file pass-LAB-4.txt
9. Start attack
10. Once the attack is finished, filter the response for 302, that is the username.
11. Repeate the same steps for passwords