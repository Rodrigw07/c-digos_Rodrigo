import streamlit as st  
st.sidebar.title("Aluguel de Carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")
carros = ["g310", "s1000", "cg160", "xre300"]
opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.title('Rdx car - Aluguel de Carros') 

st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo: {opcao}')


dias = st.text_input(f'por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

### copia daqui pra frente --- Define a diária
if opcao == 'g310':
    diaria = 450

elif opcao == 's1000':
    diaria = 500

elif opcao == 'cg160':
    diaria = 250

elif opcao == 'xre300':
    diaria = 650

### calcular 

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km *0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Voce alugou o {opcao} por {dias} dias e rodou {km}km. valor total a pagar é R${aluguel_total:.2f}')