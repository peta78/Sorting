del .\sort.exe
del .\res.txt
del .\*.png

C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe .\sort.cs /optimize+

.\sort.exe >> .\res.txt

py .\plotit.py uniform
