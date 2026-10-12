# Stockly — Sistema de Gestão de Estoque

**Um sistema desktop para simplificar o controle de produtos, compras, vendas e movimentações de estoque.**

O Stockly é uma aplicação desenvolvida em Python com interface gráfica, banco de dados local e foco na organização das operações diárias de pequenos negócios.

---

## Sobre o projeto

O Stockly surgiu da necessidade de desenvolver uma solução prática para gerenciar o estoque de um pequeno negócio, tornando o registro e o acompanhamento dos produtos mais simples e organizados.

O projeto foi desenvolvido em etapas, desde a modelagem do banco de dados e a criação das regras de negócio até a construção da interface gráfica e a geração de um executável para Windows.

A aplicação utiliza armazenamento local com SQLite, dispensando a necessidade de manter um servidor ou contratar hospedagem para seu funcionamento.

## Funcionalidades

- **Produtos:** cadastro, consulta e gerenciamento de produtos, com categoria, unidade de gerenciamento e opção de ativar ou desativar.
- **Compras:** registro de compras e reposições, incluindo produto, fornecedor, quantidade, valor e data.
- **Vendas:** registro de vendas com produto, quantidade, valor, forma de pagamento e data.
- **Estoque:** acompanhamento das quantidades disponíveis, com atualização conforme as operações registradas.
- **Movimentações:** registro de entradas e saídas de produtos, incluindo situações como perdas, brindes e consumo interno.
- **Interface gráfica:** navegação por menu lateral, formulários e mensagens para orientar o usuário.

## Tecnologias utilizadas

| **Python** | Linguagem principal e implementação das regras de negócio. |
| **PySide6** | Desenvolvimento da interface gráfica desktop. |
| **SQLite** | Banco de dados local para persistência das informações. |
| **SQLAlchemy** | Mapeamento objeto-relacional (ORM) e interação com o banco de dados. |
| **Pydantic** | Validação e estruturação dos dados utilizados pela aplicação. |
| **PyInstaller** | Geração do executável para distribuição no Windows. |

## Como foi desenvolvido

O desenvolvimento foi dividido em etapas para manter o projeto organizado e facilitar a manutenção.

**1. Modelagem dos dados**

Foram definidos os modelos responsáveis por representar os produtos, compras, vendas e movimentações. O SQLite foi escolhido para armazenar os registros localmente.

**2. Camada de acesso ao banco**

O SQLAlchemy foi utilizado para mapear as tabelas em classes Python e organizar as operações de consulta e persistência dos dados.

**3. Validação das informações**

O Pydantic foi utilizado na estruturação e validação dos dados recebidos pelas operações do sistema.

**4. Regras de negócio**

Foram implementadas operações para cadastrar e consultar produtos, registrar compras e vendas e controlar as movimentações de estoque.

**5. Interface gráfica**

Com o PySide6, foram criadas as telas e os formulários para permitir a utilização do sistema sem depender de comandos no terminal.

**6. Distribuição**

O PyInstaller foi utilizado para empacotar a aplicação em um executável para Windows, permitindo sua execução sem precisar abrir o código pelo VS Code.

## Como baixar e utilizar

Existem duas formas de utilizar o Stockly: baixar o executável pronto ou executar o projeto a partir do código-fonte.

### Opção 1 — Baixar o executável para Windows

1. Acesse a página de [Releases do Stockly](https://github.com/douglas-henrik/stockly/releases).
2. Baixe o pacote disponibilizado para Windows.
3. Extraia os arquivos, caso estejam compactados.
4. Abra a pasta extraída e execute `Stockly.exe`.

**Importante:** se a versão distribuída utilizar a estrutura `--onedir` do PyInstaller, mantenha todos os arquivos e pastas do pacote juntos. Não copie somente o executável para outra pasta.

### Opção 2 — Executar pelo código-fonte

**Pré-requisitos**

- Python instalado.
- Git, caso queira clonar o repositório.
- Terminal ou editor de código, como o Visual Studio Code.

**1. Clone o repositório**

```bash
git clone https://github.com/douglas-henrik/stockly.git
cd Stockly
```

**2. Crie e ative o ambiente virtual**

No Windows, utilizando PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Instale as dependências**

```bash
pip install PySide6 SQLAlchemy Pydantic python-dotenv
```

Se o projeto possuir um arquivo `requirements.txt` atualizado, prefira instalar as dependências por ele:

```bash
pip install -r requirements.txt
```

**4. Execute a aplicação**

Na pasta principal do projeto:

```bash
python -m app.main
```

O comando pressupõe que a estrutura do projeto mantenha o ponto de entrada em `app/main.py`.

## Armazenamento dos dados

O Stockly utiliza SQLite para guardar os registros localmente.

Na versão configurada para Windows, o banco de dados é armazenado em:

```text
%LOCALAPPDATA%\Stockly\database.db
```

Isso significa que os dados ficam separados dos arquivos do programa. Reinstalar ou substituir o executável não deve apagar o banco de dados, desde que ele não seja removido manualmente e a aplicação continue utilizando o mesmo caminho.

**Recomendação:** faça cópias de segurança periódicas do arquivo `database.db`. Antes de copiar, feche o Stockly para evitar problemas com gravações em andamento.

##  Autor

**Douglas Henrique Medeiros Serrano de Araújo**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em Python e desenvolvimento de software.

- GitHub: https://github.com/douglas-henrik
- LinkedIn: www.linkedin.com/in/douglas-araujo22
