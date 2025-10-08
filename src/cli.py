import argparse
from detector.pipeline import DetectionPipeline

def main():
    parser = argparse.ArgumentParser(description="Cloud Threat Detection Challenge CLI (AWS)")
    parser.add_argument('--in', dest='in_dir', required=True, help='Input directory containing logs')
    parser.add_argument('--out', dest='out_file', default='alerts.json', help='Output alerts JSON path')
    args = parser.parse_args()

    pipe = DetectionPipeline(in_dir=args.in_dir)
    alerts = pipe.run()
    print(f"Generated {len(alerts)} alerts")

    import json
    with open(args.out_file, 'w') as f:
        json.dump(alerts, f, indent=2)
    print(f"Wrote alerts to {args.out_file}")

if __name__ == '__main__':
    main()
