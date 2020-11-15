import time
import logging
from typing import Iterable, List, Any, Generator


LOG = logging.getLogger('')


def wait(ts: Iterable[Generator]) -> List[Any]:
    pending = list(ts)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                print(f'(iteration in loop) doing SEND for {gen}')
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                print(f'(STOP iteration in loop) doing REMOVE for {gen}')
                tasks[gen] = e.args[0]
                pending.remove(gen)

    print(f'duration = {time.time() - before:.3}')
    return list(tasks.values())
