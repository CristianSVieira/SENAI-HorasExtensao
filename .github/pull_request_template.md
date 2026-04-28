# Pull Request

## Descrição
Descreva de forma objetiva o que foi implementado neste PR.

### O que foi feito?
- Criação dos endpoints `POST /solicitacoes` e `GET /solicitacoes/aluno/{id_aluno}` 
- Regra para que todas as solicitações comecem com o status pendente e a data de postagem com a data e hora atual

### Qual o motivo da alteração?

- Permitir que alunos possam enviar e consultar solicitações

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

- Não possui

---

## Como testar
Descreva o passo a passo para validação:

1. Testar o endpoint `POST /solicitacoes` baseado no seguinte JSON:
```json
{ 
"id_projeto": "UUID do projeto aqui", 
"id_aluno": "UUID do aluno aqui", 
"comprovante": "URL do comprovante aqui", 
"observacao_aluno": "Alguma observação (se houver)" 
}
```
2. Verficar se a solicitação foi criada, se status foi salvo inicialmente como pendente e a data/hora de postagem é a data/hora atual
3. Testar o enpoint `GET /solicitacoes/aluno/{id_aluno}` 
4. Verificar se o GET retorna os dados corretamente

---

## Evidências (opcional)

---

## Impacto
Selecione os impactos deste PR:

- [ ] Sem impacto relevante
- [x] Backend
- [ ] Banco de dados

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
- [ ] Não impacta funcionalidades existentes
- [ ] Testes adicionados ou atualizados (quando aplicável)
- [ ] Documentação atualizada (quando necessário)

---

## Pontos de atenção para revisão
Indique trechos ou decisões que merecem atenção especial:

---

## Deploy
Existe alguma ação necessária para deploy?

- [x] Nenhuma
- [ ] Migration de banco de dados
- [ ] Variáveis de ambiente
- [ ] Configuração adicional

Detalhes:

- 