# Code Drop 03: 角色档案和记忆桶设计 v0.3.0

**对应文章**：Code Drop 03：角色档案和记忆桶是怎么设计的

角色档案模板、记忆桶样例、注入示意和海马体设计说明。

## 包含内容

| 文件 | 说明 |
|------|------|
| `templates/role-profiles/role.md.template` | 角色档案模板（定位/职责/SOP/红线） |
| `templates/memory-buckets/memory.example.md` | 记忆桶样例 |
| `examples/role-switch-flow.md` | 角色切换流程图 |
| `examples/inject-role-context.min.py` | 角色上下文注入示意代码 |
| `examples/dashboard-fields.md` | Dashboard 字段规划样例 |
| `guides/hippocampus-for-ai.md` | 给 AI 装海马体：记忆设计说明 |

## 解决什么问题

Hermes 如何在一个实例里装下 35 个角色：
- 角色不是 Prompt 里的一段话，而是独立的档案文件
- 记忆按角色分流，阿珍的风格偏好不会污染小美的调研记录
- 启动时动态注入，不是硬编码在系统 Prompt 里

## 使用方式

角色档案放在 `~/.hermes/roles/<团队名>/` 目录下。记忆桶按团队/项目隔离。可以直接参考这个结构设计自己的角色系统。
