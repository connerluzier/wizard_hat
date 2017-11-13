echo off
@title String Search
@echo off 
setlocal enabledelayedexpansion 
color 0a 
for /l %%i in (1,2,100) do echo Thank you for chosing String_Search! & echo Loading - %%i^% & ping localhost -n 1 >nul & cls 
:MENU

color 0a                                                          
echo PRESS 1, 2, 3 OR 4 to EXIT.				  			  
echo 1 - File List	 	  		  
echo 2 - Search	
echo 3 - About 						  	 
echo 4 - Exit									  

SET /P M=
IF %M%==1 GOTO LIST
IF %M%==2 GOTO SEARCH
IF %M%==3 GOTO ABOUT
IF %M%==4 GOTO EXIT
GOTO MENU
:LIST

dir /b /a-d
@echo off
set cnt=0
for %%A in (*) do set /a cnt+=1
echo ------------------------------
echo File count = %cnt%
echo ------------------------------
PAUSE
cls

GOTO MENU
:SEARCH

set /P search_string= Enter the string you would like to search for:
find "%search_string%" *.txt *.sql *.csv
>> G:\Folder1\Databases\results.txt
PAUSE

GOTO MENU
:ABOUT

echo                                                                
echo copyright Gonz0	                                           
echo This tool is used to search multiple files for a string.     
echo This program was written by Gonz0, do not share without giving credit.         

PAUSE
cls
GOTO MENU