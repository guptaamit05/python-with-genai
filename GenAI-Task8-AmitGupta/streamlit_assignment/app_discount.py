import streamlit as st


st.title("Price Calculator App")

product_price = st.number_input("Product Price", min_value=0, step=5)
discount = st.slider("Discount %", 0, 50, 5, step=1)
if st.button("Calculate") :
    try:

        if product_price <= 0 :
            raise ValueError("Product price should not be zero or less than zero")

        final_price = product_price - (product_price * ( discount/100))
        data = [
            {
                "Before Price":product_price,
                "After Discount Price": f"{final_price:.2f}"
            }
        ]
        st.table(data)
        st.success(f"Final Price {final_price:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
