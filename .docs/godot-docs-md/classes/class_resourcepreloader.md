<span id="class_ResourcePreloader"></span>

## ResourcePreloader

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node used to preload sub-resources inside a scene.

### Description

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

GDScript has a simplified @GDScript.preload() built-in method which can be used in most situations, leaving the use of **ResourcePreloader** for more advanced scenarios.

### Methods


| void | [add_resource](class_resourcepreloader.md#class_ResourcePreloader_method_add_resource) ( name: [StringName](class_stringname.md#class_StringName), resource: [Resource](class_resource.md#class_Resource) ) |
| --- | --- |
| [Resource](class_resource.md#class_Resource) | [get_resource](class_resourcepreloader.md#class_ResourcePreloader_method_get_resource) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_resource_list](class_resourcepreloader.md#class_ResourcePreloader_method_get_resource_list) ( ) const |
| [bool](class_bool.md#class_bool) | [has_resource](class_resourcepreloader.md#class_ResourcePreloader_method_has_resource) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_resource](class_resourcepreloader.md#class_ResourcePreloader_method_remove_resource) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_resource](class_resourcepreloader.md#class_ResourcePreloader_method_rename_resource) ( name: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) |

---

### Method Descriptions

<span id="class_ResourcePreloader_method_add_resource"></span>

void **add_resource** ( name: [StringName](class_stringname.md#class_StringName), resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_add_resource)

Adds a resource to the preloader with the given `name`. If a resource with the given `name` already exists, the new resource will be renamed to "`name` N" where N is an incrementing number starting from 2.

---

<span id="class_ResourcePreloader_method_get_resource"></span>

[Resource](class_resource.md#class_Resource) **get_resource** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_get_resource)

Returns the resource associated to `name`.

---

<span id="class_ResourcePreloader_method_get_resource_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_resource_list** ( ) *const* [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_get_resource_list)

Returns the list of resources inside the preloader.

---

<span id="class_ResourcePreloader_method_has_resource"></span>

[bool](class_bool.md#class_bool) **has_resource** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_has_resource)

Returns `true` if the preloader contains a resource associated to `name`.

---

<span id="class_ResourcePreloader_method_remove_resource"></span>

void **remove_resource** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_remove_resource)

Removes the resource associated to `name` from the preloader.

---

<span id="class_ResourcePreloader_method_rename_resource"></span>

void **rename_resource** ( name: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) [🔗](class_resourcepreloader.md#class_ResourcePreloader_method_rename_resource)

Renames a resource inside the preloader from `name` to `newname`.
