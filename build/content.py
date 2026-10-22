# -*- coding: utf-8 -*-
"""Conteúdo único usado para gerar HTML, PDF e PPTX."""

TITLE = "Plano de Estudos de Inglês: A1 → C2"
SUBTITLE = "Do iniciante à fluência profissional para empresas internacionais"

OVERVIEW = (
    "O objetivo é sair do zero e chegar a inglês profissional (C1/C2) para trabalhar em "
    "empresas internacionais, com foco em negócios, dados, finanças e tecnologia. "
    "Com 1 hora por dia, 5 dias por semana, o caminho completo leva cerca de 18 a 24 meses."
)

STEPS = [
    ("Explicação para criança de 10 anos", "a ideia em linguagem simples"),
    ("Explicação profissional", "a regra completa, com termos técnicos"),
    ("Exemplos", "frases do dia a dia e do trabalho"),
    ("Tradução", "cada exemplo em português"),
    ("Pronúncia", "escrita aproximada para falantes de português"),
    ("Erros comuns", "os deslizes típicos de brasileiros"),
    ("Exercícios", "você responde no chat"),
    ("Correção", "cada erro corrigido e explicado"),
    ("Diálogos", "situações reais de trabalho"),
    ("Flashcards", "frente/verso para revisar"),
    ("Mapa mental", "a aula inteira num esquema visual"),
    ("Teste rápido", "5 a 10 questões"),
    ("Simulado", "formato de prova, misturando aulas anteriores"),
]

CLOSING = ["Flashcards", "Prova", "Questões", "Conversação simulada", "Feedback", "Plano de revisão"]

WEEK = [
    ("Segunda", "Gramática (aula nova)", "60 min"),
    ("Terça", "Vocabulário + flashcards", "60 min"),
    ("Quarta", "Listening (podcast/série)", "60 min"),
    ("Quinta", "Speaking (diálogo simulado)", "60 min"),
    ("Sexta", "Writing + teste da semana", "60 min"),
    ("Fim de semana", "Revisão leve de flashcards", "15 min/dia"),
]

