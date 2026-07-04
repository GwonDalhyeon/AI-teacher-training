# 프로젝트 현황 및 다음 작업 명세

최종 갱신일: 2026-07-04

---

## 1. 현재 상태 요약

연수 자료 제작이 완료된 상태다. 웹앱 7개 배포, PPT 38슬라이드 제작, 참여자 지침 파일 완성까지 모두 끝났다.

배포 URL:

- 웹앱 목록: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`
- 수평 투사 운동: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- 전자기 유도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`
- 폭염 취약 지역: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/`
- 계약 성립·효력: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/`
- 스마트 도시 균형: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/smart-city-balance/`
- 도시 예산 배분: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/city-budget-for-all/`
- 상속 관계 가계도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/inheritance-family-tree/`

---

## 2. 완료 목록

### 웹앱 (7개, 전체 커밋·푸시·배포 완료)

| 앱 | 교과 | 핵심 개념 |
|----|------|----------|
| 수평 투사 운동 | 통합과학1 | 수평 속력이 달라도 낙하 시간은 같다 |
| 전자기 유도 | 통합과학2 | 가까이 있음이 아니라 자기장 변화가 전류를 만든다 |
| 폭염 취약 지역 커뮤니티 매핑 | 도시의 미래탐구 | 취약성이 겹치면 우선 지원 지역이 달라진다 |
| 계약 성립·효력 판단기 | 법과 사회 | 계약은 서명보다 의사 합치와 효력 요건을 따지는 과정이다 |
| 스마트 도시 균형 실험실 | 도시의 미래탐구 | 스마트 도시는 기술 총량보다 공공성과 참여의 균형 문제다 |
| 모두를 위한 도시 예산 배분 | 도시의 미래탐구 | 예산 선택은 누가 반영되고 미뤄지는지를 바꾼다 |
| 상속 관계 가계도 시뮬레이터 | 법과 사회 | 상속은 순위, 배우자 지위, 채무 조건이 함께 작동한다 |

### 강의 자료 (완료)

| 파일 | 역할 |
|------|------|
| `slides/PPT_원고.md` | 38슬라이드 원고 |
| `slides/ChatGPT를_이용한_수업_조언자_만들기.pptx` | 완성 PPTX (38슬라이드) |
| `lecture/강사용_원고.md` | 강사용 원고 (강사 메모 포함) |
| `lecture/연수자_자료.md` | 참여자 배포용 자료 |

### 참여자 지침 파일 (완료)

| 파일 | 용도 |
|------|------|
| `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md` | ChatGPT 프로젝트 지침 칸에 붙여넣기 |
| `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md` | 프로젝트에 소스로 업로드 |
| `연수용 프로젝트 지침모음/Gems용_수업설계조언자_시스템지침.md` | Gemini Gems용 시스템 지침 |

---

## 3. 미커밋 파일 (필요 시 커밋)

- `slides/create_pptx.py` — PPTX 빌드 스크립트
- `slides/ChatGPT를_이용한_수업_조언자_만들기.pptx` — 완성 PPTX

`slides/work_unpacked/`는 빌드 임시 디렉터리이므로 커밋하지 않는다. `.gitignore`에 추가 권장.

---

## 4. 작업 시 주의사항

- 웹앱은 단일 `index.html`, Tailwind CSS CDN, vanilla JavaScript 기준을 유지한다.
- 폴더와 파일명은 영문, UI 표시 문구는 한글로 유지한다.
- 전자기 유도 앱은 오른손법칙이 아니라 "코일 안 자기장 변화 → 전류"에 초점을 맞춘다.
- PPT 재빌드 시 `slides/create_pptx.py` 실행 후 `slides/work_unpacked/`는 커밋하지 않는다.
