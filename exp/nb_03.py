
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/03_fastai_inference.ipynb

def InferenceCapture():
    imgfai = CaptureImage_Fastai()
    r = learn.predict(imgfai)
    return r[0].obj, r