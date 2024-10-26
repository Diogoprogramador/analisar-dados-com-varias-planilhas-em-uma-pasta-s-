import pandas as pd
import os
import matplotlib.pyplot as plt

# Caminho da pasta com os arquivos CSV
folder_path = 'vendas'

# Listar todos os arquivos CSV na pasta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Criar listas para armazenar os DataFrames
sales_data = []
returns_data = []

# Loop através dos arquivos CSV e carregar os dados
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # Tente carregar o arquivo como dados de vendas
    try:
        sales_df = pd.read_csv(file_path,
                               usecols=['SKU', 'Produto', 'Quantidade Vendida', 'Primeiro Nome', 'Sobrenome', 'Data',
                                        'Loja', 'Preco Unitario'])
        sales_data.append(sales_df)
    except ValueError:
        print(f"Arquivo {file} não contém os dados de vendas esperados.")

    # Tente carregar o arquivo como dados de devoluções
    try:
        returns_df = pd.read_csv(file_path,
                                 usecols=['SKU', 'Produto', 'Quantidade Devolvida', 'Data', 'Loja', 'Preço Unitário'])
        returns_data.append(returns_df)
    except ValueError:
        print(f"Arquivo {file} não contém os dados de devoluções esperados.")

# Combinar todos os DataFrames de vendas e devoluções
all_sales = pd.concat(sales_data, ignore_index=True)
all_returns = pd.concat(returns_data, ignore_index=True)

# Exibir estatísticas básicas
print(all_sales.describe())
print(all_returns.describe())

# Análise Gráfica - Exemplo: Total de Vendas por Loja
sales_by_store = all_sales.groupby('Loja')['Quantidade Vendida'].sum()
sales_by_store.plot(kind='bar', title='Total de Vendas por Loja')
plt.ylabel('Quantidade Vendida')
plt.xlabel('Loja')
plt.show()

# Análise Gráfica - Exemplo: Total de Devoluções por Produto
returns_by_product = all_returns.groupby('Produto')['Quantidade Devolvida'].sum()
returns_by_product.plot(kind='bar', title='Total de Devoluções por Produto')
plt.ylabel('Quantidade Devolvida')
plt.xlabel('Produto')
plt.show()
