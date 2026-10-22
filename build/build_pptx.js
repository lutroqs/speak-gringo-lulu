// Gera Plano-Ingles-A1-C2.pptx a partir de content.json (exportado de content.py)
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const { applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js");

const D = JSON.parse(fs.readFileSync(path.join(__dirname, "content.json"), "utf8"));
const OUT = path.join(__dirname, "..", "site", "extras", "Plano-Ingles-A1-C2.pptx");

const THEME = {
  name: "Fluencia",
  headFontFace: "Georgia",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2933", lt1: "FFFFFF", dk2: "1A3A5C", lt2: "F2F5F9",
    accent1: "1A3A5C", accent2: "F2A541", accent3: "2E7D32", accent4: "C62828",
    accent5: "6A1B9A", accent6: "52606D", hlink: "1565C0", folHlink: "6A1B9A",
  },
};

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625
  pres.title = D.TITLE;
  pres.author = "Professor Particular de Inglês";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "Capa",
    background: { color: C.text2 },
    objects: [{ rect: { x: 0.6, y: 3.05, w: 1.2, h: 0.06, fill: { color: C.accent2 } } }],
    placeholders: [],
  });
  pres.defineSlideMaster({
    title: "Divisoria",
    background: { color: C.text2 },
    objects: [],
  });
  pres.defineSlideMaster({
    title: "Conteudo",
    background: { color: C.background1 },
    objects: [
      { text: { text: "Plano de Inglês A1 → C2", options: { x: 0.5, y: 5.25, w: 5, h: 0.25, fontSize: 9, color: C.accent6 } } },
    ],
    slideNumber: { x: 9.1, y: 5.25, w: 0.5, h: 0.25, fontSize: 9, color: C.accent6, align: "right" },
  });

  const tb = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, margin: 0 }, o));
  const title = (s, t, sub) => {
    tb(s, t, { x: 0.5, y: 0.3, w: 9, h: 0.6, fontSize: 26, bold: true, color: C.text2, fontFace: THEME.headFontFace });
    if (sub) tb(s, sub, { x: 0.5, y: 0.88, w: 9, h: 0.35, fontSize: 13, color: C.accent6 });
  };
  const hdr = (arr) => arr.map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: "1A3A5C" } } }));
  const tableOpts = (y, colW, fs = 11) => ({ x: 0.5, y, w: 9, colW, fontSize: fs, border: { type: "solid", pt: 0.5, color: "D5DBE3" }, valign: "middle", color: "1F2933", margin: 0.05 });

  let sec = "Visão geral";
  pres.addSection({ title: sec });

  // 1. Capa
  let s = pres.addSlide({ masterName: "Capa", sectionTitle: sec });
  tb(s, "INGLÊS PARA O MUNDO CORPORATIVO", { x: 0.6, y: 1.2, w: 8.8, h: 0.35, fontSize: 13, color: C.accent2, bold: true, charSpacing: 3 });
  tb(s, "Plano de Estudos A1 → C2", { x: 0.6, y: 1.6, w: 8.8, h: 1.0, fontSize: 40, bold: true, color: C.background1, fontFace: THEME.headFontFace });
  tb(s, D.SUBTITLE, { x: 0.6, y: 2.5, w: 8.8, h: 0.4, fontSize: 16, color: C.background2 });
  tb(s, "6 níveis · 48 aulas · 18 a 24 meses com 1 h/dia", { x: 0.6, y: 3.3, w: 8.8, h: 0.4, fontSize: 14, color: C.background2 });

  // 2. Jornada
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "A jornada até a fluência profissional", D.OVERVIEW.split(". ").slice(-1)[0]);
  const lvlColors = D.MODULES.map((m) => m.color);
  D.MODULES.forEach((m, i) => {
    const x = 0.5 + i * 1.52, h = 0.9 + i * 0.42, y = 4.6 - h;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 1.38, h, fill: { color: m.color }, rectRadius: 0.08, objectName: "nivel " + m.code });
    tb(s, m.code, { x, y: y + 0.12, w: 1.38, h: 0.45, fontSize: 22, bold: true, color: "FFFFFF", align: "center" });
    tb(s, m.name, { x: x + 0.05, y: y + 0.55, w: 1.28, h: 0.35, fontSize: 10, color: "FFFFFF", align: "center" });
    tb(s, m.weeks, { x, y: 4.68, w: 1.38, h: 0.3, fontSize: 9, color: C.accent6, align: "center" });
  });

  // 3. 13 etapas
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "Cada aula tem 13 etapas", "Sempre na mesma ordem, do simples ao profissional");
  D.STEPS.forEach((st, i) => {
    const col = i < 7 ? 0 : 1, row = col ? i - 7 : i;
    const x = 0.5 + col * 4.6, y = 1.4 + row * 0.53;
    s.addShape(pres.shapes.OVAL, { x, y, w: 0.38, h: 0.38, fill: { color: C.accent2 }, objectName: "num " + (i + 1) });
    tb(s, String(i + 1), { x, y, w: 0.38, h: 0.38, fontSize: 12, bold: true, color: C.text2, align: "center", valign: "middle" });
    tb(s, [{ text: st[0], options: { bold: true, color: C.text2 } }, { text: " — " + st[1], options: { color: C.accent6 } }],
      { x: x + 0.5, y, w: 4.0, h: 0.38, fontSize: 12, valign: "middle" });
  });

  // 4. Fechamento + rotina
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "Fechamento de módulo e rotina semanal", "Só avançamos de nível com 80% ou mais na prova");
  D.CLOSING.forEach((c, i) => {
    const x = 0.5 + i * 1.52;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.4, w: 1.38, h: 0.6, fill: { color: C.background2 }, line: { color: "1A3A5C", width: 1 }, rectRadius: 0.08, objectName: "fech " + c });
    tb(s, c, { x, y: 1.4, w: 1.38, h: 0.6, fontSize: 11, bold: true, color: C.text2, align: "center", valign: "middle" });
  });
  s.addTable([hdr(["Dia", "Foco", "Tempo"]), ...D.WEEK.map((r) => r.map((t) => ({ text: t })))], tableOpts(2.35, [2.2, 5, 1.8], 12));

  // Módulos
  sec = "Módulos";
  pres.addSection({ title: sec });
  D.MODULES.forEach((m) => {
    s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 0.3, w: 0.9, h: 0.6, fill: { color: m.color }, rectRadius: 0.08, objectName: "badge" });
    tb(s, m.code, { x: 0.5, y: 0.3, w: 0.9, h: 0.6, fontSize: 22, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
    tb(s, m.name + "  ·  " + m.weeks, { x: 1.6, y: 0.3, w: 7.9, h: 0.6, fontSize: 21, bold: true, color: C.text2, fontFace: THEME.headFontFace, valign: "middle" });
    tb(s, "Meta: " + m.goal, { x: 0.5, y: 0.98, w: 9, h: 0.35, fontSize: 12, italic: true, color: C.accent6 });
    const rows = [hdr(["Aula", "Gramática / Foco", "Vocabulário", "Prática"]), ...m.lessons.map((r) => r.map((t) => ({ text: t })))];
    s.addTable(rows, Object.assign(tableOpts(1.4, [0.7, 2.7, 2.8, 2.8], 10), { rowH: 0.3 }));
    s.addNotes(m.skills.map((k) => k[0] + ": " + k[1]).join("\n"));
    // habilidades
    s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
    title(s, m.code + " — habilidades e fechamento", m.name);
    m.skills.forEach((k, i) => {
      const x = 0.5 + (i % 2) * 4.6, y = 1.45 + Math.floor(i / 2) * 1.75;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 4.4, h: 1.55, fill: { color: C.background2 }, rectRadius: 0.08, objectName: "card " + k[0] });
      s.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.08, h: 1.55, fill: { color: m.color }, objectName: "marca" });
      tb(s, k[0], { x: x + 0.3, y: y + 0.15, w: 3.9, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
      tb(s, k[1], { x: x + 0.3, y: y + 0.55, w: 3.9, h: 0.9, fontSize: 12, color: C.text1, valign: "top" });
    });
  });

  // Recursos
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "Recursos e checklist de progresso");
  tb(s, D.RESOURCES.map((r, i) => ({ text: r[0] + ": " + r[1], options: { bullet: true, breakLine: i < D.RESOURCES.length - 1 } })),
    { x: 0.5, y: 1.2, w: 4.5, h: 3.8, fontSize: 12, color: C.text1, paraSpaceAfter: 8, valign: "top" });
  tb(s, D.CHECKLIST.map((c, i) => ({ text: "☐  " + c, options: { breakLine: i < D.CHECKLIST.length - 1 } })),
    { x: 5.4, y: 1.2, w: 4.1, h: 3.8, fontSize: 12, color: C.text2, paraSpaceAfter: 6, valign: "top" });

  // Aula A1.1
  sec = "Aula A1.1";
  pres.addSection({ title: sec });
  const L = D.L1;
  s = pres.addSlide({ masterName: "Divisoria", sectionTitle: sec });
  tb(s, "AULA A1.1", { x: 0.6, y: 1.6, w: 8.8, h: 0.4, fontSize: 14, bold: true, color: C.accent2, charSpacing: 3 });
  tb(s, "Verbo To Be (afirmativa)", { x: 0.6, y: 2.0, w: 8.8, h: 0.9, fontSize: 38, bold: true, color: C.background1, fontFace: THEME.headFontFace });
  tb(s, "I am · He / She / It is · You / We / They are", { x: 0.6, y: 2.9, w: 8.8, h: 0.4, fontSize: 16, color: C.background2 });

  // kid + pro
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "1–2. A ideia e a regra");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 1.2, w: 4.3, h: 3.8, fill: { color: "FFF4E0" }, rectRadius: 0.1, objectName: "crianca" });
  tb(s, "Para uma criança de 10 anos", { x: 0.75, y: 1.35, w: 3.9, h: 0.35, fontSize: 14, bold: true, color: C.text2 });
  tb(s, L.kid.join("\n\n"), { x: 0.75, y: 1.8, w: 3.9, h: 3.0, fontSize: 13, color: C.text1, valign: "top" });
  tb(s, "Explicação profissional", { x: 5.1, y: 1.35, w: 4.4, h: 0.35, fontSize: 14, bold: true, color: C.text2 });
  tb(s, L.pro, { x: 5.1, y: 1.75, w: 4.4, h: 1.5, fontSize: 11, color: C.text1, valign: "top" });
  s.addTable([hdr(["Pronome", "Verbo", "Contração"]), ...L.conj.map((r) => r.map((t) => ({ text: t })))],
    { x: 5.1, y: 3.3, w: 4.4, colW: [1.5, 0.8, 2.1], fontSize: 10, border: { type: "solid", pt: 0.5, color: "D5DBE3" }, color: "1F2933", rowH: 0.27, margin: 0.04 });

  // exemplos
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "3–5. Exemplos, tradução e pronúncia");
  s.addTable([hdr(["Inglês", "Tradução", "Pronúncia aproximada"]), ...L.examples.map((r) => [{ text: r[0], options: { bold: true } }, { text: r[1] }, { text: r[2], options: { italic: true } }])],
    Object.assign(tableOpts(1.2, [3.2, 3.0, 2.8], 13), { rowH: 0.42 }));
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 4.0, w: 9, h: 0.8, fill: { color: "FFF4E0" }, rectRadius: 0.08, objectName: "dica" });
  tb(s, "Dica: " + L.tip, { x: 0.7, y: 4.0, w: 8.6, h: 0.8, fontSize: 12, color: C.text1, valign: "middle" });

  // erros
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "6. Erros comuns de brasileiros");
  s.addTable([hdr(["Errado", "Certo", "Por quê"]), ...L.errors.map((r) => [
    { text: "✗ " + r[0], options: { color: "C62828" } }, { text: "✓ " + r[1], options: { color: "2E7D32", bold: true } }, { text: r[2] }])],
    Object.assign(tableOpts(1.2, [3, 3, 3], 14), { rowH: 0.5 }));

  // exercícios
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "7–8. Exercícios", "Responda no chat e receba a correção comentada");
  tb(s, "A) Complete com am, is ou are", { x: 0.5, y: 1.35, w: 4.4, h: 0.35, fontSize: 14, bold: true, color: C.text2 });
  tb(s, L.ex_a.map((t, i) => ({ text: (i + 1) + ". " + t, options: { breakLine: i < L.ex_a.length - 1 } })), { x: 0.5, y: 1.8, w: 4.4, h: 2.5, fontSize: 14, color: C.text1, paraSpaceAfter: 8, valign: "top" });
  tb(s, "B) Traduza para o inglês", { x: 5.1, y: 1.35, w: 4.4, h: 0.35, fontSize: 14, bold: true, color: C.text2 });
  tb(s, L.ex_b.map((t, i) => ({ text: (i + 6) + ". " + t, options: { breakLine: i < L.ex_b.length - 1 } })), { x: 5.1, y: 1.8, w: 4.4, h: 1.5, fontSize: 14, color: C.text1, paraSpaceAfter: 8, valign: "top" });
  tb(s, "C) " + L.ex_c, { x: 5.1, y: 3.5, w: 4.4, h: 0.8, fontSize: 14, color: C.text1, valign: "top" });

  // diálogo
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "9. Diálogo — primeiro dia no trabalho");
  L.dialogue.forEach((d, i) => {
    const you = d[0] === "You", y = 1.15 + i * 0.8, x = you ? 3.2 : 0.5;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 6.3, h: 0.7, fill: { color: you ? "E3EDF7" : C.background2 }, rectRadius: 0.1, objectName: "fala " + (i + 1) });
    tb(s, [{ text: d[0] + ": ", options: { bold: true, color: C.text2 } }, { text: d[1], options: { breakLine: true } }, { text: d[2], options: { fontSize: 10, color: C.accent6, italic: true } }],
      { x: x + 0.2, y, w: 5.9, h: 0.7, fontSize: 13, color: C.text1, valign: "middle" });
  });

  // flashcards
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "10. Flashcards", "Frente → verso");
  L.flashcards.forEach((f, i) => {
    const x = 0.5 + (i % 3) * 3.07, y = 1.4 + Math.floor(i / 3) * 1.85;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 2.85, h: 1.65, fill: { color: C.background2 }, line: { color: "1A3A5C", width: 1 }, rectRadius: 0.1, objectName: "card " + (i + 1) });
    tb(s, f[0], { x: x + 0.15, y: y + 0.15, w: 2.55, h: 0.75, fontSize: 15, bold: true, color: C.text2, align: "center", valign: "middle" });
    s.addShape(pres.shapes.LINE, { x: x + 0.4, y: y + 0.95, w: 2.05, h: 0, line: { color: "F2A541", width: 1.5 }, objectName: "linha" });
    tb(s, f[1], { x: x + 0.15, y: y + 1.0, w: 2.55, h: 0.55, fontSize: 14, color: C.accent3, align: "center", valign: "middle" });
  });

  // mapa mental
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "11. Mapa mental");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 3.4, y: 1.15, w: 3.2, h: 0.6, fill: { color: C.text2 }, rectRadius: 0.3, objectName: "centro" });
  tb(s, "TO BE (ser / estar)", { x: 3.4, y: 1.15, w: 3.2, h: 0.6, fontSize: 16, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
  [["AM", "I", "I'm", "2E7D32"], ["IS", "He / She / It", "He's / She's / It's", "1565C0"], ["ARE", "You / We / They", "You're / We're / They're", "6A1B9A"]].forEach((b, i) => {
    const cx = 1.85 + i * 3.15;
    s.addShape(pres.shapes.LINE, { x: Math.min(5, cx), y: 1.75, w: Math.abs(cx - 5) || 0.001, h: 0.75, flipH: cx < 5, line: { color: "9AA5B1", width: 1.5 }, objectName: "ramo" });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx - 0.8, y: 2.5, w: 1.6, h: 0.55, fill: { color: b[3] }, rectRadius: 0.08, objectName: "ramo " + b[0] });
    tb(s, b[0], { x: cx - 0.8, y: 2.5, w: 1.6, h: 0.55, fontSize: 18, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
    tb(s, b[1] + "\n" + b[2], { x: cx - 1.4, y: 3.2, w: 2.8, h: 0.7, fontSize: 13, color: C.text1, align: "center" });
  });
  tb(s, "Usos: profissão · origem · idade · lugar · estado (tired, busy)", { x: 0.5, y: 4.3, w: 9, h: 0.4, fontSize: 13, italic: true, color: C.accent6, align: "center" });

  // teste
  s = pres.addSlide({ masterName: "Conteudo", sectionTitle: sec });
  title(s, "12–13. Teste rápido e simulado");
  tb(s, L.quiz.map((q, i) => ({ text: (i + 1) + ". " + q[0] + "   " + q[1].map((o, j) => "(" + "abc"[j] + ") " + o).join("   "), options: { breakLine: i < L.quiz.length - 1 } })),
    { x: 0.5, y: 1.25, w: 9, h: 2.6, fontSize: 15, color: C.text1, paraSpaceAfter: 14, valign: "top" });
  tb(s, "Simulado: o primeiro sai ao final da Aula A1.3, misturando as três primeiras aulas.", { x: 0.5, y: 4.2, w: 9, h: 0.5, fontSize: 13, italic: true, color: C.accent6 });

  // encerramento
  s = pres.addSlide({ masterName: "Divisoria", sectionTitle: sec });
  tb(s, "Próximo passo", { x: 0.6, y: 1.7, w: 8.8, h: 0.8, fontSize: 36, bold: true, color: C.background1, fontFace: THEME.headFontFace });
  tb(s, "Responda os exercícios no chat → correção → Aula A1.2 (To Be na negativa e em perguntas)", { x: 0.6, y: 2.6, w: 8.8, h: 0.8, fontSize: 17, color: C.background2 });

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("ok", OUT);
})();
