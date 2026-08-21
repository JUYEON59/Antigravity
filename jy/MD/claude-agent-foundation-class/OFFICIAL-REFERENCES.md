# 공식 문서 참고 링크

확인일: 2026-08-02

## Claude Code

- [Skills로 Claude 확장하기](https://code.claude.com/docs/en/slash-commands)
- [Claude가 프로젝트를 기억하는 방식](https://code.claude.com/docs/en/memory)
- [설정 디버깅: `/context`, `/skills`, `/memory`](https://code.claude.com/docs/en/debug-your-config)
- [Claude Code 확장 기능 개요](https://code.claude.com/docs/en/features-overview)
- [사용자 정의 서브에이전트 만들기](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Agent Teams 운영](https://code.claude.com/docs/en/agent-teams)

## 수업에서 적용한 기준

- 프로젝트 지침은 루트의 `CLAUDE.md` 또는 `.claude/CLAUDE.md`에 둘 수 있습니다.
- 프로젝트 Skill은 `.claude/skills/<skill-name>/SKILL.md`에 둡니다.
- Skill의 명령 이름은 프로젝트 Skill 폴더 이름에서 결정됩니다.
- `description`은 Skill의 용도와 사용 시점을 설명합니다.
- `/context`는 현재 컨텍스트에 로드된 구성 요소를 보여 줍니다.
- `/memory`는 프로젝트 및 사용자 지침 파일을 확인하고 편집할 때 사용합니다.
- `/skills`는 사용 가능한 Skill과 출처를 확인할 때 사용합니다.
- `CLAUDE.md`는 구체적이고 간결하게 유지하며, 공식 문서는 약 200줄 이하를 권장합니다.
- 프로젝트 에이전트 정의는 `.claude/agents/*.md`에 둘 수 있습니다.
- 서브에이전트는 기본적으로 리더에게만 결과를 반환하고 서로 직접 대화하지 않습니다.
- Agent Teams의 팀원은 공유 작업 목록과 메시지를 사용해 서로 직접 대화할 수 있습니다.
- Agent Teams는 실험 기능이며 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 설정이 필요하고 토큰 사용량이 증가합니다.

Claude Code는 지속적으로 업데이트되므로 실제 수업 직전 공식 문서를 다시 확인합니다.
