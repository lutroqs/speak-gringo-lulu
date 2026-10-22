# -*- coding: utf-8 -*-
"""Lê luisa/*.txt e gera:
- site/luisa-data.json (dados do app)
- site/Ingles-da-Luisa.pdf (caderno com pronúncia + lições estilo app)
- site/app.html (app estilo Duolingo, a partir de build/app_template.html)
Formato das linhas: NÍVEL | inglês | pronúncia | português  (NÍVEL = B, I ou A)
"""
import glob, html, json, os, random, re, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site")
LV = {"B": "Básico", "I": "Intermediário", "A": "Avançado"}
e = html.escape


def say_text(en):
    t = re.sub(r"\([^)]*\)", "", en)
    if "→" in t:
        t = t.split("→")[-1]
    elif " — " in t:
        left, right = t.split(" — ", 1)
        t = (left + ". " + right) if re.search(r"[A-Za-z]", left) else right
    t = t.replace(" / ", ", ").replace("≠", ",").replace('"', "")
    return re.sub(r"\s+", " ", t).strip(" .,") + "."


def clean_for_build(en):
    if re.search(r"[—→/()=≠+:;\"…]", en):
        return False
    n = len(en.split())
    return 2 <= n <= 9


blocks = []
for f in sorted(glob.glob(os.path.join(ROOT, "luisa", "*.txt"))):
    blk, sec = None, None
    for line in open(f, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("@block"):
            bid, title, intro = [x.strip() for x in line[6:].split("|", 2)]
            blk = {"id": bid, "title": title, "intro": intro, "sections": []}
            blocks.append(blk)
        elif line.startswith("## "):
            sec = {"title": line[3:].strip(), "items": []}
            blk["sections"].append(sec)
        elif re.match(r"^[BIA] \|", line):
            lv, en, pr, pt = [x.strip() for x in line.split("|")]
            sec["items"].append({"lv": lv, "en": en, "pr": pr, "pt": pt,
                                 "say": say_text(en), "build": clean_for_build(en)})

total = sum(len(s["items"]) for b in blocks for s in b["sections"])
json.dump(blocks, open(os.path.join(SITE, "luisa-data.json"), "w", encoding="utf-8"), ensure_ascii=False)

# ---------- PDF ----------
rng = random.Random(21112000)


def lesson(b):
    items = [i for s in b["sections"] for i in s["items"]]
    build = [i for i in items if i["build"]]
    rng.shuffle(build)
    out, key = [], []
    n = 1
    for it in build[:4]:
        out.append(f"<li><b>Traduza:</b> {e(it['pt'])}</li>"); key.append(f"{n}. {e(it['en'])}"); n += 1
    for it in build[4:8]:
        w = it["en"].split(); s = w[:]
        while s == w and len(w) > 1:
            rng.shuffle(s)
        out.append(f"<li><b>Monte a frase:</b> <span class='tiles'>{' '.join(f'<i>{e(x)}</i>' for x in s)}</span> <small>({e(it['pt'])})</small></li>")
        key.append(f"{n}. {e(it['en'])}"); n += 1
    for it in build[8:12]:
        w = it["en"].split()
        if len(w) < 3:
            continue
        k = max(range(len(w)), key=lambda j: len(re.sub(r"\W", "", w[j])))
        blank = " ".join("_____" if j == k else w[j] for j in range(len(w)))
        out.append(f"<li><b>Complete:</b> {e(blank)} <small>({e(it['pt'])})</small></li>")
        key.append(f"{n}. {e(re.sub(r'[^\w\']', '', w[k]))}"); n += 1
    return (f"<h2>Lição prática (estilo app)</h2><ol class='ex'>{''.join(out)}</ol>"
            f"<p class='key'><b>Gabarito:</b> {' · '.join(key)}</p>")


chapters = []
toc = []
for b in blocks:
    cnt = sum(len(s["items"]) for s in b["sections"])
    toc.append(f"<a href='#{b['id']}'>{e(b['title'])}<span>{cnt} itens</span></a>")
    h = [f"<section class='chap' id='{b['id']}'><h1>{e(b['title'])}</h1><p class='intro'>{e(b['intro'])} <b>{cnt} itens.</b></p>"]
    for s in b["sections"]:
        rows = "".join(
            f"<tr><td><span class='lv {i['lv'].lower()}'>{LV[i['lv']]}</span></td><td class='en'>{e(i['en'])}</td>"
            f"<td class='pr'>{e(i['pr'])}</td><td>{e(i['pt'])}</td></tr>" for i in s["items"])
        h.append(f"<h2>{e(s['title'])}</h2><table><thead><tr><th>Nível</th><th>Inglês</th><th>Pronúncia</th><th>Português</th></tr></thead><tbody>{rows}</tbody></table>")
    h.append(lesson(b))
    h.append("</section>")
    chapters.append("".join(h))

CSS = """
body{margin:0;color:#1d2433;font:10.5pt/1.45 "DejaVu Sans",Helvetica,Arial,sans-serif}
.cover{height:1000px;background:#0f3d3e;color:#fff;padding:260px 60px 0;page-break-after:always}
.cover small{letter-spacing:3px;font-weight:bold;color:#f4b9a9}
.cover h1{font:bold 40pt/1.1 Georgia,serif;color:#fff;margin:16px 0}
.cover p{font-size:14pt;color:#d6e6e2;margin:6px 0}
.cover .me{margin-top:60px;font-size:11pt;color:#b9d3cd;line-height:1.7}
.toc{page-break-after:always}
.toc h1{font:bold 24pt Georgia,serif;color:#0f3d3e}
.toc a{display:block;color:#1d2433;text-decoration:none;padding:7px 0;border-bottom:1px solid #e4e0d6;font-size:12.5pt}
.toc a span{float:right;color:#5b6475}
.howto{background:#eef3f1;padding:12px 16px;margin-top:18px;font-size:10.5pt}
section.chap{page-break-before:always}
h1{font:bold 22pt/1.2 Georgia,serif;color:#0f3d3e;margin:0 0 6px}
.intro{color:#5b6475;margin:0 0 10px}
h2{font:bold 13.5pt/1.25 Georgia,serif;color:#0f3d3e;margin:16px 0 6px;page-break-after:avoid}
table{border-collapse:collapse;width:100%;font-size:9pt}
tr{page-break-inside:avoid}
th,td{border:1px solid #e4e0d6;padding:4px 6px;text-align:left;vertical-align:top}
th{background:#eef3f1;color:#0f3d3e}
td.en{font-weight:bold;width:32%}
td.pr{color:#8a3b2d;font-style:italic;width:24%}
.lv{color:#fff;font-weight:bold;font-size:7.5pt;padding:1px 5px;white-space:nowrap}
.lv.b{background:#2e7d5b}.lv.i{background:#c98a1b}.lv.a{background:#b8433a}
ol.ex li{margin:5px 0}
.tiles i{font-style:normal;border:1px solid #0f3d3e;border-radius:4px;padding:0 5px;margin-right:3px;background:#fff}
.key{font-size:9pt;color:#5b6475;border-top:1px dashed #c8c2b4;padding-top:6px}
"""
cover = ("<div class='cover'><small>CADERNO PERSONALIZADO</small><h1>O inglês<br>da Luisa</h1>"
         f"<p>{total} frases e palavras com pronúncia, em três níveis</p><p>Com lições práticas no estilo app em cada bloco</p>"
         "<div class='me'>Luisa · 25 anos (21/11/2000) · São Paulo<br>Administração · Estagiária de Operações<br>"
         "Rumo à vaga CLT e ao inglês fluente · Speak Gringo · 21/10/2026</div></div>")
howto = ("<div class='howto'><b>Como ler a pronúncia:</b> a sílaba em MAIÚSCULAS é a forte. "
         "<b>th</b> = língua entre os dentes (como um \"d\" ou \"f\" soprado); <b>r</b> no começo da sílaba (rái = hi, rôum = home) é o som do H inglês, um \"rr\" de \"carro\" bem suave, só com ar; "
         "<b>â</b> = o \"a\" fechado de \"cama\". Para ouvir qualquer frase com voz nativa, use o app (botão de áudio).</div>")
doc = (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>O inglês da Luisa</title><style>{CSS}</style></head><body>"
       f"{cover}<div class='toc'><h1>Sumário</h1>{''.join(toc)}{howto}</div>{''.join(chapters)}</body></html>")
pp = os.path.join(os.path.dirname(__file__), "print_luisa.html")
open(pp, "w", encoding="utf-8").write(doc)
subprocess.run(["wkhtmltopdf", "--quiet", "-s", "A4", "--margin-top", "12", "--margin-bottom", "12", "--margin-left", "10",
                "--margin-right", "10", "--title", "O inglês da Luisa", pp, os.path.join(SITE, "Ingles-da-Luisa.pdf")],
               stderr=subprocess.DEVNULL)

# ---------- App ----------
tpl = os.path.join(os.path.dirname(__file__), "app_template.html")
if os.path.exists(tpl):
    app = open(tpl, encoding="utf-8").read().replace("/*__DATA__*/[]", json.dumps(blocks, ensure_ascii=False))
    open(os.path.join(os.path.dirname(__file__), "app_artifact.html"), "w", encoding="utf-8").write(app)
    page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
            + app + '</body></html>')
    open(os.path.join(SITE, "app.html"), "w", encoding="utf-8").write(page)

print("ok", len(blocks), "blocos", total, "itens")
