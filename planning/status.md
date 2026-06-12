# 프로젝트 현황 및 세션 인계 명세

이 파일은 새 세션에서 바로 작업을 이어갈 수 있도록 현재 상태와 결정 사항을 기록한다.
최신 커밋 기준으로 갱신한다.

---

## 완료된 산출물

### 기획·설계 파일 (`planning/`)

| 파일 | 내용 |
|------|------|
| `principles.md` | 작업 원칙 |
| `plan.md` | 5단계 제작 계획 |
| `training-context.md` | 5블록 구성·타임라인·생략 우선순위 |
| `web-apps.md` | 웹앱 철학·시연 설계·교과별 주제 목록 |
| `output-standards.md` | 삼문서 구조 정의, `[강사 메모]` 형식 |
| `ai-tools-guide.md` | Block 3 플랫폼 비교, Block 4 웹/로컬 AI 설명 |

### 연수 본문 파일

| 파일 | 상태 | 비고 |
|------|------|------|
| `lecture/연수자_자료.md` | **완성** | A4 인쇄 최적화 재작성. LaTeX fbox 활동 카드 포함 |
| `slides/PPT_원고.md` | **완성** | S01–S36, 섹션별 타임라인·멘트·시연 순서 포함 |
| `lecture/강사용_원고.md` | **완성** | 연수자 자료 전체 + `[강사 메모 — S번호/시간]` 블록 |
| `lecture/수정_강의록.md` | **스텁** | 삼문서 방식 확정 전 플레이스홀더. 삭제 가능 |

### ChatGPT·Gemini 지침 파일 (`연수용 프로젝트 지침모음/`)

참여자가 ChatGPT/Gemini에 직접 업로드하는 파일. 한글 파일명 유지.

| 파일 | 용도 |
|------|------|
| `ChatGPT용_수업설계조언자_프로젝트지침.md` | ChatGPT 프로젝트 지침에 붙여넣기 (Layer 1) |
| `Layer_2_수업설계조언자.md` | 프로젝트 소스로 업로드 → Layer 2 구성 시작 |
| `Gems용_수업설계조언자_시스템지침.md` | Gemini Gems 시스템 지침 (ChatGPT 한도 초과 시) |

> `ChatGPT용_프로젝트지침.md`, `Gems용_시스템지침.md`, `Layer_2.md`는 이전 버전 파일로 삭제 검토 가능.

### 수학 웹앱 (별도 프로젝트)

- 위치: `math-webapps/probability-statistics/sample-proportion-event-readiness/` 별도 저장소
- Block 4 시연의 핵심 앱. 이 프로젝트에서는 수정하지 않음.

---

## 남은 작업: 연수 시연용 웹앱 2개

`webapps/` 폴더에 제작. 폴더와 파일명은 영문으로 쓰고, 웹에서 보이는 제목·설명만 한글로 표시한다. 기술 스택: 단일 `index.html`, Tailwind CSS CDN, vanilla JS.

### 1. 수평 투사 운동 (`webapps/horizontal-projectile/index.html`)

**교과**: 통합과학1\
**깨야 할 직관**: "빠르게 던지면 더 빨리 떨어질 것 같다"\
**아하 모먼트**: 수평 속력이 달라도 낙하 시간은 동일 (수평·수직 운동의 독립성)

시연·조작 설계:
- 기본 화면: 같은 높이의 발사대 2개, 느린 공과 빠른 공을 나란히 배치
- 버튼 1: `동시에 발사` → 두 공이 서로 다른 포물선 궤적을 그리지만 같은 순간 바닥에 닿음
- 제한된 속도 선택: `느림 / 보통 / 빠름` 프리셋 또는 단일 속력 슬라이더만 제공
- 결과 표시: 두 공의 낙하 시간은 같은 값으로 고정 표시, 수평 이동 거리만 다르게 표시
- 보조 장치: 착지 순간에 세로 기준선 또는 동시 착지 표시가 나타나도록 구성

핵심: 궤적이 다르지만 땅에 닿는 시점이 동일하다는 것을 직접 보여줌.

### 2. 전자기 유도 (`webapps/electromagnetic-induction/index.html`)

**교과**: 통합과학2\
**깨야 할 직관**: "자석이 가까이 있으면 전류가 흐를 것 같다"\
**아하 모먼트**: 자석이 움직일 때만 전류 발생 — 변화율이 핵심

시연·조작 설계:
- 기본 화면: 코일, 막대자석, 전류계 또는 전구를 한 화면에 크게 배치
- 버튼 1: `가까이 두기` → 자석이 코일 근처에 멈춰 있지만 전류 0
- 버튼 2: `천천히 넣기` → 자석이 움직이는 동안만 전류계가 약하게 흔들림
- 버튼 3: `빠르게 넣기` → 움직이는 동안만 전류계가 더 크게 흔들림
- 버튼 4: `빼기` → 전류계가 반대 방향으로 흔들림
- 자유도 제한: 자석 위치·속도·방향을 모두 따로 조절하지 않고, 시연용 버튼 중심으로 결과 차이를 명확히 보여줌

