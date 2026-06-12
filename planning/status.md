# 프로젝트 현황 및 다음 작업 명세

이 파일은 새 세션이나 다른 작업자가 바로 이어받을 수 있도록 현재까지 완료된 일, 배포 상태, 앞으로 할 일을 정리한 인수인계 명세서다.

최종 갱신일: 2026-06-13

---

## 1. 현재 상태 요약

- 저장소: `AI-teacher-training`
- 기본 브랜치: `main`
- GitHub Pages: 공개 저장소 기준으로 활성화 완료
- Pages 배포 방식: `main` 브랜치의 루트에서 정적 파일 배포
- 웹앱 기술 스택: 단일 `index.html`, Tailwind CSS CDN, vanilla JavaScript
- 파일·폴더명 원칙: 영문 사용
- 웹 화면 표시 원칙: 제목, 버튼, 관찰 문장 등 사용자에게 보이는 문구는 한글 사용
- 작업 지침: `AGENTS.md`와 `CLAUDE.md`는 현재 완료·배포 상태를 같은 기준으로 공유한다.

배포 URL:

- 웹앱 목록: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`
- 수평 투사 운동: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- 전자기 유도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`
- 폭염 취약 지역: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/`
- 계약 성립·효력: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/`
- 스마트 도시 균형: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/smart-city-balance/`
- 도시 예산 배분: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/city-budget-for-all/`
- 상속 관계 가계도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/inheritance-family-tree/`

### 웹앱 현황

| 앱 | 경로 | 상태 |
|----|------|------|
| 수평 투사 운동 | `webapps/horizontal-projectile/` | 완료·커밋·푸시·배포 확인 |
| 전자기 유도 | `webapps/electromagnetic-induction/` | 완료·커밋·푸시·배포 확인 |
| 폭염 취약 지역 | `webapps/heat-vulnerability-map/` | 완료·커밋·푸시 (배포 확인 미완) |
| 계약 성립·효력 | `webapps/contract-validity-checker/` | 완료·커밋·푸시 (배포 확인 미완) |
| 스마트 도시 균형 | `webapps/smart-city-balance/` | 완료·커밋·푸시 (배포 확인 미완) |
| 도시 예산 배분 | `webapps/city-budget-for-all/` | 완료·커밋·푸시 (배포 확인 미완) |
| 상속 관계 가계도 | `webapps/inheritance-family-tree/` | 완료·커밋·푸시 (배포 확인 미완) |

### PPT 현황

| 파일 | 상태 |
|------|------|
| `slides/ChatGPT를_이용한_수업_조언자_만들기.pptx` | 생성 완료 (38슬라이드, 146KB) |
| `slides/create_pptx.py` | 빌드 스크립트 완성 (미커밋) |
| `slides/PPT_원고.md` | 원고 완성·커밋 완료 |

PPT 파일은 PowerPoint에서 열 때 복구 경고가 발생한다. 내용과 레이아웃은 정상이며 사용자가 직접 해결 예정이다.

---

## 2. 완료된 작업

### 저장소·배포 정리

- GitHub Pages용 `webapps/` 구조를 생성했다.
- Pages 빌드 오류를 막기 위해 `_config.yml`과 `.nojekyll`을 추가했다.
- `.gitignore`에 `*.hwp`, `*.hwpx`, `manifest.jsonl`을 추가했다.
- 공개 배포 대상 URL 3개(수평 투사, 전자기 유도, 갤러리)가 열리는 것을 확인했다.

### 작업 지침 정리

- `AGENTS.md`와 `CLAUDE.md`를 현재 완료·배포 상태에 맞게 정리했다.
- `slides/PPT_원고.md`, `lecture/강사용_원고.md`, `lecture/연수자_자료.md`에 웹앱 Pages URL과 실제 조작 방식 설명을 반영했다.

### 웹앱

- 자연과학 계열 2개(수평 투사 운동, 전자기 유도): 구현·배포·검증 완료.
- 문과 계열 5개(폭염 취약 지역, 계약 성립·효력, 스마트 도시, 도시 예산, 상속 가계도): 구현·수업효과 검토 통과·커밋·푸시 완료. Pages URL 직접 열기 확인은 미완.
- `webapps/index.html` 갤러리: 7개 앱 모두 연결 완료.

### PPT

- `slides/PPT_원고.md` S01–S38 원고 완성.
- `slides/create_pptx.py`로 38슬라이드 PPTX 빌드 완료.
- 주요 슬라이드 시각 QA: S01·S04·S06·S10·S22·S23·S38 직접 확인. S23 텍스트 잘림 수정(파일 생성 → 파일 자동 생성) 후 재빌드 완료.
- 강사 멘트 전체 슬라이드 노트에 삽입 완료.

### 참여자 지침 파일

- `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md`
- `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md`
- `연수용 프로젝트 지침모음/Gems용_수업설계조언자_시스템지침.md`

---

## 3. 남은 작업 (우선순위 순)

### 1순위 — PPT 복구 경고 해결 (사용자 담당)

`slides/ChatGPT를_이용한_수업_조언자_만들기.pptx`를 PowerPoint에서 열 때 "복구할 수 없는 내용을 제거했습니다" 경고가 발생한다. 내용·레이아웃은 정상이나 XML 구조 문제로 추정된다.

해결 후 해야 할 것:
- PowerPoint에서 직접 열어 저장 (→ XML 정규화)
- 또는 `slides/create_pptx.py` XML 검토 후 재빌드

### 2순위 — 문과 계열 웹앱 5개 Pages 배포 확인

커밋·푸시는 완료. 실제 Pages URL이 열리는지 브라우저에서 직접 확인하지 않은 상태다.

확인할 URL:
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/smart-city-balance/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/city-budget-for-all/`
- `https://gwondalhyeon.github.io/AI-teacher-training/webapps/inheritance-family-tree/`
- 갤러리 페이지에서 7개 앱 링크가 모두 열리는지 확인

