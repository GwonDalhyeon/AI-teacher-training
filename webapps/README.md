# 웹앱 예시

이 폴더에는 연수 Block 4에서 보여 줄 시연용 웹앱과, 이후 확장할 수 있는 웹앱 아이디어를 둔다.

배포 목록: `https://gwondalhyeon.github.io/AI-teacher-training/webapps/`

## 구현 완료

- `horizontal-projectile/`: 수평 투사 운동 시연 앱
  - `https://gwondalhyeon.github.io/AI-teacher-training/webapps/horizontal-projectile/`
- `electromagnetic-induction/`: 전자기 유도 시연 앱
  - `https://gwondalhyeon.github.io/AI-teacher-training/webapps/electromagnetic-induction/`
- `heat-vulnerability-map/`: 폭염 취약 지역 커뮤니티 매핑 앱
  - `https://gwondalhyeon.github.io/AI-teacher-training/webapps/heat-vulnerability-map/`
- `contract-validity-checker/`: 계약 성립·효력 판단기 앱
  - `https://gwondalhyeon.github.io/AI-teacher-training/webapps/contract-validity-checker/`
- `smart-city-balance/`: 스마트 도시 균형 실험실 앱
  - `https://gwondalhyeon.github.io/AI-teacher-training/webapps/smart-city-balance/`

문과 계열 앱 3개는 `planning/humanities-webapp-work-orders/agent-workflow.md` 기준으로 수업효과 검토 에이전트가 상위 3개를 선별한 뒤 병렬 구현했고, 구현 후 사후 검토에서 모두 통과 판정을 받았다. 아직 커밋·푸시 후 Pages 배포 확인은 하지 않았다.

## 아이디어 보관

- `lesson-alignment-checker/`: 목표-활동-평가 연결 점검기
- `question-builder/`: 수업 질문 생성기
- `rubric-builder/`: 루브릭 초안 생성기
- `class-advisor-context-card/`: 수업 조언자 맥락 카드 생성기

위 네 폴더는 현재 `README.md`만 있는 아이디어 보관용이다. 실제 웹앱으로 만들 때는 단일 `index.html`, Tailwind CSS CDN, vanilla JavaScript 기준을 따른다.

웹앱 제작은 전문적인 코딩 수업이 아니라, 교사가 필요한 수업 도구를 말로 설계하고 시제품을 확인하는 경험으로 다룬다.
