# Hermes Genesis Codebook

> **一个教育从业者的 AI 实战记录。不写教程，只分享真实折腾经历。**

Hermes Genesis Season 1 的配套模板仓库。

这里放的不是 Hermes 内部源码，而是从连载里整理出来的**可公开模板和结构示意**。

---

## 📖 连载文章索引

Season 1 共 17 篇，包含 12 集故事主线 + 3 次 Code Drop 源码放送 + 官宣 + 季终回顾。

完整索引见 [docs/article-map.md](docs/article-map.md)

### 发布版本

| 版本 | 说明 |
|------|------|
| [v0.1.0-foundation](https://github.com/liuxiaoqianglongxia/hermes-genesis-codebook/releases/tag/v0.1.0-foundation) | Code Drop 01：基础工具包（术语表 + 目录规范 + STATE.md 模板） |
| [v0.2.0-workbench](https://github.com/liuxiaoqianglongxia/hermes-genesis-codebook/releases/tag/v0.2.0-workbench) | Code Drop 02：单实例工作台骨架 |
| [v0.3.0-role-memory](https://github.com/liuxiaoqianglongxia/hermes-genesis-codebook/releases/tag/v0.3.0-role-memory) | Code Drop 03：角色档案和记忆桶设计 |
| [v1.0.0-season1-bundle](https://github.com/liuxiaoqianglongxia/hermes-genesis-codebook/releases/tag/v1.0.0-season1-bundle) | Final Bundle：第一季完整交付 |

---

## 📂 目录结构

```
.
├── README.md
├── LICENSE
├── docs/
│   ├── article-map.md     # 全季文章索引
│   ├── censorship-log.md  # 审查记录
│   └── release-map.md     # Release 映射
└── releases/
    ├── v0.1.0-foundation/    # Code Drop 01 模板包
    │   ├── standards/        # 术语表 + 结构规范
    │   ├── templates/        # STATE.md / progress / registry 模板
    │   └── guides/           # 从翻车到模板的说明
    ├── v0.2.0-workbench/     # Code Drop 02 模板包
    │   ├── templates/        # 上下文注入 / team-boss 模板
    │   ├── examples/         # 多Bot对比 / 任务路由流程
    │   └── guides/           # 为什么走向单实例
    ├── v0.3.0-role-memory/   # Code Drop 03 模板包
    │   ├── templates/        # 角色档案 / 记忆桶模板
    │   ├── examples/         # 角色切换流程 / 注入脚本
    │   └── guides/           # 海马体设计说明
    └── v1.0.0-season1-bundle/  # Final Bundle
        ├── articles/         # 全季文章索引
        └── roadmap/          # 第二季预告
```

## 仓库内容

- ✅ 最小模板（术语表 / 目录规范 / 项目身份证）
- ✅ 结构示意（单实例工作台 / 角色档案 / 记忆桶）
- ✅ 可公开的流程骨架
- ❌ 不含真实密钥、群 ID、内部角色原文

## 🎯 适合谁

- 想让 AI 长期参与项目管理，但不知道从哪开始的
- 被"多 Bot 群聊"坑过，想找更稳的架构的
- 想给自己的 AI 系统建立规范，但不想从零摸索的
- 直接拿去二次改造，改完就是你的

## 🔗 更多

- 📺 微信公众号：**麦尖AI** — 一个教育从业者的 AI 实战记录
- 📝 连载全文：搜索"麦尖AI"公众号查看 Hermes Genesis 第一季系列
- 💬 交流反馈：公众号后台留言

---

*如果你觉得这个仓库有用，欢迎 Star 或转发。你的关注，是我继续折腾的最大动力。*
