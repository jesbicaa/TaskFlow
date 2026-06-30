# 🚀 TaskFlow — Sistema Ágil de Gerenciamento de Tarefas

> **Projeto prático desenvolvido para a disciplina de Engenharia de Software** > **Instituição:** Centro Universitário UniFECAF  
> **Estudante:** Jéssica Bianca da Silva | **RA:** 160289  

---

## 📝 1. Descrição do Projeto

O **TaskFlow** é uma aplicação web voltada ao gerenciamento de fluxos de trabalho utilizando os princípios da Engenharia de Software e metodologias ágeis. O sistema foi concebido sob medida para atender a uma startup de logística parceira, permitindo cadastrar, listar, transicionar status e remover demandas diárias (CRUD funcional), otimizando o monitoramento de gargalos em tempo real.

---

## 📂 2. Estrutura Clara de Diretórios

O repositório está estritamente estruturado em conformidade com as diretrizes e boas práticas de arquitetura de software exigidas pela atividade:

```text
TaskFlow/
├── .github/
│   └── workflows/
│       └── ci.yml        # Pipeline de Integração Contínua (GitHub Actions)
├── docs/                 # Pasta Obrigatória: Relatórios e documentação técnica
├── src/                  # Pasta Obrigatória: Código-fonte do sistema web
│   ├── templates/
│   │   └── index.html    # Frontend da aplicação (Painel Kanban Web)
│   └── app.py            # Backend da aplicação (Servidor Flask e Repositório)
├── tests/                # Pasta Obrigatória: Suíte de testes automatizados
│   └── test_app.py       # Casos de teste unitários com Pytest
├── README.md             # Documentação oficial do projeto
└── requirements.txt      # Gerenciador de dependências do ecossistema Python

```

---

## 📊 3. Planejamento Ágil e Quadro Kanban

O ciclo de vida do desenvolvimento do projeto foi gerenciado visualmente através da ferramenta **GitHub Projects**, utilizando o framework **Kanban** dividido nas colunas fundamentais: `To Do` (A Fazer), `In Progress` (Em Progresso) e `Done` (Concluído).

O quadro conta com **10+ cards organizados**, mapeando os requisitos de software, correções, testes e a evolução de escopo proposta.

---

## 🛠️ 4. Tecnologias Utilizadas e Como Executar

### Tecnologias e Dependências

* **Backend:** Python 3.10+ / Flask 3.0.0 (Microframework leve e modular)
* **Testes:** Pytest 7.4.0 (Framework robusto de testes automatizados)
* **Qualidade de Código:** Flake8 6.1.0 (Linter estático para garantia do padrão PEP 8)

### Passo a Passo para Execução Local

1. **Clonar o Repositório:**
```bash
git clone [https://github.com/jesbicaa/TaskFlow.git](https://github.com/jesbicaa/TaskFlow.git)
cd TaskFlow

```


2. **Instalar Dependências:**
```bash
pip install -r requirements.txt

```


3. **Executar a Aplicação Web:**
```bash
python src/app.py

```


Acesse a interface pelo navegador no endereço local: [http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)

---

## 🧪 5. Controle de Qualidade e Testes Automatizados

O projeto utiliza **testes unitários automatizados** com `Pytest` para assegurar o comportamento esperado das operações CRUD, validando o isolamento do repositório em memória e os códigos de resposta HTTP (`302 Redirect`).

Para rodar os testes localmente na sua máquina, execute:

```bash
pytest tests/

```

---

## ⚙️ 6. Pipeline de Integração Contínua (GitHub Actions)

Foi configurado um workflow de **CI (Continuous Integration)** por meio do GitHub Actions (`.github/workflows/ci.yml`). A cada `push` ou `pull request` na branch principal, o servidor em nuvem executa de forma autônoma:

1. **Setup de Ambiente:** Instalação do Python e mapeamento de dependências.
2. **Validação de Qualidade de Código:** Execução do linter `Flake8` conferindo formatação e evitando más práticas de codificação.
3. **Execução Automática da Suíte de Testes:** Inicialização do `Pytest` garantindo que nenhuma alteração quebre regras preexistentes.

---

## 🔀 7. Gerenciamento e Simulação de Mudança de Escopo

Durante as interações de feedback com os stakeholders da startup de logística, identificou-se uma nova necessidade crítica: **as tarefas precisavam de um indicador de urgência para mitigar riscos de atraso nas entregas prioritárias.**

* **A Mudança:** Inclusão da propriedade e funcionalidade de níveis de **Prioridade (Baixa, Média, Alta)** nas tarefas.
* **Impacto no Processo:**
1. Criação de um novo card correspondente no Kanban do *GitHub Projects*.
2. Atualização das classes e rotas no backend (`src/app.py`).
3. Adaptação dos seletores e tags visuais no frontend (`src/templates/index.html`).
4. Geração de um novo commit semântico isolado implementando e registrando a mudança.



---

## 🪵 8. Histórico de Commits Semânticos

O repositório adota a convenção de **Commits Semânticos** para manter o histórico claro, legível e auditável, registrando um histórico frequente ao longo do ciclo de engenharia:

| Tipo/Prefixo | Mensagem do Commit Exemplo | Objetivo |
| --- | --- | --- |
| `chore:` | mapear dependencias estruturais do ecossistema flask e pytest | Configurações do projeto |
| `docs:` | detalhar objetivos iniciais do projeto e guia de instalacao | Atualização de documentações |
| `feat:` | conceber entidades task e tarefarepository no dominio da aplicacao | Inserção de novas features |
| `feat:` | implementar rota base de listagem e mapeamento de payloads | Criação do CRUD |
| `test:` | projetar caso de teste unitario para integridade de criacao | Implementação de testes |
| `ci:` | estruturar pipeline github actions integrando linter e suite pytest | Configuração de automações |
| `feat:` | expandir escopo injetando metadados de prioridades alta media e baixa | **Mudança de Escopo** |

---
