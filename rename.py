import shutil as st
import os
for img in os.listdir("/home/reinaldo/Documentos/PetImages/Dog/"):
    a = img.split(".")[0]
    a=int(a)+12501
    st.move("/home/reinaldo/Documentos/PetImages/Dog/"+img,"/home/reinaldo/Documentos/PetImages/ALLDATA/"+str(a)+".jpg")