MODULES = [
    {
        "code": "A1", "name": "Iniciante", "weeks": "8 a 10 semanas", "color": "2E7D32",
        "goal": "Apresentar-se, falar da rotina e do trabalho com frases simples e entender perguntas básicas.",
        "lessons": [
            ("A1.1", "Verbo To Be (afirmativa)", "Cumprimentos, nomes, países", "Apresentar-se"),
            ("A1.2", "To Be (negativa e perguntas)", "Profissões e cargos", "Perguntar \"What do you do?\""),
            ("A1.3", "Pronomes, this/that, a/an", "Escritório, números 0–100", "Descrever sua mesa"),
            ("A1.4", "Present Simple (afirmativa)", "Rotina, dias, horas", "Falar da sua rotina"),
            ("A1.5", "Present Simple (negativa, do/does)", "Departamentos (HR, Finance, IT)", "Explicar onde trabalha"),
            ("A1.6", "Advérbios de frequência", "Tecnologia básica", "Frequência de tarefas"),
            ("A1.7", "There is / There are", "Excel básico (cell, row, column)", "Descrever uma planilha"),
            ("A1.8", "Can / Can't", "Habilidades e softwares", "Dizer o que você sabe fazer"),
        ],
        "skills": [
            ("Speaking", "Apresentação pessoal de 1 minuto; small talk básico."),
            ("Listening", "Áudios lentos (BBC Learning English, VOA Learning English)."),
            ("Writing", "Email curto de apresentação (5 linhas)."),
            ("Fechamento", "80 flashcards, prova de 30 questões, conversação \"primeiro dia no trabalho\"."),
        ],
    },
    {
        "code": "A2", "name": "Básico", "weeks": "10 a 12 semanas", "color": "558B2F",
        "goal": "Falar do que está acontecendo agora, do passado e de planos; escrever emails simples de trabalho.",
        "lessons": [
            ("A2.1", "Present Continuous", "Tarefas e projetos em andamento", "\"I'm working on the report\""),
            ("A2.2", "Present Simple x Continuous", "Reuniões (agenda, attendee)", "Status rápido em reunião"),
            ("A2.3", "Past Simple (regulares)", "Negócios (client, sales, deal)", "Contar o que fez ontem"),
            ("A2.4", "Past Simple (irregulares)", "Dados básicos (data, table, chart)", "Relatar tarefa concluída"),
            ("A2.5", "Future: will x going to", "Prazos (deadline, due date, ASAP)", "Planejar a semana"),
            ("A2.6", "Comparativos e superlativos", "Finanças (cost, revenue, profit)", "Comparar resultados"),
            ("A2.7", "Modais: should, must, have to", "RH (hire, salary, benefits)", "Dar recomendações"),
            ("A2.8", "Countable / uncountable", "Excel (formula, SUM, filter, sort)", "Explicar uma planilha"),
        ],
        "skills": [
            ("Speaking", "Status de projeto em 2 minutos; pedir ajuda a colegas."),
            ("Listening", "Podcasts curtos e séries com legenda em inglês."),
            ("Writing", "Emails de pedido, confirmação e agradecimento."),
            ("Fechamento", "120 flashcards, prova de 40 questões, conversação \"daily meeting\"."),
        ],
    },
    {
        "code": "B1", "name": "Intermediário", "weeks": "12 a 14 semanas", "color": "1565C0",
        "goal": "Participar de reuniões, contar experiências profissionais e se virar em uma entrevista simples.",
        "lessons": [
            ("B1.1", "Present Perfect", "Experiência profissional", "\"I have worked with Power BI for 2 years\""),
            ("B1.2", "Present Perfect x Past Simple", "Entrevistas (strengths, background)", "\"Tell me about yourself\""),
            ("B1.3", "Past Continuous", "Problemas e incidentes", "Contar um problema que resolveu"),
            ("B1.4", "Modais de possibilidade", "Tecnologia (cloud, software, bug)", "Discutir riscos"),
            ("B1.5", "Passive Voice (presente e passado)", "Processos e dados (dataset, pipeline)", "Descrever um processo"),
            ("B1.6", "Zero e First Conditional", "Finanças (budget, forecast, cash flow)", "Cenários \"If we cut costs…\""),
            ("B1.7", "Gerund x Infinitive", "Power BI (dashboard, measure, DAX)", "Apresentar um dashboard"),
            ("B1.8", "Phrasal verbs de trabalho", "Reuniões (follow up, wrap up)", "Conduzir uma reunião curta"),
        ],
        "skills": [
            ("Speaking", "Entrevista simulada (10 perguntas clássicas); opinar em reunião."),
            ("Listening", "Podcasts de negócios e notícias lentas; séries sem legenda em português."),
            ("Writing", "Currículo em inglês (versão 1) e resumo do LinkedIn."),
            ("Fechamento", "150 flashcards, prova de 50 questões, entrevista de emprego simulada completa."),
        ],
    },
    {
        "code": "B2", "name": "Intermediário-avançado", "weeks": "14 a 16 semanas", "color": "6A1B9A",
        "goal": "Trabalhar em inglês no dia a dia: apresentar resultados, negociar prazos e escrever relatórios claros.",
        "lessons": [
            ("B2.1", "Second Conditional", "Estratégia (market share, KPI)", "Propor alternativas"),
            ("B2.2", "Third Conditional", "Lições aprendidas (post-mortem)", "Analisar um projeto que falhou"),
            ("B2.3", "Reported Speech (afirmações)", "Reuniões (minutes, action items)", "Resumir o que o chefe disse"),
            ("B2.4", "Reported Speech (perguntas e ordens)", "RH (performance review, feedback)", "Repassar feedback"),
            ("B2.5", "Passive Voice avançada", "Contabilidade (ledger, accrual)", "Explicar o fechamento do mês"),
            ("B2.6", "Relative clauses", "Python (function, library, pandas)", "Explicar um script"),
            ("B2.7", "Modais no passado", "Análise de dados (trend, outlier)", "Comentar um resultado"),
            ("B2.8", "Conectores (however, therefore)", "Apresentações (agenda, takeaway)", "Apresentação de 5 minutos"),
        ],
        "skills": [
            ("Speaking", "Apresentação de resultados; negociação de prazo; networking em evento."),
            ("Listening", "Podcasts nativos (HBR IdeaCast, Planet Money), notícias em velocidade normal."),
            ("Writing", "Relatório de 1 página, emails difíceis, posts no LinkedIn."),
            ("Fechamento", "200 flashcards, prova de 60 questões, reunião simulada com cliente internacional."),
        ],
    },
    {
        "code": "C1", "name": "Avançado", "weeks": "16 a 20 semanas", "color": "C62828",
        "goal": "Falar com fluência e precisão em qualquer situação profissional, inclusive sob pressão.",
        "lessons": [
            ("C1.1", "Mixed Conditionals", "Tomada de decisão executiva", "Defender uma recomendação"),
            ("C1.2", "Inversão (Not only…, Had I known…)", "Linguagem formal de relatórios", "Abrir uma apresentação com impacto"),
            ("C1.3", "Cleft sentences", "Finanças (EBITDA, margin, ROI)", "Explicar resultados trimestrais"),
            ("C1.4", "Modais de dedução", "Data storytelling", "Contar a história dos dados"),
            ("C1.5", "Hedging e linguagem diplomática", "Negociação e conflito", "Discordar com educação"),
            ("C1.6", "Collocations e idioms", "Idioms de negócios", "Small talk natural"),
            ("C1.7", "Nominalização", "Tecnologia (ML, API, ETL)", "Explicar projeto técnico para leigos"),
            ("C1.8", "Revisão integrada de tempos", "Liderança e gestão", "Conduzir reunião de equipe"),
        ],
        "skills": [
            ("Speaking", "Entrevista para vaga sênior (método STAR); pitch de 3 minutos."),
            ("Listening", "Filmes e séries sem legenda, conferências (TED, earnings calls)."),
            ("Writing", "Currículo final, LinkedIn completo, relatório executivo, slides."),
            ("Fechamento", "250 flashcards, prova de 70 questões, painel de entrevista simulado."),
        ],
    },
    {
        "code": "C2", "name": "Proficiência", "weeks": "16+ semanas (contínuo)", "color": "37474F",
        "goal": "Comunicar-se como um profissional nativo: nuance, tom, humor e persuasão.",
        "lessons": [
            ("C2.1", "Registro e tom", "Formal, neutro, informal", "Mesmo email para CEO, colega e cliente"),
            ("C2.2", "Persuasão e retórica", "Business case", "Pedir investimento"),
            ("C2.3", "Ironia, humor e subentendidos", "Indiretas em reuniões", "Entender o não dito"),
            ("C2.4", "Pronúncia avançada", "Entonação, connected speech", "Shadowing de discursos"),
            ("C2.5", "Escrita executiva concisa", "Memos para diretoria", "Memo de uma página"),
            ("C2.6", "Debate e argumentação", "Estratégia", "Debate simulado"),
            ("C2.7", "Variações de sotaque", "EUA, Reino Unido, Índia, Austrália", "Listening multicultural"),
            ("C2.8", "Projeto final", "Tudo", "Apresentação de 15 min + Q&A difícil"),
        ],
        "skills": [
            ("Speaking", "Negociações, crises, liderança de reuniões globais."),
            ("Listening", "Qualquer conteúdo nativo, sotaques variados."),
            ("Writing", "Documentos estratégicos, artigos no LinkedIn."),
            ("Fechamento", "Simulado no formato de prova oficial (IELTS, TOEFL ou Cambridge C2) e plano de manutenção."),
        ],
    },
]

