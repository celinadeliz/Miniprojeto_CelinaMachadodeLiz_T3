import pandas as pd
import csv
import re

# ==================================================================
#  SPRINT 1 - Importação dos dados
# ==================================================================

# Leitura do arquivo com csv.DictReader com delimitador ponto e vírgula
with open('Base Varejo.csv', mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=';')

    # Guarda todas as linhas do arquivo em lista
    dados_varejo = []

    for linha in leitor_csv:
        dados_varejo.append(linha)

# Verificar os dados
print(dados_varejo[0])

# Passando dados para o Pandas
df = pd.DataFrame(dados_varejo)


# ==================================================================
#  SPRINT 2 - Transformação de Strings, Integer e Float e Datetime
# ==================================================================

# 2.1 Strings
def limpar_texto(texto):
    if pd.isna(texto):
        return texto
    # Manter somente letras, números, e espaços
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', str(texto))
    return texto_limpo.strip().upper()

# Aplicação
df['PR_NOME'] = df['PR_NOME'].apply(limpar_texto)

# 2.2 Integer
def limpar_inteiro(valor):
    if pd.isna(valor) or str(valor).strip() == '':
        return None
        # Manter apenas números para coluna FHL (FILHOS)
    valor_str = re.sub(r'[^\d]', '', str(valor))
    try:
        return int(valor_str)
    except ValueError:
        return None

df['CL_FHL'] = df['CL_FHL'].apply(limpar_inteiro)

# 2.3 Validação da Regra do Número de Compra 
def validar_id_compra(id_compra):
    if pd.isna(id_compra):
        return False
    # Verifica se o CO_ID contém somente números
    if re.match(r'^\d+$', str(id_compra).strip()):
        return True
    return False

# Separa apenas os registros com CO_ID válidos
df_valido = df[df['CO_ID'].apply(validar_id_compra)].copy()
    
# 2.4 Datetime
df_valido['DATA'] = pd.to_datetime(df_valido['DATA'], format='%d/%m/%Y', errors='coerce')

# Visualizar como ficou
print(df_valido.dtypes)

# ==================================================================
#  SPRINT 3 - Limpeza de Nulos e Duplicatas
# ==================================================================

# 3.1 Remoção de Duplicatas
# Justificativa: Registros duplicados aumentam os resultados financeiros e 
# as contagens de clientes. Ocasionando uma análise sem qualidade.
df_limpo = df_valido.drop_duplicates().copy()

# 3.2 Tratando Nulos (if/else)
def preencher_categoria(valor):
    """
    Usa a lógica if/else exigida pela rubrica para preencher 
    categorias vazias com a string padrão.
    """
    if pd.isna(valor) or str(valor).strip() == '':
        return "Sem Categoria"
    else:
        return valor

# Aplicando a função na coluna de Categoria do Produto
df_limpo['PR_CAT'] = df_limpo['PR_CAT'].apply(preencher_categoria)


# 3.3 Tratamento de Nulos Restantes 
# Justificativa: Para a coluna de filhos ('CL_FHL') se o dado estiver nulo,
# preenchemos com 0 assumindo que o cliente não possui filhos,
# evitando assim a exclusão de toda a linha da compra.
df_limpo['CL_FHL'] = df_limpo['CL_FHL'].fillna(0)

# Removendo linhas que por acaso não tenham o nome do produto (nulos críticos)
df_limpo = df_limpo.dropna(subset=['PR_NOME'])


# Visualizando quantos nulos sobraram (espera-se 0 nas colunas tratadas)
print(df_limpo.isnull().sum())

# ==================================================================
#  SPRINT 4 - Estatística Descritiva
# ==================================================================

print("1. Estatísticas: Número de Filhos (CL_FHL)")
# Calculando todos os parâmetros
contagem = df_limpo['CL_FHL'].count() 
media = df_limpo['CL_FHL'].mean()
mediana = df_limpo['CL_FHL'].median() 
desvio_padrao = df_limpo['CL_FHL'].std()
moda = df_limpo['CL_FHL'].mode()[0] # Pega o primeiro valor da moda
minimo = df_limpo['CL_FHL'].min()
maximo = df_limpo['CL_FHL'].max()

print(f"Contagem: {contagem}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}\n")

# ==========================================
print("2. Padrões de Agrupamento")

# Agrupamento 1: Quantidade de compras por Gênero (CL_GENERO)
# Ajuda a entender qual gênero compra mais na base
agrupamento_genero = df_limpo.groupby('CL_GENERO')['CO_ID'].count().reset_index(name='Qtd_Compras')
print("Compras por Gênero:")
print(agrupamento_genero, "\n")

# Agrupamento 2: Quantidade de produtos vendidos por Categoria (PR_CAT)
# Ajuda a entender quais categorias têm mais saída
agrupamento_categoria = df_limpo.groupby('PR_CAT')['PR_ID'].count().reset_index(name='Qtd_Vendida').sort_values(by='Qtd_Vendida', ascending=False)
print("Vendas por Categoria de Produto:")
print(agrupamento_categoria)


# ==========================================
# Exportando a base limpa para CSV
df_limpo.to_csv('df_limpo.csv', index=False)