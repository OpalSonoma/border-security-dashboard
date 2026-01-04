#!/usr/bin/env python3
"""
Fairness Metrics Library for AI-Driven Border Security Platform

Provides real-time fairness auditing capabilities for threat detection decisions.
Implements demographic parity, equalized odds, and custom fairness indices.
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class IncidentDecision:
    """Represents a single incident decision for fairness audit."""
    incident_id: str
    zone: str
    model_confidence: float
    decision: str  # 'escalated', 'reviewed', 'closed'
    operator: str
    timestamp: str
    outcome: str = None  # 'true_positive', 'false_positive', etc.

class FairnessMetricsCalculator:
    """Calculates fairness metrics across incident decisions."""
    
    def __init__(self, decisions: List[IncidentDecision] = None):
        self.decisions = decisions or []
        
    def add_decision(self, decision: IncidentDecision) -> None:
        """Add a decision to the audit trail."""
        self.decisions.append(decision)
    
    def demographic_parity(self, zones: List[str] = None) -> Dict[str, float]:
        """
        Calculate demographic parity across zones.
        DP = |P(Escalated | Zone A) - P(Escalated | Zone B)|
        Target: < 5% difference
        """
        if not self.decisions:
            return {}
        
        zones = zones or self._get_zones()
        parity_scores = {}
        
        for zone in zones:
            zone_decisions = [d for d in self.decisions if d.zone == zone]
            if not zone_decisions:
                parity_scores[zone] = 0.0
                continue
            
            escalated_count = sum(
                1 for d in zone_decisions if d.decision == 'escalated'
            )
            escalation_rate = escalated_count / len(zone_decisions)
            parity_scores[zone] = escalation_rate
        
        return parity_scores
    
    def equalized_odds(self, zones: List[str] = None) -> Dict[str, float]:
        """
        Calculate equalized odds (False Negative Rate parity).
        EOdds = |FNR_A - FNR_B| where FNR = FN / (FN + TP)
        Target: < 10% difference
        """
        if not self.decisions:
            return {}
        
        zones = zones or self._get_zones()
        odds_scores = {}
        
        for zone in zones:
            zone_decisions = [d for d in self.decisions 
                             if d.zone == zone and d.outcome is not None]
            
            if not zone_decisions:
                odds_scores[zone] = 0.0
                continue
            
            false_negatives = sum(
                1 for d in zone_decisions if d.outcome == 'false_negative'
            )
            true_positives = sum(
                1 for d in zone_decisions if d.outcome == 'true_positive'
            )
            
            fnr = false_negatives / (false_negatives + true_positives) \
                if (false_negatives + true_positives) > 0 else 0.0
            odds_scores[zone] = fnr
        
        return odds_scores
    
    def fairness_index(self) -> float:
        """
        Composite fairness index combining multiple metrics.
        Weighted average: 0.5 * (1 - demographic_parity) + 0.5 * (1 - equalized_odds)
        """
        if not self.decisions:
            return 0.0
        
        zones = self._get_zones()
        
        # Get parity scores
        parity_scores = self.demographic_parity(zones)
        parity_diff = max(parity_scores.values()) - min(parity_scores.values()) \
            if parity_scores else 0.0
        
        # Get odds scores
        odds_scores = self.equalized_odds(zones)
        odds_diff = max(odds_scores.values()) - min(odds_scores.values()) \
            if odds_scores else 0.0
        
        # Composite index: higher is fairer
        # Penalize large differences
        fairness = (1 - parity_diff) * 0.5 + (1 - odds_diff) * 0.5
        return max(0.0, fairness) * 100  # Return as percentage
    
    def audit_trail(self) -> List[Dict]:
        """Generate structured audit trail for compliance."""
        return [
            {
                'timestamp': d.timestamp,
                'incident_id': d.incident_id,
                'zone': d.zone,
                'model_confidence': d.model_confidence,
                'decision': d.decision,
                'operator_sign_off': d.operator,
                'outcome': d.outcome or 'pending'
            }
            for d in self.decisions
        ]
    
    def _get_zones(self) -> List[str]:
        """Extract unique zones from decisions."""
        return list(set(d.zone for d in self.decisions))
    
    def generate_report(self) -> Dict:
        """Generate comprehensive fairness report."""
        return {
            'timestamp': datetime.now().isoformat(),
            'total_decisions': len(self.decisions),
            'demographic_parity': self.demographic_parity(),
            'equalized_odds': self.equalized_odds(),
            'fairness_index': self.fairness_index(),
            'audit_trail': self.audit_trail()
        }


if __name__ == '__main__':
    # Example usage
    calculator = FairnessMetricsCalculator()
    
    # Mock decisions
    decisions = [
        IncidentDecision('T-2847', 'Bengal', 0.98, 'escalated', 'Officer K. Sharma', '2026-01-04 22:45', 'true_positive'),
        IncidentDecision('T-2843', 'Punjab', 0.87, 'reviewed', 'Officer R. Verma', '2026-01-04 22:30', 'true_positive'),
        IncidentDecision('T-2839', 'Assam', 0.72, 'reviewed', 'Officer A. Patel', '2026-01-04 21:15', 'false_positive'),
    ]
    
    for decision in decisions:
        calculator.add_decision(decision)
    
    # Generate report
    report = calculator.generate_report()
    print(json.dumps(report, indent=2))
