#  LAB-5: Username enumeration via account lock

#### :o: *Category*: Broken Authentication

#### :dart: *Goal*: Gain Access to account portal by brute-force attempts

## :large_blue_circle: Methodology

One way in which websites try to prevent brute-forcing is to lock the account if certain suspicious criteria are met, usually a set number of failed login attempts. Just as with normal login errors, responses from the server indicating that an account is locked can also help an attacker to enumerate usernames. 

## :large_blue_circle: Steps

1. With Burp running, investigate the login page and submit an invalid username and password. Send the POST /login request to Burp Intruder.

2. Select Cluster bomb attack from the attack type drop-down menu. Add a payload position to the username parameter. Add a blank payload position to the end of the request body by clicking Add §. The result should look something like this: username=§invalid-username§&password=example§§

3. In the Payloads side panel, add the list of usernames for the first payload position. For the second payload position, select the Null payloads type and choose the option to generate 5 payloads. This will effectively cause each username to be repeated 5 times. Start the attack.

4. In the results, notice that the responses for one of the usernames were longer than responses when using other usernames. Study the response more closely and notice that it contains a different error message: You have made too many incorrect login attempts. Make a note of this username.

5. Create a new Burp Intruder attack on the POST /login request, but this time select Sniper attack from the attack type drop-down menu. Set the username parameter to the username that you just identified and add a payload position to the password parameter.

6. Add the list of passwords to the payload set and create a grep extraction rule for the error message. Start the attack.

7. In the results, look at the grep extract column. Notice that there are a couple of different error messages, but one of the responses did not contain any error message. Make a note of this password.

8. Wait for a minute to allow the account lock to reset. Log in using the username and password that you identified and access the user account page to solve the lab.