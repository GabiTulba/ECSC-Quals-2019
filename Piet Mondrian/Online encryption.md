# Piet Mondrian (100 points / 36 solves)
## Problem statement:

>Piet Mondrian was a Dutch painter and theoretician who is regarded as one of the greatest artists of the 20th century. His paintings might be likened <br>
>to secret programming languages. Can you discover them?

## The problem:

using binwalk on the image that was provided revealed that there were 3 other images inside it. The title was a hit to the `piet` esoterig programming language and the 3 images extracted from the main image were code written in that esolang. Each one of the images printed one part of the flag when the code was executed. 

Flag: **ECSC{e647c19e4fc7838bf764abbdcb0c1f08adca163cdadfb889bee5201fc4397e5d}**

