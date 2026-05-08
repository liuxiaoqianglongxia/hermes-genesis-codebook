#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import argparse, json, yaml

HOME = Path.home()
REGISTRY = HOME / 'knowledge/teams/team-registry.yaml'
MEMORIES = HOME / '.hermes/memories'

def load_registry():
    return yaml.safe_load(REGISTRY.read_text(encoding='utf-8')) or {}

def resolve_bucket(team_id, role_id):
    registry = load_registry()
    aliases = registry.get('aliases', {}).get('team_ids', {})
    canonical = aliases.get(team_id, team_id)
    for team in registry.get('teams', []):
        if team.get('id') == canonical:
            bucket = (team.get('role_memory_map') or {}).get(role_id, role_id)
            return canonical, bucket
    raise SystemExit(f'unknown team: {team_id}')

def append_log(path, title, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    with path.open('a', encoding='utf-8') as f:
        f.write(f'\n## [{now}] {title}\n\n{content.strip()}\n')

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--team', required=True)
    p.add_argument('--role', required=True)
    p.add_argument('--task', required=True)
    p.add_argument('--summary', required=True)
    p.add_argument('--failure', default='')
    args = p.parse_args()
    team, bucket = resolve_bucket(args.team, args.role)
    memory_dir = MEMORIES / team / bucket
    append_log(memory_dir / 'experience-log.md', args.task, args.summary)
    if args.failure.strip():
        append_log(memory_dir / 'failure-log.md', args.task, args.failure)
    print(json.dumps({'ok': True, 'team': team, 'role': args.role, 'bucket': str(memory_dir)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
