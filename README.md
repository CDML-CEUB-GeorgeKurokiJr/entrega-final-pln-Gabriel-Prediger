# Setup Inicial - Primeira Vez

### 1. Clonar o Repositório

```bash
git clone 
cd trabalho_final/pln
```
### 2. Configurar Variáveis de Ambiente

```bash
configurar .env
# IMPORTANTE: Adicionar OPENAI_API_KEY (obrigatório)
```

**Variáveis obrigatórias:**
- `OPENAI_API_KEY` - Sua chave da OpenAI (obrigatório)

**Variáveis opcionais:**
- `GEMINI_API_KEY` - Chave do Google Gemini (opcional)


### 3. Subir os Containers

```bash
# Opção 1: Manual
docker compose up -d
```
