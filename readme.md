# Guia Rápido do Projeto Django

## Configuração do Ambiente de Desenvolvimento

Siga estes passos na ordem para configurar e rodar o projeto.

```sh
# 1. Crie o ambiente virtual (isso criará uma pasta 'venv')
python -m venv venv

# 2. Ative o ambiente virtual
#    Após a ativação, você verá (venv) no início do seu terminal.

# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
#   (Se receber um erro de permissão, execute: Set-ExecutionPolicy RemoteSigned -Scope Process)
# No Windows (CMD) ou no Linux/macOS (bash):
.\venv\Scripts\activate
# Instala o Django
pip install django
```

## 2. Criando o Projeto

```sh
# Cria um novo projeto Django na pasta atual
django-admin startproject project .
# Cria as migrações iniciais do banco de dados
python manage.py makemigrations
# Aplica as migrações ao banco de dados
python manage.py migrate

# 5. (Opcional) Crie um superusuário para acessar a área de admin:
python manage.py createsuperuser

# 6. (Opcional) Popule o banco de dados com contatos de exemplo:
python utils/create_contacts.py

# 7. Inicie o servidor de desenvolvimento:
python manage.py runserver
#    Acesse http://127.0.0.1:8000/ no seu navegador.
```

## 3. Versionamento com Git

```sh
# Inicializa o repositório git
git init
# Renomeia a branch principal para 'main' (boa prática)
git branch -M main
# Adiciona todos os arquivos
git add .
# Faz o commit inicial
git commit -m "feat: Configuração inicial do projeto"
# Adiciona o repositório remoto (troque pela sua URL)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
# Envia para o GitHub
git push -u origin main
```

## 4. Salvando Alterações em uma Nova Branch

```sh
# Cria e muda para uma nova branch
git checkout -b NOME_DA_BRANCH
# Adiciona e commita as alterações
git add .
git commit -m "Mensagem do commit"
# Envia a branch para o GitHub
git push -u origin NOME_DA_BRANCH
```
