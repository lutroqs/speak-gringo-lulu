# -*- coding: utf-8 -*-
"""Gera o guia de 5 anos: site/index.html (web) e Guia-Ingles-5-Anos.pdf (via print.html + wkhtmltopdf)."""
import glob, os, re, subprocess, markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "guia")
TITLE = "Speak Gringo — Inglês do zero ao C2 em 5 anos"

files = sorted(glob.glob(os.path.join(SRC, "*.md")))
md_text = "\n\n".join(open(f, encoding="utf-8").read() for f in files)
body = markdown.markdown(md_text, extensions=["tables", "attr_list", "fenced_code", "nl2br", "sane_lists"])
body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")

# Navegação: H1 com id
nav = re.findall(r'<h1 id="([^"]+)">(.*?)</h1>', body)
nav_html = "".join(f'<a href="#{i}">{re.sub("<.*?>", "", t)}</a>' for i, t in nav)

# Cada H1 abre uma seção (para cartões na web e quebras de página no PDF)
parts = re.split(r'(?=<h1 id=)', body)
body_sections = "".join(f'<section class="chap">{p}</section>' for p in parts if p.strip())

WEB_CSS = """
:root{--bg:#f6f4ef;--card:#fff;--ink:#1d2433;--muted:#5b6475;--line:#e4e0d6;--brand:#0f3d3e;--accent:#e2725b;--soft:#eef3f1;--code:#f3efe6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11161d;--card:#18202a;--ink:#e8ecf2;--muted:#9aa6b6;--line:#2a3442;--brand:#7cc8b8;--accent:#f0957f;--soft:#1d2a2b;--code:#1f2833}}
:root[data-theme="dark"]{--bg:#11161d;--card:#18202a;--ink:#e8ecf2;--muted:#9aa6b6;--line:#2a3442;--brand:#7cc8b8;--accent:#f0957f;--soft:#1d2a2b;--code:#1f2833}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Inter",system-ui,-apple-system,"Segoe UI",sans-serif}
.hero{background:var(--brand);color:#fff;padding:56px 16px 48px;text-align:center}
:root[data-theme="dark"] .hero{color:#0b1a1b}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .hero{color:#0b1a1b}}
.hero small{letter-spacing:.18em;text-transform:uppercase;font-weight:700;opacity:.85}
.hero h1{font:700 clamp(28px,5vw,46px)/1.15 "Fraunces",Georgia,serif;margin:10px 0}
.hero p{margin:0 auto;max-width:640px;opacity:.9}
.pills{margin-top:22px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.pills span{border:1px solid currentColor;border-radius:99px;padding:4px 12px;font-size:14px;opacity:.9}
.layout{max-width:1200px;margin:0 auto;padding:0 16px;display:grid;grid-template-columns:240px 1fr;gap:28px}
nav.side{position:sticky;top:16px;align-self:start;margin-top:28px;display:flex;flex-direction:column;gap:2px;max-height:calc(100vh - 32px);overflow:auto}
nav.side a{color:var(--muted);text-decoration:none;padding:6px 10px;border-radius:8px;font-size:14px}
nav.side a:hover{background:var(--soft);color:var(--brand)}
.side .dl{margin-top:12px;background:var(--accent);color:#fff;font-weight:600;text-align:center}
main{min-width:0}
section.chap{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:28px;margin:28px 0}
h1{font:700 30px/1.2 "Fraunces",Georgia,serif;color:var(--brand);margin:0 0 14px}
h2{font:700 22px/1.25 "Fraunces",Georgia,serif;margin:30px 0 10px;padding-top:10px;border-top:1px solid var(--line)}
h3{font-size:18px;margin:22px 0 8px}
a{color:var(--brand)}
.tw{overflow-x:auto;margin:12px 0}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--soft);color:var(--brand);font-weight:700}
blockquote{margin:14px 0;padding:12px 16px;background:var(--soft);border-left:4px solid var(--accent);border-radius:0 10px 10px 0}
pre{background:var(--code);border-radius:10px;padding:14px 16px;overflow-x:auto;font-size:14px;line-height:1.5}
code{font-family:"JetBrains Mono",ui-monospace,monospace}
footer{color:var(--muted);text-align:center;font-size:14px;padding:24px 0 48px}
.top{display:none}
@media (max-width:860px){.layout{grid-template-columns:1fr}nav.side{display:none}
.top{display:flex;gap:6px;overflow-x:auto;padding:10px 16px;background:var(--card);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.top a{white-space:nowrap;color:var(--brand);text-decoration:none;font-size:14px;font-weight:600;padding:4px 10px;border-radius:99px;background:var(--soft)}
section.chap{padding:18px}}
"""

