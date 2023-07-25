# pyqt-image-to-text
PyQt GUI example of image to text using image-to-text model

The model i'm using is <a href="https://huggingface.co/nlpconnect/vit-gpt2-image-captioning">nlpconnect/vit-gpt2-image-captioning</a> from huggingface.

This is for saving image files' name based on its image.

## Requirements
* PyQt5 >= 5.14
* transformers

## How to Install
1. git clone ~ 
2. cd pyqt-image-to-text
3. python setup.py install
4. pip install -r requirements.txt
5. cd pyqt_image_to_text
6. python main.py

See "How to Use" below 🙂

## How to Use
If you want to use this as CLI version only, see scripts.py and use `saveImage(src, dst)` function.

src can be list of files or one directory. dst is directory you want to save images.

### GUI

![image](https://github.com/yjg30737/pyqt-image-to-text/assets/55078043/f95b5c4a-8217-4b30-bcc8-5f0bfe4597cb)
Press "Set Directory" to add image files in list (only one directory per image to text process).

Support png, jpg, jpeg, bmp.

After you've done it, press "Save" button to save files to your desired directory

You can see the result of it.

For example:

<image src="https://github.com/yjg30737/pyqt-image-to-text/assets/55078043/83c3e721-ea80-430e-ae8d-54021b5886a4" width="200" height="300"/>

This image is converted into text as:

```
a tv sitting on top of a stand in a room
```

Based on the text, file will be saved to dst folder named "a_tv_sitting_on_top_of_a_stand_in_a_room".

Example image files which i was using to test are inside each src and dst, you can compare with each other :)

## Troubleshooting
If you encounter any error, check this out:
* transformers is not recent version
* required modules to transformers are not recent version or not be installed (such as sentencepiece, safetensors)
* if it is related to scikit-learn, try reinstall sckit-learn. make sure previous versions of it are all deleted

## See Also
I'm working on a lot of AI-related project.
* <a href="https://github.com/yjg30737/pyqt-openai">pyqt-openai</a> - pyqt implementation of chatgpt 
* <a href="https://github.com/yjg30737/pyqt-dreamstudio.git">pyqt-dreamstudio</a> - using stable diffusion in pyqt desktop app
