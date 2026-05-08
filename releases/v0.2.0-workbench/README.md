# v0.2.0-workbench：单实例总控多团队骨架

对应文章：EP-004 ~ EP-009、Code Drop 02

## 这个包解决什么问题

一个 Hermes 实例，如何管多个团队而不乱。

## 包含什么

| 文件/目录 | 说明 |
|---|---|
| `templates/team-registry.min.yaml` | 团队注册表示例（定义团队边界） |
| `templates/team-boss/team-boss.thinking.md` | team-boss 最小路由规则 |
| `templates/context-injection/inject.min.py` | 上下文注入脚本（派单前塞入角色档案和记忆） |
| `templates/context-injection/context-pack.example/` | 注入内容示例（project-facts.md、active-constraints.md） |
| `examples/multi-bot-vs-single-instance.md` | 为什么选单实例而非多 Bot |
| `examples/task-routing-flow.md` | 任务路由流程示意 |
| `guides/why-single-instance.md` | 单实例选择说明 |
| `guides/sub-agent-limits.md` | 子代理限制规则（新增） |

## 不包含什么（重要）

- **角色档案和角色记忆模板** → 在 v0.3.0-role-memory 中
- **基础治理模板（术语表/目录/STATE）** → 在 v0.1.0-foundation 中
- **Dashboard 源码** → 在 hermes-dashboard 仓库中

## 使用顺序

1. 先用 v0.1.0-foundation 把目录和规范建好
2. 再用本包搭总控骨架（team-boss + team-registry + 注入脚本）
3. 需要角色系统时，继续用 v0.3.0-role-memory
