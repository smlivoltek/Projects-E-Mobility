# 🚀 E-Mobility CRM Dashboard - Quick Start

## ⚡ Comece em 30 segundos

### 1️⃣ Abrir o Dashboard
- Duplo-clique em **`index.html`**
- Ou arraste o arquivo para um navegador
- ✅ Pronto! Dashboard carregado com dados

### 2️⃣ Atualizar Dados Automaticamente

#### Windows:
```
Duplo-clique em: atualizar_dados.bat
```

#### Mac/Linux:
```bash
chmod +x atualizar_dados.sh
./atualizar_dados.sh
```

#### Manual com Python:
```bash
python3 atualizar_dados.py
```

---

## 📊 O que você vê?

### Aba 1: Diretoria (Executivo)
- **"Vamos Bater a Meta?"** - Resposta direta SIM/NÃO
- Gráfico de fechamentos mensais
- Comparativo com 2 semanas atrás
- Valor em Risco por probabilidade
- Top 5 projetos por vendedor
- Aging do pipeline

### Aba 2: Bruno Reis
- KPIs: R$50M meta anual
- Alertas de oportunidades paradas
- Top 10 deals
- Todos os clientes + filtros

### Aba 3: Felipe Hanke
- KPIs: R$12M meta anual
- Mesma estrutura de Bruno
- Alerta crítico se pipeline < 1.5x meta

### Aba 4: Oportunidades
- Lista completa com filtros
- Por cliente e vendedor
- Visualização detalhada

---

## 📂 Arquivos Inclusos

```
📦 E-Mobility CRM Dashboard
├── index.html                 ← ABRIR AQUI
├── base-geral.csv            ← Dados atuais
├── snapshot.csv              ← Dados de 2 semanas atrás
├── atualizar_dados.py        ← Script Python (multiplataforma)
├── atualizar_dados.bat       ← Script Windows
├── atualizar_dados.sh        ← Script Mac/Linux
├── README.txt                ← Documentação completa
└── QUICKSTART.md             ← Este arquivo
```

---

## 🔄 Fluxo de Atualização

```
Google Sheets (Fonte)
        ↓
    (Executar script)
        ↓
Arquivos CSV locais
        ↓
    (F5 no navegador)
        ↓
Dashboard atualizado ✅
```

---

## 🎯 Dicas Úteis

### Filtrar por Vendedor
- Aba "Diretoria": Ver top 5 de cada um lado a lado
- Aba "Bruno Reis" ou "Felipe Hanke": Dados específicos

### Acompanhar Metas
- **Bruno**: R$50M/ano (≈ R$4.2M/mês)
- **Felipe**: R$12M/ano (≈ R$1M/mês)
- Dashboard mostra % vs meta automático

### Alertas Automáticos
- 🔴 Pipeline < 1.5x meta → Alerta crítico
- 🟡 Oportunidade parada > 25 dias → Alerta
- 🟢 Deals ganhos → Comemorar! 🎉

---

## ⚙️ Requisitos

✅ **Navegador moderno** (Chrome, Firefox, Safari, Edge)
✅ **Python 3.6+** (só se usar script de atualização)
✅ **Conexão com internet** (para atualizar dados)

---

## ❓ Problemas Comuns

### Dados não carregam
1. Clique no aviso vermelho "⚠️"
2. Copie todos os dados da planilha (Ctrl+A)
3. Cole no modal e clique "Carregar"

### "Arquivo local não encontrado"
- Execute `atualizar_dados.py` ou `.bat` / `.sh`
- Ou cole os dados manualmente

### Script Python falha no Windows
- Instale Python: https://python.org
- Marque "Add Python to PATH" no instalador

---

## 📞 Contato & Suporte

**Repositório**: https://github.com/smlivoltek/Projects-E-Mobility
**Última atualização**: 07/06/2026

---

**Desenvolvido com ❤️ para Livoltek E-Mobility**
