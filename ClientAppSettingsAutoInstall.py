import os
from time import sleep
user = os.getlogin() 
path = (f'C:/Users\{user}/AppData/Local/Roblox/Versions')
pathfound=False
alrexist=False
list1 = os.listdir(path)
for file1 in list1:
    if file1 == "RobloxStudioLauncherBeta.exe":
        pass
    else:

     list2 = os.listdir(f'C:/Users/{user}/AppData/Local/Roblox/Versions/{file1}')
     for x in list2:
         if x == "RobloxPlayerBeta.exe": 
             l = (f'C:/Users/{user}/AppData/Local/Roblox/Versions/{file1}')
             path=l
             print(l)
             pathfound=True
print(path)
if pathfound == True:
   
    y = os.listdir(path)
    for o in y:
        if o == "ClientSettings":
            
            alrexist=True
            break
        else:
            pass

if alrexist == True:
    print("Clientsettings already exists")
else:
    folder="ClientSettings"
    mode=0o666
    s = os.makedirs(f'{path}/ClientSettings',mode)
    zpath = (f'{path}/ClientSettings')
    sleep(1)
    json = open(f'{zpath}/ClientAppSettings.json',"w+")
    data=['{ \n','  "DFIntTaskSchedulerTargetFps": 1000, \n', '  "FFlagHandleAltEnterFullscreenManually":"False" \n', '}']
    json.writelines(data)
    json.close()
print("DONE!")
k = input("press enter to exit prompt")
