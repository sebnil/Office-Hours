At work I need to fill in my office hours into a website. Sometimes I forget.
By running a python script on login and logoff my office hours are written to a txt file.

How to use:
1. Clone this project to any folder.
2. Run gpedit.msc
3. User Configuration->Windows Settings->Scripts (Logon/Logoff)
4. Logon, Properties, Scripts, Add...
5. Choose logon.bat in repository folder
6. Do the same for logoff but choose logoff.bat

For every logon and logoff an entry should be added to office_hours.txt
Example:
'''
IN  2016-02-19 08:13:12
OUT 2016-02-19 17:17:53
'''