import pandas as pd
import json
import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:3b"

perfil = pd.read_json("./data/perfil_investidor.json", typ="series")
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))
historico = pd.read_csv("./data/historico_atendimento.csv")
transacoes = pd.read_csv("./data/transacoes.csv")

contexto = f""" 
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO:{perfil['patrimonio_total']} | RESERVA R${perfil['reserva_emergencia_atual']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTO DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """

Voce é o Maestro, um auxiliar financeiro didático que ajuda o usuário a organizar suas financias

Objetivo:
Ensinar a auxiliar na financias de forma clara, usando os dados do cliente como exemplos práticos
REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
-Se essa informação não estiver disponivel, deixe claro
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Seja um tipo de amigo consultor, ajudando o usuário
5. Pergunte se o que foi dito está claro.
6. Não tome decisão pelo usuário
7.Utilize exemplos claros
8. Caso não tenha informação o suficiente, faça pergunta para conseguir os dados.

"""


def perguntar(msg, history):
    prompt = f"""{SYSTEM_PROMPT}
    
    CONTEXTO CLIENTE:
    {contexto}
    
    Pergunta: {msg}
    """
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": 300},
        },
    )
    print(r.text)
    if r.status_code != 200:
        return (
            "Erro na requisição para o modelo. Por favor, tente novamente mais tarde."
        )

    dados = r.json()
    if "response" not in dados:
        return "Ollama retornou algo inesperado. Por favor, tente novamente mais tarde.{dados}"

    return dados["response"]


gr.ChatInterface(
    fn=perguntar,
    title="Maestro - Assistente Financeiro",
    description="Um assistente financeiro que ajuda a organizar suas finanças com base em seus dados pessoais e históricos de transações.",
).launch()
