# Análise Exploratória e Limpeza de Dados de Varejo (AED)
> **Módulo 1: Visualização de Dados e Business Intelligence — SCTEC [T3]**  
> **Mini-Projeto Avaliativo — Semana 07**
>
## Objetivo Geral do Projeto
 Este projeto consiste no desenvolvimento de uma **Análise Exploratória de Dados (AED)** e **ETL (Extract, Transform, Load)** aplicado a uma base de dados do setor varejista. O objetivo é verificar a qualidade dos dados brutos, aplicar tratamentos e padronizações utilizando **Python e Pandas**, e extrair dessa base estatísticas descritivas e agrupamentos.

## Ferramentas utilizadas
- **Pyhton (Pandas, csv, re)**
- **VS Code**
- **Git e GitHub**

## Estrutura do Repositório
Miniprojeto_CelinaMachadodeLiz_T3/

- Base Varejo.csv         # Dataset bruto baixado do Kaggle
- df_limpo.csv            # Base tratada exportada após limpeza
- projeto.py              # Script principal com o pipeline de dados
- README.md               # Documentação técnica do projeto

## Instruções de Execução
1. Abra a pasta do projeto no VS Code (ou Google Colab).
2. Certifique-se de que a base original `Base Varejo.csv` está no mesmo diretório.
3. Execute o script Python principal (`miniprojeto1.py`).
4. Os resultados estatísticos e de agrupamento serão exibidos no terminal, e o arquivo `df_limpo.csv` será gerado automaticamente na pasta.

## Reflexão Teórica: ETL e Qualidade de Dados
No cenário de Business Intelligence, o procedimento de ETL (Extração, Transformação e Carga) é a base de qualquer análise. A fase de Transformação, aqui desenvolvida no projeto, é de suma importância para se garantir a Qualidade dos Dados. Bases brutas frequentemente são prejudicadas por ruídos, tais como: nulos, duplicatas, tipagens incorretas(ex.: dados no formato de strings). A falta desse tratamento impacta diretamente a estatística descritiva e a decisão. A proteção da integridade dos dados evita a ocorrência do efeito “ Garbage In , Garbage Out”, garantindo que as ideias extraí das fornecidas à situação real do negócio. 

## Principais Observações e Conclusões
1. **Perfil Familiar dos Clientes:** O estudo revelou que, em média, cada cliente tem 1.15 filhos , e a maioria não possui filhos. A distribuição de filhos dos clientes varia de 0 a 4.
2. **Volume por Gênero:** O agrupamento de dados mostrou que o gênero " feminino" é o mais representado na base de dados com o total de 382.427 compras realizadas
3. **Classificação dos Produtos por Categoria:** A categoria “Alimentos” representa o maior volume de vendas (384.197 produtos vendidos), e é a principal responsável pelo varejo na amostra
4. **Tratamento de Categorias Ocultas:** Não houve informações na coluna de categorias, de modo que foi utilizado, para não perder volume de dados, o termo "Sem Categoria"
5. **Problemas de Inconsistência Que Permanecem Na Base:** Mesmo após a limpeza inicial, podem existir inconsistências ocultas, como características peculiares nos nomes dos produtos ou anomalias nos valores, que exigiriam uma etapa futura de normalização.
