<span id="class_GDExtensionManager"></span>

## GDExtensionManager

**Inherits:** [Object](class_object.md#class_Object)

Provides access to GDExtension functionality.

### Description

The GDExtensionManager loads, initializes, and keeps track of all available [GDExtension](class_gdextension.md#class_GDExtension) libraries in the project.

 **Note:** Do not worry about GDExtension unless you know what you are doing.

### Tutorials

- [GDExtension overview](../tutorials/scripting/gdextension/what_is_gdextension.md)

- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

### Methods


| [GDExtension](class_gdextension.md#class_GDExtension) | [get_extension](class_gdextensionmanager.md#class_GDExtensionManager_method_get_extension) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_loaded_extensions](class_gdextensionmanager.md#class_GDExtensionManager_method_get_loaded_extensions) ( ) const |
| [bool](class_bool.md#class_bool) | [is_extension_loaded](class_gdextensionmanager.md#class_GDExtensionManager_method_is_extension_loaded) ( path: [String](class_string.md#class_String) ) const |
| [LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) | [load_extension](class_gdextensionmanager.md#class_GDExtensionManager_method_load_extension) ( path: [String](class_string.md#class_String) ) |
| [LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) | [load_extension_from_function](class_gdextensionmanager.md#class_GDExtensionManager_method_load_extension_from_function) ( path: [String](class_string.md#class_String), init_func: `const GDExtensionInitializationFunction*` ) |
| [LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) | [reload_extension](class_gdextensionmanager.md#class_GDExtensionManager_method_reload_extension) ( path: [String](class_string.md#class_String) ) |
| [LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) | [unload_extension](class_gdextensionmanager.md#class_GDExtensionManager_method_unload_extension) ( path: [String](class_string.md#class_String) ) |

---

### Signals

<span id="class_GDExtensionManager_signal_extension_loaded"></span>

**extension_loaded** ( extension: [GDExtension](class_gdextension.md#class_GDExtension) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_signal_extension_loaded)

Emitted after the editor has finished loading a new extension.

 **Note:** This signal is only emitted in editor builds.

---

<span id="class_GDExtensionManager_signal_extension_unloading"></span>

**extension_unloading** ( extension: [GDExtension](class_gdextension.md#class_GDExtension) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_signal_extension_unloading)

Emitted before the editor starts unloading an extension.

 **Note:** This signal is only emitted in editor builds.

---

<span id="class_GDExtensionManager_signal_extensions_reloaded"></span>

**extensions_reloaded** ( ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_signal_extensions_reloaded)

Emitted after the editor has finished reloading one or more extensions.

---

### Enumerations

<span id="enum_GDExtensionManager_LoadStatus"></span>

enum **LoadStatus**: [🔗](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus)

<span id="class_GDExtensionManager_constant_LOAD_STATUS_OK"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.

<span id="class_GDExtensionManager_constant_LOAD_STATUS_FAILED"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or has missing dependencies.

<span id="class_GDExtensionManager_constant_LOAD_STATUS_ALREADY_LOADED"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.

<span id="class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.

<span id="class_GDExtensionManager_constant_LOAD_STATUS_NEEDS_RESTART"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.

---

### Method Descriptions

<span id="class_GDExtensionManager_method_get_extension"></span>

[GDExtension](class_gdextension.md#class_GDExtension) **get_extension** ( path: [String](class_string.md#class_String) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_get_extension)

Returns the [GDExtension](class_gdextension.md#class_GDExtension) at the given file `path`, or `null` if it has not been loaded or does not exist.

---

<span id="class_GDExtensionManager_method_get_loaded_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_loaded_extensions** ( ) *const* [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_get_loaded_extensions)

Returns the file paths of all currently loaded extensions.

---

<span id="class_GDExtensionManager_method_is_extension_loaded"></span>

[bool](class_bool.md#class_bool) **is_extension_loaded** ( path: [String](class_string.md#class_String) ) *const* [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_is_extension_loaded)

Returns `true` if the extension at the given file `path` has already been loaded successfully. See also [get_loaded_extensions()](class_gdextensionmanager.md#class_GDExtensionManager_method_get_loaded_extensions).

---

<span id="class_GDExtensionManager_method_load_extension"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **load_extension** ( path: [String](class_string.md#class_String) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_load_extension)

Loads an extension by absolute file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class_GDExtension). Returns [LOAD_STATUS_OK](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_OK) if successful.

---

<span id="class_GDExtensionManager_method_load_extension_from_function"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **load_extension_from_function** ( path: [String](class_string.md#class_String), init_func: `const GDExtensionInitializationFunction*` ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_load_extension_from_function)

Loads the extension already in address space via the given path and initialization function. The `path` needs to be unique and start with `"libgodot://"`. Returns [LOAD_STATUS_OK](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_OK) if successful.

---

<span id="class_GDExtensionManager_method_reload_extension"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **reload_extension** ( path: [String](class_string.md#class_String) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_reload_extension)

Reloads the extension at the given file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class_GDExtension), otherwise this method may return either [LOAD_STATUS_NOT_LOADED](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED) or [LOAD_STATUS_FAILED](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_FAILED).

 **Note:** You can only reload extensions in the editor. In release builds, this method always fails and returns [LOAD_STATUS_FAILED](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_FAILED).

---

<span id="class_GDExtensionManager_method_unload_extension"></span>

[LoadStatus](class_gdextensionmanager.md#enum_GDExtensionManager_LoadStatus) **unload_extension** ( path: [String](class_string.md#class_String) ) [🔗](class_gdextensionmanager.md#class_GDExtensionManager_method_unload_extension)

Unloads an extension by file path. The `path` needs to point to an already loaded [GDExtension](class_gdextension.md#class_GDExtension), otherwise this method returns [LOAD_STATUS_NOT_LOADED](class_gdextensionmanager.md#class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED).
