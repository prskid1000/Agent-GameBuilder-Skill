<span id="class_Semaphore"></span>

## Semaphore

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A synchronization mechanism used to control access to a shared resource by [Thread](class_thread.md#class_Thread) s.

### Description

A synchronization semaphore that can be used to synchronize multiple [Thread](class_thread.md#class_Thread) s. Initialized to zero on creation. For a binary version, see [Mutex](class_mutex.md#class_Mutex).

 **Warning:** Semaphores must be used carefully to avoid deadlocks.

 **Warning:** To guarantee that the operating system is able to perform proper cleanup (no crashes, no deadlocks), these conditions must be met:

- When a **Semaphore**'s reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.

- When a [Thread](class_thread.md#class_Thread)'s reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.

### Tutorials

- [Using multiple threads](../tutorials/performance/using_multiple_threads.md)

- [Thread-safe APIs](../tutorials/performance/thread_safe_apis.md)

### Methods


| void | [post](class_semaphore.md#class_Semaphore_method_post) ( count: [int](class_int.md#class_int) = 1 ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [try_wait](class_semaphore.md#class_Semaphore_method_try_wait) ( ) |
| void | [wait](class_semaphore.md#class_Semaphore_method_wait) ( ) |

---

### Method Descriptions

<span id="class_Semaphore_method_post"></span>

void **post** ( count: [int](class_int.md#class_int) = 1 ) [🔗](class_semaphore.md#class_Semaphore_method_post)

Lowers the **Semaphore**, allowing one thread in, or more if `count` is specified.

---

<span id="class_Semaphore_method_try_wait"></span>

[bool](class_bool.md#class_bool) **try_wait** ( ) [🔗](class_semaphore.md#class_Semaphore_method_try_wait)

Like [wait()](class_semaphore.md#class_Semaphore_method_wait), but won't block, so if the value is zero, fails immediately and returns `false`. If non-zero, it returns `true` to report success.

---

<span id="class_Semaphore_method_wait"></span>

void **wait** ( ) [🔗](class_semaphore.md#class_Semaphore_method_wait)

Waits for the **Semaphore**, if its value is zero, blocks until non-zero.
