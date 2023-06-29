from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd


data = [
    {"leite": False, "café": True, "cerveja": False, "pão": True, "manteiga": True, "arroz": False, "feijão": False},
    {"leite": True, "café": False, "cerveja": True, "pão": True, "manteiga": True, "arroz": False, "feijão": False},
    {"leite": False, "café": True, "cerveja": False, "pão": True, "manteiga": True, "arroz": False, "feijão": False},
    {"leite": True, "café": True, "cerveja": False, "pão": True, "manteiga": True, "arroz": False, "feijão": False},
    {"leite": False, "café": False, "cerveja": True, "pão": False, "manteiga": False, "arroz": False, "feijão": False},
    {"leite": False, "café": False, "cerveja": False, "pão": False, "manteiga": True, "arroz": False, "feijão": False},
    {"leite": False, "café": False, "cerveja": False, "pão": True, "manteiga": False, "arroz": False, "feijão": False},
    {"leite": False, "café": False, "cerveja": False, "pão": False, "manteiga": False, "arroz": False, "feijão": True},
    {"leite": False, "café": False, "cerveja": False, "pão": False, "manteiga": False, "arroz": True, "feijão": True},
    {"leite": False, "café": False, "cerveja": False, "pão": False, "manteiga": False, "arroz": True, "feijão": False}
]

# Criar DataFrame a partir dos dados
df = pd.DataFrame(data)

# Executar algoritmo Apriori para encontrar itemsets frequentes
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Gerar as regras associativas
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Exibir as regras associativas
#print(rules)

# Selecionar as colunas de interesse
columns = ['antecedents', 'consequents', 'support', 'confidence']

# Criar um novo DataFrame apenas com as colunas selecionadas
result = rules[columns]

# Exibir o DataFrame com antecedentes, consequentes, suporte e confiança
print(result) 
