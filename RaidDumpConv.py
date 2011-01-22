import sys
import wx

IN_FILE="raiddump.txt"
OUT_FILE="fakeraiddump.txt"
RACE="FakeRace"
GUILD="Eternal Sovereign"
ZONE="raiddump"


app = wx.PySimpleApp()
dialog = wx.FileDialog(None, "Select the file you wish to convert: ")
if dialog.ShowModal() == wx.ID_OK:
    IN_FILE = dialog.GetPath()
else:
    dialog.Destroy()
    sys.exit(1)
dialog.Destroy()

dialog = wx.FileDialog(None, "Select the file to output to: ")
if dialog.ShowModal() == wx.ID_OK:
    OUT_FILE = dialog.GetPath()
else:
    dialog.Destroy()
    sys.exit(1)
dialog.Destroy()

print "IN_FILE = %s" % IN_FILE
print "OUT_FILE = %s" % OUT_FILE

try:
    inFile = open(IN_FILE, "rU")
except Exception, err:
    print "Could not open %s for reading: %s" % (IN_FILE, err)
    sys.exit(1)

try:
    outFile = open(OUT_FILE, "w")
except:
    print "Could not open %s for writing: %s" (OUT_FILE, err)
    inFile.close()
    sys.exit(1)
    
for row in inFile:
    charInfo = row.split('\t')
    outLine = "[Day Mon 01 00:00:00 2010] [%s %s (%s)] %s (%s) <%s> ZONE: %s\n" % (charInfo[2], charInfo[3], charInfo[3], charInfo[1], RACE, GUILD, ZONE) 
    outFile.write(outLine)

inFile.close()
outFile.close()

sys.exit()