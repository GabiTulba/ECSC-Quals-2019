# Unusual Communication (200 points / 25 solves)
## Problem statement:

>A network administrator made a screenshot of the password from a CISCO router from a client. He must send this screenshot to a colleague who is in a remote location. Unfortunately, the network to which it is connected does not allow it to send emails. Eventually he managed to find a way. Can you find the password from the captured traffic?

## The problem:

This pcap had some ICMP ping packets. The loads sent through those packets was a PNG (the flag PNG), the PNG contained the password which was the flag encrypted with CISCO password 7. I used an OCR tool to extract the text from the image and then an decoder site from the web.

Flag: **ECSC{5d0d4436ad7e07d5375948ad13746fe2987aa7fd7126dfdd47acedf89905a0a4}**

