# asyncio-demo

Code samples from EdgeDB `asyncio` [tutorial videos](https://youtu.be/Xbl7XjFYsN4)
by Łukasz Langa.

## TOC

- [x] [The Asyncio Ecosystem](https://youtu.be/Xbl7XjFYsN4)
    - [Threading Problem](src/the_async_ecosystem/threading_problem.py)
- [x] [The Event Loop](https://youtu.be/E7Yn5biBZ58)
    - [Event Loop Example](src/the_event_loop/event_loop_example.py)
    - [Scheduling Prints](src/the_event_loop/schedule_print.py)
    - [Trampoline](src/the_event_loop/trampoline_example.py)
    - [Long Sync Operation](src/the_event_loop/long_sync_operation.py)
    - [`uvloop` Example](src/the_event_loop/uvloop_example.py)
- [ ] [Using Coroutines](https://youtu.be/-CzqsgaXUM8)
    - [Await Instruction](src/using_coroutines/await_instruction.py)
    - [Async Function](src/using_coroutines/async_function.py)
    - [Graceful Exception Handling](src/using_coroutines/graceful_exception_handling.py)
    - [Missing `await`](src/using_coroutines/missing_await.py)
    - [Coroutine Basic](src/using_coroutines/coroutine.py)
    - [Successive Execution](src/using_coroutines/successive_execution.py)
    - [Concurrent Execution](src/using_coroutines/concurrent_execution.py)
    - [Handle Keyboard Interrupt Concurrent](src/using_coroutines/handle_keyboard_interrupt_concurrent.py)
- [ ] Coroutines Under the Hood
- [ ] Batteries Included
- [ ] An Example Web Application
- [ ] Interacting with the Blocking World
- [ ] Error Handling, Testing, Debugging
