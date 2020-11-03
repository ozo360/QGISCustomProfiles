REM @echo off
SET DIR=%~dp0
call "%DIR%bin\qgis-ltr.bat" ^
--profiles-path "%DIR:~0,-1%" ^
--profile naked ^
--project "%DIR%projects\sample.qgs"
REM @echo on
