<span id="doc_godot_architecture_diagram"></span>

## Godot's architecture overview

The following diagram describes the most important aspects of Godot's architecture.
It's not designed to be exhaustive, with the purpose of just giving a high-level overview of
the main components and their relationships to each other.

.. figure:: img/godot-architecture-diagram.webp
   :alt: Diagram of Godot's Architecture; divided into three layers (from top to bottom: Scene layer, Server layer, and Drivers & Platform interface layer), with Core and Main separated on the right side since they interact with all layers.

   Credit: Hendrik Brucker

Scene Layer
~~~~~~~~~~~

The Scene layer is the highest level of Godot's architecture, providing the scene system, which is the main way to build and structure your applications or games.
See [class_SceneTree](../../classes/class_scenetree.md#class_SceneTree) / [doc_scene_tree](../../tutorials/scripting/scene_tree.md#doc_scene_tree) and [class_Node](../../classes/class_node.md#class_Node) for more information.

Corresponding source code: /scene/*

Server Layer
~~~~~~~~~~~~

Server components implement most of Godot's subsystems (rendering, audio, physics, etc.). They are singleton objects initialized at engine startup.

Why does Godot use servers and RIDs?

Corresponding source code: /servers/*

Drivers / Platform Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This layer abstracts low-level platform-specific details, containing drivers for graphics APIs, audio backends and operating system interfaces
(all platform-specific [class_OS](../../classes/class_os.md#class_OS) and [class_DisplayServer](../../classes/class_displayserver.md#class_DisplayServer) implementations).

Corresponding source code: /drivers/* and /platform/*

Core
~~~~

The Engine's core contains essential functionality and data structures used throughout the engine,
like [class_Object](../../classes/class_object.md#class_Object) and [class_ClassDB](../../classes/class_classdb.md#class_ClassDB), [memory management](core_types.md#doc_core_types), [containers](core_types.md#doc_core_types), file I/O, [Variant](variant_class.md#doc_variant_class), and [other utilities](common_engine_methods_and_macros.md#doc_common_engine_methods_and_macros).

Corresponding source code: /core/*

Main
~~~~

The Main component is responsible for initializing and managing the engine lifecycle, including startup, shutdown, and the main loop. See [class_MainLoop](../../classes/class_mainloop.md#class_MainLoop) for more details.

Corresponding source code: /main/*
