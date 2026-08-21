# Claude 에이전트 기초 수업 패키지

이 폴더는 하나의 주제를 **리서치 → 트렌드 분석 → 제안서 → PPT**로 연결하는 7차시 실습 프로젝트입니다.

## 10분 빠른 시작

1. 이 폴더를 원하는 위치에 복사하거나 ZIP을 해제합니다.
2. `input/topic.md`와 `input/client-brief.md`를 수업 주제에 맞게 수정합니다.
3. 이 폴더에서 Claude Code를 실행합니다.
4. `/context`를 실행해 `CLAUDE.md`가 Memory files에 표시되는지 확인합니다.
5. `/skills`를 실행해 핵심 Skill 4개와 선택 심화 `workflow-council`을 확인합니다.
6. 아래 순서로 실행하고, 각 결과를 검토한 뒤 명시적으로 승인합니다.

```text
/research input/topic.md를 기준으로 조사해줘
리서치 결과를 승인해
/trend-analysis output/01_research/research-report.md를 분석해줘
트렌드 분석 결과를 승인해
/proposal output/02_trend-analysis/trend-analysis.md를 바탕으로 제안서를 작성해줘
제안서를 승인해
/presentation output/03_proposal/proposal.md를 발표 자료로 구성해줘
슬라이드 구성안을 승인해. 실제 PPT를 생성해줘
/workflow-council 전체 결과물의 근거 연결과 실행 가능성을 종합 심의해줘
```

## 핵심 파일

| 파일 또는 폴더 | 용도 |
|---|---|
| `CLAUDE.md` | 프로젝트 전체에서 항상 지킬 규칙 |
| `.claude/skills/` | 단계별 전문 작업 절차 |
| `.claude/agents/` | 통합 심의에서 서로 토론하는 전문 에이전트 역할 |
| `input/` | 주제, 의뢰 정보, 참고 자료 |
| `templates/` | 단계별 결과물 형식 |
| `output/workflow-status.md` | 초안·승인 상태 기록 |
| `lessons/` | 1~7차시 학생용 실습안 |
| `checklists/` | 검증표, 평가표, 문제 해결 |

## 중요한 운영 원칙

- 다음 단계 명령은 직전 결과의 자동 승인이 아닙니다.
- 승인 전에는 다음 단계로 넘어가지 않습니다.
- 수정 시 기존 파일은 각 단계의 `archive/` 폴더에 보존합니다.
- 실제 `.pptx` 생성 도구가 없다면 가짜 PPT 파일을 만들지 않습니다. 구성안까지 완성한 뒤 필요한 도구 설치 권한을 확인합니다.
- `/workflow-council`은 선택 심화 단계이며 Agent Teams를 사용하므로 토큰 사용량이 증가합니다.

## 수업 자료 순서

강사는 `lessons/00-instructor-guide.md`부터 읽고, 학생은 `lessons/01-project-rules.md`부터 차례로 진행합니다. 에이전트 토론은 `lessons/08-agent-council.md`에서 선택 심화로 진행합니다.
