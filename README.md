# 📆 Agenda Django

Projeto de uma agenda desenvolvido com Django. Permite criar, atualizar e deletar contatos, cada um com diversos campos. A exclusão de contatos é restrita ao usuário que os criou.

## ✨ Funcionalidades

- Cadastro de contatos com os seguintes campos:
  - Nome
  - Sobrenome
  - Foto
  - Email
  - Descrição
  - Dono (usuário que criou o contato)
- Atualização de informações dos contatos
- Exclusão de contatos (apenas pelo dono)
- Interface web responsiva
- Autenticação de usuários

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- SQLite (planeja-se utilizar MySQL no deploy)
- HTML, CSS 

## 🚀 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Rdtcm/agenda.git
   cd agenda
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Unix ou MacOS
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

   Acesse o projeto em `http://127.0.0.1:8000/`.

## 👤 Autor

- [Rdtcm](https://github.com/Rdtcm)
