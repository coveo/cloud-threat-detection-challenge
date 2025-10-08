from .sources import load_cloudtrail, load_vpc_flows, load_guardduty_findings
from .rules import RuleEngine
from datetime import datetime

class DetectionPipeline:
    def __init__(self, in_dir: str):
        self.in_dir = in_dir
        self.rules = RuleEngine()

    def run(self):
        alerts = []
        ct_events = load_cloudtrail(self.in_dir)
        vpc_flows = load_vpc_flows(self.in_dir)
        gd_findings = load_guardduty_findings(self.in_dir)

        for ev in ct_events:
            for alert in self.rules.apply_cloudtrail(ev):
                alert['ts'] = ev.get('eventTime') or datetime.utcnow().isoformat() + 'Z'
                alerts.append(alert)

        for fin in gd_findings:
            for alert in self.rules.apply_guardduty(fin):
                alert['ts'] = fin.get('service',{}).get('eventLastSeen') or datetime.utcnow().isoformat() + 'Z'
                alerts.append(alert)

        for rec in vpc_flows:
            for alert in self.rules.apply_vpc_flow(rec):
                alert['ts'] = datetime.utcnow().isoformat() + 'Z'
                alerts.append(alert)

        return alerts
