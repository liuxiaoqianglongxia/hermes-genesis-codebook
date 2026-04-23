# Code Drop 02: 单实例工作台骨架 v0.2.0

**对应文章**：源码放送：单实例工作台骨架，直接拿去用

单实例工作台骨架：上下文注入、team-boss 路由、对比说明、任务路由流程。

## 包含内容

| 文件 | 说明 |
|------|------|
| `templates/context-injection/inject.min.py` | 上下文注入示意代码 |
| `templates/context-injection/context-pack.example/` | 项目事实包 + 约束样例 |
| `templates/team-boss/team-boss.thinking.md` | 团队总控思考流程模板 |
| `examples/multi-bot-vs-single-instance.md` | 多 Bot vs 单实例对比表 |
| `examples/task-routing-flow.md` | 任务路由流程图 |
| `guides/why-single-instance.md` | 为什么最终走向单实例 |

## 解决什么问题

Hermes 从"多 Bot 群聊"回归"单实例总控"的架构转变：
- 十几个 Bot 在群里热闹，但信息碎片化严重
- 单实例 + 角色切换，记忆统一、上下文完整
- 工作台是 AI 的执行空间，不是聊天室

## 使用方式

可以直接作为自己项目的起点。角色定义、上下文注入方式都可以根据实际需求调整。
