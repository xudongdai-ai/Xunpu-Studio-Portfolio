"""Public interface illustration. Synthetic candidates; no private analysis engine."""
from dataclasses import asdict, dataclass
import json

@dataclass(frozen=True)
class ReviewCandidate:
    module: str
    measure: int
    observation: str
    status: str = "needs_human_review"

    def __post_init__(self):
        if self.module not in {"harmony", "form", "assignment_feedback"}:
            raise ValueError("Unknown review module")
        if type(self.measure) is not int or self.measure < 1:
            raise ValueError("Measure must be a positive integer")

if __name__ == "__main__":
    examples = [
        ReviewCandidate("harmony", 1, "Illustrative candidate chord; verify against the score."),
        ReviewCandidate("form", 5, "Illustrative possible boundary; inspect neighbouring measures."),
        ReviewCandidate("assignment_feedback", 2, "Illustrative voice-leading observation; teacher review required."),
    ]
    print(json.dumps({"synthetic": True, "candidates": [asdict(x) for x in examples]}, indent=2))
