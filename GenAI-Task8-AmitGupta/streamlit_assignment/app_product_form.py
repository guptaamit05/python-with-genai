import streamlit as st

st.sidebar.title("Product Form")
product = st.sidebar.text_input("enter product name")
category = st.sidebar.selectbox(label="select category", options=["car", "mobile", "laptop", "watch", "bracelet", "perfume"])
price = st.sidebar.number_input("enter price", min_value=0)
btn = st.sidebar.button("Add Product")

if btn:
    try:
        product = product.strip()
        if not product:
            raise ValueError("Product name is required")

        if product.isdigit():
            raise ValueError("Product name should contain text, not only numbers")
        data = [{
            "Product Name":product,
            "Price": price,
            "Category":category,
        }]
        st.sidebar.success("Product Added successfully!")
        st.sidebar.table(data)
    except Exception as e:
        st.sidebar.error(f"Error: {e}")