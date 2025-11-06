
import streamlit as st
import pandas as pd


st.title('Motos')
st.sidebar.title("Aluguel de Motos")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha a moto ideal para você!")
Motos = ["Xre300", "G310", "S1000", "CG160"]
opcao = st.sidebar.selectbox('Escolha a moto que foi alugado', motos)

st.title('Rdx Motos - Aluguel de Motos') 

st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo: {opcao}')


dias = st.text_input(f'por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

### copia daqui pra frente --- Define a diária
if opcao == 'XRE300':
    diaria = 450

elif opcao == 'G310':
    diaria = 500

elif opcao == 'S1000':
    diaria = 250

elif opcao == 'CG160':
    diaria = 650

### calcular 

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km *0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Voce alugou o {opcao} por {dias} dias e rodou {km}km. valor total a pagar é R${aluguel_total:.2f}')