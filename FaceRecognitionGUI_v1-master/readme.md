# Face Recognition ft _WxPython_
I have used the image reconition that i learned from Coursera - Convolutional Networks and a Wxpython interface to make it more intuitive.
In this model of face recognition inception network model is used. The network architecture follows the Inception model from [Szegedy *et al.*](https://arxiv.org/abs/1409.4842). 
This face recogntion is also inspired from from [FaceNet](https://arxiv.org/pdf/1503.03832.pdf)

I have added a interface using WxPython. 


<img src="images/img1.png">

* Make sure to install all the libraries as required. Additionally install autocrop for cropping facial pics.
* For testing or training new images you need a 96x96 image
* I have used [Autocrop](https://pypi.org/project/autocrop/). It automatically identifies face in an image and crops it to custom size.I have used it in the Notebook (ln 11). 
    * First place image that you want to crop into images/pics directory
    * Run _ln 11_ or open your prompt, go to your env and run the command
    * If pics are detected then it crops the images and puts it into _crop_ folder else unidentified images are put in *rejected* folder
    * Note that images that have filters cannot be used to detect faces.
    
 * I have kept 3 entities in database but you can add more in the run time.
 
 
 ## Future Works
 * Connect the application with a database
 * Have more funtionality
 * Use better cropping techniques
 * Make it a standalone application 
