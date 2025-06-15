import yaml

def load_rules(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def check_compliance(text, rules):
    for rule in rules:
        print(f"\nChecking Rule: {rule['rule_id']} - {rule['title']}")
        missing = [phrase for phrase in rule['match_criteria']['must_include'] if phrase not in text]
        if missing:
            print(f"❌ Not Compliant: Missing {missing}")
            print(rule['consequence']['if_missing'])
        else:
            print("✅ Compliant")

if __name__ == "__main__":
    sample_text = open("examples/demo_input_policy.txt").read()
    rules = load_rules("rules/issb/climate.yaml")
    check_compliance(sample_text, rules)
