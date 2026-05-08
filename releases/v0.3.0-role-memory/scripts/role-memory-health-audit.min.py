#!/usr/bin/env python3
from pathlib import Path
import json, yaml

HOME = Path.home()
REGISTRY = HOME / 'knowledge/teams/team-registry.yaml'
ROLES = HOME / '.hermes/roles'
MEMORIES = HOME / '.hermes/memories'

def main():
    reg=yaml.safe_load(REGISTRY.read_text(encoding='utf-8')) or {}
    rows=[]
    for team in reg.get('teams', []):
        if team.get('status')!='active': continue
        tid=team['id']
        for role,bucket in (team.get('role_memory_map') or {}).items():
            p=ROLES/tid/f'{role}.md'; m=MEMORIES/tid/bucket
            rows.append({
                'team':tid,'role':role,
                'profile':p.exists(),
                'experience':(m/'experience-log.md').exists(),
                'holographic_digest':(m/'holographic-digest.md').exists(),
                'evolved_profile': p.exists() and 'ROLE_PROFILE_EVOLVE_START' in p.read_text(encoding='utf-8', errors='ignore'),
            })
    total=len(rows)
    out={
        'active_roles': total,
        'experience_coverage': f"{sum(x['experience'] for x in rows)}/{total}",
        'holographic_digest_coverage': f"{sum(x['holographic_digest'] for x in rows)}/{total}",
        'evolved_profile_coverage': f"{sum(x['evolved_profile'] for x in rows)}/{total}",
        'issues': [x for x in rows if not (x['profile'] and x['experience'])]
    }
    out['status']='ok' if not out['issues'] else 'warning'
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
