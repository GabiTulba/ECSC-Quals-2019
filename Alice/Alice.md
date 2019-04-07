# Alice (e00 points / 45 solves)
## Problem statement:

>To use her e-mail, Alice needs to connect to a mail server. The authentication is unilateral, and works as follows: <br>
>1.	Alice requests access to the server by sending her username. <br>
>2.	The server randomly selects 2 values index1 and index2 (1 <= index1 < index2 <= 64), and challenges Alice with (index1, index2). <br>
>3.	Alice applies SHA256 to her password, keeps the hex characters placed on the positions index1 and index2 unchanged and changes all the other hex characters to a different value. Then, she sends the result to the server. <br>
>4.	The server receives the response, and checks if the received string equals the SHA256 value stored in the database for Alice’s username in exactly two positions: index1 and index2. <br>
>5.	To decrease the chances to obtain access by luck, the server repeats the procedure and sends several requests to Alice before allowing her to access the e-mail. If Alice replies correctly to all challenges, then she is successfully authenticated; if not, Alice is denied access. <br>
>For example: <br>
>•	username: Alice <br>
>•	password: ageneralpassword <br>
>•	SHA256(password) = aad3eda32ce777fa1cb3ca97ac7e1bfdd726053e05e0109b3526a63fed4519b7 <br>
>•	index1 = 5 and index2 = 60 <br>
>•	Valid reply (only hex characters on positions 5 and 60 are unchanged): <br>
>4c77ef3010c2f5c274ebbb0ff5abe001eeb5ce0f944dd1402caaf9ddx475bffe <br>
>•	Invalid reply (hex characters on positions 9 and 57 are also the same): <br>
>4c77ef3020c2f5c274ebbb0ff5abe001eeb5ce0f944dd1402caaf9dde475bffe <br>
>•	Invalid reply (hex character on position 5 is different): <br>
>4c77ff3010c2f5c274ebbb0ff5abe001eeb5ce0f944dd1402caaf9ddx475bffe <br>
>An adversary masquerades the server, and fools Alice to reply to his challenges. You are not given access to the challenges, but you know that the adversary only queried positions from the first half of the hash. You also have all the replies from Alice in Alice_replies.txt, and you know that the adversary found the complete hash. This hash is your flag. <br>

## The problem:

So for this task from the Problem Statement we could understand that each of the first character from the first 32 tehere was only one unique and for the last 32 characters there was only one hexdigit that was not appearing, this is the only way to get a unique hash.

Flag: **TODO**

