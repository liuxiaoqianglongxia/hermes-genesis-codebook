# 基础治理包：最小验证步骤

对应文章：EP-001 ~ EP-003、Code Drop 01

## 目标

用最少步骤验证"AI 不再乱找文件"。

## 步骤

### 1. 建目录

在你的 Hermes 实例中创建以下目录结构：

```text
~/.hermes/                    ← Hermes 系统目录
~/knowledge/                  ← 知识库
  standards/                  ← 全局规范
    01-terminology.md         ← 术语表
    02-structure.md           ← 目录结构规范
~/projects/                   ← 项目目录
  <项目名>/
    STATE.md                  ← 项目事实源
    docs/
      progress.md             ← 进度记录
```

### 2. 填内容

把本 release 的 templates/ 和 standards/ 文件复制到对应位置。

### 3. 写导航

在 config.yaml 的 agent.system_prompt 中加入导航层规则。
参考 guides/config-yaml-nav-layer.example.yaml。

### 4. 验证

新开一个会话，问 AI：

> "术语表在哪？"
> "项目清单在哪？"
> "我的规范在哪？"

如果它能准确回答路径（如 ~/knowledge/standards/01-terminology.md），说明导航层生效。

### 5. 常见翻车

- 问它答不出来 → 导航层没写对，检查 config.yaml
- 它答了一个不存在的旧文件 → 有残留文件干扰，清理旧目录
- 它每次回答不一样 → 没有事实源，补上 STATE.md
