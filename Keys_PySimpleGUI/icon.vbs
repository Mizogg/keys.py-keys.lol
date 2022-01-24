Set FSO = CreateObject("Scripting.FileSystemObject")
Set F = FSO.GetFile(Wscript.ScriptFullName)
 
Set WshShell = WScript.CreateObject("WScript.Shell") 
DesktopPath = WshShell.SpecialFolders("Desktop") 
Lnk_Title = "\keys_GUI.lnk" 
Set Shortcut = WshShell.CreateShortcut(DesktopPath&Lnk_Title) 
 
Shortcut.TargetPath = WshShell.ExpandEnvironmentStrings(FSO.GetParentFolderName(F) + "\keys_GUI_Start.bat") 
Shortcut.WorkingDirectory = WshShell.ExpandEnvironmentStrings(FSO.GetParentFolderName(F)) 
Shortcut.IconLocation = FSO.GetParentFolderName(F) + "\miz.ico"
Shortcut.WindowStyle = 1 
 
Shortcut.Save 