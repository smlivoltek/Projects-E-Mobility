#!/usr/bin/env python3
"""
Script para atualizar dados do Google Sheets automaticamente
Funciona tanto localmente quanto no GitHub Actions
"""

import urllib.request
import sys
import os
from pathlib import Path

# Google Sheets export URLs (usam formato CSV público)
SHEET_ID = "2PACX-1vTrkAsblLjOQi2CMC8pxjoGRyLHnxYoB5TV5nMTA3fUjdB_ehsudQGUaUnlACpcN6kRDfyVE19_ghnf"

# IDs das abas (gid)
ABAS = {
    "base-geral": "1937499442",      # Aba Base-Geral (dados atuais)
    "snapshot": "202441246"           # Aba Snapshot (2 semanas atrás)
}

def criar_url_csv(aba_id):
    """Cria URL de export CSV do Google Sheets"""
    return f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/pub?gid={aba_id}&single=true&output=csv"

def baixar_csv(url, arquivo_saida):
    """Baixa CSV do Google Sheets e salva localmente"""
    try:
        print(f"📥 Baixando de: {url}")
        
        # Criar header customizado para evitar bloqueios
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        request = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(request, timeout=30) as response:
            conteudo = response.read().decode('utf-8')
        
        # Salvar arquivo
        Path(arquivo_saida).parent.mkdir(parents=True, exist_ok=True)
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        # Validar que arquivo não está vazio
        linhas = conteudo.strip().split('\n')
        print(f"✅ Arquivo salvo: {arquivo_saida}")
        print(f"   Linhas: {len(linhas)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao baixar {arquivo_saida}: {str(e)}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🔄 Atualizando dados do Google Sheets")
    print("=" * 60)
    
    sucesso = True
    
    for nome, aba_id in ABAS.items():
        arquivo = f"{nome}.csv"
        url = criar_url_csv(aba_id)
        
        if not baixar_csv(url, arquivo):
            sucesso = False
    
    print("=" * 60)
    
    if sucesso:
        print("✅ Todos os dados foram atualizados com sucesso!")
        return 0
    else:
        print("⚠️  Alguns arquivos falharam. Verifique os erros acima.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```
---
