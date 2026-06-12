# 프로젝트 현황 및 다음 작업 명세

이 파일은 새 세션이나 다른 작업자가 바로 이어받을 수 있도록 현재까지 완료된 일, 배포 상태, 앞으로 할 일을 정리한 인수인계 명세서다.

최종 갱신일: 2026-06-12

---

## 1. 현재 상태 요약

- 저장소: `AI-teacher-training`
- 기본 브랜치: `main`
- GitHub Pages: 공개 저장소 기준으로 활성화 완료
- Pages 배포 방식: `main` 브랜치의 루트에서 정적 파일 배포
- 웹앱 기술 스택: 단일 `index.html`, Tailwind CSS CDN, vanilla JavaScript
- 파일·폴더명 원칙: 영문 사용
- 웹 화면 표시 원칙: 제목, 버튼, 관찰 문장 등 사용자에게 보이는 문구는 한글 사용
- 작업 지침: `AGENTS.md`와 `CLAUDE.md`는 현재 웹앱 완료·배포 상태를 같은 기준으로 공유한다.

배포 URL:

- 웹앱 목록: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`
- 수평 투사 운동: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- 전자기 유도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`

현재 핵심 웹앱 2개는 구현, 커밋, 푸시, Pages 배포 확인까지 완료된 상태다.

문과 계열 상위 3개 웹앱은 로컬 구현과 수업효과 사후 검토까지 완료했다. 아직 커밋, 푸시, Pages 배포 확인은 하지 않았다.

로컬 구현 완료 앱:

- 폭염 취약 지역 커뮤니티 매핑: `webapps/heat-vulnerability-map/index.html`
- 계약 성립·효력 판단기: `webapps/contract-validity-checker/index.html`
- 스마트 도시 균형 실험실: `webapps/smart-city-balance/index.html`

---

## 2. 완료된 작업

### 저장소·배포 정리

- GitHub Pages용 `webapps/` 구조를 생성했다.
- Pages 빌드 오류를 막기 위해 `_config.yml`과 `.nojekyll`을 추가했다.
- Pages가 전체 저장소 Markdown을 Jekyll로 처리하다가 실패하지 않도록 배포 대상을 `webapps` 중심으로 제한했다.
- 저장소를 공개해도 문제가 될 가능성이 큰 파일과 개인정보 노출 요소를 정리했다.
- `.gitignore`에 `*.hwp`, `*.hwpx`, `manifest.jsonl`을 추가했다.
- 공개 배포 대상 URL 3개가 열리는 것을 확인했다.

### 작업 지침 정리

- `AGENTS.md`를 추가해 Codex가 이 저장소에서 따라야 할 작업 원칙을 정리했다.
- `CLAUDE.md`와 `AGENTS.md`를 비교해 현재 웹앱 2개 완료·배포 상태 기준으로 통합했다.
- 산출물 완료 여부와 다음 작업 우선순위는 `planning/status.md`를 기준으로 삼도록 정리했다.
- `README.md`, `webapps/README.md`, `planning/plan.md`, `planning/web-apps.md`, `planning/webapp-work-order.md`를 현재 웹앱 완료·배포 상태에 맞게 갱신했다.
- `slides/PPT_원고.md`, `lecture/강사용_원고.md`, `lecture/연수자_자료.md`에 웹앱 Pages URL과 실제 조작 방식 설명을 반영했다.
- `planning/webapp-work-order.md`에 연수 시연용 웹앱 제작 지시서를 작성했다.
- 문과 계열 교과서 PDF 3종(`도시의 미래탐구`, `법과 사회`, `화법과언어`)을 검토하고, 도시·법 웹앱 후보 6개에 대한 개별 작업지시서를 `planning/humanities-webapp-work-orders/`에 작성했다.
- 문과 계열 웹앱 병렬 구현을 위해 `planning/humanities-webapp-work-orders/agent-workflow.md`에 조율 에이전트, 수업효과 검토 에이전트, 구현 에이전트의 역할과 검토 기준을 정리했다.
- 수업효과 검토 에이전트가 후보 6개를 평가해 상위 3개(`폭염 취약 지역 커뮤니티 매핑`, `계약 성립·효력 판단기`, `스마트 도시 균형 실험실`)를 선별했다.
- 구현 에이전트 3명이 상위 3개 웹앱을 각자 독립 폴더에 병렬 구현했다.
- 구현 후 수업효과 검토 에이전트가 세 앱 모두 `통과` 판정을 냈다.
- 조율 단계에서 `webapps/index.html`과 `webapps/README.md`에 문과 계열 앱 3개를 연결했다.
- `화법과 언어`는 작업지시서가 아니라 아하포인트가 생길 만한 주제 제안으로 정리했다. 위치: `planning/humanities-webapp-work-orders/korean-language-topic-proposals.md`
- 사용자 피드백을 반영해 전자기 유도 앱의 초점을 오른손법칙이 아니라 "코일을 지나는 자기장 변화와 전류계 반응"으로 수정했다.

