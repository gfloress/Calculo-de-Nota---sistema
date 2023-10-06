# Calculo-de-Nota---sistema
Trabalho da disciplina Linguagens de Programação em 2023.2

Planejamento do Sistema de Gerenciamento de Notas em Flask

O sistema de gerenciamento de notas em Flask que estamos planejando visa fornecer uma plataforma eficiente para professores e alunos monitorarem o desempenho acadêmico. Abaixo está o planejamento detalhado do sistema, dividido em funcionalidades e requisitos técnicos.

Funcionalidades:

- Login:
Autenticação de usuários com nome de usuário e senha.
Proteção de rotas e funcionalidades do sistema com autenticação.

- Cadastro de Tarefas:
Professores podem adicionar informações sobre as tarefas a serem realizadas.
Cada tarefa possui um nome, uma descrição, uma data de entrega e um peso.

- Cadastro de Notas:
Professores podem adicionar notas para cada tarefa de cada aluno.
As notas são adicionadas de acordo com o desempenho dos alunos nas tarefas.
Os dados das notas (t1 e t2) e listas de atividades são armazenados no banco de dados.
Cálculo da Nota:

A nota do aluno é calculada usando a fórmula:
  np = (t1 + t2) * 0.8 + (soma de todas as listas / número de listas) * 0.2

A nota final é então usada para determinar a situação do aluno (aprovado, reprovado, recuperação, etc.).

Requisitos Técnicos:
- Flask Framework:
O sistema será desenvolvido usando o Flask, um framework web em Python.

- Banco de Dados:
Utilização de um banco de dados em SQLite para armazenar informações de usuários, tarefas e notas dos alunos.

- Autenticação de Usuários:
Implementação de um sistema de login seguro para autenticação de professores e alunos.

- Frontend Responsivo:
Implementação de uma interface de usuário responsiva usando HTML para melhorar a experiência do usuário.

- Segurança:
Adoção de práticas de segurança, como proteção contra injeção SQL e autenticação segura para proteger os dados do sistema.

- API para Cálculo de Nota:
Desenvolvimento de uma API para calcular as notas dos alunos com base nos dados fornecidos.

- Testes e Validação:
Implementação de testes automatizados para garantir que o sistema funcione corretamente.
Validação dos dados de entrada para evitar erros e inconsistências.
