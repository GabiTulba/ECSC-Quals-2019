# Online encryption (100 points / 49 solves)
## Problem statement:

> This is why you should not trust online encryption for your most awesome secrets.

## The problem:

In this task I messed around with the http packets of the pcap until I found a base64 ecoded string `UlBGUHtxcTU0NXNvczEyc3E2MDhxbm44cDIwMXM1MHM5NXA4NTIwb3JwOXM3NDRuMzU3M28xcXAwb3A1M3ByMDE5NzI2fQ==` that decrypted to `RPFP{qq545sos12sq608qnn8p201s50s95p8520orp9s744n3573o1qp0op53pr019726}` which was the rot13 of the flag. <br><br>

Flag: **ECSC{dd545fbf12fd608daa8c201f50f95c8520bec9f744a3573b1dc0bc53ce019726}**