핵심: 정적 상태(가까이 있기만 함)와 동적 상태(이동 중)의 차이가 즉시 보임.

---

## PDF 생성 방법

아래 명령어로 세 파일을 PDF로 변환한다. `exports/` 디렉토리에 저장되나 `.gitignore`에 포함되어 있어 커밋되지 않는다.

```bash
pandoc "lecture/연수자_자료.md" \
  -o "exports/연수자_자료.pdf" \
  --pdf-engine=xelatex \
  -V mainfont="Malgun Gothic" \
  -V monofont="Malgun Gothic" \
  -V fontsize=11pt \
  -V geometry:margin=2cm \
  -V lang=ko \
  --toc \
  --toc-depth=2 \
  --from markdown+raw_tex
```

- `--from markdown+raw_tex` 필수: 연수자_자료.md에 LaTeX fbox 블록이 포함되어 있음
- PPT_원고.md, 강사용_원고.md는 raw_tex 블록 없으므로 `--from` 옵션 생략 가능
- 알려진 누락 문자: ✓, ✗, ⏩ (Malgun Gothic 미포함) — 텍스트 대체 필요 시 일괄 교체 가능
- 환경: pandoc 3.9.0.2 + xelatex (MiKTeX 25.12) + Malgun Gothic (C:/WINDOWS/Fonts/malgun.ttf)

---

## 주요 결정 사항

### 삼문서 구조 확정

연수자 자료(`연수자_자료.md`)를 기준으로 나머지 두 파일이 파생된다.
- `slides/PPT_원고.md`: 슬라이드 원고, 섹션 번호가 연수자 자료와 연동
- `lecture/강사용_원고.md`: 연수자 자료 전체 + `[강사 메모]` 블록

`lecture/수정_강의록.md`는 이 구조 확정 전 플레이스홀더였으므로 사실상 불필요.

### 웹앱 설계 원칙

퀴즈·OX·비교표 형태 지양. 조건:
1. 깨야 할 직관이 있을 것
2. 슬라이더·버튼 → 즉각 시각 변화
3. 정지 이미지·숫자로는 전달 안 되는 아하 모먼트

Block 4 시연 웹앱은 2개: 수평 투사 운동(통합과학1), 전자기 유도(통합과학2).
수학 앱(`sample-proportion-event-readiness`)은 `math-webapps` 별도 프로젝트.

### 미니 활동지 통합

별도 활동지 파일 대신 `연수자_자료.md` 섹션 3에 LaTeX fbox 카드로 포함.
`worksheets/교사용_활동지.md`는 이전 버전 파일로 사실상 불필요.

### ChatGPT 한도 초과 대응

Block 2에서 ChatGPT 무료 한도 초과 시 Gemini Gems로 전환하는 절차를 연수자 자료에 포함.
Layer 2 대화 내용을 복사해 새 Gem에 붙여넣는 방식으로 이어가도록 안내.

---

## 파일 구조 요약

```
AI-teacher-training/
├── CLAUDE.md                          ← 프로젝트 인덱스
├── planning/
│   ├── status.md                      ← 이 파일 (세션 인계)
│   ├── training-context.md            ← 블록 구성·타임라인
│   ├── web-apps.md                    ← 웹앱 철학·시연 설계
│   ├── output-standards.md            ← 삼문서 형식 정의
│   ├── ai-tools-guide.md              ← AI 플랫폼·로컬 AI 설명
│   ├── principles.md
│   └── plan.md
├── lecture/
│   ├── 연수자_자료.md                  ← 참여자 배포 (A4 인쇄용)
│   └── 강사용_원고.md                  ← 연수자 자료 + [강사 메모]
├── slides/
│   └── PPT_원고.md                    ← S01–S36 슬라이드 원고
├── webapps/
│   ├── horizontal-projectile/index.html       ← 제작 필요 (통합과학1)
│   └── electromagnetic-induction/index.html   ← 제작 필요 (통합과학2)
├── 연수용 프로젝트 지침모음/
│   ├── ChatGPT용_수업설계조언자_프로젝트지침.md
│   ├── Layer_2_수업설계조언자.md
│   └── Gems용_수업설계조언자_시스템지침.md
├── exports/                           ← .gitignore (PDF 생성 결과물)
│   ├── 연수자_자료.pdf
│   ├── PPT_원고.pdf
│   └── 강사용_원고.pdf
└── source/                            ← 교과서 PDF (참고용, .gitignore)
```
