# Pull Request

## Descrição
Implementação completa do sistema de autenticação e gerenciamento de perfis de usuários, conforme os requisitos da Sprint 1.

O que foi feito?

Criação do modelo de dados do usuário em models/user.py.

Implementação de lógica de hash de senha (Bcrypt) e geração de tokens (JWT) em core/security.py.

Desenvolvimento dos endpoints de Login e consulta de Perfil em routes/auth.py.

Definição de esquemas de validação de dados em schemas/for_users.py.

Qual o motivo da alteração?

Garantir a segurança no acesso ao sistema e fornecer os dados necessários para as telas de perfil do Aluno e Docente.
---

## Tipo de alteração
Selecione uma opção:

- [x] feat (nova funcionalidade)
- [ ] fix (correção de bug)
- [ ] refactor (melhoria interna sem alteração de comportamento)
- [ ] chore (tarefas técnicas ou manutenção)
- [ ] docs (documentação)

---

## Issue relacionada
Informe a issue vinculada, se houver:

Closes #

---

## Como testar
Descreva o passo a passo para validação:

Certifique-se de que o banco de dados tem a tabela usuario com a coluna senha_hash.

Execute docker-compose up --build para subir o ambiente.

Acesse http://localhost:8000/docs.

Teste o endpoint POST /auth/login enviando um CPF e senha válidos.

Utilize o ID retornado para testar o endpoint GET /auth/perfil/{id_usuario}.

---

## Evidências (opcional)
Inclua prints, logs ou exemplos que ajudem na validação.

---

## Impacto
Selecione os impactos deste PR:

- [ ] Sem impacto relevante
- [x] Backend
- [x] Banco de dados

---

## Riscos
Classifique o risco da alteração:

- [ ] Baixo
- [x] Médio
- [ ] Alto

Detalhamento (se necessário):

---

## Checklist
Antes de solicitar revisão, confirme:

- [ ] Código testado localmente
- [ ] Segue os padrões do projeto
- [x] Não impacta funcionalidades existentes
- [ ] Testes adicionados ou atualizados (quando aplicável)
- [ ] Documentação atualizada (quando necessário)

---

## Pontos de atenção para revisão
Verificação da SECRET_KEY no arquivo security.py.

Validação da lógica de tratamento de erro no login quando o CPF não é encontrado.

---

## Deploy
Existe alguma ação necessária para deploy?

- [ ] Nenhuma
- [ ] Migration de banco de dados
- [x] Variáveis de ambiente
- [ ] Configuração adicional

Detalhes:

-