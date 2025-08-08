# 📊 Dashboard de Análise de Salários na Área de Dados

Este projeto é um dashboard interativo desenvolvido com **Streamlit**, **Pandas** e **Plotly Express** para analisar salários na área de dados. Ele foi criado como parte da **Imersão de Dados da Alura**.

A **fonte de dados** inicial é um arquivo CSV fornecido pela Alura. O arquivo `config.py` é responsável por realizar a limpeza, tratamento e preparação inicial desses dados, salvando o resultado em um novo arquivo CSV.

### 🚀 Funcionalidades

O dashboard oferece as seguintes funcionalidades principais, acessíveis através de uma barra lateral interativa e visualizações claras:

1. **Filtros Interativos:** Filtre os dados por **Ano**, **Senioridade**, **Tipo de Contrato** e **Tamanho da Empresa**.
2. **KPIs (Métricas Principais):** Veja rapidamente o **salário médio anual**, **salário máximo anual**, **total de registros** e o **cargo mais frequente**.
3. **Visualizações Gráficas:** Explore diversos gráficos que incluem:
   * **Ranking de cargos por salário médio**
   * **Distribuição de salários anuais**
   * **Proporção dos tipos de trabalho** (presencial, remoto, híbrido)
   * **Salário médio de Cientista de Dados por país** (em um mapa coroplético)
4. **Tabela de Dados Detalhados:** Uma tabela no final da página permite visualizar os dados brutos filtrados em tempo real.

---

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Streamlit:** Framework para a criação da interface do dashboard.
* **Pandas:** Biblioteca para manipulação e análise de dados.
* **Plotly Express:** Biblioteca para visualização de dados interativa.

---

### ⚙️ Como Executar o Projeto

Para rodar este dashboard localmente, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/corocine/dashboard-python.git
   cd dashboard-python
   ```
2. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: `venv\Scripts\activate`
   ```
3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o dashboard:**

   ```
   streamlit run app.py
   ```
5. **O aplicativo será aberto no seu navegador padrão.**

### 📝 Notas do Desenvolvedor

Agradeço à Alura pela Imersão de Dados e pelo material de apoio. Este projeto é um exemplo prático de como transformar dados brutos em insights valiosos usando ferramentas de código aberto.

---

### 📜 Licença

Este projeto está sob a licença [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/).
