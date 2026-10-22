# -*- coding: utf-8 -*-
"""Gera index.html (versão web) e print.html (versão para PDF)."""
import html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import *

e = html.escape
OUT = os.path.join(os.path.dirname(__file__), "..")


def table(headers, rows, cls=""):
    h = "".join(f"<th>{e(x)}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


MINDMAP = """
<svg class="mindmap" viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa mental do verbo to be">
  <g stroke="#9aa5b1" stroke-width="2" fill="none">
    <path d="M320 55 L120 120"/><path d="M320 55 L320 120"/><path d="M320 55 L520 120"/>
    <path d="M120 150 L120 185"/><path d="M320 150 L320 185"/><path d="M520 150 L520 185"/>
  </g>
  <rect x="215" y="20" width="210" height="40" rx="20" fill="#1a3a5c"/>
  <text x="320" y="46" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">TO BE (ser / estar)</text>
  <g font-size="15" font-weight="700" text-anchor="middle" fill="#fff">
    <rect x="70" y="120" width="100" height="32" rx="8" fill="#2E7D32"/><text x="120" y="141">AM</text>
    <rect x="270" y="120" width="100" height="32" rx="8" fill="#1565C0"/><text x="320" y="141">IS</text>
    <rect x="470" y="120" width="100" height="32" rx="8" fill="#6A1B9A"/><text x="520" y="141">ARE</text>
  </g>
  <g font-size="13" text-anchor="middle" fill="#1f2933">
    <text x="120" y="202">I</text><text x="120" y="220">I'm</text>
    <text x="320" y="202">He / She / It</text><text x="320" y="220">He's / She's / It's</text>
    <text x="520" y="202">You / We / They</text><text x="520" y="220">You're / We're / They're</text>
  </g>
  <text x="320" y="245" text-anchor="middle" font-size="12" fill="#52606d">Usos: profissão · origem · idade · lugar · estado (tired, busy)</text>
</svg>
"""

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#f5f7fa;color:#1f2933;font-family:"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.55;font-size:15px}
.wrap{max-width:960px;margin:0 auto;padding:0 16px 48px}
header.hero{background:#1a3a5c;color:#fff;padding:48px 16px 40px;text-align:center}
header.hero h1{margin:0 0 8px;font-size:32px}
header.hero p{margin:0;opacity:.85;font-size:17px}
nav.toc{background:#fff;border-bottom:1px solid #e1e5ea;padding:10px 16px;text-align:center;font-size:14px}
nav.toc a{color:#1a3a5c;text-decoration:none;margin:0 8px;font-weight:600;display:inline-block;padding:4px 0}
section{background:#fff;border:1px solid #e1e5ea;border-radius:10px;padding:24px;margin:24px 0}
h2{margin:0 0 12px;font-size:24px;color:#1a3a5c}
h3{page-break-after:avoid;margin:22px 0 8px;font-size:18px;color:#1a3a5c}
.badge{display:inline-block;color:#fff;border-radius:6px;padding:2px 10px;font-weight:700;margin-right:8px}
.meta{color:#52606d;font-size:14px;margin-top:-4px}
.goal{background:#eef4fb;border-left:4px solid #1a3a5c;padding:10px 14px;border-radius:4px;margin:12px 0}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
th,td{border:1px solid #e1e5ea;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f0f3f7;color:#1a3a5c}
tr{page-break-inside:avoid}
.tablewrap{overflow-x:auto}
ol.steps li,ul li{margin:3px 0}
.flow{font-weight:600;color:#1a3a5c}
.tip{background:#fff8e1;border-left:4px solid #f9a825;padding:10px 14px;border-radius:4px;margin:12px 0}
.wrong{color:#c62828}.right{color:#2E7D32;font-weight:600}
.dialogue p{margin:6px 0}.dialogue .pt{color:#52606d;font-size:13px;display:block}
.mindmap{width:100%;max-width:640px;display:block;margin:8px auto}
.check li{list-style:none}.check{padding-left:4px}
footer{text-align:center;color:#52606d;font-size:13px;margin-top:24px}
.pagebreak{page-break-before:always}
.mod{page-break-inside:avoid}
@media (max-width:600px){header.hero h1{font-size:24px}section{padding:16px}}
"""


def build(print_mode=False):
    p = []
    p.append(f'<header class="hero"><h1>{e(TITLE)}</h1><p>{e(SUBTITLE)}</p></header>')
    if not print_mode:
        links = ['<a href="#visao">Visão geral</a>'] + [f'<a href="#{m["code"]}">{m["code"]}</a>' for m in MODULES] + \
                ['<a href="#recursos">Recursos</a>', '<a href="#aula">Aula A1.1</a>']
        p.append('<nav class="toc">' + "".join(links) + "</nav>")
    p.append('<div class="wrap">')

    # Visão geral
    steps = "".join(f"<li><strong>{e(a)}</strong> — {e(b)}</li>" for a, b in STEPS)
    p.append(f"""<section id="visao"><h2>Visão geral</h2><p>{e(OVERVIEW)}</p>
<h3>Como funciona cada aula (13 etapas)</h3><ol class="steps">{steps}</ol>
<h3>Fechamento de cada módulo</h3><p class="flow">{' → '.join(e(c) for c in CLOSING)}</p>
<p>Só avançamos de nível com 80% ou mais na prova.</p>
<h3>Rotina semanal sugerida (1 h/dia)</h3><div class="tablewrap">{table(['Dia','Foco','Tempo'], WEEK)}</div>
<h3>Como pedir as aulas</h3><p>Escreva no chat, por exemplo: <em>"Aula A1.1"</em>, <em>"Corrija meu exercício"</em>, <em>"Simulado do A1"</em> ou <em>"Conversação: entrevista de emprego"</em>.</p></section>""")

    for i, m in enumerate(MODULES):
        skills = "".join(f"<li><strong>{e(a)}:</strong> {e(b)}</li>" for a, b in m["skills"])
        brk = ''
        p.append(f"""<section id="{m['code']}" class="mod{brk}"><h2><span class="badge" style="background:#{m['color']}">{m['code']}</span>{e(m['name'])}</h2>
<div class="meta">Duração estimada: {e(m['weeks'])}</div><div class="goal"><strong>Meta:</strong> {e(m['goal'])}</div>
<div class="tablewrap">{table(['Aula','Gramática / Foco','Vocabulário','Prática'], m['lessons'])}</div><ul>{skills}</ul></section>""")

    res = "".join(f"<li><strong>{e(a)}:</strong> {e(b)}</li>" for a, b in RESOURCES)
    chk = "".join(f"<li>☐ {e(c)}</li>" for c in CHECKLIST)
    p.append(f"""<section id="recursos" class="mod"><h2>Recursos e acompanhamento</h2><ul>{res}</ul>
<h3>Checklist de progresso</h3><ul class="check">{chk}</ul></section>""")

    # Aula
    L = L1
    kid = "".join(f"<p>{e(x)}</p>" for x in L["kid"])
    errs = "".join(f'<tr><td class="wrong">✗ {e(a)}</td><td class="right">✓ {e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in L["errors"])
    exa = "".join(f"<li>{e(x)}</li>" for x in L["ex_a"])
    exb = "".join(f"<li>{e(x)}</li>" for x in L["ex_b"])
    dia = "".join(f'<p><strong>{e(s)}:</strong> {e(t)}<span class="pt">{e(pt)}</span></p>' for s, t, pt in L["dialogue"])
    quiz = "".join(f"<li>{e(q)} " + " ".join(f"({chr(97+j)}) {e(o)}" for j, o in enumerate(opts)) + "</li>" for q, opts in L["quiz"])
    p.append(f"""<section id="aula" class="{'pagebreak' if print_mode else ''}"><h2>{e(L['title'])}</h2>
<h3>1. Explicação para uma criança de 10 anos</h3>{kid}
<h3>2. Explicação profissional</h3><p>{e(L['pro'])}</p><div class="tablewrap">{table(['Pronome','Verbo','Contração'], L['conj'])}</div>
<h3>3, 4 e 5. Exemplos, tradução e pronúncia</h3><div class="tablewrap">{table(['Inglês','Tradução','Pronúncia aproximada'], L['examples'])}</div>
<div class="tip">💡 {e(L['tip'])}</div>
<h3>6. Erros comuns de brasileiros</h3><div class="tablewrap"><table><thead><tr><th>Errado</th><th>Certo</th><th>Por quê</th></tr></thead><tbody>{errs}</tbody></table></div>
<h3>7. Exercícios</h3><p><strong>A) Complete com am, is ou are:</strong></p><ol>{exa}</ol>
<p><strong>B) Traduza para o inglês:</strong></p><ol start="6">{exb}</ol><p><strong>C)</strong> {e(L['ex_c'])}</p>
<h3>8. Correção</h3><p>Envie suas respostas no chat: cada uma é corrigida e explicada.</p>
<h3>9. Diálogo — primeiro dia no trabalho</h3><div class="dialogue">{dia}</div>
<h3>10. Flashcards</h3><div class="tablewrap">{table(['Frente','Verso'], L['flashcards'])}</div>
<h3>11. Mapa mental</h3>{MINDMAP}
<h3>12. Teste rápido</h3><ol>{quiz}</ol>
<h3>13. Simulado</h3><p>O primeiro simulado sai ao final da Aula A1.3, misturando as três primeiras aulas.</p></section>""")
    p.append('<footer>Plano de Estudos de Inglês · atualizado em 21/10/2026</footer></div>')

    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Plano de Inglês A1–C2</title>
<style>{CSS}</style></head><body>{''.join(p)}</body></html>"""


if __name__ == "__main__":
    open(os.path.join(OUT, "site", "extras", "plano-a1-c2.html"), "w", encoding="utf-8").write(build(False))
    open(os.path.join(os.path.dirname(__file__), "print.html"), "w", encoding="utf-8").write(build(True))
    print("ok")
