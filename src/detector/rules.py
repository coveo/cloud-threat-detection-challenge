from typing import Dict, Iterable

SENSITIVE_BUCKETS = {'coveo-secrets', 'prod-secrets', 'backups'}
UNUSUAL_IPS = {'95.142.122.10','178.62.100.33','101.99.12.4'}

SEVERITY_MAP = {
    'low':'low','medium':'medium','high':'high','critical':'critical'
}

class RuleEngine:
    # CloudTrail detections
    def apply_cloudtrail(self, event: Dict) -> Iterable[Dict]:
        source = event.get('eventSource')
        name = event.get('eventName')
        if source == 'iam.amazonaws.com' and name == 'DeleteUser':
            if event.get('sourceIPAddress') in UNUSUAL_IPS:
                yield {
                    'event_id': event.get('event_id'),
                    'threat_type': 'IAMPrivilegeTampering',
                    'severity': 'high',
                    'reason': 'DeleteUser from unusual IP'
                }
        if source == 's3.amazonaws.com' and name == 'GetObject':
            bucket = (event.get('requestParameters') or {}).get('bucketName')
            bytes_out = (event.get('additionalEventData') or {}).get('bytesTransferredOut', 0)
            if bucket in SENSITIVE_BUCKETS and bytes_out and bytes_out > 1_000_000_000:
                yield {
                    'event_id': event.get('event_id'),
                    'threat_type': 'S3DataExfiltration',
                    'severity': 'critical',
                    'reason': f'Large exfiltration from sensitive bucket {bucket}'
                }
        if source == 'signin.amazonaws.com' and name == 'ConsoleLogin':
            if (event.get('additionalEventData') or {}).get('MFAUsed') == 'No' and event.get('sourceIPAddress') in UNUSUAL_IPS:
                yield {
                    'event_id': event.get('event_id'),
                    'threat_type': 'ConsoleLoginNoMFAAnomalousIP',
                    'severity': 'medium',
                    'reason': 'ConsoleLogin without MFA from unusual IP'
                }

    # GuardDuty finding mapping
    def apply_guardduty(self, finding: Dict) -> Iterable[Dict]:
        ftype = finding.get('type','')
        sev = finding.get('severity', 0.0)  # 0..8
        # Map some canonical types
        if 'UnauthorizedAccess:AnonymousIPCaller' in ftype:
            yield {
                'finding_id': finding.get('id'),
                'threat_type': 'GD_UnauthorizedAccess_AnonymousIP',
                'severity': 'high',
                'reason': 'Anonymous IP invoked sensitive API'
            }
        elif 'CryptoCurrency:EC2/BitcoinTool' in ftype:
            yield {
                'finding_id': finding.get('id'),
                'threat_type': 'GD_CryptoCurrency_SuspectedMining',
                'severity': 'medium',
                'reason': 'EC2 making mining pool DNS queries'
            }
        elif 'DefenseEvasion:IAMUser/PasswordPolicyChange' in ftype:
            yield {
                'finding_id': finding.get('id'),
                'threat_type': 'GD_DefenseEvasion_PasswordPolicyChange',
                'severity': 'medium',
                'reason': 'Password policy weakened'
            }
        elif 'Persistence:IAMUser/AccessKeyCreated' in ftype:
            yield {
                'finding_id': finding.get('id'),
                'threat_type': 'GD_Persistence_AccessKeyForDormantUser',
                'severity': 'high',
                'reason': 'Access key created for dormant user'
            }
        else:
            return []

    # Bonus: VPC scanning placeholder (left for candidates)
    def apply_vpc_flow(self, rec: Dict) -> Iterable[Dict]:
        return []
