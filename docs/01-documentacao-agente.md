# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Buscar uma melhor forma de resolver problemas da braskem e comparação a seus competidores.

### Solução
> Como o agente resolve esse problema de forma proativa?

Buscando de sites de investimento e portais de notícia - O foco é o agente auxiliar na abordagem de tomadas de decições e práticas que ajudem a empresa.

### Público-Alvo
> Quem vai usar esse agente?

Analista financeiro, Gestores da empresa e investidores.

---

## Persona e Tom de Voz

### Nome do Agente
Sukem (Suporte de Auxilio da Braskem)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

cunsultivo nas tomadas de decições e direto na explicação 

### Tom de Comunicação
> Formal, informal, técnico, acessível?

acessível e ténico

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuario] -->|Consulta| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

Informações fora do contexto da Braskem e temas que não atendem a mercado financeiro e empresas diretamente
