import time
from typing import Iterable, List, Any, Generator



def wait(tasks: Iterable[Generator]) -> List[Any]:
    pending = list(tasks)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                tasks[gen] = e.args[0]
                pending.remove(gen)

    print(f'duration = {time.time() - before:.3}')
    return list(tasks.values())


