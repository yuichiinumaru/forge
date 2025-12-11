from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Dict, Optional, Any
from datetime import datetime

class Phase(str, Enum):
    INIT = "init"
    SPEC = "spec"
    PLAN = "plan"
    TASKS = "tasks"
    IMPLEMENT = "implement"
    OPTIMIZE = "optimize"
    SHIP = "ship"
    COMPLETE = "complete"

class Status(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    id: str
    description: str
    status: Status = Status.PENDING
    file_path: Optional[str] = None
    test_file: Optional[str] = None

@dataclass
class QualityGate:
    name: str
    passed: bool
    timestamp: str
    details: Optional[str] = None

@dataclass
class FeatureState:
    name: str
    phase: Phase = Phase.INIT
    status: Status = Status.PENDING
    tasks: List[Task] = field(default_factory=list)
    artifacts: Dict[str, str] = field(default_factory=dict)
    quality_gates: List[QualityGate] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FeatureState':
        # Handle nested objects
        tasks = [Task(**t) for t in data.get("tasks", [])]
        quality_gates = [QualityGate(**q) for q in data.get("quality_gates", [])]

        # Convert string enums back to Enum objects
        phase = Phase(data.get("phase", Phase.INIT))
        status = Status(data.get("status", Status.PENDING))

        return cls(
            name=data["name"],
            phase=phase,
            status=status,
            tasks=tasks,
            artifacts=data.get("artifacts", {}),
            quality_gates=quality_gates,
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", "")
        )
