"""Workflow Executor - Execute workflow tasks."""
from typing import Dict, Any, Callable

class WorkflowExecutor:
    def __init__(self):
        self.handlers: Dict[str, Callable] = {}
    
    def register(self, action: str, handler: Callable) -> None:
        self.handlers[action] = handler
    
    def execute(self, action: str, data: dict) -> Any:
        h = self.handlers.get(action)
        return h(data) if h else None

__all__ = ["WorkflowExecutor"]
