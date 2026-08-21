---
name: presentation
description: "승인된 proposal.md를 먼저 슬라이드 구성안·콘텐츠·발표 원고로 변환하고, 구성안 승인 후 실제 presentation.pptx를 생성·검증한다. 제안서 다음 단계에서 /presentation으로 사용한다."
argument-hint: "[제안서 경로 또는 구성안 승인 지시]"
disable-model-invocation: true
---

# 프레젠테이션 제작

이 Skill은 반드시 **구성안 작성 → 사용자 승인 → 실제 PPT 생성**의 두 단계로 실행한다. 구성안을 스스로 승인하지 않는다.

## 승인 게이트

1. `${CLAUDE_PROJECT_DIR}/CLAUDE.md`와 `output/workflow-status.md`를 읽는다.
2. 제안서 상태가 `approved`인지 확인한다.
3. `output/03_proposal/proposal.md`가 존재하는지 확인한다.
4. 승인이나 파일이 없으면 무엇이 필요한지 알리고 중단한다.

사용자 요청: `$ARGUMENTS`

## 1단계: 구성안

구성안이 아직 승인되지 않았다면 다음만 수행한다.

1. 제안서, 트렌드 분석, 리서치 보고서를 읽는다.
2. 청중, 발표 목적, 발표 시간, 원하는 행동을 입력에서 찾는다.
3. 정보가 없으면 `input/client-brief.md`를 사용하고 합리적인 가정을 표시한다.
4. `templates/presentation-template.md`를 사용해 다음 파일을 만든다.
   - `output/04_presentation/presentation-outline.md`
   - `output/04_presentation/presentation-content.md`
   - `output/04_presentation/presentation-script.md`
5. 12~16장을 기본 범위로 삼되 발표 시간과 내용량에 맞게 조정한다.
6. 한 슬라이드에 하나의 핵심 메시지만 사용한다.
7. 제목은 내용을 요약하는 결론형 문장으로 작성한다.
8. 제안서의 긴 문단을 복사하지 말고 화면용 문구로 압축한다.
9. 모든 수치, 인용, 출처 번호를 원문과 대조한다.
10. 각 슬라이드에 원본 제안서 절과 권장 시각화를 연결한다.
11. 상태표에서 프레젠테이션 구성안을 `draft`로 변경한다.
12. 구성안 요약과 누락 점검 결과를 보고하고 승인을 요청한 뒤 멈춘다.

구성안 승인 전에는 `.pptx`를 생성하지 않는다.

## 2단계: 실제 PPT

사용자가 현재 대화에서 구성안을 명시적으로 승인했거나 상태표에 구성안이 `approved`로 기록된 경우에만 수행한다.

1. 승인 표현을 상태표에 기록하고 구성안을 `approved`로 변경한다.
2. `references/pptx-production.md`를 읽는다.
3. 승인된 구성안, 콘텐츠, 발표 원고를 다시 읽는다.
4. 사용 가능한 PPT 생성 기능이나 호환 라이브러리를 확인한다.
5. 생성 도구가 없고 설치가 필요하면 설치 대상과 이유를 설명하고 사용자 허가를 받은 뒤 계속한다.
6. 텍스트 확장자만 바꾼 가짜 `.pptx`를 만들지 않는다.
7. 편집 가능한 텍스트, 도형, 표, 차트를 우선 사용한다.
8. 슬라이드별 발표자 노트를 지원하는 도구라면 `presentation-script.md`를 노트에 넣는다.
9. 기존 `presentation.pptx`가 있으면 `archive/`에 타임스탬프 이름으로 보존한다.
10. `output/04_presentation/presentation.pptx`를 생성한다.

## PPT 검증

- 파일이 존재하고 크기가 0보다 큰가?
- 실제 OOXML 프레젠테이션 패키지이며 정상적으로 열리는가?
- 슬라이드 수와 순서가 승인된 구성안과 일치하는가?
- 제목, 본문, 수치, 출처가 `presentation-content.md`와 일치하는가?
- 잘림, 겹침, 화면 밖 요소가 없는가?
- 한글 글꼴이 대체되어도 읽을 수 있는가?
- 발표자 노트 또는 별도 발표 원고가 모든 슬라이드에 있는가?

가능하면 슬라이드를 렌더링해 시각적으로 검사한다. 렌더링 도구가 없으면 수행하지 못한 검증을 명확히 보고한다.

검증을 통과하면 실제 PPT 상태를 `approved`로 바꾸지 말고 `draft`로 기록한다. 최종 승인은 사용자가 파일을 열어 본 뒤에만 기록한다.

완료 후 생성 파일, 슬라이드 수, 검증 결과, 남은 한계, 최종 승인 대상을 보고한다.

