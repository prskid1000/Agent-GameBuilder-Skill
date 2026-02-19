<span id="class_EditorFileSystem"></span>

## EditorFileSystem

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Resource filesystem, as the editor sees it.

### Description

This object holds information of all resources in the filesystem, their types, etc.

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_filesystem()](class_editorinterface.md#class_EditorInterface_method_get_resource_filesystem).

### Methods


| [String](class_string.md#class_String) | [get_file_type](class_editorfilesystem.md#class_EditorFileSystem_method_get_file_type) ( path: [String](class_string.md#class_String) ) const |
| --- | --- |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) | [get_filesystem](class_editorfilesystem.md#class_EditorFileSystem_method_get_filesystem) ( ) |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) | [get_filesystem_path](class_editorfilesystem.md#class_EditorFileSystem_method_get_filesystem_path) ( path: [String](class_string.md#class_String) ) |
| [float](class_float.md#class_float) | [get_scanning_progress](class_editorfilesystem.md#class_EditorFileSystem_method_get_scanning_progress) ( ) const |
| [bool](class_bool.md#class_bool) | [is_importing](class_editorfilesystem.md#class_EditorFileSystem_method_is_importing) ( ) const |
| [bool](class_bool.md#class_bool) | [is_scanning](class_editorfilesystem.md#class_EditorFileSystem_method_is_scanning) ( ) const |
| void | [reimport_files](class_editorfilesystem.md#class_EditorFileSystem_method_reimport_files) ( files: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| void | [scan](class_editorfilesystem.md#class_EditorFileSystem_method_scan) ( ) |
| void | [scan_sources](class_editorfilesystem.md#class_EditorFileSystem_method_scan_sources) ( ) |
| void | [update_file](class_editorfilesystem.md#class_EditorFileSystem_method_update_file) ( path: [String](class_string.md#class_String) ) |

---

### Signals

<span id="class_EditorFileSystem_signal_filesystem_changed"></span>

**filesystem_changed** ( ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_filesystem_changed)

Emitted if the filesystem changed.

---

<span id="class_EditorFileSystem_signal_resources_reimported"></span>

**resources_reimported** ( resources: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_resources_reimported)

Emitted if a resource is reimported.

---

<span id="class_EditorFileSystem_signal_resources_reimporting"></span>

**resources_reimporting** ( resources: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_resources_reimporting)

Emitted before a resource is reimported.

---

<span id="class_EditorFileSystem_signal_resources_reload"></span>

**resources_reload** ( resources: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_resources_reload)

Emitted if at least one resource is reloaded when the filesystem is scanned.

---

<span id="class_EditorFileSystem_signal_script_classes_updated"></span>

**script_classes_updated** ( ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_script_classes_updated)

Emitted when the list of global script classes gets updated.

---

<span id="class_EditorFileSystem_signal_sources_changed"></span>

**sources_changed** ( exist: [bool](class_bool.md#class_bool) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_signal_sources_changed)

Emitted if the source of any imported file changed.

---

### Method Descriptions

<span id="class_EditorFileSystem_method_get_file_type"></span>

[String](class_string.md#class_String) **get_file_type** ( path: [String](class_string.md#class_String) ) *const* [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_get_file_type)

Returns the resource type of the file, given the full path. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---

<span id="class_EditorFileSystem_method_get_filesystem"></span>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) **get_filesystem** ( ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_get_filesystem)

Gets the root directory object.

---

<span id="class_EditorFileSystem_method_get_filesystem_path"></span>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) **get_filesystem_path** ( path: [String](class_string.md#class_String) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_get_filesystem_path)

Returns a view into the filesystem at `path`.

---

<span id="class_EditorFileSystem_method_get_scanning_progress"></span>

[float](class_float.md#class_float) **get_scanning_progress** ( ) *const* [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_get_scanning_progress)

Returns the scan progress for 0 to 1 if the FS is being scanned.

---

<span id="class_EditorFileSystem_method_is_importing"></span>

[bool](class_bool.md#class_bool) **is_importing** ( ) *const* [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_is_importing)

Returns `true` if resources are currently being imported.

---

<span id="class_EditorFileSystem_method_is_scanning"></span>

[bool](class_bool.md#class_bool) **is_scanning** ( ) *const* [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_is_scanning)

Returns `true` if the filesystem is being scanned.

---

<span id="class_EditorFileSystem_method_reimport_files"></span>

void **reimport_files** ( files: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_reimport_files)

Reimports a set of files. Call this if these files or their `.import` files were directly edited by script or an external program.

If the file type changed or the file was newly created, use [update_file()](class_editorfilesystem.md#class_EditorFileSystem_method_update_file) or [scan()](class_editorfilesystem.md#class_EditorFileSystem_method_scan).

 **Note:** This function blocks until the import is finished. However, the main loop iteration, including timers and [Node._process()](class_node.md#class_Node_private_method__process), will occur during the import process due to progress bar updates. Avoid calls to [reimport_files()](class_editorfilesystem.md#class_EditorFileSystem_method_reimport_files) or [scan()](class_editorfilesystem.md#class_EditorFileSystem_method_scan) while an import is in progress.

---

<span id="class_EditorFileSystem_method_scan"></span>

void **scan** ( ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_scan)

Scan the filesystem for changes.

---

<span id="class_EditorFileSystem_method_scan_sources"></span>

void **scan_sources** ( ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_scan_sources)

Check if the source of any imported resource changed.

---

<span id="class_EditorFileSystem_method_update_file"></span>

void **update_file** ( path: [String](class_string.md#class_String) ) [🔗](class_editorfilesystem.md#class_EditorFileSystem_method_update_file)

Add a file in an existing directory, or schedule file information to be updated on editor restart. Can be used to update text files saved by an external program.

This will not import the file. To reimport, call [reimport_files()](class_editorfilesystem.md#class_EditorFileSystem_method_reimport_files) or [scan()](class_editorfilesystem.md#class_EditorFileSystem_method_scan) methods.
