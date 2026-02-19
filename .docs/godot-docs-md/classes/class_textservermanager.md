<span id="class_TextServerManager"></span>

## TextServerManager

**Inherits:** [Object](class_object.md#class_Object)

A singleton for managing [TextServer](class_textserver.md#class_TextServer) implementations.

### Description

**TextServerManager** is the API backend for loading, enumerating, and switching [TextServer](class_textserver.md#class_TextServer) s.

 **Note:** Switching text server at runtime is possible, but will invalidate all fonts and text buffers. Make sure to unload all controls, fonts, and themes before doing so.

### Methods


| void | [add_interface](class_textservermanager.md#class_TextServerManager_method_add_interface) ( interface: [TextServer](class_textserver.md#class_TextServer) ) |
| --- | --- |
| [TextServer](class_textserver.md#class_TextServer) | [find_interface](class_textservermanager.md#class_TextServerManager_method_find_interface) ( name: [String](class_string.md#class_String) ) const |
| [TextServer](class_textserver.md#class_TextServer) | [get_interface](class_textservermanager.md#class_TextServerManager_method_get_interface) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_interface_count](class_textservermanager.md#class_TextServerManager_method_get_interface_count) ( ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_interfaces](class_textservermanager.md#class_TextServerManager_method_get_interfaces) ( ) const |
| [TextServer](class_textserver.md#class_TextServer) | [get_primary_interface](class_textservermanager.md#class_TextServerManager_method_get_primary_interface) ( ) const |
| void | [remove_interface](class_textservermanager.md#class_TextServerManager_method_remove_interface) ( interface: [TextServer](class_textserver.md#class_TextServer) ) |
| void | [set_primary_interface](class_textservermanager.md#class_TextServerManager_method_set_primary_interface) ( index: [TextServer](class_textserver.md#class_TextServer) ) |

---

### Signals

<span id="class_TextServerManager_signal_interface_added"></span>

**interface_added** ( interface_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_textservermanager.md#class_TextServerManager_signal_interface_added)

Emitted when a new interface has been added.

---

<span id="class_TextServerManager_signal_interface_removed"></span>

**interface_removed** ( interface_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_textservermanager.md#class_TextServerManager_signal_interface_removed)

Emitted when an interface is removed.

---

### Method Descriptions

<span id="class_TextServerManager_method_add_interface"></span>

void **add_interface** ( interface: [TextServer](class_textserver.md#class_TextServer) ) [🔗](class_textservermanager.md#class_TextServerManager_method_add_interface)

Registers a [TextServer](class_textserver.md#class_TextServer) interface.

---

<span id="class_TextServerManager_method_find_interface"></span>

[TextServer](class_textserver.md#class_TextServer) **find_interface** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_textservermanager.md#class_TextServerManager_method_find_interface)

Finds an interface by its `name`.

---

<span id="class_TextServerManager_method_get_interface"></span>

[TextServer](class_textserver.md#class_TextServer) **get_interface** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_textservermanager.md#class_TextServerManager_method_get_interface)

Returns the interface registered at a given index.

---

<span id="class_TextServerManager_method_get_interface_count"></span>

[int](class_int.md#class_int) **get_interface_count** ( ) *const* [🔗](class_textservermanager.md#class_TextServerManager_method_get_interface_count)

Returns the number of interfaces currently registered.

---

<span id="class_TextServerManager_method_get_interfaces"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_interfaces** ( ) *const* [🔗](class_textservermanager.md#class_TextServerManager_method_get_interfaces)

Returns a list of available interfaces, with the index and name of each interface.

---

<span id="class_TextServerManager_method_get_primary_interface"></span>

[TextServer](class_textserver.md#class_TextServer) **get_primary_interface** ( ) *const* [🔗](class_textservermanager.md#class_TextServerManager_method_get_primary_interface)

Returns the primary [TextServer](class_textserver.md#class_TextServer) interface currently in use.

---

<span id="class_TextServerManager_method_remove_interface"></span>

void **remove_interface** ( interface: [TextServer](class_textserver.md#class_TextServer) ) [🔗](class_textservermanager.md#class_TextServerManager_method_remove_interface)

Removes an interface. All fonts and shaped text caches should be freed before removing an interface.

---

<span id="class_TextServerManager_method_set_primary_interface"></span>

void **set_primary_interface** ( index: [TextServer](class_textserver.md#class_TextServer) ) [🔗](class_textservermanager.md#class_TextServerManager_method_set_primary_interface)

Sets the primary [TextServer](class_textserver.md#class_TextServer) interface.
