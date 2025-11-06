#  LAB-3: Username enumeration via response timing

#### :o: *Category*: Broken Authentication

#### :dart: *Goal*: Gain Access to account portal by brute-force attempts

## :large_blue_circle: Methodology

As there is IP restriction which tells us that X-Forwarded-For is supported, so we use pitch-fork attack to spoof IP and another payload parameter for username. After attack is completed, we add a response completed column, the time which takes longest is the username (arkansas:ginger). Make sure to keep password length more than 100 and then start attack. Repeat the same for password

## :large_blue_circle: Steps

1. Capture the /login POST request in Burp Suite and send it to intruder
2. Select Attack Type as Pitch-Fork
3. Place payload positions on the Username and X-Forwarderd-For (Add header if not found)
4. For the payload 1, select number and set range from 1- 100 with step of 1
5. For payload position 2, use the username file from wordlists folder
6. Start attack
7. Once the attack is finished, add Response Completed cloumn to the result and sort descending, ther response with the highest response time is the username
8. Repeate the above steps for passowrd
