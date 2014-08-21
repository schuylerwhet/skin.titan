import xbmcplugin
import xbmcgui
import shutil

currentVersion = xbmc.getInfoLabel("System.AddonVersion(skin.titan)")
previousVersion = xbmc.getInfoLabel("Skin.String(LastKnownVersion)")

print('[Titanskin] currentVersion: ' + currentVersion)
print('[Titanskin] previousVersion: ' + previousVersion)

if currentVersion != previousVersion:

    fileName = str(xbmc.translatePath("special://skin/1080i/")) + "IncludesHomeMenuItems.xml"
    
    backuppath = str(xbmc.translatePath("special://userdata/addon_data/skin.titan"))
    fileName_backup =  backuppath + "/IncludesHomeMenuItems.xml"
    
    if os.path.isfile(fileName_backup):
        shutil.copy(fileName_backup, fileName)
        print('[Titanskin] backup of home items is restored!')
        
    xbmc.executebuiltin('Skin.SetString(LastKnownVersion,' + currentVersion + ')')    
    xbmc.executebuiltin('xbmc.ReloadSkin')
    
else:
    print('[Titanskin] no action needed')
