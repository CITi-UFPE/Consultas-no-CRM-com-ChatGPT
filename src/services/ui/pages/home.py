import streamlit as st

# Configurações globais da página, incluindo o título, ícone do CITi, layout largo e estado inicial da barra lateral
st.set_page_config(
    page_title="CRM de Vendas",
    page_icon="assets/images/Logo.svg",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Colunas para melhorar a visualização e disposição da pagina
col1, col2 = st.columns([0.5,2])

with col1:
    # Exibição da imagem do logo
    import streamlit as st
    from pathlib import Path

    # Pega o caminho do arquivo atual (home.py)
    script_path = Path(__file__).resolve()

    # Navega "para cima" na árvore de diretórios até a pasta raiz do projeto
    # A estrutura é: home.py -> pages -> ui -> services -> src -> RaizDoProjeto
    project_root = script_path.parent.parent.parent.parent.parent

    # Constrói o caminho completo e correto para a imagem
    image_path = project_root / "assets" / "images" / "icon_citi.png"

    # Exibe a imagem usando o caminho absoluto que acabamos de criar
    # É importante converter o objeto 'Path' para string com str()
    st.image(str(image_path))
with col2:
# Uso de HTML para estilizar o alinhamento, espaçamento e tamanho das letras e margens
    st.markdown("<h1 style='text-align: start; text-indent: 25px;'>Interface de consultas do CRM do CITi</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='width: 71%; height: 2px; margin-top: 0px; margin-bottom: 25px;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: start; font-size: 20px; font-weight: 520; margin-bottom: 45px;'>Navegue pelas opções no menu lateral para visualizar as análises e ferramentas disponíveis.</p>", unsafe_allow_html=True)


# Uso do container, junto com markdown para organizar o conteúdo e a formatação (também com HMTL)
with st.container():
    st.markdown("<h2 style='text-align: center;'>Informações Gerais 🔎 </h2>", unsafe_allow_html=True)
    
# Organizar perguntas em colunas para uma visualização mais agradável
    col1, col2 = st.columns(2)
    
    with col1:
    # st.expander para criar uma aba expandível com o título de perguntas e st.write para exibir o conteúdo/resposta 
        with st.expander("Qual a motivação da criação do site?"):
            st.write("""
            A interface foi criada com a finalidade de ser uma ferramenta para centralizar e facilitar o acesso aos dados do CRM de vendas,
            proporcionando uma visualização intuitiva e prática pela equipe de Comercial e Diretoria.
            Por isso, o objetivo principal é auxiliar na tomada de decisões estratégicas e na compreensão do cenário do CRM.
            """)
        
        with st.expander("Como os dados foram obtidos?"):
            st.markdown("""
            Os dados foram extraídos a partir do CRM de Vendas presente no Pipefy e alimentado pela equipe de Comercial. <br>
            Usando a API da plataforma e integrando com o Google Sheets, conseguimos ter uma base de dados que atualiza automaticamente e fornece o conteúdo para essa interface 🤯.
            """, unsafe_allow_html=True)

    with col2:
        with st.expander("Como utilizar o chat da plataforma?"):
            st.write("""
            O chat está disponível na aba 'Chat Consultas', onde você poderá conhecer nosso CITiAssistant e tirar dúvidas sobre diversas informações do CRM de vendas.
            Use com moderação 💚.
            """)
        
        with st.expander("Quem pode acessar esses dados?"):
            st.write("""
            A Interface de Consultas do CRM foi desenvolvida exclusivamente para uso pelo time de Negócios e pela Direx.
                     
                     Pedimos que não compartilhem essas informações.
            """)