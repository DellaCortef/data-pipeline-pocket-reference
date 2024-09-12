import streamlit as st
from contract import Sales
from datetime import datetime, time

# Main function for the frontend
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow")

    # Input fields for data
    seller_email = st.text_input("Email do Vendedor")
    purchase_data = st.date_input("Data da compra", datetime.now())
    purchase_time = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    product_value = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    product_quantity = st.number_input("Quantidade de produtos", min_value=1, step=1)
    product_type = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama 3.0"])

    # Submit button
    if st.button("Salvar"):
        # Combining the selected date and time to create the datetime
        date_time = datetime.combine(purchase_data, purchase_time)

        # importing contract classes
        contract(seller_email, purchase_data, purchase_time, product_value, product_quantity, product_type)

        sale = Sales(
            email = seller_email,
            date_time = date_time,
            product_value = product_value,
            product_quantity = product_quantity,
            product_type = product_type
        )

        # Displaying the data on the screen
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {seller_email}")
        st.write(f"Data e Hora da Compra: {date_time}")
        st.write(f"Valor da Venda: R$ {product_value:.2f}")
        st.write(f"Quantidade de Produtos: {product_quantity}")
        st.write(f"Produto: {product_type}")

if __name__ == "__main__":
    main()