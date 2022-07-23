# 导入相关模块
import pymongo
import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.signal import argrelextrema
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Gearbench digitai visualization",
    layout="wide")


# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['IRCdatabase']
table = db['IRB1210axis2_03_endurance']
#'''读取txt'''
# dt=pd.read_csv('1#-1118h_20211221.txt',skiprows=13,index_col=None,sep='\t')
# data=pd.DataFrame(dt)
# t=data['%Time_s']
# speed=data['GB_IRB1210_ax2__6464__1']
# position=data['GB_IRB1210_ax2__1717__1']
# torque=data['GB_IRB1210_ax2__4947__1']

# 读取mongodb数据库数据
# data = pd.DataFrame(list(table.find())).drop(['_id'],axis=1)
data = pd.DataFrame(list(table.find()))

# print(data)
# 选择需要显示的字段
# data = data[['Time', 'GB_IRB1210_ax2__speed__1','GB_IRB1210_ax2__position__1','GB_IRB1210_ax2__torque__1']]
# dataid=data['_id'].astype(float)
t=data['Time'].astype(float)
speed=data['GB_IRB1210_ax2__speed__1'].astype(float)
torque=data['GB_IRB1210_ax2__torque_ref__1'].astype(float)

st.sidebar.selectbox('select bench',('1210axis2-1','1210axis2-2','1210axis2-3'))
st.sidebar.radio('select number',('1#','2#','3#','4#'))

fig1=px.line(data_frame=None, x=t,y=speed)
fig2=px.line(data_frame=None, x=t,y=torque)


left_column,right_column=st.columns(2)
left_column.plotly_chart(fig1,use_container_width=True)
right_column.plotly_chart(fig2,use_container_width=True)

# 隐藏streamlit默认格式信息
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <![]()yle>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)









# # 打印输出
# print(dataid)
# plt.figure(figsize=(12,8))
# plt.subplot(2,1,1)
# plt.plot(t,speed)
# plt.subplot(2,1,2)
# plt.plot(t,torque)
# plt.show()


#'''读取mongodb数据库方法二'''
# cursor = table.find()
# columns = []
# data_list = []
# for data in cursor:
#     if len(columns) == 0:
#         columns = list(data)
#         # print(columns)
#         columns.remove('_id')
#     row_data = []
#     for column in columns:
#         row_data.append(float(data[column]))
#     # print(list(row_data))
#     data_list.append(row_data)
# datafr = pd.DataFrame(list(data_list))
# client.close()
#
# plt.figure(figsize=(12,8))
# plt.subplot(3,1,1)
# plt.plot(datafr[0],datafr[1])
# plt.subplot(3,1,2)
# plt.plot(datafr[0],datafr[2])
# plt.subplot(3,1,3)
#
# plt.plot(datafr[0],datafr[3])
# plt.show()