import streamlit as st
import os

def show_textbox():
    txt = st.text_area(
        "餐厅的名儿：",
        
            )

    #st.write(f'You wrote {len(txt)} characters.')
    
    # st.write(txt + " 给你加上了嗷")
    
    if txt:
        write_in_restaurant_txt(txt)
        st.success(txt + " 给你加上了嗷")

def write_in_restaurant_txt(txt):
    path = os.path.dirname(__file__)
    file = path + '/restaurant.txt'
    with open(file, 'a',encoding='utf-8') as file:
    
    # 将数据写入文件
        file.write('\n' + txt)

if __name__ == '__main__':
    show_textbox()