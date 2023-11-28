import streamlit as st
import os
import random
import pandas as pd
import time

# 从txt中读取餐厅列表
def read_restaurant():
    path = os.path.dirname(__file__)
    restaurant_file = path + '/pages/restaurant.txt'
    with open(restaurant_file, 'r', encoding='utf-8') as file:
        restaurant = [line.strip() for line in file.readlines()]
    return restaurant

def random_select():
    rand = st.button('随机选一个吧老登!🖕🏻')

    random_number = 0
    if rand:
        random_number = random.randint(1, len(restaurant) - 1)
        progress_bar()
        st.success("🏓决定就是你了！\n" + restaurant[random_number])# 出来结果吧老登！
        
    # st.write(restaurant[random_number])

def make_list_to_df(restaurant):
    df = pd.DataFrame(
        {
            "🖕🏻这都是你们选的b餐厅嗷" : restaurant[1:] #为了不显示第一个空的占位
        }
    )
    return df

def restaurant_list(restaurant):
    res_df = make_list_to_df(restaurant)

    st.data_editor(
    res_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
        hide_index=False,
    )

def progress_bar():
    progress_text = "👴🏻正给你选着呢..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

if __name__ == '__main__':
    st.write("""
    ### 吃啥         
    """)

    restaurant = read_restaurant()
    restaurant_list(restaurant)
    

    random_select()
    
    
    
    