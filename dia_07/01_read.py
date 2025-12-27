# %%

nome_arquivo = "historia.txt"

open_file = open(nome_arquivo)
# %%
conteudo = open_file.read()

print(conteudo)