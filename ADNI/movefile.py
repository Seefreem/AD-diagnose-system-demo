#  --*--  encoding:utf-8 --*--
import os  
import shutil
#get data's full name
def listdir(path = r'H:\graduation project\datafile\batch\result'):  
    #path在这里默认是 H:\graduation project\datafile\simulatingfile\sourcedata
    #所有的待处理的数据都在该文件夹下面
    #文件名= path + '\\' + File[i] + '\\mri\\' + 'mwp1*.nii'
     
    Files = os.listdir(path)
    #print('number :', len(Files))
    Fullname = []
    Pathlist = []
    for f in Files:
        path2 = path + '\\' + f 
        Pathlist.append(path2)
        Files2 = os.listdir(path2)
        for name in Files2:
            if name.startswith('s4s8'):
                path3 = path2 + '\\' + name
                Fullname.append(path3)
                print(path3)
    #well done.
    return Fullname, Pathlist

Fullname, Pathlist = listdir()


#remove 
for fn in Fullname:
    os.remove(fn)  


# #move
# for fn in Fullname:
#     fnlist = fn.split('\\')
#     srcname = fn
#     trgname = r'H:\graduation project\datafile\batch\result'+'\\'+ fnlist[5]+'\\'+ fnlist[7];
#     #copy
#     print(trgname)
# #     if not os.path.exists(trgname):
# #             os.makedirs(trgname) 
# #     shutil.copyfile(srcname,trgname)  
#     shutil.move(srcname,trgname) 
#     pass
