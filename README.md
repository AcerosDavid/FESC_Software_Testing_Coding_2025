<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Python — Code Analysis, Refactoring & SOLID Principles</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#9aa4b2; --accent:#7dd3fc;
      --glass: rgba(255,255,255,0.02);
    }
    body{
      margin:0; font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial;
      background: linear-gradient(180deg,#071129 0%, #071827 100%);
      color:#e6eef6; line-height:1.6; padding:28px;
    }
    .container{max-width:900px;margin:0 auto;background:var(--glass);border-radius:12px;padding:28px;box-shadow:0 6px 30px rgba(2,6,23,0.6);}
    header{display:flex;gap:16px;align-items:center;margin-bottom:18px;}
    .title{display:flex;flex-direction:column;}
    h1{margin:0;font-size:1.6rem;}
    p.lead{margin:6px 0 0;color:var(--muted);}
    .badges{display:flex;gap:8px;align-items:center;margin-left:auto;}
    .badge{background:#071833;padding:6px 10px;border-radius:8px;font-size:0.8rem;color:var(--muted);}
    nav.toc{margin:18px 0;padding:12px;background:#061122;border-radius:8px;}
    nav.toc ul{margin:0;padding:0 0 0 18px;color:var(--muted);}
    section.card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); padding:18px;border-radius:10px;margin-top:16px;}
    h2{margin:0 0 8px 0;}
    ul.clean{margin:8px 0 0 18px;color:var(--muted);}
    .muted{color:var(--muted);font-size:0.95rem;}
    .structure{background:#061226;padding:12px;border-radius:8px;color:#cfe9ff;margin-top:10px;font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;}
    footer{margin-top:22px;color:var(--muted);font-size:0.9rem;}
    .cta{margin-top:12px;}
    .emoji{font-size:1.1rem}
    @media (max-width:640px){ .badges{display:none} }
  </style>
</head>
<body>
  <div class="container" role="main" aria-labelledby="project-title">
    <header>
      <div class="title">
        <h1 id="project-title">🐍 Python — Code Analysis, Refactoring & SOLID Principles</h1>
        <p class="lead">Best practices, design principles and project setup guidance to build maintainable Python projects — explained clearly and without rodeos.</p>
      </div>

      <!-- Badges (placeholders) -->
      <div class="badges" aria-hidden="true">
        <div class="badge">Python • 3.x</div>
        <div class="badge">License: MIT</div>
        <div class="badge">Status: Draft</div>
      </div>
    </header>

    <nav class="toc" aria-label="Table of contents">
      <strong>📖 Table of Contents</strong>
      <ul>
        <li><a href="#code-analysis">1. Code Analysis & Refactoring</a></li>
        <li><a href="#solid">2. SOLID Principles in Action</a></li>
        <li><a href="#project-setup">3. Project Setup & Environment Management</a></li>
        <li><a href="#conclusion">Conclusion</a></li>
      </ul>
    </nav>

    <section id="code-analysis" class="card" aria-labelledby="code-analysis-title">
      <h2 id="code-analysis-title">🔹 1. Code Analysis & Refactoring</h2>
      <p class="muted">
        Context: the original script receives two values separated by a comma — a number and a string — and verifies that the number is within a valid range (0–150). The implementation analyzed showed several common issues that reduce robustness and maintainability.
      </p>

      <h3 style="margin-top:12px">⚠️ Problems detected</h3>
      <ul class="clean">
        <li>Poor readability and unclear variable names.</li>
        <li>Insufficient input validation (edge cases not considered).</li>
        <li>Weak or missing error handling — the program can fail silently or crash.</li>
        <li>Functions doing multiple unrelated tasks (violates single responsibility).</li>
      </ul>

      <h3 style="margin-top:12px">✅ Refactoring goals & best practices</h3>
      <ul class="clean">
        <li><strong>Descriptive names:</strong> variables and functions must communicate intent.</li>
        <li><strong>Input validation:</strong> explicitly check types, bounds and formats.</li>
        <li><strong>Error handling:</strong> catch and surface meaningful errors; avoid swallowing exceptions.</li>
        <li><strong>Single Responsibility:</strong> each function or component should do one job and do it well.</li>
      </ul>

      <p class="muted" style="margin-top:12px">Resultado: código más legible, menos bugs y más fácil de testear y mantener. Sí, suena obvio — pero la diferencia se nota en producción.</p>
    </section>

    <section id="solid" class="card" aria-labelledby="solid-title">
      <h2 id="solid-title">🔹 2. SOLID Principles in Action — Notification System</h2>
      <p class="muted">
        Use case: a notification system that can send messages via different channels (email, SMS, push). A naive implementation tiende a mezclar responsabilidades y a volverse frágil ante cambios. Aplicamos principios SOLID para evitar eso.
      </p>

      <h3 style="margin-top:12px">Principios aplicados</h3>
      <ul class="clean">
        <li><strong>SRP (Single Responsibility):</strong> cada tipo de notificación tiene su propio componente o clase.</li>
        <li><strong>OCP (Open/Closed):</strong> el sistema permite agregar nuevos canales sin modificar la lógica existente.</li>
        <li><strong>DIP (Dependency Inversion):</strong> los módulos de alto nivel dependen de abstracciones (interfaces), no de implementaciones concretas.</li>
      </ul>

      <h3 style="margin-top:12px">Beneficios</h3>
      <ul class="clean">
        <li>Facilidad para añadir nuevos canales (ej.: push, webhooks) sin tocar código que ya funciona.</li>
        <li>Mejor testabilidad: se pueden mockear las abstracciones en tests unitarios.</li>
        <li>Menos probabilidades de introducir bugs al extender el sistema.</li>
      </ul>

      <p class="muted" style="margin-top:12px">Tip práctico: define claramente la interfaz de envío (qué inputs acepta, qué errores puede devolver) y haz que cada implementación cumpla ese contrato.</p>
    </section>

    <section id="project-setup" class="card" aria-labelledby="project-setup-title">
      <h2 id="project-setup-title">🔹 3. Project Setup & Environment Management</h2>
      <p class="muted">
        Antes de meter funciones y scripts a lo loco, organiza el proyecto: esto evita el clásico “funciona en mi máquina” y facilita la incorporación de nuevos colaboradores.
      </p>

      <h3 style="margin-top:12px">Principales prácticas</h3>
      <ul class="clean">
        <li><strong>Virtual environment:</strong> aisla dependencias por proyecto para evitar conflictos.</li>
        <li><strong>Dependencias controladas:</strong> un archivo de requisitos permite reproducir el entorno exacto.</li>
        <li><strong>Separación de ambientes:</strong> configuraciones claras para <em>development</em> (debug, logs detallados) y <em>production</em> (performance, seguridad).</li>
        <li><strong>Testing y CI:</strong> incluye tests automatizados y una pipeline básica para validaciones en cada PR.</li>
      </ul>

      <h3 style="margin-top:12px">Estructura recomendada</h3>
      <div class="structure" aria-label="Suggested project structure">
project-name/
│── src/               # Source code
│   ├── main.py
│   ├── notifications.py
│   └── utils.py
│── tests/             # Unit and integration tests
│   └── test_main.py
│── requirements.txt   # Project dependencies
│── README.md          # Project documentation
│── .gitignore         # Files to ignore in git
      </div>

      <p class="muted" style="margin-top:12px">Extra: documenta las decisiones importantes (por qué se eligió una abstracción, qué tradeoffs se aceptaron). Esa bitácora agiliza la incorporación de nuevos devs y evita discusiones eternas.</p>
    </section>

    <section id="conclusion" class="card" aria-labelledby="conclusion-title">
      <h2 id="conclusion-title">📌 Conclusion</h2>
      <ul class="clean">
        <li>Refactoring — no es lujo: es supervivencia. Código claro = menos incidentes.</li>
        <li>SOLID — estructura que permite crecer sin romper lo que ya funciona.</li>
        <li>Project setup — papelón si no lo haces bien; alivio si lo haces desde el inicio.</li>
      </ul>

      <div class="cta">
        <p class="muted">¿Quieres que convierta esto en un <strong>README.md</strong> listo para GitHub (Markdown) o que genere la versión HTML para subir como página de proyecto? Puedo dejarte también los badges listos y una sección de "How to contribute".</p>
      </div>
    </section>

    <footer>
      <p class="muted">Made with clarity and a bit of Colombian sazón. 🇨🇴</p>
    </footer>
  </div>
</body>
</html>
