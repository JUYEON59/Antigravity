---
name: workflow-council
description: "완료된 리서치·트렌드 분석·제안서·프레젠테이션을 네 명의 전문 에이전트가 서로 검토하고 반론한 뒤 통합 판정과 이견 기록을 만든다. 전체 결과물의 최종 교차 검토가 필요할 때 /workflow-council로 사용한다."
argument-hint: "[심의 목적 또는 특별 검토 기준]"
disable-model-invocation: true
---

# 통합 에이전트 심의회

사용자 요청: `$ARGUMENTS`

이 Skill은 Claude Code Agent Teams를 사용한다. 네 관점의 에이전트가 서로 메시지를 주고받아 검토하고, 현재 세션의 리더가 합의안과 이견을 기록한다.

## 시작 조건

1. `${CLAUDE_PROJECT_DIR}/CLAUDE.md`와 `output/workflow-status.md`를 읽는다.
2. 리서치, 트렌드 분석, 제안서, 프레젠테이션 구성안, 실제 PPT가 모두 `approved`인지 확인한다.
3. 필수 결과물 파일이 모두 존재하는지 확인한다.
4. `stale` 또는 `revision_requested` 상태가 하나라도 있으면 심의를 시작하지 않는다.
5. Agent Teams가 활성화되지 않았으면 상호 토론을 흉내 내지 말고 `.claude/settings.json` 적용과 Claude Code 재시작을 안내한다.

이 명령의 직접 호출을 네 명의 읽기 전용 팀원을 소집하는 사용자 승인으로 간주한다.

## 팀 구성

현재 세션이 리더가 되어 다음 에이전트 유형과 같은 이름으로 팀원을 생성한다.

- `research-auditor`
- `trend-auditor`
- `proposal-auditor`
- `presentation-auditor`

각 팀원에게 입력 파일 경로, 심의 목적, 판정 기준, 다른 팀원의 이름을 전달한다. 네 팀원은 결과물 파일을 수정하지 않는다.

## 협의 순서

1. **독립 감사**: 네 팀원이 동시에 자기 영역을 검토한다.
2. **초기 공유**: 각 팀원이 발견 사항과 잠정 판정을 다른 세 팀원에게 보낸다.
3. **상호 반론**: 각 팀원이 다른 관점의 주장 하나 이상을 근거로 검증한다.
4. **응답과 수정**: 최초 주장을 유지·수정·철회하고 이유를 공유한다.
5. **최종 투표**: 각 팀원이 `통과 권고`, `조건부 통과`, `재작업 필요` 중 하나를 선택한다.
6. **리더 종합**: `references/decision-rules.md`에 따라 합의, 이견, 조치 순서를 작성한다.

리더는 모든 팀원의 초기 의견과 반론이 도착하기 전에 결론을 내리지 않는다.

## 결과 저장

기존 심의 결과가 있으면 `output/05_council/archive/`에 보존한 뒤 다음을 만든다.

- `output/05_council/council-decision.md`
- `output/05_council/dissent-log.md`
- `output/05_council/action-items.md`

`council-decision.md`에는 다음을 포함한다.

- 심의 범위와 참여자
- 관점별 판정
- 합의된 발견
- 차단 문제와 주요 문제
- 최종 권고
- 권고의 근거
- 사용자가 결정할 항목

`dissent-log.md`에는 소수 의견과 해소되지 않은 이견을 삭제하지 않고 기록한다.

## 상태와 권한

- 심의 결과를 만들면 상태표의 통합 심의를 `draft`로 기록한다.
- `재작업 필요`이면 관련 단계의 상태를 자동 변경하지 말고, 변경 권고만 `action-items.md`에 적는다.
- 기존 결과물을 직접 수정하거나 승인 상태를 취소하지 않는다.
- 에이전트 합의는 최종 사용자 승인을 대체하지 않는다.
- 사용자가 심의 결과를 승인한 뒤에만 통합 심의를 `approved`로 변경한다.

모든 팀원의 완료를 확인한 뒤 생성 파일, 투표 결과, 합의 사항, 남은 이견, 사용자 결정 항목을 보고한다.

