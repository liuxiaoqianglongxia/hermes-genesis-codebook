# v0.3.0-role-memory：角色档案与角色记忆

对应文章：EP-006 ~ EP-007 延伸、Code Drop 02 补丁

## 这个包解决什么问题

AI Agent 如何拥有"角色"，并且角色的经验能持续沉淀。

## 包含什么

| 文件/目录 | 说明 |
|---|---|
| `templates/role-profiles/role.md.template` | 角色档案模板（定位/职责/SOP/红线） |
| `templates/memory-buckets/memory.example.md` | 记忆桶样例（经验/失败/动态） |
| `templates/role-profile-evolve-block.md` | 档案演化块模板 |
| `examples/role-switch-flow.md` | 角色切换流程图 |
| `examples/inject-role-context.min.py` | 角色上下文注入示意 |
| `examples/dashboard-fields.md` | Dashboard 角色记忆健康度字段样例 |
| `guides/hippocampus-for-ai.md` | 给 AI 装海马体：记忆设计说明 |
| `scripts/` | 角色记忆闭环脚本（capture/export/evolve/audit） |

## 注意

- 本包依赖 v0.2.0-workbench 中的注入骨架。
- scripts/ 中的脚本是示意级，需根据你本地的 Hermes 版本调整路径。
- `__pycache__/` 已从本 release 中移除（.gitignore 已更新）。
