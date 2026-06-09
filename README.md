# 🚀 OrbitalGuard — Sistema Inteligente de Monitoramento e Rastreamento de Lixo Espacial

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13+-blue?logo=python" />
<img src="https://img.shields.io/badge/Flask-WebApp-black?logo=flask" />
<img src="https://img.shields.io/badge/Status-Concluído-brightgreen" />
<img src="https://img.shields.io/badge/Algorithms-Dijkstra%20%7C%20Greedy%20%7C%20MonteCarlo%20%7C%20DP-orange" />
<img src="https://img.shields.io/badge/License-MIT-lightgrey" />

</p>

---

# 🌍 Visão Geral

O OrbSafe é uma plataforma web desenvolvida para monitoramento, análise e gerenciamento de objetos em órbita terrestre, incluindo satélites ativos e detritos espaciais. Desde o lançamento do Sputnik em 1957, a humanidade tem enviado satélites, sondas e foguetes ao espaço. O problema é que muito do que sobe, fica por lá. Hoje, a Órbita Baixa da Terra (LEO - Low Earth Orbit), que fica entre 160 km e 2.000 km de altitude, transformou-se em um verdadeiro "lixão cósmico".

O sistema foi criado para demonstrar a aplicação prática de algoritmos clássicos de otimização, busca e simulação em um contexto realista de monitoramento espacial.

Além do rastreamento orbital, a plataforma oferece:

- Visualização de órbitas
- Simulação probabilística de colisões
- Planejamento de missões
- Priorização inteligente de remoção de detritos
- Análise de grafos orbitais
- Relatórios executivos exportáveis
- Dashboard operacional em tempo real

---

# 🎯 Objetivos do Projeto

O crescimento exponencial da quantidade de satélites e fragmentos espaciais tornou o monitoramento orbital um desafio global. O grande perigo dos detritos espaciais não é o tamanho deles, mas sim a sua velocidade.

Na Órbita Baixa da Terra, os objetos viajam a aproximadamente 28.000 km/h (cerca de 7,8 km/s). Nessa velocidade, a energia cinética de um impacto é devastadora:

Uma minúscula lasca de tinta pode trincar o para-brisa blindado da Estação Espacial Internacional (ISS).

Um fragmento do tamanho de uma bolinha de gude tem o impacto equivalente a uma granada de mão e pode destruir completamente um satélite ativo.

Objetos maiores que 10 cm causam fragmentação catastrófica, pulverizando o alvo e gerando milhares de novos pedaços de lixo.

*Impacto no Cotidiano da Terra*

O colapso das órbitas terrestres devido ao lixo espacial não afetaria apenas os astronautas; ele paralisaria a sociedade moderna. Dependemos da órbita para:

Comunicação e Internet: Sistemas de telecomunicações globais.

Geolocalização (GPS): Navegação de aviões, navios, carros e funcionamento de transações bancárias (que usam o relógio atômico dos satélites).

Monitoramento Climático: Previsão de desastres naturais, furacões e estudos sobre o aquecimento global.

Segurança Nacional: Satélites militares e de monitoramento de fronteiras.

*O OrbitalGuard foi desenvolvido para:*

✅ Monitorar objetos espaciais

✅ Identificar riscos orbitais

✅ Simular possíveis colisões

✅ Priorizar ações de mitigação

✅ Planejar missões de remoção

✅ Aplicar algoritmos estudados em sala de aula

✅ Transformar dados em informações estratégicas

---

# 🧠 Algoritmos Implementados

O projeto atende integralmente aos requisitos da disciplina.

## 1️⃣ Dijkstra — Caminho Mínimo

### Objetivo

Encontrar a rota orbital de menor custo entre dois objetos espaciais.

### Aplicação

O sistema modela satélites e detritos como um grafo.

As arestas representam proximidade orbital baseada na diferença de altitude.

### Entrada

- Origem
- Destino

### Saída

- Caminho encontrado
- Custo total
- Etapas da rota

### Complexidade

O(E log V)

---

## 2️⃣ Algoritmo Guloso

### Objetivo

Priorizar os detritos mais perigosos para monitoramento ou remoção.

### Estratégia

O algoritmo seleciona sempre o objeto com maior prioridade local.

### Critérios

Prioridade = Risco × Fator Orbital

### Resultado

Ranking completo de objetos críticos.

### Complexidade

O(n log n)

---

## 3️⃣ Monte Carlo

### Objetivo

Simular cenários probabilísticos de colisão.

### Estratégia

O sistema gera milhares de cenários variando:

- Distância relativa
- Velocidade orbital
- Densidade de detritos

### Resultado

- Probabilidade de colisão
- Classificação de risco
- Amostras simuladas

### Complexidade

O(n)

onde n representa o número de simulações.

---

## 4️⃣ Programação Dinâmica

### Objetivo

Otimizar missões espaciais.

### Modelagem

Problema da Mochila 0/1.

### Recursos

Combustível disponível

### Objetivo

- Maximizar benefício operacional
- Minimizar desperdício

### Resultado

- Manobras selecionadas
- Combustível utilizado
- Benefício máximo
- Eficiência operacional

### Complexidade

O(n × capacidade)

---

# 🛰 Funcionalidades do Sistema

