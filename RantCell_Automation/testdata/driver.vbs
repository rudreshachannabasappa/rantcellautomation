
projectscreenshotpath = "C:\Users\RudreshaC\PycharmProjects\RantCell_Automation\screenshots\"

Dim dtmValue, strDate, strTime
Dim objFSO

'Create the file system object for creating folders
Set objFSO = CreateObject("Scripting.FileSystemObject")

'Get current time in to a variable

dtmValue = Now()

'use date /time part functions to create the folder names as required
'Assuming that you are creating these folders in C:\
strDate = projectscreenshotpath & Month(dtmValue) & "_" & Day(dtmValue) & "_" & Year(dtmValue)
'strDate = Month(dtmValue) & "_" & Day(dtmValue) & "_" & Year(dtmValue)
strTime = strDate & "_" & Hour(dtmValue) & "-" & Minute(dtmValue) & "-" & Second(dtmValue)

msgbox strTime

'msgbox strTime
if objFSO.FolderExists(strTime) Then
Else
'	objFSO.CreateFolder(strTime)
End if

'Create the folders using objFSO
'First check if folders exists and create only they dont exist
'if objFSO.FolderExists(strDate & "_" & strTime) Then
'	if not objFSO.FolderExists(strTime) Then
'		objFSO.CreateFolder(strTime)
'	End If
'Else
'	'Create Top level folder first
'	objFSO.CreateFolder(strDate & "_" & strTime)
'End If 



' oShell.Run "sqlplus -l " & strUserName & "/" & strPassword & "@" & strServiceName & " @" & strFileName, 0, True
Set oShell = CreateObject ("WScript.Shell") 
'oShell.run "cmd.exe pytest -v -s --alluredir=" & chr(34) & strTime &chr(34) &  " C:\Users\RudreshaC\PycharmProjects\RantCell_Automation\testcases",0,True
oShell.run "cmd.exe /c pytest -v -s --alluredir=" & chr(34) & strTime &chr(34) &  " C:\Users\RudreshaC\PycharmProjects\RantCell_Automation\testcases",0,True