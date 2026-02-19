<span id="class_FileSystemDock"></span>

## FileSystemDock

**Inherits:** [EditorDock](class_editordock.md#class_EditorDock) **<** [MarginContainer](class_margincontainer.md#class_MarginContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's dock for managing files in the project.

### Description

This class is available only in [EditorPlugin](class_editorplugin.md#class_EditorPlugin) s and can't be instantiated. You can access it using [EditorInterface.get_file_system_dock()](class_editorinterface.md#class_EditorInterface_method_get_file_system_dock).

While **FileSystemDock** doesn't expose any methods for file manipulation, it can listen for various file-related signals.

### Methods


| void | [add_resource_tooltip_plugin](class_filesystemdock.md#class_FileSystemDock_method_add_resource_tooltip_plugin) ( plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin) ) |
| --- | --- |
| void | [navigate_to_path](class_filesystemdock.md#class_FileSystemDock_method_navigate_to_path) ( path: [String](class_string.md#class_String) ) |
| void | [remove_resource_tooltip_plugin](class_filesystemdock.md#class_FileSystemDock_method_remove_resource_tooltip_plugin) ( plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin) ) |

---

### Signals

<span id="class_FileSystemDock_signal_display_mode_changed"></span>

**display_mode_changed** ( ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_display_mode_changed)

Emitted when the user switches file display mode or split mode.

---

<span id="class_FileSystemDock_signal_file_removed"></span>

**file_removed** ( file: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_file_removed)

Emitted when the given `file` was removed.

---

<span id="class_FileSystemDock_signal_files_moved"></span>

**files_moved** ( old_file: [String](class_string.md#class_String), new_file: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_files_moved)

Emitted when a file is moved from `old_file` path to `new_file` path.

---

<span id="class_FileSystemDock_signal_folder_color_changed"></span>

**folder_color_changed** ( ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_folder_color_changed)

Emitted when folders change color.

---

<span id="class_FileSystemDock_signal_folder_moved"></span>

**folder_moved** ( old_folder: [String](class_string.md#class_String), new_folder: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_folder_moved)

Emitted when a folder is moved from `old_folder` path to `new_folder` path.

---

<span id="class_FileSystemDock_signal_folder_removed"></span>

**folder_removed** ( folder: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_folder_removed)

Emitted when the given `folder` was removed.

---

<span id="class_FileSystemDock_signal_inherit"></span>

**inherit** ( file: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_inherit)

Emitted when a new scene is created that inherits the scene at `file` path.

---

<span id="class_FileSystemDock_signal_instantiate"></span>

**instantiate** ( files: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_instantiate)

Emitted when the given scenes are being instantiated in the editor.

---

<span id="class_FileSystemDock_signal_resource_removed"></span>

**resource_removed** ( resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_resource_removed)

Emitted when an external `resource` had its file removed.

---

<span id="class_FileSystemDock_signal_selection_changed"></span>

**selection_changed** ( ) [🔗](class_filesystemdock.md#class_FileSystemDock_signal_selection_changed)

Emitted when the selection changes. Use [EditorInterface.get_selected_paths()](class_editorinterface.md#class_EditorInterface_method_get_selected_paths) in the connected method to get the selected paths.

---

### Method Descriptions

<span id="class_FileSystemDock_method_add_resource_tooltip_plugin"></span>

void **add_resource_tooltip_plugin** ( plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin) ) [🔗](class_filesystemdock.md#class_FileSystemDock_method_add_resource_tooltip_plugin)

Registers a new [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin).

---

<span id="class_FileSystemDock_method_navigate_to_path"></span>

void **navigate_to_path** ( path: [String](class_string.md#class_String) ) [🔗](class_filesystemdock.md#class_FileSystemDock_method_navigate_to_path)

Sets the given `path` as currently selected, ensuring that the selected file/directory is visible.

---

<span id="class_FileSystemDock_method_remove_resource_tooltip_plugin"></span>

void **remove_resource_tooltip_plugin** ( plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin) ) [🔗](class_filesystemdock.md#class_FileSystemDock_method_remove_resource_tooltip_plugin)

Removes an [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin). Fails if the plugin wasn't previously added.
