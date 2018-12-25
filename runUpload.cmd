SET PORT=COM4
SET JMENO=filesUpload.txt

dir /b *.py > %JMENO%


FOR /f "delims=/" %%A IN (%JMENO%) DO (
ampy -p %PORT% put %%A %%A )