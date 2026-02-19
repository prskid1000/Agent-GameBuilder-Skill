<span id="doc_performance"></span>

## Performance

### Introduction

Godot follows a balanced performance philosophy. In the performance world,
there are always tradeoffs, which consist of trading speed for usability
and flexibility. Some practical examples of this are:

-  Rendering large amounts of objects efficiently is easy, but when a
   large scene must be rendered, it can become inefficient. To solve this,
   visibility computation must be added to the rendering. This makes rendering
   less efficient, but at the same time, fewer objects are rendered. Therefore,
   the overall rendering efficiency is improved.

-  Configuring the properties of every material for every object that
   needs to be rendered is also slow. To solve this, objects are sorted by
   material to reduce the costs. At the same time, sorting has a cost.

-  In 3D physics, a similar situation happens. The best algorithms to
   handle large amounts of physics objects (such as SAP) are slow at
   insertion/removal of objects and raycasting. Algorithms that allow faster
   insertion and removal, as well as raycasting, will not be able to handle as
   many active objects.

And there are many more examples of this! Game engines strive to be
general-purpose in nature. Balanced algorithms are always favored over
algorithms that might be fast in some situations and slow in others, or
algorithms that are fast but are more difficult to use.

Godot is not an exception to this. While it is designed to have backends
swappable for different algorithms, the default backends prioritize balance and
flexibility over performance.

With this clear, the aim of this tutorial section is to explain how to get the
maximum performance out of Godot. While the tutorials can be read in any order,
it is a good idea to start from [doc_general_optimization](general_optimization.md#doc_general_optimization).

### Common

- [General Optimization](general_optimization.md)
- [Using Servers](using_servers.md)
- [Cpu](CPU.md)
- [   ](---.md)
- [Cpu Optimization](cpu_optimization.md)
- [Gpu](GPU.md)
- [   ](---.md)
- [Gpu Optimization](gpu_optimization.md)
- [Using Multimesh](using_multimesh.md)
- [Pipeline Compilations](pipeline_compilations.md)
- [3D](3D.md)
- [  ](--.md)
- [Optimizing 3D Performance](optimizing_3d_performance.md)
- [Vertex Animation/Index](vertex_animation/index.md)
- [Threads](Threads.md)
- [       ](-------.md)
- [Using Multiple Threads](using_multiple_threads.md)
- [Thread Safe Apis](thread_safe_apis.md)