### 3순위 — Block 4 연결 점검

`slides/PPT_원고.md`, `lecture/강사용_원고.md`, `lecture/연수자_자료.md`에서 아래 항목을 확인한다.

- 갤러리 URL (`webapps/index.html`) 안내가 들어가 있는가
- QR 코드 또는 단축 URL 안내가 필요한가
- Block 4 흐름(웹 AI vs 로컬 AI → 수학 사례 → 갤러리 소개 → 대표 시연 3개 → 아이디어 스케치 → 조언자에 요청)이 슬라이드·원고와 일치하는가

### 4순위 — 교실 환경 최종 점검

- 빔프로젝터 비율(4:3, 16:9)에서 글자 크기와 레이아웃
- 모바일 화면에서 버튼·슬라이더가 접히거나 겹치지 않는가
- 학교 네트워크에서 Tailwind CDN 차단 여부 (차단 시 CSS 인라인 내장 버전 필요)

### 5순위 — PPT 및 빌드 스크립트 커밋

현재 미커밋 상태:
- `slides/ChatGPT를_이용한_수업_조언자_만들기.pptx`
- `slides/create_pptx.py`

복구 경고 해결 후 함께 커밋한다. `slides/work_unpacked/`는 빌드 임시 디렉터리이므로 `.gitignore`에 추가 권장.

---

## 4. 파일 구조

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
│   ├── PPT_원고.md
│   ├── create_pptx.py          ← 미커밋
│   └── ChatGPT를_이용한_수업_조언자_만들기.pptx  ← 미커밋
├── 연수용 프로젝트 지침모음/
│   ├── ChatGPT용_수업설계조언자_프로젝트지침.md
│   ├── Layer_2_수업설계조언자.md
│   └── Gems용_수업설계조언자_시스템지침.md
└── webapps/
    ├── index.html
    ├── README.md
    ├── horizontal-projectile/index.html
    ├── electromagnetic-induction/index.html
    ├── heat-vulnerability-map/index.html
    ├── contract-validity-checker/index.html
    ├── smart-city-balance/index.html
    ├── city-budget-for-all/index.html
    └── inheritance-family-tree/index.html
```

---

## 5. 작업 시 주의사항

- 이미 사용자가 만든 변경을 되돌리지 않는다.
- 한글로 보이는 UI는 유지하되, 폴더와 파일명은 영문으로 유지한다.
- 웹앱은 자유 탐구 도구보다 "변화에 따른 결과가 분명한 시연 도구"로 유지한다.
- 전자기 유도 앱은 오른손법칙 설명 앱이 아니라, 코일 안 자기장 변화가 전류를 만든다는 점을 보여주는 앱으로 유지한다.
- 앱을 수정한 뒤에는 로컬 확인, Pages 배포 확인, 주요 버튼 동작 확인을 한 번씩 수행한다.
- PPT 재빌드 시 `slides/create_pptx.py`를 실행한 뒤 `slides/work_unpacked/`는 커밋하지 않는다.
