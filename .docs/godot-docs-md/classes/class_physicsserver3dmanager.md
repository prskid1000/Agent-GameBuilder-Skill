<span id="class_PhysicsServer3DManager"></span>

## PhysicsServer3DManager

**Inherits:** [Object](class_object.md#class_Object)

A singleton for managing [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) implementations.

### Description

**PhysicsServer3DManager** is the API for registering [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) implementations and for setting the default implementation.

 **Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

### Methods


| void | [register_server](class_physicsserver3dmanager.md#class_PhysicsServer3DManager_method_register_server) ( name: [String](class_string.md#class_String), create_callback: [Callable](class_callable.md#class_Callable) ) |
| --- | --- |
| void | [set_default_server](class_physicsserver3dmanager.md#class_PhysicsServer3DManager_method_set_default_server) ( name: [String](class_string.md#class_String), priority: [int](class_int.md#class_int) ) |

---

### Method Descriptions

<span id="class_PhysicsServer3DManager_method_register_server"></span>

void **register_server** ( name: [String](class_string.md#class_String), create_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_physicsserver3dmanager.md#class_PhysicsServer3DManager_method_register_server)

Register a [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) implementation by passing a `name` and a [Callable](class_callable.md#class_Callable) that returns a [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) object.

---

<span id="class_PhysicsServer3DManager_method_set_default_server"></span>

void **set_default_server** ( name: [String](class_string.md#class_String), priority: [int](class_int.md#class_int) ) [🔗](class_physicsserver3dmanager.md#class_PhysicsServer3DManager_method_set_default_server)

Set the default [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
