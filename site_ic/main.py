import streamlit as st

st.markdown("<h1 style='line-height:1.2'>Projeto Iniciação Científica <br>Caio Pereira Neris, UFABC</h1>", unsafe_allow_html=True)

st.write("Esse site tem como objetivo apresentar o trabalho 'Obtenção de uma carteira ótima de investimentos com base em métodos de otimização e aprendizado de máquinas', feito por Caio Pereira Neris. Aluno da UFABC, bolsista do CNPq e orientado pelo professor Dr. Jair Donadelli.")

st.header("Visão geral")

st.write( '''Este trabalho explora, principalmente, a teoria de métodos de otimização de portfólios, com foco no modelo de Black--Litterman, mas também aplica tais métodos no mercado de ações brasileiro. O objetivo principal foi demonstrar, estudar, implementar e avaliar o método, integrando com previsões de visões do investidor geradas por algoritmos de aprendizado de máquina. Os portfólios otimizados pelo método de Black--Litterman,  de Markowitz e a Eficiência Reamostrada são comparados entre si e comparados com o desempenho do índice Ibovespa. Os resultados demonstram que, embora os modelos de aprendizado de máquina apresentem baixo poder preditivo isoladamente, a estrutura do modelo Black--Litterman se mostra robusta. A conclusão evidencia o valor do modelo Black--Litterman como uma ferramenta eficaz para a gestão de carteiras, capaz de agregar valor mesmo em cenários de alta incerteza e com previsões imperfeitas. ''')

footer = """
<style>
    a:link, a:visited {
        color: black;
        text-decoration: none;
        
    }
    a:hover, a:active {
        color: red;
        text-decoration: underline;;
       
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color:  #f9f9f9;
        color: black;
        text-align: center;
        padding: 10px 0;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10rem;
    }
    .footer img {
        max-height: 70px;
        width: 100px;
        padding: auto 10px 10px auto;
    }
    .footer-text {
        flex-grow: 1;
        text-align: center;
        padding: 0 20px;
    }
</style>

<div class="footer">
    <img src="https://www.ufabc.edu.br/images/logo-ufabc-link.png" alt="Imagem Esquerda">
<p> Projeto IC de <a href="https://github.com/Caio-P-Neris/IC_2024" target="_blank"> Caio Pereira Neris 🔗</a></p>
<img src="https://seeklogo.com/images/C/CNPq-logo-0A524884BE-seeklogo.com.png" alt="Imagem Direita">
</div>
"""
st.markdown(footer,unsafe_allow_html=True)