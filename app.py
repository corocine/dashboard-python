import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---

st.sidebar.markdown("<h1 style='text-align: center;'>🔍 Filtros</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")
# Filtro de Ano
st.sidebar.subheader("📅 Ano")
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("", anos_disponiveis, default=anos_disponiveis)
st.sidebar.markdown("---")

# Filtro de Senioridade
st.sidebar.subheader("⭐ Senioridade")
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("", senioridades_disponiveis, default=senioridades_disponiveis)
st.sidebar.markdown("---")


# Filtro por Tipo de Contrato
st.sidebar.subheader("📄 Tipo de Contrato")
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("", contratos_disponiveis, default=contratos_disponiveis)
st.sidebar.markdown("---")

# Filtro por Tamanho da Empresa
st.sidebar.subheader("🏢 Tamanho da Empresa")
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Filtragem do DataFrame ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("📊️ Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", f"${salario_medio:,.0f}")
    col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
    col3.metric("Total de registros", f"{total_registros:,}")
    col4.metric("Cargo mais frequente", cargo_mais_frequente)
else:
    st.warning("Nenhum dado selecionado com os filtros. Por favor, ajuste suas seleções.")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", "$0")
    col2.metric("Salário máximo", "$0")
    col3.metric("Total de registros", "0")
    col4.metric("Cargo mais frequente", "N/A")

st.markdown("---")

# --- Análises Visuais com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Ranking de cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        
        grafico_cargos.update_traces(
            hovertemplate=(
                '<b>Média salarial anual (USD)</b>: %{x}<br>'
                '<b>Cargo</b>: %{y}<br>'
            )
        )
        grafico_cargos.update_layout(
            title_x=0.1,
            yaxis={'categoryorder':'total ascending',
                   'tickfont': dict(
                    size=15, 
                )},
            
            title=dict(
                font=dict(size=20)
            )
            )
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")
with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ' '},
            
        )
        
        grafico_hist.update_traces(
            hovertemplate=(
                '<b>Faixa Salarial (USD)</b>: %{x}<br>'
                '<b>Contagem</b>: %{y}<br>'
            )
        )

        grafico_hist.update_layout(
            title_x=0.1,
            title=dict(
                font=dict(size=20)
            ))
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5  
        )
        grafico_remoto.update_traces(
            hovertemplate=(
                '<b>Tipo</b>: %{label}<br>'
                '<b>Quantidade</b>: %{value}<br>'
                '<b>Porcentagem</b>: %{percent}<br>'
            )
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(
            title_x=0.1,
            title=dict(
                font=dict(size=20)
            ))
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_traces(
            hovertemplate=(
                '<b>País</b>: %{location}<br>'
                '<b>Salário Médio (USD)</b>: %{z:,.0f}<br>'
            )
            )
        grafico_paises.update_layout(
            title_x=0.1,
            title=dict(
                font=dict(size=20)
            ))
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")
        
st.markdown("---")

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
if not df_filtrado.empty:
    st.dataframe(df_filtrado)
else:
    st.warning("Não há dados para exibir na tabela com os filtros atuais.")
