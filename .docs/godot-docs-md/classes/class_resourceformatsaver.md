<span id="class_ResourceFormatSaver"></span>

## ResourceFormatSaver

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Saves a specific resource type to a file.

### Description

The engine can save resources when you do it from the editor, or when you use the [ResourceSaver](class_resourcesaver.md#class_ResourceSaver) singleton. This is accomplished thanks to multiple **ResourceFormatSaver** s, each handling its own format and called automatically by the engine.

By default, Godot saves resources as `.tres` (text-based), `.res` (binary) or another built-in format, but you can choose to create your own format by extending this class. Be sure to respect the documented return types and values. You should give it a global class name with `class_name` for it to be registered. Like built-in ResourceFormatSavers, it will be called automatically when saving resources of its recognized type(s). You may also implement a [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader).

### Methods


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_recognized_extensions](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__get_recognized_extensions) ( resource: [Resource](class_resource.md#class_Resource) ) | virtual | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_recognize](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__recognize) ( resource: [Resource](class_resource.md#class_Resource) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_recognize_path](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__recognize_path) ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String) ) | virtual | const |
| Error | [_save](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__save) ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int) ) virtual |
| Error | [_set_uid](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__set_uid) ( path: [String](class_string.md#class_String), uid: [int](class_int.md#class_int) ) virtual |

---

### Method Descriptions

<span id="class_ResourceFormatSaver_private_method__get_recognized_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_recognized_extensions** ( resource: [Resource](class_resource.md#class_Resource) ) *virtual* *const* [🔗](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__get_recognized_extensions)

Returns the list of extensions available for saving the resource object, provided it is recognized (see [_recognize()](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__recognize)).

---

<span id="class_ResourceFormatSaver_private_method__recognize"></span>

[bool](class_bool.md#class_bool) **_recognize** ( resource: [Resource](class_resource.md#class_Resource) ) *virtual* *const* [🔗](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__recognize)

Returns whether the given resource object can be saved by this saver.

---

<span id="class_ResourceFormatSaver_private_method__recognize_path"></span>

[bool](class_bool.md#class_bool) **_recognize_path** ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__recognize_path)

Returns `true` if this saver handles a given save path and `false` otherwise.

If this method is not implemented, the default behavior returns whether the path's extension is within the ones provided by [_get_recognized_extensions()](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__get_recognized_extensions).

---

<span id="class_ResourceFormatSaver_private_method__save"></span>

Error **_save** ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int) ) *virtual* [🔗](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__save)

Saves the given resource object to a file at the target `path`. `flags` is a bitmask composed with [SaverFlags](class_resourcesaver.md#enum_ResourceSaver_SaverFlags) constants.

Returns @GlobalScope.OK on success, or an Error constant in case of failure.

---

<span id="class_ResourceFormatSaver_private_method__set_uid"></span>

Error **_set_uid** ( path: [String](class_string.md#class_String), uid: [int](class_int.md#class_int) ) *virtual* [🔗](class_resourceformatsaver.md#class_ResourceFormatSaver_private_method__set_uid)

Sets a new UID for the resource at the given `path`. Returns @GlobalScope.OK on success, or an Error constant in case of failure.
