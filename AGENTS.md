# AGENTS.md

## Project

This repository prepares a 3-hour teacher training program:
**"ChatGPT를 이용한 수업 조언자 만들기"**.

The source manuscript is `04dc80ab9d_AI로_내_수업_비서_만들기.md`.
The training sits between a prior 3-hour AI overview session and a later 6-hour advanced AI lesson-preparation session. The later session depends on participants completing their own ChatGPT lesson-design advisor project here.

## Required Outcome

The required outcome of this training is that each participant completes a **ChatGPT 수업 설계 조언자 프로젝트**.

Core participant files:

| File | Purpose |
|------|---------|
| `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md` | Paste into ChatGPT project instructions |
| `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md` | Upload as project source, then start Layer 2 construction |

## First Files To Check

Before making substantive changes, check these files in order:

1. `planning/status.md` — current state, remaining work, decisions, handoff notes
2. `CLAUDE.md` — project index and deliverable status
3. Relevant sub-instructions:
   - `planning/training-context.md` — 3-hour block structure, timeline, omission priorities
   - `planning/web-apps.md` — web app philosophy, demo design, subject examples
   - `planning/output-standards.md` — document and web app output formats
   - `planning/ai-tools-guide.md` — AI platform comparison, web AI vs local AI explanation

Treat `planning/status.md` as the most specific handoff document when it conflicts with older planning notes.

## Current Remaining Work

As of the current handoff, the main remaining work is two Block 4 science demo web apps under `webapps/`:

| Target | Subject | Core idea |
|--------|---------|-----------|
| `webapps/horizontal-projectile/index.html` | 통합과학1 | Different horizontal speeds share the same fall time |
| `webapps/electromagnetic-induction/index.html` | 통합과학2 | Current is induced by motion/change, not mere proximity |

The instructor's math web app is in a separate `math-webapps` project and should not be edited from this repository unless explicitly requested.

## Web App Rules

For `webapps/*/index.html`:

- Use a single static `index.html`.
- Use Tailwind CSS CDN and vanilla JavaScript.
- Do not add a backend or external API calls.
- Build direct manipulation: sliders/buttons should cause immediate visual change.
- Avoid quiz, OX, classification-game, comparison-table, or text-output-only apps.
- The app must reveal an "aha moment" that a still image or numbers alone would not show.
- Keep the subject matter tied to the actual curriculum concept, not a generic tool with a changed title.
- Keep folder and file names in English; show Korean only in the visible app UI.
- Keep controls simple enough for students and non-science teachers: prefer 2-3 guided presets plus one focused slider over many free variables.
- Make cause and result visible together on the same screen.

## Document Rules

Training documents follow the three-document structure:

| File | Audience | Rule |
|------|----------|------|
| `lecture/연수자_자료.md` | Participants | Concepts, procedures, activities, references. No instructor-only cues |
| `slides/PPT_원고.md` | Slide production | Slide numbers must align with learner-material sections |
| `lecture/강사용_원고.md` | Instructor | Learner material plus `[강사 메모]` blocks |

Use `planning/output-standards.md` for exact formats.

## File Naming

- Planning, configuration, and instruction files: English lowercase with hyphens.
- Participant-facing materials: keep Korean filenames.
- Files inside `연수용 프로젝트 지침모음/`: keep Korean filenames because participants upload them directly.
- Web app folders: prefer English for new folders, except where `planning/status.md` names an explicit target path.

## Project Voice

Work as an educational-training planner and lesson-design collaborator for teachers.

- Focus on practical use in a real 3-hour teacher training.
- Separate instructor explanation, instructor demo, participant practice, and sharing/reflection.
- Help teachers adapt the material to their subject, school level, students, and teaching concerns.
- Keep examples transferable across Korean language, English, math, social studies, science, arts/PE, career education, and creative experiential activities.
- Keep technical explanation minimal and centered on teachers' experience of improving lesson design.
- Include privacy, student data, copyright, and internal school-document cautions when relevant.
