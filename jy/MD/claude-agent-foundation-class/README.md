# Claude Code 컨텍스트·하네스 설계 기초

## 프로젝트 목표

반복 프롬프트를 파일 기반 작업 체계로 바꾸고, 앞 단계의 산출물을 다음 단계의 입력으로 연결합니다.

```text
CLAUDE.md
    ↓
/research
    ↓
research-report.md
    ↓
/trend-analysis
    ↓
trend-analysis.md
    ↓
/proposal
    ↓
proposal.md
    ↓
/presentation
    ↓
presentation-outline.md → presentation.pptx
    ↓
/workflow-council
    ↓
council-decision.md
```

## 학습 성과

수업을 마치면 다음을 할 수 있습니다.

1. 프로젝트 공통 규칙과 특정 작업 절차를 분리한다.
2. 프로젝트 Skill을 직접 호출하고 로딩 상태를 확인한다.
3. 출처가 있는 리서치 보고서를 만든다.
4. 사실 자료에서 변화 신호와 트렌드를 도출한다.
5. 트렌드를 실행 가능한 제안과 측정 지표로 바꾼다.
6. 승인된 제안서를 슬라이드 구조와 실제 PPT로 변환한다.
7. 단계 승인, 버전 보존, 산출물 연결을 검증한다.
8. 전문 에이전트 팀이 서로 반론하고 합의·이견·조치안을 만드는 과정을 운영한다.

## 권장 환경

- 최신 Claude Code
- 인터넷 연결: 최신 정보 조사에 필요
- 실제 PPT 생성이 가능한 도구 또는 라이브러리
- 결과 확인용 PowerPoint, Keynote, LibreOffice Impress 또는 호환 뷰어

설치 환경은 기관마다 다르므로 수업 전에 `lessons/00-instructor-guide.md`의 사전 점검을 수행합니다.

## 수업 편성

| 차시 | 주제 | 주요 산출물 |
|---:|---|---|
| 1 | 프로젝트 구조와 `CLAUDE.md` | 공통 규칙 확인 |
| 2 | Skill 구조와 등록 | 핵심 Skill 4개 확인 |
| 3 | 리서치 | `research-report.md` |
| 4 | 트렌드 분석 | `trend-analysis.md` |
| 5 | 제안서 | `proposal.md` |
| 6 | 프레젠테이션 | 구성안, 원고, `.pptx` |
| 7 | 전체 연결과 오류 수정 | 통합 프로젝트 |
| 선택 심화 | 에이전트 심의회 | 합의안, 이견 기록, 조치안 |

## 공식 문서 기준

이 패키지는 2026-08-02에 확인한 Claude Code 공식 문서의 프로젝트 `CLAUDE.md`, `.claude/skills/<name>/SKILL.md`, `.claude/agents/`, Agent Teams, `/context`, `/memory`, `/skills` 동작을 기준으로 작성했습니다. 링크는 `OFFICIAL-REFERENCES.md`에 정리되어 있습니다.
