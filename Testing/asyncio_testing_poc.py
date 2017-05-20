import asyncio
import time
 
@asyncio.coroutine
def my_coroutine(future, task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))

    # Yield from is used specifically in the framework in order to specify that we want to "asynchronously" use
    #   the result of this co-routine, (IE call it). 
    # If you weren't to use yield from (and say use just sleep instead) that python will stay in your co-routine
    #   due to the fact that the event loop is only actually running a single co-routine at a given time. However because we
    #   use the asyncio.sleep co-routine, it frees the event loop up to run other events in the mean time

    # task1 is going to synchronously block the entire event loop for 10 seconds, meaning that task2 won't be executed
    #   (either initially, or at least executed again) until task1 is done.
    # This effect can be seen if you change the if statement to not match task1.
    #   Will see task 2 finish in 1 second because task1 is sleeping asynchronously
    if task_name == "task1":
        time.sleep(10)
    else:
        yield from asyncio.sleep(seconds_to_sleep)

    future.set_result('{0} is finished'.format(task_name))
 
 
def got_result(future):
    print(future.result())
 
loop = asyncio.get_event_loop()
future1 = asyncio.Future()
future2 = asyncio.Future()
 
tasks = [
    my_coroutine(future1, 'task1', 10),
    my_coroutine(future2, 'task2', 1)]
 
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)
 
loop.run_until_complete(asyncio.wait(tasks)) 
loop.close()