RESOURCES = [
    ("Flashcards", "Anki (repetição espaçada): importe os cards de cada aula."),
    ("Pronúncia", "YouGlish (palavras em vídeos reais) e dicionário Cambridge online."),
    ("Listening", "BBC Learning English, VOA Learning English, podcasts de negócios, séries com legenda em inglês."),
    ("Speaking", "Gravar-se no celular e conversação simulada com o professor."),
]

CHECKLIST = [
    "A1 concluído (prova ≥ 80%)", "A2 concluído (prova ≥ 80%)", "B1 concluído (prova ≥ 80%)",
    "B2 concluído (prova ≥ 80%)", "C1 concluído (prova ≥ 80%)", "C2 concluído (simulado oficial)",
    "Currículo em inglês pronto", "LinkedIn em inglês pronto", "Primeira entrevista real em inglês",
]

# ---------------- Aula A1.1 ----------------
L1 = {
    "title": "Aula A1.1 — Verbo To Be (afirmativa)",
    "kid": [
        "O verbo to be é o verbo \"ser\" e \"estar\" ao mesmo tempo.",
        "Ele muda de roupa dependendo de quem fala: I usa AM; He / She / It usam IS; You / We / They usam ARE.",
        "É como um uniforme: cada pessoa tem o seu.",
    ],
    "pro": (
        "O to be é um verbo irregular que funciona como verbo de ligação (linking verb): conecta o sujeito "
        "a um estado, identidade, cargo, lugar ou característica. No presente tem três formas: am / is / are. "
        "Em inglês o sujeito é obrigatório: não dá para dizer só \"Is analyst\"."
    ),
    "conj": [
        ("I", "am", "I'm"), ("You", "are", "You're"), ("He / She / It", "is", "He's / She's / It's"),
        ("We", "are", "We're"), ("They", "are", "They're"),
    ],
    "examples": [
        ("I am a data analyst.", "Eu sou analista de dados.", "ai ém a dêira ÉN-a-list"),
        ("She is in a meeting.", "Ela está em uma reunião.", "xi iz in a MÍ-rin"),
        ("We are from Brazil.", "Nós somos do Brasil.", "uí ar from bra-ZIL"),
        ("It is urgent.", "É urgente.", "it iz ÂR-djent"),
        ("They are my colleagues.", "Eles são meus colegas.", "dêi ar mai CÓ-ligz"),
    ],
    "tip": "O som do TH em \"they\": ponha a ponta da língua entre os dentes e diga \"d\". Não é \"dei\" nem \"zei\".",
    "errors": [
        ("Is my boss.", "He is my boss.", "sujeito obrigatório"),
        ("I have 30 years.", "I am 30 years old.", "idade usa to be"),
        ("I am agree.", "I agree.", "agree já é verbo"),
        ("She are tired.", "She is tired.", "she usa is"),
        ("She's a analyst.", "She's an analyst.", "an antes de som de vogal"),
    ],
    "ex_a": [
        "I ___ a financial analyst.", "My manager ___ from Canada.", "The reports ___ ready.",
        "You ___ very organized.", "Excel ___ an important tool.",
    ],
    "ex_b": ["Eu sou do Brasil.", "Ela está no escritório.", "Nós somos uma equipe."],
    "ex_c": "Escreva 3 frases sobre você (nome, profissão, cidade).",
    "dialogue": [
        ("Sarah", "Hi! I'm Sarah. I'm the HR manager.", "Oi! Sou a Sarah, gerente de RH."),
        ("You", "Nice to meet you, Sarah. I'm Lucas. I'm the new data analyst.", "Prazer, Sarah. Sou o Lucas, o novo analista de dados."),
        ("Sarah", "Welcome! Where are you from?", "Bem-vindo! De onde você é?"),
        ("You", "I'm from São Paulo, Brazil.", "Sou de São Paulo, Brasil."),
        ("Sarah", "Great! Your team is on the third floor. They are very friendly.", "Ótimo! Sua equipe fica no terceiro andar. Eles são muito simpáticos."),
    ],
    "flashcards": [
        ("I ___", "am"), ("She / He / It ___", "is"), ("You / We / They ___", "are"),
        ("\"Eu tenho 25 anos\"", "I am 25 years old"), ("Contração de they are", "they're"),
        ("colleague", "colega de trabalho"),
    ],
    "quiz": [
        ("They ___ in the meeting room.", ["is", "am", "are"]),
        ("Qual está correto?", ["I have 28 years", "I am 28 years old"]),
        ("\"She is\" contraído fica:", ["She's", "Shes'", "S'is"]),
        ("___ is a great tool.", ["Power BI", "Are", "Am"]),
    ],
}
