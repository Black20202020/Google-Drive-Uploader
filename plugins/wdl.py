import os
import subprocess

def wget_dl(url):
        try:
            print("بدء التنزيل")
            # i was facing some problem in filename That's Why i did this ,
            #  i will fix it later :(

            filename = os.path.basename(url)
            output = subprocess.check_output("wget '--output-document' '{}' '{}' ".format(filename , url), stderr=subprocess.STDOUT, shell=True)
            
            print("إكتمل التنزيل",filename)
            return filename
        except Exception as e:
            print("خطأ في التنزيل :",e)
           
            return "error",filename
        
# wget_dl(url)
