


# Import the required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


def axis_inputs(Open,High,Low,AdjClose,Volume):
    prediction1=model.predict([[Open,High,Low,AdjClose,Volume]])
    print(prediction1)
    return prediction1


comp=st.sidebar.selectbox("Company",["Axis","ITI","IIFL","LIC","Mahindra","Union"])
nav=st.sidebar.radio("Menu",["Home","Predictor","Graph Section","FAQ"])

if comp=="Axis":
    model = tf.keras.models.load_model("C:\\Users\\User\\Desktop\\Mutual_Funds\\Axis_Mutual_Funds.h5")
    data = pd.read_csv("C:\\Users\\User\\Desktop\\Mutual_Funds\\AXISNIFTY.NS.csv")
    corr_mat = data.corr()

    if nav == "Home":

        st.markdown("Home Page")
        # st.image("logo.jpeg", width=300)
        st.title("Welcome to Mutual Funds")
        st.header("Your Trusted bank")
        # st.image("kot.jpg", width=500)

        st.markdown("Want to know the Chart visually?")

        if st.button("Yes"):
            st.line_chart(data)
        elif st.button("No"):
            st.header("Know Our Growth History Below!")

        if st.checkbox("Wanna see our complete dataset?"):
            st.write(data)

        if st.button("Want To know the Growth History Column Wise?"):
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2,
                                                         ncols=2,
                                                         figsize=(10, 5))
            ax1.bar(data['High'],data['Close'])
            ax2.scatter(data['Low'],data['Close'])
            ax3.plot(data["Volume"],data['Close'])
            ax4.scatter(data['Adj Close'],data['Close'])
            st.pyplot(fig)

    if nav == "Predictor":

        if st.checkbox("Mutual Funds Predictor Inputs"):
            st.write("1. Low = Takes Low price of the fund till date")
            st.write("2. Volume = Amount of the fund")
            st.write("3. AdjClose = Adjacent Closing price of the data")
            st.write("4. Open=Opening price of the data")
            st.write("5. High=Highest price of the day")

        st.title("Welcome To Kotak Predictor!!")
        Open = st.number_input("Enter the Previous Close Price", 27.00, 2040.00, step=40.0)
        High = st.number_input("Enter the Low Price", 27.00, 2000.00, step=40.0)
        Low = st.number_input("Enter VWAP", 27.00, 2038.00, step=40.0)
        AdjClose= st.number_input("Enter the Volume", 40.00, 3000.00, step=200.0)
        Volume = st.number_input("Enter Deliverable Volume", 40.0, 3000.0, step=200.0)

        result = ""

        if st.button("Predict"):
            result = axis_inputs(Open,High,Low,AdjClose,Volume)
        st.success(f"Your Predicted Price is : {result}")



    if nav=="Graph Section":
        st.title("Welcome to Mutula Funds Graph mate")

        graph = st.selectbox("What Kind Of Graph?",
                             ["None", "Adjacent Close Price Vs Close Price", "Highest Price Vs Close Price",
                              "Volume Vs Close Price", "Analyze The Complete data at one go", "Mutual Funds Classic"])

        if graph == "Adjacent Close Price Vs Close Price":
            sns.set_style("darkgrid")
            prevclo = sns.relplot(data=data, x='Adj Close', y='Close')
            st.pyplot(prevclo)

        if graph == "Highest Price Vs Close Price":
            sns.set_style("darkgrid")
            higclo = sns.relplot(data=data, x='High', y='Close')
            st.pyplot(higclo)
        if graph == "Volume Vs Close Price":
            sns.set_style("darkgrid")
            volvsclo = sns.relplot(data=data, x='Volume', y='Close')
            st.pyplot(volvsclo)
        if graph == "Analyze The Complete data at one go":
            # fig,ax=plt.subplots(figsize=(20,20))
            analyzer = sns.pairplot(corr_mat)
            st.pyplot(analyzer)
            analyzer.fig.set_size_inches(20, 20)

        if graph == "Mutual Funds Classic":
            plt.style.use('dark_background')
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.scatter(data['Low'], data['High'], c=data['Close'], cmap='winter')
            ax.set(title="Data Analyzer",
                   xlabel="Low",
                   ylabel="High")
            ax.legend()
            ax.axhline(data['High'].mean(),
                       linestyle='--',
                       c='green')
            st.pyplot(fig)
    if nav=='FAQ':
        st.title("Welocme To Mutual Funds FAQ section")
        st.header("FAQ")
        if st.button("Is Mutual Funds Safe?"):
            st.write("Now Mutual Funds is Predicting the closing prices on the previous old data sets "
                     "So, it isn't predicting the accurate closing prices of the company.Which may also "
                     "make The user fall into loss or in Profit there is no surrity "
                     "As soon as we start getting the live or original data from the companies we ",
                     "asure that Mutual Funds Predictor will lift you upp with profit")

        if st.button("Is Mutual Funds recommended for real life investment purposes?"):
            st.write("No,As Mutual Funds has no original data available with them so it is not at all recomended "
                     "for real life predictions.But,Mutual Funds definitely helps to maske user learn "
                     "What are Predictions? "
                     "How it works "
                     "Necessity in Real Life "
                     "And Much More")

        if st.button("What is the target/ambition of Mutual Funds Price Predictor?"):

            st.write("Mutual Funds Predictor is an Indian web application. "
                     "Which wants it's every citizen to be good financially good. "
                     "Though Mutual Funds Predictor is not predicting on the real data. "
                     "But Mutual Funds predictor assures that everyone can understand the importance and use of Mutual Funds Predictor")

        if st.button("Why should you consider investing in Mutual Funds?"):

            st.header("1. It’s easy")
            st.write("Investing in Mutual Funds has never been so easy."
                     "Now you can invest from the comfort of your homes." 
                     "All you need is a smartphone and you are good to go.")

            st.header( "2. Power of compounding")
            st.write("If you let your investments stay for a long time and let the "
                     " interests compound, you will reap good results and will get one of the best benefits of investing in Mutual Funds.")
            st.header("3. Win the race against inflation ")
            st.write("The interests in conventional bank system at times are close to the inflation rates"
                     "leaving you with little or no profit at all in the long term.  investment returns can "
                     "fetch you double-digit inflation returns if done intelligently and help you reach the"
                     "corpus you desire in a relatively shorter time frame.")
            st.header("5. The powerful long term investment ")
            st.write("Bajaj Finance, a non-banking finance company, between December 2009 and December "
                     "2019 gave a whopping 13,000% returns in its Mutual Funds. However, this does not mean that"
                     "every investment can yield returns so high but it will certainly serve as a great tool to "
                     "multiply your money to the best extent possible")



