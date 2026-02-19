<span id="class_NavigationServer2DManager"></span>

## NavigationServer2DManager

**Inherits:** [Object](class_object.md#class_Object)

A singleton for managing [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) implementations.

### Description

**NavigationServer2DManager** is the API for registering [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) implementations and setting the default implementation.

 **Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

### Methods


| void | [register_server](class_navigationserver2dmanager.md#class_NavigationServer2DManager_method_register_server) ( name: [String](class_string.md#class_String), create_callback: [Callable](class_callable.md#class_Callable) ) |
| --- | --- |
| void | [set_default_server](class_navigationserver2dmanager.md#class_NavigationServer2DManager_method_set_default_server) ( name: [String](class_string.md#class_String), priority: [int](class_int.md#class_int) ) |

---

### Method Descriptions

<span id="class_NavigationServer2DManager_method_register_server"></span>

void **register_server** ( name: [String](class_string.md#class_String), create_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_navigationserver2dmanager.md#class_NavigationServer2DManager_method_register_server)

Registers a [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) implementation by passing a `name` and a [Callable](class_callable.md#class_Callable) that returns a [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) object.

---

<span id="class_NavigationServer2DManager_method_set_default_server"></span>

void **set_default_server** ( name: [String](class_string.md#class_String), priority: [int](class_int.md#class_int) ) [🔗](class_navigationserver2dmanager.md#class_NavigationServer2DManager_method_set_default_server)

Sets the default [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
