# Topicos-Desafio2-Celula06

# 🚛 Coleta Seletiva Inteligente — Logística Verde

> Solução para otimização de rotas de coleta seletiva em cooperativas de bairros periféricos, com processamento contínuo de dados de descarte e governança de TI aplicada.

---

## 📋 Problema Prático

Uma startup de logística verde precisa otimizar a coleta seletiva de materiais recicláveis em cooperativas de bairros periféricos. O sistema antigo gerava **rotas fixas**, desperdiçando combustível em bairros com caçambas vazias.

Para resolver o problema, a célula deve criar uma solução que processe um **fluxo contínuo de dados de descarte**, dividida entre dois times:

- **Time ADS** — desenvolverá o motor lógico de repetição que simula a passagem do caminhão e valida o estouro de capacidade de carga.
- **Time SI** — desenvolverá a estrutura de dados complexa (**Dicionário de Configuração**) que mapeia o peso específico de densidade de cada tipo de material (Plástico, Vidro, Metal) para calcular o volume real ocupado, aplicando regras de Governança de TI.

---

## ✅ Critérios de Aceite e Desenvolvimento Profissional

### 🔧 Metas para as Células de ADS
*Foco na Engenharia do Algoritmo*

| Critério | Descrição |
|---|---|
| **O Script** | Desenvolver o arquivo `src/coleta.py` utilizando obrigatoriamente um laço `while` baseado em interrupção dinâmica (`break`) |
| **Tratamento de Exceções** | Implementar blocos `try/except` para capturar erros de digitação (letras no lugar de números), exibindo `"Erro: Entrada Invalida"` sem derrubar o programa |
| **Saída Padronizada** | Exibir ao fim as strings exatas: `"Volume Total: X m³"` e `"Status: Capacidade Maxima Atingida"` |

---

### 🏗️ Metas para as Células de SI
*Foco no Desenvolvimento de Arquitetura de Dados*

| Critério | Descrição |
|---|---|
| **Arquivo de Estrutura** | Criar o arquivo `src/config_negocio.py` com um dicionário Python estruturado contendo as regras de negócio de densidade e o limite de compliance ambiental da frota |
| **Cálculo de Viabilidade Econômica** | Desenvolver uma função que calcule o custo de ociosidade caso o caminhão retorne com menos de **30% da carga** |
| **Seção de Compliance no README** | Justificar as decisões de arquitetura de dados com base nas metas de **Green IT** e sustentabilidade |

---

## 🌱 Compliance — Green IT & Sustentabilidade

> *Esta seção deve ser preenchida pelo Time de SI.*

Justifique aqui as decisões de arquitetura tomadas em `src/config_negocio.py`, conectando cada escolha às metas de Green IT:

- Por que os materiais foram modelados como dicionário e não como variáveis avulsas?
- Como o limite de 30% de carga contribui para a redução de emissões?
- De que forma a estrutura de dados facilita auditorias de compliance ambiental?

Justificativa: 

O arquivo governanca_si.py organiza os dados de compliance ambiental em um dicionário, facilitando a consulta, manutenção e auditoria das informações. O sistema considera a capacidade máxima de 50 m³ e identifica como ociosa uma viagem com carga inferior a 15 m³, que representa 30% da capacidade do caminhão. Esse controle ajuda a identificar viagens com pouca carga e auxilia no planejamento das rotas. Assim, é possível reduzir viagens desnecessárias, economizar combustível e diminuir a emissão de carbono. Dessa forma, o sistema contribui para a Governança de TI e para os princípios de Green IT, utilizando os dados para melhorar a eficiência da coleta, facilitar auditorias e reduzir impactos ambientais.

---

## 📁 Estrutura do Repositório

```
📦 raiz do projeto
 ┣ 📂 src
 ┃ ┣ 📄 coleta.py           # Motor lógico — Time ADS
 ┃ ┗ 📄 config_negocio.py   # Arquitetura de dados — Time SI
 ┗ 📄 README.md
```

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd seu-repositorio

# Execute o script principal
python src/coleta.py
```