### 웹앱 1: 수평 투사 운동

파일: `webapps/horizontal-projectile/index.html`

완료 내용:

- 같은 높이에서 출발하는 두 공을 동시에 보여준다.
- 수평 속력은 다르지만 낙하 시간은 같다는 점을 애니메이션으로 보여준다.
- `느림 vs 빠름`, `보통 vs 빠름`, `매우 빠름 vs 빠름` 프리셋을 제공한다.
- `동시에 발사`, `다시 보기` 버튼으로 시연 흐름을 단순화했다.
- 착지 순간 `동시 착지` 배지를 표시한다.
- 학생이나 타교과 교사가 보아도 "수평 거리만 다르고 낙하 시간은 같다"는 결론을 확인할 수 있게 구성했다.

검증:

- 로컬 정적 서버에서 페이지 응답 확인
- JavaScript 문법 확인
- headless Chrome으로 주요 버튼 동작 확인
- Pages 배포 후 URL 확인

### 웹앱 2: 전자기 유도

파일: `webapps/electromagnetic-induction/index.html`

완료 내용:

- 교과서식 그림에 가깝게, 코일이 감긴 원통 안으로 막대자석이 들어갔다가 나오는 장면으로 구현했다.
- `가까이 두기`, `천천히 넣기`, `빠르게 넣기`, `빼기` 버튼을 제공한다.
- 자석이 멈춰 있을 때는 전류계가 0으로 돌아오도록 했다.
- 자석이 움직일 때만 전류계가 흔들리며, 빠르게 넣을 때 더 크게 반응한다.
- 자석을 뺄 때는 전류계가 반대 방향으로 흔들리도록 했다.
- 코일 안 자기장 상태를 `변화 없음`, `증가`, `빠르게 증가`, `감소`처럼 바로 읽을 수 있게 표시했다.
- 핵심 문장은 "가까움이 아니라 변화가 중요하다"로 정리했다.

검증:

- 로컬 정적 서버에서 페이지 응답 확인
- JavaScript 문법 확인
- Chrome DevTools Protocol 기반 버튼 동작 확인
- `빠르게 넣기` 중 자기장 변화, 전류 방향, 세기 상태 확인
- `빼기` 중 전류 방향 반전 확인
- Pages 배포 후 URL 확인

---

## 3. 현재 작업 파일 구조

```text
AI-teacher-training/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── _config.yml
├── .nojekyll
├── planning/
│   ├── status.md
│   ├── webapp-work-order.md
│   ├── web-apps.md
│   ├── training-context.md
│   ├── output-standards.md
│   ├── ai-tools-guide.md
│   ├── principles.md
│   └── plan.md
├── lecture/
│   ├── 연수자_자료.md
│   └── 강사용_원고.md
├── slides/
│   └── PPT_원고.md
└── webapps/
    ├── index.html
    ├── README.md
    ├── horizontal-projectile/
    │   └── index.html
    ├── electromagnetic-induction/
    │   └── index.html
    ├── heat-vulnerability-map/
    │   └── index.html
    ├── contract-validity-checker/
    │   └── index.html
    └── smart-city-balance/
        └── index.html
```

---

## 4. 다음 작업 우선순위

### 1순위: 연수 시연 흐름 점검

실제 연수 상황을 기준으로 두 웹앱을 1-2분씩 시연해 본다.

확인할 것:

- 강사가 질문을 던지고 버튼을 누르는 흐름이 자연스러운가
- 학생이나 타교과 교사가 첫 화면만 보고도 무엇을 비교하는지 알 수 있는가
- 버튼을 누른 뒤 결과가 너무 빠르거나 느리지 않은가
- 핵심 관찰 문장이 화면에서 충분히 잘 보이는가

필요하면 `planning/webapp-work-order.md`의 시연 흐름과 각 앱 화면 문구를 함께 조정한다.

### 2순위: 목록 페이지 다듬기

파일: `webapps/index.html`

현재 목록 페이지는 두 앱으로 이동하는 허브 역할을 한다. 실제 연수 시연 순서, 각 앱의 "깨야 할 직관", "보여 줄 변화" 문구를 반영해 다듬었다.

추가 검토:

- 현장용 링크 또는 QR 코드 제작 여부 결정

### 3순위: 슬라이드·강사용 원고 연결 점검

파일:

- `slides/PPT_원고.md`
- `lecture/강사용_원고.md`
- `lecture/연수자_자료.md`

현재 반영된 내용:

