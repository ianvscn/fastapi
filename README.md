# TodoApp

## Descrição
O **TodoApp** é uma aplicação web para gerenciamento de tarefas (To-Do), projetada para ser simples, escalável e fácil de usar. 
Ela permite que os usuários gerenciem tarefas pessoais, organizem prioridades e acompanhem o progresso de suas atividades diárias.

## Funcionalidades Principais
- **Gestão de Tarefas**: Criação, leitura, atualização e exclusão de tarefas.
- **Sistema de Usuários**: Registro, login e autenticação de usuários.
- **Administração**: Recursos específicos para administradores gerenciarem usuários e permissões.
- **Interface Web**: Integração de templates HTML para uma experiência de usuário intuitiva.

## Estrutura do Projeto
```
TodoApp/
|-- alembic/           # Gerenciamento de migrações do banco de dados
|-- routers/           # Rotas e endpoints da API
|   |-- admin.py       # Funcionalidades administrativas
|   |-- auth.py        # Rotas de autenticação
|   |-- todos.py       # Rotas para tarefas
|   |-- users.py       # Rotas para gestão de usuários
|-- static/            # Arquivos estáticos (CSS, JS, imagens)
|-- templates/         # Templates HTML
|-- test/              # Testes automatizados
|-- main.py            # Arquivo principal para iniciar a aplicação
|-- database.py        # Configuração do banco de dados
|-- models.py          # Definição dos modelos de dados
|-- alembic.ini        # Configuração do Alembic
|-- requirements.txt   # Dependências do projeto
```

## Requisitos
- **Python 3.8+**
- **Banco de Dados**: PostgreSQL (ou adaptável a outros bancos suportados pelo SQLAlchemy)

## Configuração e Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/ianvscn/fastapi.git
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o banco de dados no arquivo `database.py`.
5. Execute as migrações:
   ```bash
   alembic upgrade head
   ```
6. Inicie a aplicação:
   ```bash
   uvicorn TodoApp.main:app --reload
   ```
7. Acesse a aplicação no navegador: Abra o navegador e vá para
`http://127.0.0.1:8000` para visualizar e interagir com o TodoApp.
9. Fechar o programa (uvicorn)
Para interromper o servidor uvicorn que está executando sua aplicação FastAPI,
pressione `Ctrl + C` no terminal onde o servidor está sendo executado.
Isso irá interromper o processo de execução do servidor e fechar a aplicação.
10. Encerrar o ambiente virtual
Após fechar o servidor, você pode sair do ambiente virtual com o comando: `deactivate`

## Testes
Para executar os testes automatizados:
```bash
pytest
```

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

