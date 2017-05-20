import asyncio
import time

# Forks off tasks until hitting a base case. Interesting to note that yield from explicity waits for the results
#   to become available meaning that the original task does not return (or even enter its own yield-sleep) until the last
#   task in the chain has returned

@asyncio.coroutine
def my_coroutine(task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))

    if task_name != "task1111":
        yield from my_coroutine(task_name+"1", 1)

    yield from asyncio.sleep(seconds_to_sleep)

    print('{0} is finished'.format(task_name))

 
loop = asyncio.get_event_loop()

tasks = [
    my_coroutine('task', 1)]
 
 
loop.run_until_complete(asyncio.wait(tasks)) 
loop.close()