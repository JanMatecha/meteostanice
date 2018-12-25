SET PORT=COM4
SET JMENO=soubory.txt

ampy -p %PORT% ls > %JMENO%

FOR /f "delims=/" %%A IN (%JMENO%) DO (
ampy -p %PORT% rm %%A )