# CLAUDE.md

## Project

**"ChatGPT를 이용한 수업 조언자 만들기"** — 교사 대상 3시간 연수 자료 제작.

Source: `04dc80ab9d_AI로_내_수업_비서_만들기.md`

## Training Position

    [앞 강의 3h] → [이 강의 3h] → [뒤 강의 6h]
    다른 강사       권달현 (수학)    다른 강사
    AI 활용 개론                     AI 수업 준비·활용 심화

뒤 강사는 이 연수에서 참여자가 완성한 ChatGPT 프로젝트를 기반으로 6시간 심화 연수를 진행한다.

## Required Outcome

참여자 각자의 **ChatGPT 수업 설계 조언자 프로젝트** 완성이 이 3시간 연수의 필수 목표다.

Core participant files:

| File | Purpose |
|------|---------|
| `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md` | ChatGPT 프로젝트 지침에 붙여넣기 |
| `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md` | 프로젝트 소스로 업로드 후 Layer 2 구성 시작 |

## Instructor Context

- 강사: 권달현
- 교과: 수학
- 수학 웹앱은 `math-webapps` 별도 프로젝트에서 제작한다.
- 이 저장소의 웹앱은 여러 교과 교사가 볼 수 있는 Block 4 시연용 교과별 웹앱 갤러리다.

## Current State

최종 상태 기준일: 2026-06-12

현재 과학 계열 핵심 웹앱 2개는 구현, 커밋, 푸시, GitHub Pages 배포 확인까지 완료된 상태다. 문과 계열 웹앱 5개는 로컬 구현과 수업효과 검토를 통과했으며, 커밋·푸시와 Pages 배포 확인이 남아 있다.

| Target | Subject | State | Core idea |
|--------|---------|-------|-----------|
| `webapps/horizontal-projectile/index.html` | 통합과학1 | 완료·배포 | 수평 속력이 달라도 같은 높이에서 출발하면 낙하 시간은 같다 |
| `webapps/electromagnetic-induction/index.html` | 통합과학2 | 완료·배포 | 가까이 있음이 아니라 자기장 변화가 전류를 만든다 |
| `webapps/heat-vulnerability-map/index.html` | 도시의 미래탐구 | 로컬 완료 | 취약성이 겹치면 우선 지원 지역이 달라진다 |
| `webapps/contract-validity-checker/index.html` | 법과 사회 | 로컬 완료 | 계약은 서명보다 의사 합치와 효력 요건을 따지는 과정이다 |
| `webapps/smart-city-balance/index.html` | 도시의 미래탐구 | 로컬 완료 | 스마트 도시는 기술 총량보다 공공성과 참여의 균형 문제다 |
| `webapps/city-budget-for-all/index.html` | 도시의 미래탐구 | 로컬 완료 | 예산 선택은 누가 반영되고 미뤄지는지를 바꾼다 |
| `webapps/inheritance-family-tree/index.html` | 법과 사회 | 로컬 완료 | 상속은 순위, 배우자 지위, 채무 조건이 함께 작동한다 |

Deployment URLs:

- Web app index: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`
- Horizontal projectile: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- Electromagnetic induction: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`

현재 상태, 배포 여부, 다음 작업 우선순위는 `planning/status.md`를 기준으로 삼는다. 지침 파일과 상태 문서가 충돌하면 `planning/status.md`를 우선한다.

## First Files To Check

Before making substantive changes, check these files in order:

1. `planning/status.md` — current state, deployment URLs, remaining work, handoff notes
2. `AGENTS.md` — Codex용 작업 지침과 산출물 맥락
3. Relevant sub-instructions:
   - `planning/training-context.md` — 3시간 블록 구성, 미니 활동지, 생략 우선순위
   - `planning/web-apps.md` — 웹앱 철학, 시연 설계, 교과별 예시
   - `planning/output-standards.md` — 강의록, PPT, 웹앱 작성 형식
   - `planning/ai-tools-guide.md` — AI 플랫폼 비교, 웹 AI vs 로컬 AI, Claude Code·Codex 소개

## Deliverables

산출물의 현재 완료 여부는 `planning/status.md`를 기준으로 한다. 주요 완성 산출물은 다음과 같다.

