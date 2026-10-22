# speak-gringo-lulu

Guia completo para ir do zero ao **C2 em inglês em 5 anos**, com preparação para as certificações Cambridge **B2 First**, **C1 Advanced** e **C2 Proficiency**. Pensado para viver, estudar e trabalhar em um país de língua inglesa e em empresas internacionais (dados, finanças, tecnologia).

## Onde abrir

| Arquivo | O que é |
| --- | --- |
| [`site/index.html`](site/index.html) | Site do guia (o mesmo publicado na Vercel) |
| [`site/Guia-Ingles-5-Anos.pdf`](site/Guia-Ingles-5-Anos.pdf) | Guia completo em PDF (39 páginas) |
| [`site/extras/`](site/extras/) | Plano anterior A1–C2 em HTML, PDF e slides (.pptx) |
| [`guia/`](guia/) | Conteúdo original em Markdown, um arquivo por capítulo |
| [`build/`](build/) | Scripts que geram o site, o PDF e os slides |

## O que tem no guia

1. Comece aqui: metas por ano, as 14 etapas de cada aula e o modo nativo
2. Plano de 5 anos (objetivos, gramática, vocabulário, metas de palavras, leitura, escrita, conversação, listening e simulados Cambridge)
3. Planos diários de 1h, 2h e 4h
4. Trilha A1 (alfabeto, números, dias, meses, horas, cores, família, animais, casa, escola, objetos)
5. Comida (frutas, verduras, legumes, carnes, bebidas, restaurantes, padarias, mercados, lanches, fast food)
6. Situações reais: supermercado, cinema, viagem, conversação e inglês para o trabalho (com perguntas de entrevista)
7. Gramática completa: 25 tópicos com explicação simples, avançada, exemplos, exercícios, pegadinhas e gabarito
8. Vocabulário por tema (20 temas) e falsos cognatos
9. Gírias americanas, britânicas, australianas e canadenses + abreviações
10. Músicas, livros, séries e filmes por nível
11. Flashcards, revisão espaçada, mapas mentais, desafios diários, testes e provas
12. Aula 1 completa: Verbo To Be nas 14 etapas

## Como editar e regenerar

Edite os arquivos em `guia/` e rode:

```bash
pip install markdown        # e tenha o wkhtmltopdf instalado para o PDF
python3 build/build_guia.py # gera site/index.html e site/Guia-Ingles-5-Anos.pdf
```

Plano anterior (opcional): `python3 build/build_html.py` e `node build/build_pptx.js` (requer `pptxgenjs`).

## Publicação

O site é estático. A Vercel publica a pasta `site/` (configurado em `vercel.json`). Para usar o GitHub Pages, aponte o Pages para a pasta `site/` via GitHub Actions ou copie o conteúdo para `docs/`.
