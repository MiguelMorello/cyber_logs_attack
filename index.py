import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
  # Substitua pelo caminho correto do arquivo
data = pd.read_csv('/content/sample_data/cyber.csv')


# 1. Distribuição de severidade de ataques
def plot_attack_severity_distribution(data):
    severity_counts = data['Attack_Severity'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=severity_counts.index, y=severity_counts.values, palette="viridis")
    plt.title('Distribuição de Severidade de Ataques', fontsize=14)
    plt.xlabel('Severidade', fontsize=12)
    plt.ylabel('Contagem', fontsize=12)
    plt.xticks(rotation=45)
    plt.show()

# 2. Incidentes ao longo do tempo
def plot_incidents_over_time(data):
    data['Date'] = pd.to_datetime(data['Date'])  # Converter a coluna 'Date' para datetime
    incidents_by_date = data.groupby(data['Date'].dt.date).size()
    plt.figure(figsize=(12, 6))
    plt.plot(incidents_by_date.index, incidents_by_date.values, marker='o', linestyle='-')
    plt.title('Incidentes ao Longo do Tempo', fontsize=14)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Contagem de Incidentes', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# 3. Tipos de ataque por severidade
def plot_attack_types_by_severity(data):
    plt.figure(figsize=(12, 8))
    sns.countplot(data=data, x='Attack_Vector', hue='Attack_Severity', palette='muted')
    plt.title('Tipos de Ataque por Severidade', fontsize=14)
    plt.xlabel('Tipo de Ataque', fontsize=12)
    plt.ylabel('Contagem', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Severidade')
    plt.show()

# 4. Comparação entre sistemas atualizados e desatualizados
def plot_patch_status_comparison(data):
    patch_counts = data['System_Patch_Status'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=patch_counts.index, y=patch_counts.values, palette='coolwarm')
    plt.title('Sistemas Atualizados vs. Desatualizados', fontsize=14)
    plt.xlabel('Status do Patch', fontsize=12)
    plt.ylabel('Contagem', fontsize=12)
    plt.xticks(rotation=45)
    plt.show()

# Chamar as funções para gerar os gráficos
plot_attack_severity_distribution(data)
plot_incidents_over_time(data)
plot_attack_types_by_severity(data)
plot_patch_status_comparison(data)
