@echo off
start wscript //e:VBScript Execute("CreateObject(""WScript.Shell"").Run ""pythonw.exe C:\Users\notyo\OneDrive\Desktop\EmailDrafts_Copy\bridge.pyw"", 0, False")
start "" "C:\Users\notyo\OneDrive\Desktop\EmailDrafts_Copy\outreach_portal.html"
exit
