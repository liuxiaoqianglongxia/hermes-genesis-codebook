#!/usr/bin/env python3
from pathlib import Path
import argparse, re, yaml

HOME = Path.home()
REGISTRY = HOME / 'knowledge/teams/team-registry.yaml'
ROLES = HOME / '.hermes/roles'
MEMORIES = HOME / '.hermes/memories'
START = '<!-- ROLE_PROFILE_EVOLVE_START -->'
END = '<!-- ROLE_PROFILE_EVOLVE_END -->'

def entries():
    reg = yaml.safe_load(REGISTRY.read_text(encoding='utf-8')) or {}
    for team in reg.get('teams', []):
        if team.get('status') != 'active':
            continue
        for role, bucket in (team.get('role_memory_map') or {}).items():
            yield team['id'], role, bucket

def read(p):
    return p.read_text(encoding='utf-8') if p.exists() else ''

def extract(memdir):
    raw = '\n'.join(read(memdir / n) for n in ['experience-log.md', 'failure-log.md', 'holographic-digest.md'])
    lines = []
    for line in raw.splitlines():
        s = line.strip('- 0123456789.、')
        if 12 <= len(s) <= 160 and any(k in s for k in ['必须', '禁止', '验证', '失败', '正确', '优先']):
            if s not in lines:
                lines.append(s)
    return lines[:12]

def block(lines):
    body = '\n'.join(f'- {x}' for x in lines) or '- 暂无足够实战经验。'
    return f'{START}\n## 🔁 已验证经验演化区（自动维护）\n\n{body}\n{END}'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    changed = 0
    for team, role, bucket in entries():
        profile = ROLES / team / f'{role}.md'
        mem = MEMORIES / team / bucket
        if not profile.exists():
            continue
        text = read(profile)
        b = block(extract(mem))
        if START in text:
            new = re.sub(f'{re.escape(START)}.*?{re.escape(END)}', b, text, flags=re.S)
        else:
            new = text.rstrip() + '\n\n' + b + '\n'
        if new != text:
            changed += 1
            if args.apply:
                profile.write_text(new, encoding='utf-8')
    print({'ok': True, 'changed': changed, 'apply': args.apply})

if __name__ == '__main__':
    main()
