import os
import re
import unicodedata

base_path = "/data/magic_topics"

for fname in os.listdir(base_path):
    if fname.startswith("topic_") and fname.endswith(".md"):
        full_path = os.path.join(base_path, fname)

        # Lê a primeira linha do arquivo (que contém o título do tópico)
        with open(full_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()

        # Extrai algo como "100. Geral"
        match = re.match(r"^(\d{3}\.?\s?.*)", first_line)
        if not match:
            print(f"Não consegui extrair título de {fname}")
            continue

        titulo = match.group(1).strip()

        # Remove caracteres inválidos de filename
        titulo_limpo = re.sub(r"[^0-9A-Za-z._-]", "", titulo)

        novo_nome = f"{titulo_limpo}.md"
        novo_path = os.path.join(base_path, novo_nome)

        os.rename(full_path, novo_path)
        print(f"{fname} → {novo_nome}")
