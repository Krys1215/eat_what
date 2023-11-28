import streamlit as st
import pandas as pd
import os
from eat_what import read_restaurant, restaurant_list


if __name__ == '__main__':
    st.write("""
    ### 现在又想着删了，加的时候咋妹好好加呢？         
    """)
    restaurant = read_restaurant()
    df = restaurant_list(restaurant)
    
    selected = st.multiselect(
        '之前不好好加，现在又想删了是吧',
        df,
        placeholder='好好想想选哪个几个删吧你',
    )
    
    # 使用列表推导式
    updated_list =  [item for item in restaurant if item not in selected]
    #st.write(newnew)
    
    clicked = st.button("确认删了嗷？", type="primary")
    if clicked:
        path = os.path.dirname(__file__)
        restaurant_file = path + '/restaurant.txt'
        
        with open(restaurant_file, 'w',encoding='utf-8') as file:
            # file.write('\n')
            file.write('\n'.join(updated_list))
        st.error("行了给你删了，你瞅瞅吧")
        st.rerun()
        

            