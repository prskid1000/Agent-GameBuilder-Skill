<span id="class_GDExtension"></span>

## GDExtension

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A native library for GDExtension.

### Description

The **GDExtension** resource type represents a shared library which can expand the functionality of the engine. The [GDExtensionManager](class_gdextensionmanager.md#class_GDExtensionManager) singleton is responsible for loading, reloading, and unloading **GDExtension** resources.

 **Note:** GDExtension itself is not a scripting language and has no relation to [GDScript](class_gdscript.md#class_GDScript) resources.

### Tutorials

- [GDExtension overview](../tutorials/scripting/gdextension/what_is_gdextension.md)

- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

### Methods


| [InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) | [get_minimum_library_initialization_level](class_gdextension.md#class_GDExtension_method_get_minimum_library_initialization_level) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_library_open](class_gdextension.md#class_GDExtension_method_is_library_open) ( ) const |

---

### Enumerations

<span id="enum_GDExtension_InitializationLevel"></span>

enum **InitializationLevel**: [🔗](class_gdextension.md#enum_GDExtension_InitializationLevel)

<span id="class_GDExtension_constant_INITIALIZATION_LEVEL_CORE"></span>

[InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the engine.

<span id="class_GDExtension_constant_INITIALIZATION_LEVEL_SERVERS"></span>

[InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine's servers (such as [RenderingServer](class_renderingserver.md#class_RenderingServer) or [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D)).

<span id="class_GDExtension_constant_INITIALIZATION_LEVEL_SCENE"></span>

[InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine's scene-related classes.

<span id="class_GDExtension_constant_INITIALIZATION_LEVEL_EDITOR"></span>

[InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine's editor classes. Only happens when loading the GDExtension in the editor.

---

### Method Descriptions

<span id="class_GDExtension_method_get_minimum_library_initialization_level"></span>

[InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) **get_minimum_library_initialization_level** ( ) *const* [🔗](class_gdextension.md#class_GDExtension_method_get_minimum_library_initialization_level)

Returns the lowest level required for this extension to be properly initialized (see the [InitializationLevel](class_gdextension.md#enum_GDExtension_InitializationLevel) enum).

---

<span id="class_GDExtension_method_is_library_open"></span>

[bool](class_bool.md#class_bool) **is_library_open** ( ) *const* [🔗](class_gdextension.md#class_GDExtension_method_is_library_open)

Returns `true` if this extension's library has been opened.
