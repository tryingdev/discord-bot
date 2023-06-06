Dim iURL 
Dim objShell


set objShell = CreateObject("Shell.Application")
set wshshell = wscript.createobject("Wscript.shell")
objShell.ShellExecute "msedge.exe"

wscript.sleep 2000
wshshell.SendKeys "%f"
wscript.sleep 2000
wshshell.SendKeys "c"
wscript.sleep 2000
wshshell.SendKeys "c"
wscript.sleep 2000
wshshell.SendKeys "{ENTER}"
wscript.sleep 2000
wshshell.SendKeys "Compatibilidade do Internet Explorer"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{tab}"
wscript.sleep 2000
wshshell.SendKeys "{enter}"
wshshell.SendKeys "http://srvad-01/ev"
wscript.sleep 2000
wshshell.SendKeys "{ENTER}"
wscript.sleep 2000
wshshell.SendKeys "%{f4}"
wscript.sleep 2000


