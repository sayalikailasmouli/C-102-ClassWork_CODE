import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.videoCapture(0)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        startTime=time.time
        result=False
    return img_name
    print("SNAPSHOT HAS BEEN TAKEN")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token="sl.A4nyrhPDh1-99cM-6YIIGY81EiKyDGsCx2abX3HLo30PeymTyxKl_W9JAIluJ_91gPAk1_Gm-SAe3k1-SNG63Ur5W3JSZ442I8mwMfhKk4gU2IwZ0lRk6NDqVlW5NEp66rbu8do"
    file=img_name
    file_from=file
    file_to="/testFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_files(name)
main()