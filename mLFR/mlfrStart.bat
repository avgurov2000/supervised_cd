@echo off
SETLOCAL ENABLEEXTENSIONS
SET /A MBT=1024*1024-1
SET /A MBT1=MBT/10

:phys
for /f "tokens=2 delims==" %%A in ('wmic computersystem get TotalPhysicalMemory /VALUE') DO CALL :phystot %%A
GOTO :slot

:phystot
  SET MEMPHY=%1
  SET/A MEMPHYMB=%MEMPHY:~0,-1%/MBT1
GOTO :eof

:slot
for /f "tokens=2 delims==" %%A in ('wmic memorychip get Capacity /VALUE') DO CALL :slotot %%A
GOTO :run

:slotot
  SET MEMSLO=%1
  SET/A MEMSLOMB=%MEMSLO:~0,-1%/MBT1
  SET/A MEMTOTIN=MEMTOTIN+MEMSLOMB
GOTO :eof

:run
IF %MEMTOTIN% GTR 1025 (
  java -Xmx1024M -jar mLFR.jar %*
) ELSE IF %MEMTOTIN% GTR 513 (
  java -Xmx512M -jar mLFR.jar %*
) ELSE IF %MEMTOTIN% GTR 257 (
  java -Xmx257M -jar mLFR.jar %*
) ELSE (
  java -jar mLFR.jar %*
)