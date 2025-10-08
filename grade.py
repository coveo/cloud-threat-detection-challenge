import argparse, json

def load_truth(path):
    with open(path) as f:
        return json.load(f)

def load_alerts(path):
    with open(path) as f:
        return json.load(f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alerts', required=True)
    ap.add_argument('--truth', required=True)
    args = ap.parse_args()

    truth = load_truth(args.truth)
    alerts = load_alerts(args.alerts)

    # Build truth sets keyed by event_id or finding_id + threat_type
    truth_pairs = set()
    for t in truth:
        if 'event_id' in t:
            truth_pairs.add(('event', t['event_id'], t['threat_type']))
        elif 'finding_id' in t:
            truth_pairs.add(('finding', t['finding_id'], t['threat_type']))

    alert_pairs = set()
    for a in alerts:
        ttype = a.get('threat_type')
        if not ttype: continue
        if a.get('event_id'):
            alert_pairs.add(('event', a['event_id'], ttype))
        if a.get('finding_id'):
            alert_pairs.add(('finding', a['finding_id'], ttype))

    tp = len(alert_pairs & truth_pairs)
    fp = len(alert_pairs - truth_pairs)
    fn = len(truth_pairs - alert_pairs)

    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0

    print('=== Grading Report (AWS Edition) ===')
    print(f'True Positives: {tp}')
    print(f'False Positives: {fp}')
    print(f'False Negatives: {fn}')
    print(f'Precision: {prec:.2f}  Recall: {rec:.2f}')
    if fn:
        print('\nMissed:')
        for k,id_,tt in (truth_pairs - alert_pairs):
            kind = 'CloudTrail' if k=='event' else 'GuardDuty'
            print(f' - {kind} id={id_} threat_type={tt}')

if __name__ == '__main__':
    main()
