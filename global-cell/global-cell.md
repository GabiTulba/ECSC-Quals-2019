# global-cell (300 points / 30 solves)
## Problem statement:

>You have the following pcap. In order to complete this challenge you need to find a message that leaks a location. You also have to map the leaked info to coordinates. <br>
>The validation flag is ECSC{SHA256(the area code of the town.(numbers only))} <br>
## My opinion:

In this task we were given a pcap with some GSM packets and we needed to find the location of a phone, I didn't really use Wireshark for anything else than looking at the what packets it contains.

## The problem:

The pcap had quite a lot of packets and quite varied, the problem statement was a huge help and pretty much told me that I had to look only for the GSM ones, so I closed wireshark and then used the command `strings challenge.pcapng | grep "GSM"` and got a lot of junk, so I googled `gsm phone coordinates` and found a [site](https://cellidfinder.com/) that asked for a `MCC` a `MNC` a `LAC` and a `CID` or `Cell ID` so I "greped" again for `MCC` and got the following result `MCC: 208, MNC: 20, LAC: 22510, Cell ID: 1106`. Putting those into the site I found got me the location of a location named Lanton in France, so I just had to [google](https://www.codes-postaux.org/uk/zip-code-33138.htm) the area code and find it was `33229` then calculate it's hash.<br><br> 

Flag: **ECSC{bab4d1bdea5baf2a5ce69c2fd7e4945edd39970bc0eb49ea390d58a7d24c3986}**

