import streamlit as st

st.title("Simple Sales Dashboard")
st.write("this is simple sales dashboard, that shows each months sales data.")

sales = {
    "January":1200,
    "February":150,
    "March":900,
    "April":2000,
    "May":1100,
}
months = st.selectbox("Select Month", list(sales.keys()))

st.metric(
    label=f"{months} Sales",
    value=f"${sales[months]:,}"
)
st.bar_chart(sales)

