SET PORT=COM4
SET JMENO=filesDownload.txt

ampy -p %PORT% ls > %JMENO%

FOR /f "delims=/" %%A IN (%JMENO%) DO (
ampy -p %PORT% get %%A %%A )