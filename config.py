import pandas as pd
# from variables import seniority_translated, columns_translated, contract_translated, company_size_translated, contract_type

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

columns_translated = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

seniority_translated = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

contract_translated = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}

company_size_translated = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'
}

contract_type = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
# Renomeações
df.rename(columns=columns_translated, inplace=True) # Renomear colunas com rename

df['senioridade'] = df['senioridade'].replace(seniority_translated) # Renomear campos com replace

df['contrato'] = df['contrato'].replace(contract_translated)

df['tamanho_empresa'] = df['tamanho_empresa'].replace(company_size_translated)

df['remoto'] = df['remoto'].replace(contract_type)

# print(df.describe(include=['object'])) # análise de dados com texto ou categórico.

print(df.isnull().sum()) # descobrir onde existem campos nulos
print(df[df.isnull().any(axis=1)]) 
# print(df['ano'].unique()) # descobrir quais valores existem no campo 

print(df[df.isnull().any(axis=1)]) # Exibir as linhas que contenham valores nulos

df_clean = df.dropna() # remover valores nulos
print(df_clean[df_clean.isnull().any(axis=1)]) 
print(df_clean.isnull().sum())
df_clean = df_clean.assign(ano=df_clean['ano'].astype('Int64'))
print(df_clean.head())

df_clean.to_csv('dados-imersao.csv', index=False)

# if __name__ == '__config__':
#         print(df_clean.head())