PRINT_CSS = """
body{margin:0;color:#1d2433;font:11.5pt/1.5 "DejaVu Sans",Helvetica,Arial,sans-serif}
.cover{height:1000px;background:#0f3d3e;color:#fff;padding:280px 60px 0;page-break-after:always}
.cover small{letter-spacing:3px;font-weight:bold;color:#f4b9a9}
.cover h1{font:bold 40pt/1.15 Georgia,serif;color:#fff;margin:16px 0}
.cover p{font-size:15pt;color:#d6e6e2}
.toc{page-break-after:always;padding:20px 0}
.toc h1{font:bold 24pt Georgia,serif;color:#0f3d3e}
.toc a{display:block;color:#1d2433;text-decoration:none;padding:6px 0;border-bottom:1px solid #e4e0d6;font-size:13pt}
section.chap{page-break-before:always}
h1{font:bold 24pt/1.2 Georgia,serif;color:#0f3d3e;margin:0 0 12px}
h2{font:bold 16pt/1.25 Georgia,serif;color:#0f3d3e;margin:22px 0 8px;page-break-after:avoid}
h3{font-size:13pt;margin:16px 0 6px;page-break-after:avoid}
a{color:#0f3d3e}
table{border-collapse:collapse;width:100%;font-size:9.5pt;margin:8px 0}
tr,blockquote,pre{page-break-inside:avoid}
th,td{border:1px solid #e4e0d6;padding:5px 7px;text-align:left;vertical-align:top}
th{background:#eef3f1;color:#0f3d3e}
blockquote{margin:10px 0;padding:8px 12px;background:#eef3f1;border-left:4px solid #e2725b}
pre{background:#f3efe6;padding:10px 12px;font-size:10pt;white-space:pre-wrap}
"""

PILLS = '<div class="pills"><span>A1 → C2</span><span>5 anos</span><span>B2 First · C1 Advanced · C2 Proficiency</span><span>Aulas em 14 etapas</span></div>'

web = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Speak Gringo — Inglês A1 a C2</title>
<meta name="description" content="Plano completo de 5 anos para ir do zero ao C2 em inglês, com preparação para Cambridge B2 First, C1 Advanced e C2 Proficiency.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>{WEB_CSS}</style></head><body>
<header class="hero"><small>Professor particular de inglês</small><h1>Do zero ao C2 em 5 anos</h1>
<p>Plano completo para viver, estudar e trabalhar em inglês, com preparação para as certificações Cambridge.</p>{PILLS}</header>
<nav class="top">{nav_html}</nav>
<div class="layout"><nav class="side">{nav_html}<a class="dl" href="Guia-Ingles-5-Anos.pdf">Baixar PDF</a><a href="extras/plano-a1-c2.html">Plano anterior (A1–C2)</a></nav>
<main>{body_sections}<footer>Speak Gringo · guia atualizado em 21/10/2026 · <a href="Guia-Ingles-5-Anos.pdf">PDF</a></footer></main></div>
</body></html>"""

toc = "".join(f'<a href="#{i}">{re.sub("<.*?>", "", t)}</a>' for i, t in nav)
prn = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{TITLE}</title><style>{PRINT_CSS}</style></head><body>
<div class="cover"><small>PROFESSOR PARTICULAR DE INGLÊS</small><h1>Do zero ao C2<br>em 5 anos</h1>
<p>Plano completo com preparação para Cambridge B2 First, C1 Advanced e C2 Proficiency</p><p style="margin-top:220px;font-size:11pt">Speak Gringo · 21/10/2026</p></div>
<div class="toc"><h1>Sumário</h1>{toc}</div>{body_sections}</body></html>"""

site = os.path.join(ROOT, "site")
os.makedirs(site, exist_ok=True)
open(os.path.join(site, "index.html"), "w", encoding="utf-8").write(web)
pp = os.path.join(os.path.dirname(__file__), "print_guia.html")
open(pp, "w", encoding="utf-8").write(prn)
subprocess.run(["wkhtmltopdf", "--quiet", "-s", "A4", "--margin-top", "14", "--margin-bottom", "14",
                "--margin-left", "12", "--margin-right", "12", "--title", TITLE, pp,
                os.path.join(site, "Guia-Ingles-5-Anos.pdf")], stderr=subprocess.DEVNULL)
print("ok", len(nav), "capítulos")
