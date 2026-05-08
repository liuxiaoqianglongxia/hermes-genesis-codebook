#!/usr/bin/env python3
"""Minimal conservative exporter: Holographic facts -> role holographic-digest.md."""
from pathlib import Path
from datetime import datetime
import argparse, sqlite3, yaml

HOME = Path.home()
REGISTRY = HOME / 'knowledge/teams/team-registry.yaml'
DB = HOME / '.hermes/memory_store.db'
MEMORIES = HOME / '.hermes/memories'

def entries():
    reg = yaml.safe_load(REGISTRY.read_text(encoding='utf-8')) or {}
    for team in reg.get('teams', []):
        if team.get('status') != 'active':
            continue
        for role, bucket in (team.get('role_memory_map') or {}).items():
            yield team['id'], role, bucket

def facts():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn.execute('select fact_id, content, tags from facts order by fact_id desc limit 1000').fetchall()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    rows = facts()
    total = 0
    for team, role, bucket in entries():
        hints = [team, role, bucket]
        picked = [r for r in rows if any(h.lower() in (r['content'] or '').lower() for h in hints)][:20]
        total += len(picked)
        if args.apply and picked:
            out = MEMORIES / team / bucket / 'holographic-digest.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open('a', encoding='utf-8') as f:
                f.write(f'\n## {datetime.now().date()} Holographic digest\n')
                for r in picked:
                    f.write(f"- fact_id={r['fact_id']} {r['content'][:240]}\n")
    print({'ok': True, 'apply': args.apply, 'matched': total})

if __name__ == '__main__':
    main()