## 📊 Dashboard Executivo

Tela principal do sistema.

Apresenta:

- Satélites monitorados
- Detritos monitorados
- Alertas críticos
- Status dos algoritmos
- Indicadores operacionais
- Recomendações automáticas

---

## 📡 Rastreamento Orbital

Sistema avançado de consulta.

### Recursos

- Busca inteligente
- Filtros por tipo
- Filtros por risco
- Ordenação dinâmica
- Painel lateral interativo
- Recomendações automáticas

---

## 🌍 Radar Orbital

Visualização dinâmica dos objetos em órbita.

### Recursos

- Radar animado
- Varredura orbital
- Filtros por categoria
- Seleção de objetos
- Informações em tempo real

---

## 🪐 Mapa Orbital

Representação visual das órbitas.

### Camadas

#### LEO

Low Earth Orbit

Até 2.000 km

#### MEO

Medium Earth Orbit

Até 35.786 km

#### GEO

Geostationary Orbit

Acima de 35.786 km

### Recursos

- Distribuição orbital
- Legenda visual
- Contadores automáticos
- Classificação orbital

---

## 🕸 Grafo Orbital

Modelagem dos objetos como rede.

### Recursos

- Nós orbitais
- Conexões
- Densidade do grafo
- Tabela de conexões
- Visualização da rede

---

## 🚨 Central de Alertas

Monitoramento de riscos.

### Recursos

- Alertas críticos
- Classificação de severidade
- Recomendações operacionais
- Plano de resposta

---

## 📜 Histórico de Eventos

Timeline operacional.

### Eventos

- Alertas
- Simulações
- Recalculo de rotas
- Exportação de relatórios
- Operações do sistema

---

## 📈 Analytics

Painel analítico.

### Indicadores

- Distribuição orbital
- Risco por objeto
- Satélites x detritos
- Métricas operacionais

---

## 🎯 Priorização Gulosa

Ordenação automática de objetos.

### Saída

- Ranking de prioridade
- Justificativas
- Score operacional

---

## ☄ Simulação Monte Carlo

Análise probabilística.

### Saída

- Probabilidade de colisão
- Cenários simulados
- Classificação de risco

---

## 🧠 Mission Planner

Otimização de missões.

### Recursos

- Seleção automática de manobras
- Benefício máximo
- Combustível utilizado
- Combinações ótimas

---

## 📄 Relatório Executivo

Sistema de geração de relatórios.

### Exportações

#### CSV

- Dados operacionais
- Indicadores
- Insights
- Recomendações

#### Excel (.xlsx)

Abas:

- Dashboard
- Objects
- Risk Analysis
- Executive Insights

---

# 🗂 Estrutura do Projeto

```txt
orbitalguard/

│
├── app.py
│
├── services/
│   ├── data_service.py
│   ├── graph_service.py
│   ├── dijkstra_service.py
│   ├── greedy_service.py
│   ├── montecarlo_service.py
│   └── dynamic_programming.py
│
├── data/
│   └── orbital_objects.json
│
├── templates/
│   ├── dashboard.html
│   ├── tracking.html
│   ├── radar.html
│   ├── map.html
│   ├── graph.html
│   ├── alerts.html
│   ├── history.html
│   ├── route.html
│   ├── greedy.html
│   ├── collision.html
│   ├── mission_planner.html
│   ├── analytics.html
│   └── report.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── radar.js
│       └── tracking.js
│
└── requirements.txt
```

# ⚙️ Tecnologias Utilizadas

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### Algoritmos

- NetworkX
- Dijkstra
- Greedy
- Monte Carlo
- Programação Dinâmica

### Relatórios

- CSV
- OpenPyXL
- Excel XLSX

---

# 📦 Instalação

## Clonar projeto

```bash
git clone https://github.com/seuusuario/orbitalguard.git

cd orbitalguard
```

## Criar ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar

```bash
python app.py
```

## Abrir navegador

```txt
http://127.0.0.1:5000
```

---

# 📚 Aplicação Acadêmica

Este projeto demonstra a aplicação prática de:

- Estruturas de Dados
- Grafos
- Busca em Grafos
- Heurísticas
- Simulação Probabilística
- Programação Dinâmica
- Visualização de Dados
- Desenvolvimento Web

---

# 🌎 Impacto Real

O monitoramento de lixo espacial é um dos principais desafios da exploração espacial moderna.

Sistemas semelhantes são utilizados por NASA, ESA e SpaceX para reduzir riscos de colisão, preservar satélites operacionais e garantir a sustentabilidade das atividades espaciais.

---

# 👨‍💻 Autores

Felipe Marceli - RM560456


Projeto acadêmico desenvolvido para aplicação de algoritmos clássicos em um cenário de monitoramento e gestão de lixo espacial, combinando otimização, análise de risco e visualização interativa de dados orbitais.

---

## ⭐ Destaques do Projeto

✅ WebApp completo

✅ Interface profissional

✅ Dashboard executivo

✅ Visualizações interativas

✅ 4 algoritmos obrigatórios implementados

✅ Exportação CSV e Excel

✅ Relatórios executivos

✅ Simulações probabilísticas

✅ Aplicação prática de Grafos

✅ Projeto alinhado a problemas reais da indústria espacial 🚀