# LinkedIn Automation

Este projeto automatiza a conexão com pessoas no LinkedIn usando palavras-chave específicas. 

## Descrição

A automação faz login no LinkedIn, pesquisa por palavras-chave, filtra os resultados para mostrar apenas pessoas relacionadas a essa chave e faz a solicitação para conectar-se com elas enviando uma mensagem personalizada com o nome de cada uma em seu privado.

## Estrutura do Projeto

- `main.py`: Script principal que executa a automação.
- `config.py`: Arquivo de configuração para armazenar credenciais e palavras-chave.
- `utils/`: Pasta contendo módulos auxiliares para o navegador, login, pesquisa e conexão.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/GS-Rodrigues/LinkedIn-Automation.git
    cd LinkedInAutomation
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    pip install -r requirements.txt
    ```

3. Configure suas credenciais no arquivo `config.py`.

## Uso

Execute o script principal:
```bash
python main.py
