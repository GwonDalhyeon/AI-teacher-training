# ChatGPT 수업 조언자 만들기 연수 준비

이 저장소는 교사 대상 3시간 연수인 "ChatGPT를 이용한 수업 조언자 만들기"의 자료를 제작하고 관리하기 위한 작업 공간입니다.

기본 원고는 `04dc80ab9d_AI로_내_수업_비서_만들기.md`이며, 연수에서는 이 원고의 흐름을 바탕으로 ChatGPT 프로젝트 설정, 수업 조언자 만들기, 교과 공통 실습, 웹앱 제작 개론과 시연을 다룹니다.

현재 상태와 다음 작업 우선순위는 `planning/status.md`를 기준으로 확인합니다.

## 연수 방향

- AI를 교사의 대체자가 아니라 수업 설계와 판단을 돕는 조언자로 다룹니다.
- 특정 교과에 묶이지 않고 모든 교과 교사가 자기 맥락에 맞게 적용할 수 있도록 구성합니다.
- 설명보다 직접 경험을 중시하되, 시간이 부족하면 강사 시연으로 대체할 수 있게 설계합니다.
- ChatGPT 프로젝트의 지침, 파일, 채팅 맥락, 테스트 질문의 역할을 구분해 설명합니다.
- 웹앱 제작은 코딩 교육이 아니라 교사가 필요한 수업 도구를 말로 설계하고 시제품을 확인하는 경험으로 다룹니다.

## 폴더 구조

```text
AI-teacher-training/
├─ source/       원본 자료와 참고 문서
├─ converted/    변환된 원고와 추출 텍스트
├─ planning/     연수 설계, 일정, 작업 계획
├─ lecture/      수정 강의록과 강사용 진행 원고
├─ worksheets/   교사용 활동지와 실습지
├─ slides/       PPT 원고와 슬라이드 구성안
├─ prompts/      ChatGPT 프로젝트 지침과 실습 프롬프트
├─ webapps/      Block 4 시연용 웹앱과 아이디어 보관
├─ assets/       이미지, 아이콘, 보조 자료
└─ exports/      PDF, PPTX, 배포용 산출물
```

## 핵심 산출물

| 파일 | 용도 |
|------|------|
| `lecture/연수자_자료.md` | 참여자 배포용 자료 |
| `lecture/강사용_원고.md` | 강사용 진행 원고 |
| `slides/PPT_원고.md` | PPT 제작 원고 |
| `연수용 프로젝트 지침모음/ChatGPT용_수업설계조언자_프로젝트지침.md` | 참여자가 ChatGPT 프로젝트 지침에 붙여넣는 파일 |
| `연수용 프로젝트 지침모음/Layer_2_수업설계조언자.md` | 참여자가 프로젝트 소스로 업로드하는 파일 |
| `webapps/horizontal-projectile/index.html` | 수평 투사 운동 시연 앱 |
| `webapps/electromagnetic-induction/index.html` | 전자기 유도 시연 앱 |

## 웹앱 배포

- 웹앱 목록: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`
- 수평 투사 운동: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- 전자기 유도: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`

현재 웹앱 2개는 구현과 GitHub Pages 배포 확인까지 완료된 상태입니다. 다음 작업은 연수 자료 안에 위 URL 또는 QR 안내를 연결하고, 실제 교실 환경에서 시연 흐름을 점검하는 것입니다.

