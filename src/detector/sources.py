import json, os, csv

def load_cloudtrail(in_dir: str):
    path = os.path.join(in_dir, 'cloudtrail.jsonl')
    events = []
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line=line.strip()
                if not line: continue
                try: events.append(json.loads(line))
                except json.JSONDecodeError: pass
    return events

def load_vpc_flows(in_dir: str):
    path = os.path.join(in_dir, 'vpc_flow.csv')
    rows=[]
    if os.path.exists(path):
        with open(path) as f:
            reader = csv.reader(f)
            for r in reader:
                if len(r) < 14: continue
                rows.append({
                    'version': r[0], 'account': r[1], 'eni': r[2],
                    'srcaddr': r[3], 'dstaddr': r[4],
                    'srcport': int(r[5]), 'dstport': int(r[6]),
                    'protocol': int(r[7]), 'packets': int(r[8]), 'bytes': int(r[9]),
                    'start': int(r[10]), 'end': int(r[11]),
                    'action': r[12], 'status': r[13]
                })
    return rows

def load_guardduty_findings(in_dir: str):
    path = os.path.join(in_dir, 'guardduty_findings.jsonl')
    arr=[]
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line=line.strip()
                if not line: continue
                try: arr.append(json.loads(line))
                except json.JSONDecodeError: pass
    return arr
