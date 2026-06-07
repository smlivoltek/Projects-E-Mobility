#!/usr/bin/env python3
"""
Script para atualizar dados do dashboard E-Mobility CRM
Baixa os CSVs do Google Sheets e atualiza os arquivos locais
"""

import requests
import sys
from pathlib import Path
from datetime import datetime

# URLs do Google Sheets (com output=csv)
URLS = {
    'base': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTrkAsblLjOQi2CMC8pxjoGRyLHnxYoB5TV5nMTA3fUjdB_ehsudQGUaUnlACpcN6kRDfyVE19_ghnf/pub?gid=1937499442&single=true&output=csv',
    'snapshot': 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTrkAsblLjOQi2CMC8pxjoGRyLHnxYoB5TV5nMTA3fUjdB_ehsudQGUaUnlACpcN6kRDfyVE19_ghnf/pub?gid=202441246&single=true&output=csv'
}

FILES = {
    'base': 'base-geral.csv',
    'snapshot': 'snapshot.csv'
}

def download_csv(url, filename):
    """Baixa um CSV do Google Sheets e salva localmente"""
    print(f"📥 Baixando {filename}...", end=' ')
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Salvar arquivo
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        lines = response.text.count('\n')
        print(f"✅ {lines} linhas")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro: {e}")
        return False

def main():
    print("\n" + "="*50)
    print("🚀 Atualizador de Dados - E-Mobility CRM")
    print("="*50 + "\n")
    
    success_count = 0
    
    for key, url in URLS.items():
        filename = FILES[key]
        if download_csv(url, filename):
            success_count += 1
    
    print(f"\n✅ {success_count}/{len(URLS)} arquivos atualizados com sucesso!")
    print(f"📅 Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\n💡 Recarregue o dashboard no navegador (F5) para ver os dados!")
    print("="*50 + "\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Atualização cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erro fatal: {e}")
        sys.exit(1)