- Block 4 시연 위치에 각 앱 Pages URL을 삽입했다.
- 강사용 원고에 각 앱별 질문 문장과 조작 흐름을 추가했다.
- 연수자 자료에는 다른 교과 시연 앱 URL 2개를 안내했다.

추가 검토:

- 최종 배포본에서는 긴 URL을 QR 코드 또는 목록 페이지 URL 중심으로 줄일지 결정한다.

예시 질문:

- 수평 투사 운동: "빠르게 던진 공이 먼저 떨어질까요?"
- 전자기 유도: "자석을 가까이 두기만 하면 전류가 흐를까요?"

### 4순위: 모바일·교실 환경 최종 검수

확인할 것:

- 교실 빔프로젝터 비율에서 글자가 잘 보이는가
- 모바일 화면에서 버튼이 접히거나 겹치지 않는가
- Pages URL을 학교 네트워크에서 열 수 있는가
- Tailwind CDN 접속이 제한되는 환경이면 대체 방식이 필요한가

현재 구현은 CDN 기반이므로, 학교 네트워크에서 CDN이 막히는 경우 오프라인용 CSS 내장 버전을 별도로 만들 수 있다.

### 5순위: 문과 계열 웹앱 배포 확인

로컬 구현과 수업효과 검토를 통과한 문과 계열 웹앱 3개를 커밋·푸시한 뒤 Pages에서 열리는지 확인한다.

확인할 URL:

- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/smart-city-balance/`

확인할 것:

- 목록 페이지에서 세 앱 링크가 열린다.
- 각 앱의 핵심 버튼과 토글이 Pages 환경에서도 동작한다.
- Tailwind CDN이 학교 네트워크에서 차단되는지 확인한다.

### 6순위: 지침 문서 동기화 유지

다른 컴퓨터나 다른 AI 도구에서 작업한 뒤에는 `AGENTS.md`, `CLAUDE.md`, `planning/status.md`가 서로 충돌하지 않는지 확인한다.

운영 원칙:

- 현재 상태와 남은 작업은 `planning/status.md`에 가장 구체적으로 기록한다.
- `AGENTS.md`와 `CLAUDE.md`에는 반복 작업 규칙, 프로젝트 맥락, 현재 핵심 산출물만 간결하게 유지한다.
- 웹앱 제작 여부처럼 바뀔 수 있는 표현은 "제작 필요"로 남기지 말고 완료·배포 여부를 확인한 뒤 갱신한다.

### 후속 후보: 문과 계열 웹앱 작업지시서

위치: `planning/humanities-webapp-work-orders/`

도시의 미래탐구:

- `city-smart-city-balance.md`
- `city-heat-vulnerability-map.md`
- `city-budget-for-all.md`

법과 사회:

- `law-contract-validity-checker.md`
- `law-inheritance-family-tree.md`
- `law-youth-rights-age-lab.md`

화법과 언어:

- `korean-language-topic-proposals.md`

도시·법 상위 3개 웹앱은 구현과 수업효과 검토를 통과했다. 나머지 3개를 실제 구현할 때는 위 개별 작업지시서를 기준으로 하되, 기존 과학 웹앱과 마찬가지로 단일 `index.html`, Tailwind CSS CDN, vanilla JavaScript 기준을 유지한다.

병렬 구현 시에는 `planning/humanities-webapp-work-orders/agent-workflow.md`를 먼저 따른다. 수업효과 검토 에이전트가 후보 6개를 엄격히 평가해 상위 3개를 먼저 선택하고, 구현 결과가 학습목표와 아하포인트를 충분히 살리지 못하면 수정 요구 또는 보류 판정을 낼 수 있다.

---

## 5. 다음 커밋 후보

앞으로 작업을 계속한다면 아래처럼 커밋을 나누는 것을 권장한다.

- `Polish webapp index page`
- `Connect demo links to training materials`
- `Add classroom rehearsal notes`
- `Prepare offline-friendly webapp assets`

---

## 6. 작업 시 주의사항

- 이미 사용자가 만든 변경을 되돌리지 않는다.
- 한글로 보이는 UI는 유지하되, 폴더와 파일명은 영문으로 유지한다.
- 웹앱은 자유 탐구 도구보다 "변화에 따른 결과가 분명한 시연 도구"로 유지한다.
- 수식과 숫자는 보조 정보로만 사용하고, 핵심 이해는 움직임, 색, 방향, 강도 변화로 전달한다.
- 전자기 유도 앱은 오른손법칙 설명 앱이 아니라, 코일 안 자기장 변화가 전류를 만든다는 점을 보여주는 앱으로 유지한다.
- 앱을 수정한 뒤에는 로컬 확인, Pages 배포 확인, 주요 버튼 동작 확인을 한 번씩 수행한다.