| File | Role |
|------|------|
| `planning/principles.md` | 연수 설계 원칙 |
| `planning/plan.md` | 전체 연수 계획 |
| `planning/training-context.md` | 3시간 블록 구성과 운영 맥락 |
| `planning/web-apps.md` | 웹앱 철학과 예시 |
| `planning/output-standards.md` | 문서·웹앱 산출 형식 |
| `planning/ai-tools-guide.md` | AI 도구 비교와 설명 |
| `prompts/chatgpt-instructions.md` | ChatGPT 프로젝트 지침 초안 |
| `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md` | 참여자 업로드·붙여넣기용 지침 |
| `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md` | Layer 2 구성용 소스 |
| `연수용 프로젝트 지침모음/Gems용_수업설계조언자_시스템지침.md` | Gemini Gems용 시스템 지침 |
| `lecture/연수자_자료.md` | 참여자 자료 |
| `slides/PPT_원고.md` | PPT 제작 원고 |
| `lecture/강사용_원고.md` | 강사용 원고 |
| `webapps/index.html` | 교과별 웹앱 갤러리 허브 |
| `webapps/horizontal-projectile/index.html` | 수평 투사 운동 시연 앱 |
| `webapps/electromagnetic-induction/index.html` | 전자기 유도 시연 앱 |
| `webapps/heat-vulnerability-map/index.html` | 폭염 취약 지역 커뮤니티 매핑 앱 |
| `webapps/contract-validity-checker/index.html` | 계약 성립·효력 판단기 앱 |
| `webapps/smart-city-balance/index.html` | 스마트 도시 균형 실험실 앱 |
| `webapps/city-budget-for-all/index.html` | 모두를 위한 도시 예산 배분 앱 |
| `webapps/inheritance-family-tree/index.html` | 상속 관계 가계도 시뮬레이터 앱 |

## Next Work

현재 웹앱 제작 자체는 완료되었다. 다음 작업은 새 기능 제작보다 연수 현장 연결과 검수에 가깝다.

- Block 2의 ChatGPT 프로젝트 생성, Layer 1 프로젝트 지침 붙여넣기, Layer 2 파일 업로드 과정이 모든 자료에 유지되는지 점검
- Block 4에서 `webapps/index.html` 갤러리 소개 + 대표 사례 3개 압축 시연 흐름 점검
- `slides/PPT_원고.md`, `lecture/강사용_원고.md`, `lecture/연수자_자료.md`에 갤러리 URL 또는 QR 안내 연결
- 문과 계열 웹앱 5개 커밋·푸시와 Pages 배포 확인
- 빔프로젝터, 모바일, 학교 네트워크, Tailwind CDN 차단 가능성 최종 확인

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
- The electromagnetic induction app should focus on "magnetic-field change through the coil creates current", not on the right-hand rule.

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
- Web app folders: English names.

## Project Voice

Work as an educational-training planner and lesson-design collaborator for teachers.

- Focus on practical use in a real 3-hour teacher training.
- Separate instructor explanation, instructor demo, participant practice, and sharing/reflection.
- Help teachers adapt the material to their subject, school level, students, and teaching concerns.
- Keep examples transferable across Korean language, English, math, social studies, science, arts/PE, career education, and creative experiential activities.
- Keep technical explanation minimal and centered on teachers' experience of improving lesson design.
- Include privacy, student data, copyright, and internal school-document cautions when relevant.

## 공유 자료 (AI_Workspace)

저작권 교과서·지도서·참고자료 등 git에 올릴 수 없는 공유 자료는 이 저장소 밖의 `AI_Workspace`에 보관한다.

- **참조 경로**: 프로젝트 루트 기준 상대경로 `../AI_Workspace/`. 하위 폴더에서 작업 중이어도 항상 프로젝트 루트를 기준으로 해석한다. 모든 PC에서 `AI_Workspace`를 프로젝트와 같은 상위 폴더(형제)에 두면 로컬이 달라도 동일하게 동작한다.
- **먼저 목록 확인**: 매번 자료를 스캔하지 말고 `../AI_Workspace/INDEX.md`를 읽어 무엇이 있는지 파악한 뒤 필요한 파일만 연다.
- **참조 예**: `../AI_Workspace/shared/...` (구체 경로는 INDEX.md 참고)
- **프로젝트 기획안 경로**: `../AI_Workspace/projects/AI-teacher-training/기획안/`
- **규칙**: `shared/` 자료는 읽기 전용 참조다. `projects/AI-teacher-training/기획안/`은 이 프로젝트의 비공개 작업 문서 영역이므로 사용자 요청에 따라 읽고 편집할 수 있다. 두 영역 모두 저작권·개인정보 보호를 위해 프로젝트(git) 안으로 복사하지 않는다.
