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

- Python 3
- Django 4
- SQLite (planejo utilizar MySQL no deploy)
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

## Formulario de Login

- A tabela de contatos está preenchida com dados fictícios gerados pela biblioteca Faker.

![image](https://github.com/user-attachments/assets/e1535657-990a-4057-a7bf-848256038619)

![image](https://github.com/user-attachments/assets/8cc85771-b52c-44e4-9d1d-c868ceb42a71)

![image](https://github.com/user-attachments/assets/fcfef8bf-fcdb-43d5-8ca2-ff986c29cf15)

![image](https://github.com/user-attachments/assets/d33d94c1-5df5-4180-9a2d-27815d477d08)





