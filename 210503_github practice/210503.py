import streamlit as st
import pandas as pd
import numpy as np 
import time
import altair as alt

# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# import seaborn as sns
# sns.set()
from PIL import Image

st.title("Akkey")
st.write('practice streamlit')

#メディアの表示可否
if st.checkbox("show nicchan"):
    img = Image.open("IMG_0901.JPG")
    st.image(img, caption="Nicchan", use_column_width=True)

option= st.sidebar.selectbox(
    "あなたが好きな数字は？",
    list(range(1,11))
)
"あなたが好きな数字は",option,"です。"

#st.slider('ラベル', 最小値, 最大値, 初期値, 刻み)
condition = st.sidebar.slider('ラベル', 0, 100, 50, 5)
"あなたの今の調子は", condition,"です。"

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.write('====')

# "Start!"
# latest_iteration=st.empty()
# bar=st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)
# "Done!"



#[command+D]で選択できる

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムの表示")
if button:
    right_column.write("右カラム")


#st.write("自由記述")
text= st.text_input("自由記述　100字以下")
text

# df= pd.read_csv('1.02. Multiple linear regression.csv')
# st.table(df.style.background_gradient(cmap='viridis', low=.5, high=0))


# data=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(data)
# st.area_chart(data)


# data1=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139],
#     columns=['lat', 'lon']
# )
# st.map(data1)

# """
# ```python
# import streamlit as st
# import pandas as pd
# import numpy as np 
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# import seaborn as sns
# sns.set()
# ```
# """