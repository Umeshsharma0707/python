"""Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. If the string length is less than 2, return
instead of the empty string.
o Sample String: w3resource' o
Expected Result: 'w3ce' o Sample
String: 'w3' o Expected Result:
'w3w3' o Sample String: ' w' o
Expected Result: Empty String"""

s1 = "w3resource"
s2 = "w3"
s3 = "w"
result1 = ""
result2= ""
result3 = ""
if len(s1) >= 2:
    result1 = s1[:2] + s1[-2:]
    print(result1)
else:
    print("")

if len(s2) >= 2:
    result2 = s2[:2] + s2[-2:]
    print(result2)
else:
    print("")


if len(s3) >= 2:
    result3 = s3[:2] + s3[-2:]
    print(result3)
else:
    print("")







    
