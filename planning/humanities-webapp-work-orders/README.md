# Humanities Web App Work Orders

이 폴더는 문과 계열 교과서 내용을 바탕으로 연수 시연용 웹앱을 만들 때 사용할 개별 작업지시서를 모은다.

공통 원칙:

- 각 웹앱은 `webapps/{english-folder}/index.html` 단일 파일로 만든다.
- Tailwind CSS CDN과 vanilla JavaScript만 사용한다.
- 백엔드, 빌드 도구, 외부 API, 패키지 설치를 사용하지 않는다.
- 폴더명과 파일명은 영문으로 유지하고, 화면에 보이는 문구는 한글로 작성한다.
- 퀴즈나 단순 정답 확인보다, 조건·관점·이해관계·판단 기준을 바꾸면 결과가 달라지는 경험을 우선한다.
- 교과서를 그대로 복제하지 말고, 교과 개념을 수업 시연에 맞게 축약해 구현한다.

병렬 구현 운영:

- `agent-workflow.md`
- 도시·법 후보 6개를 바로 동시에 구현하지 않고, 수업효과 검토 에이전트가 먼저 엄격히 평가해 상위 3개를 고른다.
- 수업효과 검토 에이전트는 구현 보류와 수정 요구 권한을 가진다.
- 구현 에이전트는 자기 앱 폴더의 `index.html`만 수정하고, 공통 파일은 조율 에이전트가 마지막에 통합한다.

## 도시의 미래탐구

- `city-smart-city-balance.md`
- `city-heat-vulnerability-map.md`
- `city-budget-for-all.md`

## 법과 사회

- `law-contract-validity-checker.md`
- `law-inheritance-family-tree.md`
- `law-youth-rights-age-lab.md`

## 화법과 언어 주제 제안

`화법과 언어`는 아직 작업지시서로 확정하지 않았다. 표현 교정형 앱보다 구조·규칙·담론 흐름이 보이는 주제를 더 찾아 제안 문서로 정리했다.

- `korean-language-topic-proposals.md`
