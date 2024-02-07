'''我的主页'''
import streamlit as st
from PIL import Image
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(b,g,r)
    return img


def page_1():
    a=':blue[名著推荐]'
    st.write(a)


def page_2():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取图片的名称,类型和大小
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
    st.link_button('美图秀秀', 'https://mt.meipai.com/')
    st.image('新海诚.jpg')
    st.image('周星驰.jpg')
def page_3():
    '''我的智慧词典'''
    st.write('我的智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v)+'\n'
            message=message[:-1]
            f.write(message)
            
        st.write('查询次数:',times_dict[n])
    st.write('----')
    st.write('床前明月光，_________.')
    cb1 = st.checkbox('疑是地上霜')
    cb2 = st.checkbox('低头思故乡')
    cb3 = st.checkbox('一览众山小')
    cb4 = st.checkbox('受降城外月如霜')
    l = [cb1]
    if st.button('确认答案'):
        if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
            st.write('好厉害！真实答案就是“疑是地上霜”')
        else:
            st.write('答错了，再好好想想吧”')


    
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        massages_list=f.read().split('\n')
        for i in range(len(massages_list)):
            massages_list[i]=massages_list[i].split('#')
        for i in massages_list:
            if i[1]=='阿短':
                with st.chat_message('🤡'):
                    st.write(i[1],':',i[2])
            elif i[1]=='编程猫':
                with st.chat_message('🤠'):
                    st.write(i[1],':'+i[2])
    name=st.selectbox('我是...',['阿短','编程猫'])
    new_message=st.text_input('想要说的话...')
    if st.button('留言'):
        massages_list.append([str(int(massages_list[-1][0])+1),name,new_message])
        
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=''
            for i in massages_list:
                message += i[0] + '#' + i[1]+'#'+i[2]+'\n'
                print(message)
            message=message[:-1]
            f.write(message)
if page=='我的兴趣推荐':
    page_1()
elif page=='我的图片处理工具':
    page_2()
    
elif page=='我的智慧词典':
    page_3()
elif page=='我的留言区':
    page_4()

