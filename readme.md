# Guia Rápido do Projeto Django

## 1. Preparação do Ambiente

```sh
# Cria o ambiente virtual
python -m venv venv
# Ativa o ambiente virtual (Windows PowerShell)
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
# Inicia o servidor de desenvolvimento
python manage.py runserver
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
