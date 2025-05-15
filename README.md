# AlstomCAD

![Badge de status do projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

AlstomCAD é uma ferramenta de automação desenvolvida para detecção de alterações em arquivos CAD e atualização automática de planilhas Excel com as alterações detectadas. Este projeto foi desenvolvido para a empresa Alstom.

## Protótipo

Insira uma captura de tela da sua aplicação ou um link para um protótipo online:

![Captura de Tela](link-da-imagem-exemplo.png)

Você pode acessar o protótipo [aqui](link-do-prototipo-online).

## Índice

- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)

## Descrição

AlstomCAD é uma ferramenta interna desenvolvida para automatizar o processo de atualização de planilhas Excel com base em alterações detectadas em arquivos CAD. Utilizando Python e bibliotecas específicas de automação para CAD, a ferramenta monitora os arquivos, detecta modificações e realiza as atualizações necessárias nas planilhas de maneira automática.

## Tecnologias Utilizadas

### Backend

- **[Python](https://www.python.org/)** - Linguagem de programação de alto nível.
- **[Bibliotecas de Automação para CAD]** - Bibliotecas específicas utilizadas para interagir e automatizar processos com arquivos CAD.

### Planilhas

- **[Openpyxl](https://openpyxl.readthedocs.io/en/stable/)** - Biblioteca Python para ler/escrever arquivos Excel (.xlsx).

## Instalação

Para clonar e executar este projeto, você precisará do [Git](https://git-scm.com), [Python](https://www.python.org/), e preferencialmente de um ambiente virtual (virtualenv).

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/alstomcad.git

# Entre no diretório do projeto
cd alstomcad

# Crie e ative um ambiente virtual
python -m venv venv
# No Windows
venv\Scripts\activate
# No Unix ou MacOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
