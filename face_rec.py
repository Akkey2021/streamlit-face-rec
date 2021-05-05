import streamlit as st
from PIL import Image
import requests
from PIL import ImageDraw
import io

subscription_key="98c0050da5aa48408a43ff9d91076155"
assert subscription_key
face_api_url = 'https://20210503ak-python.cognitiveservices.azure.com/face/v1.0/detect'

st.title("Face Rcognition App")
uploaded_file=st.file_uploader("choose an image…", type="jpg")
if uploaded_file is not None:
    #uploaded_fileが入っていたら、、、という意味のIf文
    img = Image.open("people.jpg")
    with io.BytesIO() as output:
        img.save(output, format='JPEG')
        binary_img=output.getvalue() #バイナリの取得

    headers = {
    'Content-Type':'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
    'returnFaceId': 'true',
    'returnFaceAttributes':'age,gender,emotion,smile,hair'
    }

    res = requests.post(face_api_url, params=params,headers=headers, data=binary_img)


    results= res.json()

    for result in results:
        rect=result['faceRectangle']

        draw = ImageDraw.Draw(img)
        draw.rectangle(
            [
                rect['left'],rect['top'],
                rect['left']+rect['width'],rect['top']+rect['height'] #rectangleは左上と右下の座標だけでOK
            ],fill=None, outline='red', width=5)
        
    st.image(img, caption="uploaded image", use_column_width=True)
