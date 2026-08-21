# 05 통합 에이전트 심의 결과

최종 PPT까지 사용자 승인이 끝난 뒤 다음 명령을 실행합니다.

```text
/workflow-council 전체 결과물의 근거 연결과 실행 가능성을 종합 심의해줘
```

생성 파일:

- `council-decision.md`: 관점별 판정과 종합 권고
- `dissent-log.md`: 해소되지 않은 이견과 소수 의견
- `action-items.md`: 수정 대상, 담당 단계, 재검증 조건

Agent Teams는 실험 기능이며 네 개의 별도 Claude 세션을 사용하므로 일반 Skill보다 토큰 사용량이 큽니다. 에이전트의 합의는 사용자 승인을 대신하지 않습니다.

