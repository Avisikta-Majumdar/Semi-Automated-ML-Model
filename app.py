import streamlit as st
import pandas as pd 
import numpy as np
from flask import  Flask , render_template,request
import seaborn as sb 
import matplotlib.pyplot as plt 


'''def main():
    st.title("Semi Automatic ML Model")
    st.write(" *--Built using StreamLit--* ")
    activities = ["EDA" , "PLOT", "ABOUT"]
    choice = st.sidebar.radio("Select Activity :" ,activities)
    

    if choice == "EDA":
        st.subheader("--Exploratory Data Analysis--")
        st.write(""" ## *Upload Dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])   
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)
            if st.checkbox("SHOW SHAPE"):
                st.write(df.shape)
            if st.checkbox("SHOW SIZE"):
                st.write(df.size)
            if st.checkbox("SHOW COLUMN "):
                st.write(df.columns)
            if st.checkbox("SELECT COLUMN NAME"):
                select_columns = st.multiselect("Select Column" , df.columns)
                new_df = df[select_columns]
                st.dataframe(new_df)
            if st.checkbox("SHOW MISSING VALUES"):
                st.write(df.isna().sum())
            if st.checkbox("SHOW VALUE COUNTS"):
                column = st.selectbox("Select Columns" , df.columns)
                st.write(df[column].value_counts())
            if st.checkbox("SHOW SUMMARY"):
                st.write(df.describe())


    elif choice == "PLOT":
        st.subheader("--Data Visualization--")
        st.write(""" ## *Upload Dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)

            if st.checkbox("CORRELATION"):
                st.write(sb.heatmap(df.corr() , annot = True))
                st.pyplot()

            if st.checkbox("BAR GRAPH"):
                x_axis = st.selectbox("Select x axis:" , df.columns)
                x_axis = df[x_axis]
                y_axis = st.selectbox("Select y axis:" , df.columns)
                y_axis = df[y_axis]
                st.write(sb.barplot(x_axis , y_axis))
                st.pyplot()
                plt.xticks(rotation = 90)
                plt.legend()
                plt.grid()

            
            if st.checkbox("COUNT PLOT"):
                c = st.selectbox("Select  axis:" , df.columns)
                c_main = df[c]
                st.write(sb.countplot(c_main))
                st.pyplot()
                plt.grid()
                plt.xticks(rotation = 90)
                plt.legend()


            if st.checkbox("PIE CHART"):
                col = st.selectbox("Select 1 column" , df.columns)
                pie = df[col].value_counts().plot.pie(autopct = "%1.1f%%")
                st.write(pie)
                st.pyplot()

            
    else:
        st.subheader("--About Me--")
        st.write(''' ''')
      #  st.write('''# ***Built by Avisikta Majumdar*** ''')
       # st.write(''' #***Linkedin*** : https://www.linkedin.com/in/avisikta-majumdar/ ''')
        #st.write(''' #***Github*** : https://github.com/avisikta-majumdar ''')'''


app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("homepage.html")

@app.route("/data",methods=["GET","POST"])
def data():
    if request.method=="POST":
        f = request.files["csvfile"]
        operation = request.form["operation"]
        if operation=="EDA":
            return render_template("EDA.html")

@app.route("/eda",methods=["GET","POST"])
def eda():
    if request.method == "POST":
        f = request.files["csvfile"]
        data = pd.read_csv(f)
        operation = request.form["operation"]
        shape=data.shape


        if operation == "Shape":
            return render_template("shape.html",row=shape[0],column = shape[1])
        elif operation == "Size":
            res = (shape[0]*shape[1])
            return render_template("size.html",size=(res))
        elif operation=="Columns":
            col = [data.columns]
            return render_template("Columns.html" , colName = col)



       
if __name__ == "__main__":
    app.run(debug=True)
