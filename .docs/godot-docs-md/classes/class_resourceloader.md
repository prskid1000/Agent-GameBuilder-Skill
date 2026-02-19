<span id="class_ResourceLoader"></span>

## ResourceLoader

**Inherits:** [Object](class_object.md#class_Object)

A singleton for loading resource files.

### Description

A singleton used to load resource files from the filesystem.

It uses the many [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) classes registered in the engine (either built-in or from a plugin) to load files into memory and convert them to a format that can be used by the engine.

 **Note:** You have to import the files into the engine first to load them using [load()](class_resourceloader.md#class_ResourceLoader_method_load). If you want to load [Image](class_image.md#class_Image) s at run-time, you may use [Image.load()](class_image.md#class_Image_method_load). If you want to import audio files, you can use the snippet described in [AudioStreamMP3.data](class_audiostreammp3.md#class_AudioStreamMP3_property_data).

 **Note:** Non-resource files such as plain text files cannot be read using **ResourceLoader**. Use [FileAccess](class_fileaccess.md#class_FileAccess) for those files instead, and be aware that non-resource files are not exported by default (see notes in the [FileAccess](class_fileaccess.md#class_FileAccess) class description for instructions on exporting them).

### Tutorials

- Threaded Loading Demo

- Operating System Testing Demo

### Methods


| void | [add_resource_format_loader](class_resourceloader.md#class_ResourceLoader_method_add_resource_format_loader) ( format_loader: [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader), at_front: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [exists](class_resourceloader.md#class_ResourceLoader_method_exists) ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "" ) |
| [Resource](class_resource.md#class_Resource) | [get_cached_ref](class_resourceloader.md#class_ResourceLoader_method_get_cached_ref) ( path: [String](class_string.md#class_String) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_dependencies](class_resourceloader.md#class_ResourceLoader_method_get_dependencies) ( path: [String](class_string.md#class_String) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_recognized_extensions_for_type](class_resourceloader.md#class_ResourceLoader_method_get_recognized_extensions_for_type) ( type: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [get_resource_uid](class_resourceloader.md#class_ResourceLoader_method_get_resource_uid) ( path: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [has_cached](class_resourceloader.md#class_ResourceLoader_method_has_cached) ( path: [String](class_string.md#class_String) ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [list_directory](class_resourceloader.md#class_ResourceLoader_method_list_directory) ( directory_path: [String](class_string.md#class_String) ) |
| [Resource](class_resource.md#class_Resource) | [load](class_resourceloader.md#class_ResourceLoader_method_load) ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "", cache_mode: [CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) = 1 ) |
| [Resource](class_resource.md#class_Resource) | [load_threaded_get](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get) ( path: [String](class_string.md#class_String) ) |
| [ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) | [load_threaded_get_status](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get_status) ( path: [String](class_string.md#class_String), progress: [Array](class_array.md#class_Array) = [] ) |
| Error | [load_threaded_request](class_resourceloader.md#class_ResourceLoader_method_load_threaded_request) ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "", use_sub_threads: [bool](class_bool.md#class_bool) = false, cache_mode: [CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) = 1 ) |
| void | [remove_resource_format_loader](class_resourceloader.md#class_ResourceLoader_method_remove_resource_format_loader) ( format_loader: [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) ) |
| void | [set_abort_on_missing_resources](class_resourceloader.md#class_ResourceLoader_method_set_abort_on_missing_resources) ( abort: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_ResourceLoader_ThreadLoadStatus"></span>

enum **ThreadLoadStatus**: [🔗](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus)

<span id="class_ResourceLoader_constant_THREAD_LOAD_INVALID_RESOURCE"></span>

[ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) **THREAD_LOAD_INVALID_RESOURCE** = `0`

The resource is invalid, or has not been loaded with [load_threaded_request()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_request).

<span id="class_ResourceLoader_constant_THREAD_LOAD_IN_PROGRESS"></span>

[ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) **THREAD_LOAD_IN_PROGRESS** = `1`

The resource is still being loaded.

<span id="class_ResourceLoader_constant_THREAD_LOAD_FAILED"></span>

[ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) **THREAD_LOAD_FAILED** = `2`

Some error occurred during loading and it failed.

<span id="class_ResourceLoader_constant_THREAD_LOAD_LOADED"></span>

[ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) **THREAD_LOAD_LOADED** = `3`

The resource was loaded successfully and can be accessed via [load_threaded_get()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get).

---

<span id="enum_ResourceLoader_CacheMode"></span>

enum **CacheMode**: [🔗](class_resourceloader.md#enum_ResourceLoader_CacheMode)

<span id="class_ResourceLoader_constant_CACHE_MODE_IGNORE"></span>

[CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) **CACHE_MODE_IGNORE** = `0`

Neither the main resource (the one requested to be loaded) nor any of its subresources are retrieved from cache nor stored into it. Dependencies (external resources) are loaded with [CACHE_MODE_REUSE](class_resourceloader.md#class_ResourceLoader_constant_CACHE_MODE_REUSE).

<span id="class_ResourceLoader_constant_CACHE_MODE_REUSE"></span>

[CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) **CACHE_MODE_REUSE** = `1`

The main resource (the one requested to be loaded), its subresources, and its dependencies (external resources) are retrieved from cache if present, instead of loaded. Those not cached are loaded and then stored into the cache. The same rules are propagated recursively down the tree of dependencies (external resources).

<span id="class_ResourceLoader_constant_CACHE_MODE_REPLACE"></span>

[CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) **CACHE_MODE_REPLACE** = `2`

Like [CACHE_MODE_REUSE](class_resourceloader.md#class_ResourceLoader_constant_CACHE_MODE_REUSE), but the cache is checked for the main resource (the one requested to be loaded) as well as for each of its subresources. Those already in the cache, as long as the loaded and cached types match, have their data refreshed from storage into the already existing instances. Otherwise, they are recreated as completely new objects.

<span id="class_ResourceLoader_constant_CACHE_MODE_IGNORE_DEEP"></span>

[CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) **CACHE_MODE_IGNORE_DEEP** = `3`

Like [CACHE_MODE_IGNORE](class_resourceloader.md#class_ResourceLoader_constant_CACHE_MODE_IGNORE), but propagated recursively down the tree of dependencies (external resources).

<span id="class_ResourceLoader_constant_CACHE_MODE_REPLACE_DEEP"></span>

[CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) **CACHE_MODE_REPLACE_DEEP** = `4`

Like [CACHE_MODE_REPLACE](class_resourceloader.md#class_ResourceLoader_constant_CACHE_MODE_REPLACE), but propagated recursively down the tree of dependencies (external resources).

---

### Method Descriptions

<span id="class_ResourceLoader_method_add_resource_format_loader"></span>

void **add_resource_format_loader** ( format_loader: [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader), at_front: [bool](class_bool.md#class_bool) = false ) [🔗](class_resourceloader.md#class_ResourceLoader_method_add_resource_format_loader)

Registers a new [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader). The ResourceLoader will use the ResourceFormatLoader as described in [load()](class_resourceloader.md#class_ResourceLoader_method_load).

This method is performed implicitly for ResourceFormatLoaders written in GDScript (see [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) for more information).

---

<span id="class_ResourceLoader_method_exists"></span>

[bool](class_bool.md#class_bool) **exists** ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "" ) [🔗](class_resourceloader.md#class_ResourceLoader_method_exists)

Returns whether a recognized resource exists for the given `path`.

An optional `type_hint` can be used to further specify the [Resource](class_resource.md#class_Resource) type that should be handled by the [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader). Anything that inherits from [Resource](class_resource.md#class_Resource) can be used as a type hint, for example [Image](class_image.md#class_Image).

 **Note:** If you use [Resource.take_over_path()](class_resource.md#class_Resource_method_take_over_path), this method will return `true` for the taken path even if the resource wasn't saved (i.e. exists only in resource cache).

---

<span id="class_ResourceLoader_method_get_cached_ref"></span>

[Resource](class_resource.md#class_Resource) **get_cached_ref** ( path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_get_cached_ref)

Returns the cached resource reference for the given `path`.

 **Note:** If the resource is not cached, the returned [Resource](class_resource.md#class_Resource) will be invalid.

---

<span id="class_ResourceLoader_method_get_dependencies"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_dependencies** ( path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_get_dependencies)

Returns the dependencies for the resource at the given `path`.

Each dependency is a string that can be divided into sections by `::`. There can be either one section or three sections, with the second section always being empty. When there is one section, it contains the file path. When there are three sections, the first section contains the UID and the third section contains the fallback path.

::

    for dependency in ResourceLoader.get_dependencies(path):
        if dependency.contains("::"):
            print(dependency.get_slice("::", 0)) # Prints the UID.
            print(dependency.get_slice("::", 2)) # Prints the fallback path.
        else:
            print(dependency) # Prints the path.

---

<span id="class_ResourceLoader_method_get_recognized_extensions_for_type"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_recognized_extensions_for_type** ( type: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_get_recognized_extensions_for_type)

Returns the list of recognized extensions for a resource type.

---

<span id="class_ResourceLoader_method_get_resource_uid"></span>

[int](class_int.md#class_int) **get_resource_uid** ( path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_get_resource_uid)

Returns the ID associated with a given resource path, or `-1` when no such ID exists.

---

<span id="class_ResourceLoader_method_has_cached"></span>

[bool](class_bool.md#class_bool) **has_cached** ( path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_has_cached)

Returns whether a cached resource is available for the given `path`.

Once a resource has been loaded by the engine, it is cached in memory for faster access, and future calls to the [load()](class_resourceloader.md#class_ResourceLoader_method_load) method will use the cached version. The cached resource can be overridden by using [Resource.take_over_path()](class_resource.md#class_Resource_method_take_over_path) on a new resource for that same path.

---

<span id="class_ResourceLoader_method_list_directory"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **list_directory** ( directory_path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_list_directory)

Lists a directory, returning all resources and subdirectories contained within. The resource files have the original file names as visible in the editor before exporting. The directories have `"/"` appended.

::

    # Prints ["extra_data/", "model.gltf", "model.tscn", "model_slime.png"]
    print(ResourceLoader.list_directory("res://assets/enemies/slime"))

 **Note:** The order of files and directories returned by this method is not deterministic, and can vary between operating systems.

 **Note:** To normally traverse the filesystem, see [DirAccess](class_diraccess.md#class_DirAccess).

---

<span id="class_ResourceLoader_method_load"></span>

[Resource](class_resource.md#class_Resource) **load** ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "", cache_mode: [CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) = 1 ) [🔗](class_resourceloader.md#class_ResourceLoader_method_load)

Loads a resource at the given `path`, caching the result for further access.

The registered [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) s are queried sequentially to find the first one which can handle the file's extension, and then attempt loading. If loading fails, the remaining ResourceFormatLoaders are also attempted.

An optional `type_hint` can be used to further specify the [Resource](class_resource.md#class_Resource) type that should be handled by the [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader). Anything that inherits from [Resource](class_resource.md#class_Resource) can be used as a type hint, for example [Image](class_image.md#class_Image).

The `cache_mode` property defines whether and how the cache should be used or updated when loading the resource.

Returns an empty resource if no [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) could handle the file, and prints an error if no file is found at the specified path.

GDScript has a simplified @GDScript.load() built-in method which can be used in most situations, leaving the use of **ResourceLoader** for more advanced scenarios.

 **Note:** If ProjectSettings.editor/export/convert_text_resources_to_binary is `true`, @GDScript.load() will not be able to read converted files in an exported project. If you rely on run-time loading of files present within the PCK, set ProjectSettings.editor/export/convert_text_resources_to_binary to `false`.

 **Note:** Relative paths will be prefixed with `"res://"` before loading, to avoid unexpected results make sure your paths are absolute.

---

<span id="class_ResourceLoader_method_load_threaded_get"></span>

[Resource](class_resource.md#class_Resource) **load_threaded_get** ( path: [String](class_string.md#class_String) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get)

Returns the resource loaded by [load_threaded_request()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_request).

If this is called before the loading thread is done (i.e. [load_threaded_get_status()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get_status) is not [THREAD_LOAD_LOADED](class_resourceloader.md#class_ResourceLoader_constant_THREAD_LOAD_LOADED)), the calling thread will be blocked until the resource has finished loading. However, it's recommended to use [load_threaded_get_status()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get_status) to known when the load has actually completed.

---

<span id="class_ResourceLoader_method_load_threaded_get_status"></span>

[ThreadLoadStatus](class_resourceloader.md#enum_ResourceLoader_ThreadLoadStatus) **load_threaded_get_status** ( path: [String](class_string.md#class_String), progress: [Array](class_array.md#class_Array) = [] ) [🔗](class_resourceloader.md#class_ResourceLoader_method_load_threaded_get_status)

Returns the status of a threaded loading operation started with [load_threaded_request()](class_resourceloader.md#class_ResourceLoader_method_load_threaded_request) for the resource at `path`.

An array variable can optionally be passed via `progress`, and will return a one-element array containing the ratio of completion of the threaded loading (between `0.0` and `1.0`).

 **Note:** The recommended way of using this method is to call it during different frames (e.g., in [Node._process()](class_node.md#class_Node_private_method__process), instead of a loop).

---

<span id="class_ResourceLoader_method_load_threaded_request"></span>

Error **load_threaded_request** ( path: [String](class_string.md#class_String), type_hint: [String](class_string.md#class_String) = "", use_sub_threads: [bool](class_bool.md#class_bool) = false, cache_mode: [CacheMode](class_resourceloader.md#enum_ResourceLoader_CacheMode) = 1 ) [🔗](class_resourceloader.md#class_ResourceLoader_method_load_threaded_request)

Loads the resource using threads. If `use_sub_threads` is `true`, multiple threads will be used to load the resource, which makes loading faster, but may affect the main thread (and thus cause game slowdowns).

The `cache_mode` parameter defines whether and how the cache should be used or updated when loading the resource.

---

<span id="class_ResourceLoader_method_remove_resource_format_loader"></span>

void **remove_resource_format_loader** ( format_loader: [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_remove_resource_format_loader)

Unregisters the given [ResourceFormatLoader](class_resourceformatloader.md#class_ResourceFormatLoader).

---

<span id="class_ResourceLoader_method_set_abort_on_missing_resources"></span>

void **set_abort_on_missing_resources** ( abort: [bool](class_bool.md#class_bool) ) [🔗](class_resourceloader.md#class_ResourceLoader_method_set_abort_on_missing_resources)

Changes the behavior on missing sub-resources. The default behavior is to abort loading.
