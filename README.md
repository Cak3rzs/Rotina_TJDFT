## Rotina de Download e Leitura de Diários do TJDFT
Este projeto é uma automação simples que utiliza Selenium e requests para baixar e ler os diários mais recentes do Tribunal de Justiça do Distrito Federal e Territórios (TJDFT). A rotina acessa a página oficial do TJDFT, fecha avisos de consentimento, localiza o PDF mais recente e o salva localmente. Além disso, a aplicação lê o conteúdo do PDF e exibe o número de páginas e o texto extraído.

### Funcionalidades
Download Automático: Baixa o PDF mais recente do diário do TJDFT.

Leitura de PDF: Lê e extrai texto do PDF baixado, permitindo visualizar o conteúdo diretamente no console.

Flexibilidade: O código pode ser facilmente adaptado para acessar outros documentos e realizar ações semelhantes.

### Tecnologias Utilizadas
Python: Linguagem de programação utilizada para a automação.

Selenium: Biblioteca para automação de navegadores web.

requests: Biblioteca para fazer requisições HTTP e baixar arquivos.

PyPDF2: Biblioteca para manipulação e leitura de arquivos PDF.
Pré-requisitos
Python 3.x
Bibliotecas: selenium, requests, PyPDF2
WebDriver do Chrome instalado e configurado.


### Como Usar
Clone este repositório:

bash

Copiar código
``git clone https://github.com/seu_usuario/Rotina_TJDFT.git``
cd seu_repositorio
Instale as dependências:

bash
Copiar código
```python
pip install selenium requests PyPDF2
```
Execute o script em um Jupyter Notebook, iniciando pela célula que faz o download do PDF, seguida pela célula que lê o conteúdo do PDF.
