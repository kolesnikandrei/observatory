import time
from task import Task, Sleep
from typing import Iterable, List, Any, Set
from random import randint


def wait(ts: Iterable[Task]) -> List[Any]:
    orig: List[Task] = list(ts)
    pending: Set[Task] = set(orig)
    before = time.time()

    while pending:
        for task in list(pending):
            task.run()
            if task.ready:
                pending.remove(task)
    print(f'duration = {time.time() - before:.3}')
    return [task.result for task in orig]


tasks = [Sleep(randint(1, 3)) for _ in range(1000)]
wait(tasks)
