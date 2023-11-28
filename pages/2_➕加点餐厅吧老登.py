import streamlit as st
import os
from eat_what import read_restaurant, restaurant_list

def show_textbox():
    st.write("""
    ### 现在又想着加了，删的时候咋妹好好删呢？         
    """)
    
    restaurant = read_restaurant()
    df = restaurant_list(restaurant)
    
    
    txt = st.text_area(
        "餐厅的名儿：",
        placeholder='好好打你那个餐厅的名字，别到时候又要去删'
            )
    
    #st.write(f'You wrote {len(txt)} characters.')
    
    # st.write(txt + " 给你加上了嗷")
    clicked = st.button("真给你加了嗷？", type="primary")
    if txt and clicked:
        write_in_restaurant_txt(txt)
        st.success(txt + " 给你加上了嗷")
        st.error("别一会儿又上左边删去")
        st.rerun()

def write_in_restaurant_txt(txt):
    path = os.path.dirname(__file__)
    file = path + '/restaurant.txt'
    with open(file, 'a',encoding='utf-8') as file:
    
    # 将数据写入文件
        file.write('\n' + txt)

if __name__ == '__main__':
    show_textbox()