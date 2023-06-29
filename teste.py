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

df = pd.DataFrame(data)

print(df)