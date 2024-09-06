from condition import Condition
from bson import ObjectId

class RuleAggregator:
    def __init__(self, category=None, disease_name=None, disease_code=None, rules=None, _id=None):
        self.category = category
        self.disease_name = disease_name
        self.disease_code = disease_code
        self.rules = rules if rules is not None else []
        self._id = _id

    def to_dict(self):
        return {
            'category': self.category,
            'disease_name': self.disease_name,
            'disease_code': self.disease_code,
            'rules': [self._rule_entry_to_dict(rule) for rule in self.rules]
        }

    @staticmethod
    def from_dict(rule_data):
        rules = [RuleAggregator._rule_entry_from_dict(rule_entry) for rule_entry in rule_data.get('rules', [])]
        return RuleAggregator(
            rule_data.get('category'),
            rule_data.get('disease_name'),
            rule_data.get('disease_code'),
            rules
        )

    def _rule_entry_to_dict(self, rule_entry):
        return {
            'rule_id': rule_entry['rule_id'],
            'conditions': [condition.to_dict() for condition in rule_entry['conditions']]
        }

    @staticmethod
    def _rule_entry_from_dict(rule_entry_data):
        conditions = [Condition.from_dict(condition) for condition in rule_entry_data.get('conditions', [])]
        return {
            'rule_id': rule_entry_data.get('rule_id'),
            'conditions': conditions
        }