import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_literation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_literation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'done!!!!!'

left_column, right_column = st.beta_columns(2)
botton = left_column.button('右カラムに文字を表示')
if botton:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ２の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ３の回答')



# text = st.text_input('あなたの好きな趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの好きな趣味は', text,'です'
# 'コンディション:', condition


# if st.checkbox('Show Image'):
#     img = Image.open('/Users/kuniya/画像表示アプリ/544332123.959633.jpg')
#     st.image(img, caption='華麗なるガチャピン', use_column_width=True)


