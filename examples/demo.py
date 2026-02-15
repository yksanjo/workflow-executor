#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import WorkflowExecutor
def main():
    print("Workflow Executor Demo")
    e = WorkflowExecutor()
    e.register("test", lambda d: d["x"] * 2)
    r = e.execute("test", {"x": 5})
    print(f"Result: {r}")
    print("Done!")
if __name__ == "__main__": main()
