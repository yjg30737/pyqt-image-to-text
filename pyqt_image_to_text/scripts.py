# pip install sentencepiece
# pip install safetensors

import os
import shutil

### In case of you want to use this script only ###
# don't have dst, this function will not handle it,
# so make it sure that you execute this before:
# os.makedirs(dst)

def saveImage(src, dst):
    image_to_text = ''
    filenames = []
    if os.path.isdir(src):
        from transformers import pipeline

        image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), src)

        filenames = [os.path.join(directory, filename) for filename in os.listdir(directory)
                     if os.path.splitext(filename)[-1] in ['.png', '.jpg', 'jpeg', 'bmp']]
    else:
        if isinstance(src, list):
            from transformers import pipeline

            image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

            filenames = src

    if image_to_text:
        filenames_dict = dict()
        for first_filename in filenames:
            second_filename = image_to_text(first_filename)[0].get('generated_text', first_filename)
            second_filename = '_'.join(second_filename.split(' ')) + os.path.splitext(first_filename)[-1]
            filenames_dict[first_filename] = second_filename

        for f, s in filenames_dict.items():
            shutil.copy(f, os.path.join(dst, s))