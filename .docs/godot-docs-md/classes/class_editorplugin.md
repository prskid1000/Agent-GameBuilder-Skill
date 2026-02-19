<span id="class_EditorPlugin"></span>

## EditorPlugin

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [GridMapEditorPlugin](class_gridmapeditorplugin.md#class_GridMapEditorPlugin)

Used by the editor to extend its functionality.

### Description

Plugins are used by the editor to extend functionality. The most common types of plugins are those which edit a given node or resource type, import plugins and export plugins. See also [EditorScript](class_editorscript.md#class_EditorScript) to add functions to the editor.

 **Note:** Some names in this class contain "left" or "right" (e.g. [DOCK_SLOT_LEFT_UL](class_editorplugin.md#class_EditorPlugin_constant_DOCK_SLOT_LEFT_UL)). These APIs assume left-to-right layout, and would be backwards when using right-to-left layout. These names are kept for compatibility reasons.

### Tutorials

- [Editor plugins documentation index](../tutorials/plugins/editor/index.md)

### Methods


| void | [_apply_changes](class_editorplugin.md#class_EditorPlugin_private_method__apply_changes) ( ) virtual |
| --- | --- |
| [bool](class_bool.md#class_bool) | [_build](class_editorplugin.md#class_EditorPlugin_private_method__build) ( ) virtual |
| void | [_clear](class_editorplugin.md#class_EditorPlugin_private_method__clear) ( ) virtual |
| void | [_disable_plugin](class_editorplugin.md#class_EditorPlugin_private_method__disable_plugin) ( ) virtual |
| void | [_edit](class_editorplugin.md#class_EditorPlugin_private_method__edit) ( object: [Object](class_object.md#class_Object) ) virtual |
| void | [_enable_plugin](class_editorplugin.md#class_EditorPlugin_private_method__enable_plugin) ( ) virtual |
| void | [_forward_3d_draw_over_viewport](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_draw_over_viewport) ( viewport_control: [Control](class_control.md#class_Control) ) virtual |
| void | [_forward_3d_force_draw_over_viewport](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport) ( viewport_control: [Control](class_control.md#class_Control) ) virtual |
| [int](class_int.md#class_int) | [_forward_3d_gui_input](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_gui_input) ( viewport_camera: [Camera3D](class_camera3d.md#class_Camera3D), event: [InputEvent](class_inputevent.md#class_InputEvent) ) virtual |
| void | [_forward_canvas_draw_over_viewport](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_draw_over_viewport) ( viewport_control: [Control](class_control.md#class_Control) ) virtual |
| void | [_forward_canvas_force_draw_over_viewport](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport) ( viewport_control: [Control](class_control.md#class_Control) ) virtual |
| [bool](class_bool.md#class_bool) | [_forward_canvas_gui_input](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_gui_input) ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_breakpoints](class_editorplugin.md#class_EditorPlugin_private_method__get_breakpoints) ( ) | virtual | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_get_plugin_icon](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_icon) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_plugin_name](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_name) ( ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_state](class_editorplugin.md#class_EditorPlugin_private_method__get_state) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_unsaved_status](class_editorplugin.md#class_EditorPlugin_private_method__get_unsaved_status) ( for_scene: [String](class_string.md#class_String) ) | virtual | const |
| void | [_get_window_layout](class_editorplugin.md#class_EditorPlugin_private_method__get_window_layout) ( configuration: [ConfigFile](class_configfile.md#class_ConfigFile) ) virtual |
| [bool](class_bool.md#class_bool) | [_handles](class_editorplugin.md#class_EditorPlugin_private_method__handles) ( object: [Object](class_object.md#class_Object) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_has_main_screen](class_editorplugin.md#class_EditorPlugin_private_method__has_main_screen) ( ) | virtual | const |
| void | [_make_visible](class_editorplugin.md#class_EditorPlugin_private_method__make_visible) ( visible: [bool](class_bool.md#class_bool) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_run_scene](class_editorplugin.md#class_EditorPlugin_private_method__run_scene) ( scene: [String](class_string.md#class_String), args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) | virtual | const |
| void | [_save_external_data](class_editorplugin.md#class_EditorPlugin_private_method__save_external_data) ( ) virtual |
| void | [_set_state](class_editorplugin.md#class_EditorPlugin_private_method__set_state) ( state: [Dictionary](class_dictionary.md#class_Dictionary) ) virtual |
| void | [_set_window_layout](class_editorplugin.md#class_EditorPlugin_private_method__set_window_layout) ( configuration: [ConfigFile](class_configfile.md#class_ConfigFile) ) virtual |
| void | [add_autoload_singleton](class_editorplugin.md#class_EditorPlugin_method_add_autoload_singleton) ( name: [String](class_string.md#class_String), path: [String](class_string.md#class_String) ) |
| void | [add_context_menu_plugin](class_editorplugin.md#class_EditorPlugin_method_add_context_menu_plugin) ( slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin) ) |
| [Button](class_button.md#class_Button) | [add_control_to_bottom_panel](class_editorplugin.md#class_EditorPlugin_method_add_control_to_bottom_panel) ( control: [Control](class_control.md#class_Control), title: [String](class_string.md#class_String), shortcut: [Shortcut](class_shortcut.md#class_Shortcut) = null ) |
| void | [add_control_to_container](class_editorplugin.md#class_EditorPlugin_method_add_control_to_container) ( container: [CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer), control: [Control](class_control.md#class_Control) ) |
| void | [add_control_to_dock](class_editorplugin.md#class_EditorPlugin_method_add_control_to_dock) ( slot: [DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot), control: [Control](class_control.md#class_Control), shortcut: [Shortcut](class_shortcut.md#class_Shortcut) = null ) |
| void | [add_custom_type](class_editorplugin.md#class_EditorPlugin_method_add_custom_type) ( type: [String](class_string.md#class_String), base: [String](class_string.md#class_String), script: [Script](class_script.md#class_Script), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [add_debugger_plugin](class_editorplugin.md#class_EditorPlugin_method_add_debugger_plugin) ( script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) ) |
| void | [add_dock](class_editorplugin.md#class_EditorPlugin_method_add_dock) ( dock: [EditorDock](class_editordock.md#class_EditorDock) ) |
| void | [add_export_platform](class_editorplugin.md#class_EditorPlugin_method_add_export_platform) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) |
| void | [add_export_plugin](class_editorplugin.md#class_EditorPlugin_method_add_export_plugin) ( plugin: [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin) ) |
| void | [add_import_plugin](class_editorplugin.md#class_EditorPlugin_method_add_import_plugin) ( importer: [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin), first_priority: [bool](class_bool.md#class_bool) = false ) |
| void | [add_inspector_plugin](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin) ( plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) ) |
| void | [add_node_3d_gizmo_plugin](class_editorplugin.md#class_EditorPlugin_method_add_node_3d_gizmo_plugin) ( plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class_EditorNode3DGizmoPlugin) ) |
| void | [add_resource_conversion_plugin](class_editorplugin.md#class_EditorPlugin_method_add_resource_conversion_plugin) ( plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin) ) |
| void | [add_scene_format_importer_plugin](class_editorplugin.md#class_EditorPlugin_method_add_scene_format_importer_plugin) ( scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter), first_priority: [bool](class_bool.md#class_bool) = false ) |
| void | [add_scene_post_import_plugin](class_editorplugin.md#class_EditorPlugin_method_add_scene_post_import_plugin) ( scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin), first_priority: [bool](class_bool.md#class_bool) = false ) |
| void | [add_tool_menu_item](class_editorplugin.md#class_EditorPlugin_method_add_tool_menu_item) ( name: [String](class_string.md#class_String), callable: [Callable](class_callable.md#class_Callable) ) |
| void | [add_tool_submenu_item](class_editorplugin.md#class_EditorPlugin_method_add_tool_submenu_item) ( name: [String](class_string.md#class_String), submenu: [PopupMenu](class_popupmenu.md#class_PopupMenu) ) |
| void | [add_translation_parser_plugin](class_editorplugin.md#class_EditorPlugin_method_add_translation_parser_plugin) ( parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class_EditorTranslationParserPlugin) ) |
| void | [add_undo_redo_inspector_hook_callback](class_editorplugin.md#class_EditorPlugin_method_add_undo_redo_inspector_hook_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| [EditorInterface](class_editorinterface.md#class_EditorInterface) | [get_editor_interface](class_editorplugin.md#class_EditorPlugin_method_get_editor_interface) ( ) |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_export_as_menu](class_editorplugin.md#class_EditorPlugin_method_get_export_as_menu) ( ) |
| [String](class_string.md#class_String) | [get_plugin_version](class_editorplugin.md#class_EditorPlugin_method_get_plugin_version) ( ) const |
| [ScriptCreateDialog](class_scriptcreatedialog.md#class_ScriptCreateDialog) | [get_script_create_dialog](class_editorplugin.md#class_EditorPlugin_method_get_script_create_dialog) ( ) |
| [EditorUndoRedoManager](class_editorundoredomanager.md#class_EditorUndoRedoManager) | [get_undo_redo](class_editorplugin.md#class_EditorPlugin_method_get_undo_redo) ( ) |
| void | [hide_bottom_panel](class_editorplugin.md#class_EditorPlugin_method_hide_bottom_panel) ( ) |
| void | [make_bottom_panel_item_visible](class_editorplugin.md#class_EditorPlugin_method_make_bottom_panel_item_visible) ( item: [Control](class_control.md#class_Control) ) |
| void | [queue_save_layout](class_editorplugin.md#class_EditorPlugin_method_queue_save_layout) ( ) |
| void | [remove_autoload_singleton](class_editorplugin.md#class_EditorPlugin_method_remove_autoload_singleton) ( name: [String](class_string.md#class_String) ) |
| void | [remove_context_menu_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_context_menu_plugin) ( plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin) ) |
| void | [remove_control_from_bottom_panel](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_bottom_panel) ( control: [Control](class_control.md#class_Control) ) |
| void | [remove_control_from_container](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_container) ( container: [CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer), control: [Control](class_control.md#class_Control) ) |
| void | [remove_control_from_docks](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_docks) ( control: [Control](class_control.md#class_Control) ) |
| void | [remove_custom_type](class_editorplugin.md#class_EditorPlugin_method_remove_custom_type) ( type: [String](class_string.md#class_String) ) |
| void | [remove_debugger_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_debugger_plugin) ( script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) ) |
| void | [remove_dock](class_editorplugin.md#class_EditorPlugin_method_remove_dock) ( dock: [EditorDock](class_editordock.md#class_EditorDock) ) |
| void | [remove_export_platform](class_editorplugin.md#class_EditorPlugin_method_remove_export_platform) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) |
| void | [remove_export_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_export_plugin) ( plugin: [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin) ) |
| void | [remove_import_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_import_plugin) ( importer: [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin) ) |
| void | [remove_inspector_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_inspector_plugin) ( plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) ) |
| void | [remove_node_3d_gizmo_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_node_3d_gizmo_plugin) ( plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class_EditorNode3DGizmoPlugin) ) |
| void | [remove_resource_conversion_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_resource_conversion_plugin) ( plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin) ) |
| void | [remove_scene_format_importer_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_scene_format_importer_plugin) ( scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter) ) |
| void | [remove_scene_post_import_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_scene_post_import_plugin) ( scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin) ) |
| void | [remove_tool_menu_item](class_editorplugin.md#class_EditorPlugin_method_remove_tool_menu_item) ( name: [String](class_string.md#class_String) ) |
| void | [remove_translation_parser_plugin](class_editorplugin.md#class_EditorPlugin_method_remove_translation_parser_plugin) ( parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class_EditorTranslationParserPlugin) ) |
| void | [remove_undo_redo_inspector_hook_callback](class_editorplugin.md#class_EditorPlugin_method_remove_undo_redo_inspector_hook_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| void | [set_dock_tab_icon](class_editorplugin.md#class_EditorPlugin_method_set_dock_tab_icon) ( control: [Control](class_control.md#class_Control), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_force_draw_over_forwarding_enabled](class_editorplugin.md#class_EditorPlugin_method_set_force_draw_over_forwarding_enabled) ( ) |
| void | [set_input_event_forwarding_always_enabled](class_editorplugin.md#class_EditorPlugin_method_set_input_event_forwarding_always_enabled) ( ) |
| [int](class_int.md#class_int) | [update_overlays](class_editorplugin.md#class_EditorPlugin_method_update_overlays) ( ) const |

---

### Signals

<span id="class_EditorPlugin_signal_main_screen_changed"></span>

**main_screen_changed** ( screen_name: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_main_screen_changed)

Emitted when user changes the workspace (**2D**, **3D**, **Script**, **Game**, **AssetLib**). Also works with custom screens defined by plugins.

---

<span id="class_EditorPlugin_signal_project_settings_changed"></span>

**project_settings_changed** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_project_settings_changed)

**Deprecated:** Use [ProjectSettings.settings_changed](class_projectsettings.md#class_ProjectSettings_signal_settings_changed) instead.

Emitted when any project setting has changed.

---

<span id="class_EditorPlugin_signal_resource_saved"></span>

**resource_saved** ( resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_resource_saved)

Emitted when the given `resource` was saved on disc. See also [scene_saved](class_editorplugin.md#class_EditorPlugin_signal_scene_saved).

---

<span id="class_EditorPlugin_signal_scene_changed"></span>

**scene_changed** ( scene_root: [Node](class_node.md#class_Node) ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_scene_changed)

Emitted when the scene is changed in the editor. The argument will return the root node of the scene that has just become active. If this scene is new and empty, the argument will be `null`.

---

<span id="class_EditorPlugin_signal_scene_closed"></span>

**scene_closed** ( filepath: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_scene_closed)

Emitted when user closes a scene. The argument is a file path to the closed scene.

---

<span id="class_EditorPlugin_signal_scene_saved"></span>

**scene_saved** ( filepath: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_signal_scene_saved)

Emitted when a scene was saved on disc. The argument is a file path to the saved scene. See also [resource_saved](class_editorplugin.md#class_EditorPlugin_signal_resource_saved).

---

### Enumerations

<span id="enum_EditorPlugin_CustomControlContainer"></span>

enum **CustomControlContainer**: [🔗](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer)

<span id="class_EditorPlugin_constant_CONTAINER_TOOLBAR"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_TOOLBAR** = `0`

Main editor toolbar, next to play buttons.

<span id="class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_MENU"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_SPATIAL_EDITOR_MENU** = `1`

The toolbar that appears when 3D editor is active.

<span id="class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_SIDE_LEFT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_SPATIAL_EDITOR_SIDE_LEFT** = `2`

Left sidebar of the 3D editor.

<span id="class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT** = `3`

Right sidebar of the 3D editor.

<span id="class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_BOTTOM"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_SPATIAL_EDITOR_BOTTOM** = `4`

Bottom panel of the 3D editor.

<span id="class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_MENU"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_CANVAS_EDITOR_MENU** = `5`

The toolbar that appears when 2D editor is active.

<span id="class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_SIDE_LEFT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_CANVAS_EDITOR_SIDE_LEFT** = `6`

Left sidebar of the 2D editor.

<span id="class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_SIDE_RIGHT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_CANVAS_EDITOR_SIDE_RIGHT** = `7`

Right sidebar of the 2D editor.

<span id="class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_BOTTOM"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_CANVAS_EDITOR_BOTTOM** = `8`

Bottom panel of the 2D editor.

<span id="class_EditorPlugin_constant_CONTAINER_INSPECTOR_BOTTOM"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_INSPECTOR_BOTTOM** = `9`

Bottom section of the inspector.

<span id="class_EditorPlugin_constant_CONTAINER_PROJECT_SETTING_TAB_LEFT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_PROJECT_SETTING_TAB_LEFT** = `10`

Tab of Project Settings dialog, to the left of other tabs.

<span id="class_EditorPlugin_constant_CONTAINER_PROJECT_SETTING_TAB_RIGHT"></span>

[CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer) **CONTAINER_PROJECT_SETTING_TAB_RIGHT** = `11`

Tab of Project Settings dialog, to the right of other tabs.

---

<span id="enum_EditorPlugin_DockSlot"></span>

enum **DockSlot**: [🔗](class_editorplugin.md#enum_EditorPlugin_DockSlot)

<span id="class_EditorPlugin_constant_DOCK_SLOT_NONE"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_NONE** = `-1`

The dock is closed.

<span id="class_EditorPlugin_constant_DOCK_SLOT_LEFT_UL"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

<span id="class_EditorPlugin_constant_DOCK_SLOT_LEFT_BL"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

<span id="class_EditorPlugin_constant_DOCK_SLOT_LEFT_UR"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).

<span id="class_EditorPlugin_constant_DOCK_SLOT_LEFT_BR"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem dock).

<span id="class_EditorPlugin_constant_DOCK_SLOT_RIGHT_UL"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Node, and History docks).

<span id="class_EditorPlugin_constant_DOCK_SLOT_RIGHT_BL"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

<span id="class_EditorPlugin_constant_DOCK_SLOT_RIGHT_UR"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

<span id="class_EditorPlugin_constant_DOCK_SLOT_RIGHT_BR"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

<span id="class_EditorPlugin_constant_DOCK_SLOT_BOTTOM"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.

<span id="class_EditorPlugin_constant_DOCK_SLOT_MAX"></span>

[DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) **DOCK_SLOT_MAX** = `9`

Represents the size of the [DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot) enum.

---

<span id="enum_EditorPlugin_AfterGUIInput"></span>

enum **AfterGUIInput**: [🔗](class_editorplugin.md#enum_EditorPlugin_AfterGUIInput)

<span id="class_EditorPlugin_constant_AFTER_GUI_INPUT_PASS"></span>

[AfterGUIInput](class_editorplugin.md#enum_EditorPlugin_AfterGUIInput) **AFTER_GUI_INPUT_PASS** = `0`

Forwards the [InputEvent](class_inputevent.md#class_InputEvent) to other EditorPlugins.

<span id="class_EditorPlugin_constant_AFTER_GUI_INPUT_STOP"></span>

[AfterGUIInput](class_editorplugin.md#enum_EditorPlugin_AfterGUIInput) **AFTER_GUI_INPUT_STOP** = `1`

Prevents the [InputEvent](class_inputevent.md#class_InputEvent) from reaching other Editor classes.

<span id="class_EditorPlugin_constant_AFTER_GUI_INPUT_CUSTOM"></span>

[AfterGUIInput](class_editorplugin.md#enum_EditorPlugin_AfterGUIInput) **AFTER_GUI_INPUT_CUSTOM** = `2`

Pass the [InputEvent](class_inputevent.md#class_InputEvent) to other editor plugins except the main [Node3D](class_node3d.md#class_Node3D) one. This can be used to prevent node selection changes and work with sub-gizmos instead.

---

### Method Descriptions

<span id="class_EditorPlugin_private_method__apply_changes"></span>

void **_apply_changes** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__apply_changes)

This method is called when the editor is about to save the project, switch to another tab, etc. It asks the plugin to apply any pending state changes to ensure consistency.

This is used, for example, in shader editors to let the plugin know that it must apply the shader code being written by the user to the object.

---

<span id="class_EditorPlugin_private_method__build"></span>

[bool](class_bool.md#class_bool) **_build** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__build)

This method is called when the editor is about to run the project. The plugin can then perform required operations before the project runs.

This method must return a boolean. If this method returns `false`, the project will not run. The run is aborted immediately, so this also prevents all other plugins' [_build()](class_editorplugin.md#class_EditorPlugin_private_method__build) methods from running.

---

<span id="class_EditorPlugin_private_method__clear"></span>

void **_clear** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__clear)

Clear all the state and reset the object being edited to zero. This ensures your plugin does not keep editing a currently existing node, or a node from the wrong scene.

---

<span id="class_EditorPlugin_private_method__disable_plugin"></span>

void **_disable_plugin** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__disable_plugin)

Called by the engine when the user disables the **EditorPlugin** in the Plugin tab of the project settings window.

---

<span id="class_EditorPlugin_private_method__edit"></span>

void **_edit** ( object: [Object](class_object.md#class_Object) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__edit)

This function is used for plugins that edit specific object types (nodes or resources). It requests the editor to edit the given object.

 `object` can be `null` if the plugin was editing an object, but there is no longer any selected object handled by this plugin. It can be used to cleanup editing state.

---

<span id="class_EditorPlugin_private_method__enable_plugin"></span>

void **_enable_plugin** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__enable_plugin)

Called by the engine when the user enables the **EditorPlugin** in the Plugin tab of the project settings window.

---

<span id="class_EditorPlugin_private_method__forward_3d_draw_over_viewport"></span>

void **_forward_3d_draw_over_viewport** ( viewport_control: [Control](class_control.md#class_Control) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_draw_over_viewport)

Called by the engine when the 3D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling [update_overlays()](class_editorplugin.md#class_EditorPlugin_method_update_overlays).

.. tabs::

```
```

    func _forward_3d_draw_over_viewport(overlay):
        # Draw a circle at the cursor's position.
        overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

    func _forward_3d_gui_input(camera, event):
        if event is InputEventMouseMotion:
            # Redraw the viewport when the cursor is moved.
            update_overlays()
            return EditorPlugin.AFTER_GUI_INPUT_STOP
        return EditorPlugin.AFTER_GUI_INPUT_PASS

```
```

    public override void _Forward3DDrawOverViewport(Control viewportControl)
    {
        // Draw a circle at the cursor's position.
        viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
    }

    public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D viewportCamera, InputEvent @event)
    {
        if (@event is InputEventMouseMotion)
        {
            // Redraw the viewport when the cursor is moved.
            UpdateOverlays();
            return EditorPlugin.AfterGuiInput.Stop;
        }
        return EditorPlugin.AfterGuiInput.Pass;
    }

---

<span id="class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport"></span>

void **_forward_3d_force_draw_over_viewport** ( viewport_control: [Control](class_control.md#class_Control) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport)

This method is the same as [_forward_3d_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_draw_over_viewport), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using [set_force_draw_over_forwarding_enabled()](class_editorplugin.md#class_EditorPlugin_method_set_force_draw_over_forwarding_enabled).

---

<span id="class_EditorPlugin_private_method__forward_3d_gui_input"></span>

[int](class_int.md#class_int) **_forward_3d_gui_input** ( viewport_camera: [Camera3D](class_camera3d.md#class_Camera3D), event: [InputEvent](class_inputevent.md#class_InputEvent) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_gui_input)

Called when there is a root node in the current edited scene, [_handles()](class_editorplugin.md#class_EditorPlugin_private_method__handles) is implemented, and an [InputEvent](class_inputevent.md#class_InputEvent) happens in the 3D viewport. The return value decides whether the [InputEvent](class_inputevent.md#class_InputEvent) is consumed or forwarded to other **EditorPlugin** s. See [AfterGUIInput](class_editorplugin.md#enum_EditorPlugin_AfterGUIInput) for options.

.. tabs::

```
```

    # Prevents the InputEvent from reaching other Editor classes.
    func _forward_3d_gui_input(camera, event):
        return EditorPlugin.AFTER_GUI_INPUT_STOP

```
```

    // Prevents the InputEvent from reaching other Editor classes.
    public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
    {
        return EditorPlugin.AfterGuiInput.Stop;
    }

This method must return [AFTER_GUI_INPUT_PASS](class_editorplugin.md#class_EditorPlugin_constant_AFTER_GUI_INPUT_PASS) in order to forward the [InputEvent](class_inputevent.md#class_InputEvent) to other Editor classes.

.. tabs::

```
```

    # Consumes InputEventMouseMotion and forwards other InputEvent types.
    func _forward_3d_gui_input(camera, event):
        return EditorPlugin.AFTER_GUI_INPUT_STOP if event is InputEventMouseMotion else EditorPlugin.AFTER_GUI_INPUT_PASS

```
```

    // Consumes InputEventMouseMotion and forwards other InputEvent types.
    public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
    {
        return @event is InputEventMouseMotion ? EditorPlugin.AfterGuiInput.Stop : EditorPlugin.AfterGuiInput.Pass;
    }

---

<span id="class_EditorPlugin_private_method__forward_canvas_draw_over_viewport"></span>

void **_forward_canvas_draw_over_viewport** ( viewport_control: [Control](class_control.md#class_Control) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_draw_over_viewport)

Called by the engine when the 2D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling [update_overlays()](class_editorplugin.md#class_EditorPlugin_method_update_overlays).

.. tabs::

```
```

    func _forward_canvas_draw_over_viewport(overlay):
        # Draw a circle at the cursor's position.
        overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

    func _forward_canvas_gui_input(event):
        if event is InputEventMouseMotion:
            # Redraw the viewport when the cursor is moved.
            update_overlays()
            return true
        return false

```
```

    public override void _ForwardCanvasDrawOverViewport(Control viewportControl)
    {
        // Draw a circle at the cursor's position.
        viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
    }

    public override bool _ForwardCanvasGuiInput(InputEvent @event)
    {
        if (@event is InputEventMouseMotion)
        {
            // Redraw the viewport when the cursor is moved.
            UpdateOverlays();
            return true;
        }
        return false;
    }

---

<span id="class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport"></span>

void **_forward_canvas_force_draw_over_viewport** ( viewport_control: [Control](class_control.md#class_Control) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport)

This method is the same as [_forward_canvas_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_draw_over_viewport), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using [set_force_draw_over_forwarding_enabled()](class_editorplugin.md#class_EditorPlugin_method_set_force_draw_over_forwarding_enabled).

---

<span id="class_EditorPlugin_private_method__forward_canvas_gui_input"></span>

[bool](class_bool.md#class_bool) **_forward_canvas_gui_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_gui_input)

Called when there is a root node in the current edited scene, [_handles()](class_editorplugin.md#class_EditorPlugin_private_method__handles) is implemented, and an [InputEvent](class_inputevent.md#class_InputEvent) happens in the 2D viewport. If this method returns `true`, `event` is intercepted by this **EditorPlugin**, otherwise `event` is forwarded to other Editor classes.

.. tabs::

```
```

    # Prevents the InputEvent from reaching other Editor classes.
    func _forward_canvas_gui_input(event):
        return true

```
```

    // Prevents the InputEvent from reaching other Editor classes.
    public override bool ForwardCanvasGuiInput(InputEvent @event)
    {
        return true;
    }

This method must return `false` in order to forward the [InputEvent](class_inputevent.md#class_InputEvent) to other Editor classes.

.. tabs::

```
```

    # Consumes InputEventMouseMotion and forwards other InputEvent types.
    func _forward_canvas_gui_input(event):
        if (event is InputEventMouseMotion):
            return true
        return false

```
```

    // Consumes InputEventMouseMotion and forwards other InputEvent types.
    public override bool _ForwardCanvasGuiInput(InputEvent @event)
    {
        if (@event is InputEventMouseMotion)
        {
            return true;
        }
        return false;
    }

---

<span id="class_EditorPlugin_private_method__get_breakpoints"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_breakpoints** ( ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_breakpoints)

This is for editors that edit script-based objects. You can return a list of breakpoints in the format (`script:line`), for example: `res://path_to_script.gd:25`.

---

<span id="class_EditorPlugin_private_method__get_plugin_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_get_plugin_icon** ( ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_icon)

Override this method in your plugin to return a [Texture2D](class_texture2d.md#class_Texture2D) in order to give it an icon.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "AssetLib" buttons.

Ideally, the plugin icon should be white with a transparent background and 16×16 pixels in size.

.. tabs::

```
```

    func _get_plugin_icon():
        # You can use a custom icon:
        return preload("res://addons/my_plugin/my_plugin_icon.svg")
        # Or use a built-in icon:
        return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")

```
```

    public override Texture2D _GetPluginIcon()
    {
        // You can use a custom icon:
        return ResourceLoader.Load<Texture2D>("res://addons/my_plugin/my_plugin_icon.svg");
        // Or use a built-in icon:
        return EditorInterface.Singleton.GetEditorTheme().GetIcon("Node", "EditorIcons");
    }

---

<span id="class_EditorPlugin_private_method__get_plugin_name"></span>

[String](class_string.md#class_String) **_get_plugin_name** ( ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_name)

Override this method in your plugin to provide the name of the plugin when displayed in the Godot editor.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "AssetLib" buttons.

---

<span id="class_EditorPlugin_private_method__get_state"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_state** ( ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_state)

Override this method to provide a state data you want to be saved, like view position, grid settings, folding, etc. This is used when saving the scene (so state is kept when opening it again) and for switching tabs (so state can be restored when the tab returns). This data is automatically saved for each scene in an `editstate` file in the editor metadata folder. If you want to store global (scene-independent) editor data for your plugin, you can use [_get_window_layout()](class_editorplugin.md#class_EditorPlugin_private_method__get_window_layout) instead.

Use [_set_state()](class_editorplugin.md#class_EditorPlugin_private_method__set_state) to restore your saved state.

 **Note:** This method should not be used to save important settings that should persist with the project.

 **Note:** You must implement [_get_plugin_name()](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_name) for the state to be stored and restored correctly.

::

    func _get_state():
        var state = { "zoom": zoom, "preferred_color": my_color }
        return state

---

<span id="class_EditorPlugin_private_method__get_unsaved_status"></span>

[String](class_string.md#class_String) **_get_unsaved_status** ( for_scene: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_unsaved_status)

Override this method to provide a custom message that lists unsaved changes. The editor will call this method when exiting or when closing a scene, and display the returned string in a confirmation dialog. Return empty string if the plugin has no unsaved changes.

When closing a scene, `for_scene` is the path to the scene being closed. You can use it to handle built-in resources in that scene.

If the user confirms saving, [_save_external_data()](class_editorplugin.md#class_EditorPlugin_private_method__save_external_data) will be called, before closing the editor.

::

    func _get_unsaved_status(for_scene):
        if not unsaved:
            return ""

        if for_scene.is_empty():
            return "Save changes in MyCustomPlugin before closing?"
        else:
            return "Scene %s has changes from MyCustomPlugin. Save before closing?" % for_scene.get_file()

    func _save_external_data():
        unsaved = false

If the plugin has no scene-specific changes, you can ignore the calls when closing scenes:

::

    func _get_unsaved_status(for_scene):
        if not for_scene.is_empty():
            return ""

---

<span id="class_EditorPlugin_private_method__get_window_layout"></span>

void **_get_window_layout** ( configuration: [ConfigFile](class_configfile.md#class_ConfigFile) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__get_window_layout)

Override this method to provide the GUI layout of the plugin or any other data you want to be stored. This is used to save the project's editor layout when [queue_save_layout()](class_editorplugin.md#class_EditorPlugin_method_queue_save_layout) is called or the editor layout was changed (for example changing the position of a dock). The data is stored in the `editor_layout.cfg` file in the editor metadata directory.

Use [_set_window_layout()](class_editorplugin.md#class_EditorPlugin_private_method__set_window_layout) to restore your saved layout.

::

    func _get_window_layout(configuration):
        configuration.set_value("MyPlugin", "window_position", $Window.position)
        configuration.set_value("MyPlugin", "icon_color", $Icon.modulate)

---

<span id="class_EditorPlugin_private_method__handles"></span>

[bool](class_bool.md#class_bool) **_handles** ( object: [Object](class_object.md#class_Object) ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__handles)

Implement this function if your plugin edits a specific type of object (Resource or Node). If you return `true`, then you will get the functions [_edit()](class_editorplugin.md#class_EditorPlugin_private_method__edit) and [_make_visible()](class_editorplugin.md#class_EditorPlugin_private_method__make_visible) called when the editor requests them. If you have declared the methods [_forward_canvas_gui_input()](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_gui_input) and [_forward_3d_gui_input()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_gui_input) these will be called too.

 **Note:** Each plugin should handle only one type of objects at a time. If a plugin handles more types of objects and they are edited at the same time, it will result in errors.

---

<span id="class_EditorPlugin_private_method__has_main_screen"></span>

[bool](class_bool.md#class_bool) **_has_main_screen** ( ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__has_main_screen)

Returns `true` if this is a main screen editor plugin (it goes in the workspace selector together with **2D**, **3D**, **Script**, **Game**, and **AssetLib**).

When the plugin's workspace is selected, other main screen plugins will be hidden, but your plugin will not appear automatically. It needs to be added as a child of [EditorInterface.get_editor_main_screen()](class_editorinterface.md#class_EditorInterface_method_get_editor_main_screen) and made visible inside [_make_visible()](class_editorplugin.md#class_EditorPlugin_private_method__make_visible).

Use [_get_plugin_name()](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_name) and [_get_plugin_icon()](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_icon) to customize the plugin button's appearance.

::

    var plugin_control

    func _enter_tree():
        plugin_control = preload("my_plugin_control.tscn").instantiate()
        EditorInterface.get_editor_main_screen().add_child(plugin_control)
        plugin_control.hide()

    func _has_main_screen():
        return true

    func _make_visible(visible):
        plugin_control.visible = visible

    func _get_plugin_name():
        return "My Super Cool Plugin 3000"

    func _get_plugin_icon():
        return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")

---

<span id="class_EditorPlugin_private_method__make_visible"></span>

void **_make_visible** ( visible: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__make_visible)

This function will be called when the editor is requested to become visible. It is used for plugins that edit a specific object type.

Remember that you have to manage the visibility of all your editor controls manually.

---

<span id="class_EditorPlugin_private_method__run_scene"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_run_scene** ( scene: [String](class_string.md#class_String), args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* *const* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__run_scene)

This function is called when an individual scene is about to be played in the editor. `args` is a list of command line arguments that will be passed to the new Godot instance, which will be replaced by the list returned by this function.

::

    func _run_scene(scene, args):
        args.append("--an-extra-argument")
        return args

 **Note:** Text that is printed in this method will not be visible in the editor's Output panel unless EditorSettings.run/output/always_clear_output_on_play is `false`.

---

<span id="class_EditorPlugin_private_method__save_external_data"></span>

void **_save_external_data** ( ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__save_external_data)

This method is called after the editor saves the project or when it's closed. It asks the plugin to save edited external scenes/resources.

---

<span id="class_EditorPlugin_private_method__set_state"></span>

void **_set_state** ( state: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__set_state)

Restore the state saved by [_get_state()](class_editorplugin.md#class_EditorPlugin_private_method__get_state). This method is called when the current scene tab is changed in the editor.

 **Note:** Your plugin must implement [_get_plugin_name()](class_editorplugin.md#class_EditorPlugin_private_method__get_plugin_name), otherwise it will not be recognized and this method will not be called.

::

    func _set_state(data):
        zoom = data.get("zoom", 1.0)
        preferred_color = data.get("my_color", Color.WHITE)

---

<span id="class_EditorPlugin_private_method__set_window_layout"></span>

void **_set_window_layout** ( configuration: [ConfigFile](class_configfile.md#class_ConfigFile) ) *virtual* [🔗](class_editorplugin.md#class_EditorPlugin_private_method__set_window_layout)

Restore the plugin GUI layout and data saved by [_get_window_layout()](class_editorplugin.md#class_EditorPlugin_private_method__get_window_layout). This method is called for every plugin on editor startup. Use the provided `configuration` file to read your saved data.

::

    func _set_window_layout(configuration):
        $Window.position = configuration.get_value("MyPlugin", "window_position", Vector2())
        $Icon.modulate = configuration.get_value("MyPlugin", "icon_color", Color.WHITE)

---

<span id="class_EditorPlugin_method_add_autoload_singleton"></span>

void **add_autoload_singleton** ( name: [String](class_string.md#class_String), path: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_autoload_singleton)

Adds a script at `path` to the Autoload list as `name`.

---

<span id="class_EditorPlugin_method_add_context_menu_plugin"></span>

void **add_context_menu_plugin** ( slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_context_menu_plugin)

Adds a plugin to the context menu. `slot` is the context menu where the plugin will be added.

 **Note:** A plugin instance can belong only to a single context menu slot.

---

<span id="class_EditorPlugin_method_add_control_to_bottom_panel"></span>

[Button](class_button.md#class_Button) **add_control_to_bottom_panel** ( control: [Control](class_control.md#class_Control), title: [String](class_string.md#class_String), shortcut: [Shortcut](class_shortcut.md#class_Shortcut) = null ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_control_to_bottom_panel)

**Deprecated:** Use [add_dock()](class_editorplugin.md#class_EditorPlugin_method_add_dock) instead, with [EditorDock.default_slot](class_editordock.md#class_EditorDock_property_default_slot) set to [DOCK_SLOT_BOTTOM](class_editorplugin.md#class_EditorPlugin_constant_DOCK_SLOT_BOTTOM).

Adds a control to the bottom panel (together with Output, Debug, Animation, etc.). Returns a reference to a button that is outside the scene tree. It's up to you to hide/show the button when needed. When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_bottom_panel()](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_bottom_panel) and free it with [Node.queue_free()](class_node.md#class_Node_method_queue_free).

 `shortcut` is a shortcut that, when activated, will toggle the bottom panel's visibility. The shortcut object is only set when this control is added to the bottom panel.

 **Note** See the default editor bottom panel shortcuts in the Editor Settings for inspiration. By convention, they all use :kbd:`Alt` modifier.

---

<span id="class_EditorPlugin_method_add_control_to_container"></span>

void **add_control_to_container** ( container: [CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer), control: [Control](class_control.md#class_Control) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_control_to_container)

Adds a custom control to a container in the editor UI.

Please remember that you have to manage the visibility of your custom controls yourself (and likely hide it after adding it).

When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_container()](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_container) and free it with [Node.queue_free()](class_node.md#class_Node_method_queue_free).

---

<span id="class_EditorPlugin_method_add_control_to_dock"></span>

void **add_control_to_dock** ( slot: [DockSlot](class_editorplugin.md#enum_EditorPlugin_DockSlot), control: [Control](class_control.md#class_Control), shortcut: [Shortcut](class_shortcut.md#class_Shortcut) = null ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_control_to_dock)

**Deprecated:** Use [add_dock()](class_editorplugin.md#class_EditorPlugin_method_add_dock) instead.

Adds the control to a specific dock slot.

If the dock is repositioned and as long as the plugin is active, the editor will save the dock position on further sessions.

When your plugin is deactivated, make sure to remove your custom control with [remove_control_from_docks()](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_docks) and free it with [Node.queue_free()](class_node.md#class_Node_method_queue_free).

Optionally, you can specify a shortcut parameter. When pressed, this shortcut will open and focus the dock.

---

<span id="class_EditorPlugin_method_add_custom_type"></span>

void **add_custom_type** ( type: [String](class_string.md#class_String), base: [String](class_string.md#class_String), script: [Script](class_script.md#class_Script), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_custom_type)

Adds a custom type, which will appear in the list of nodes or resources.

When a given node or resource is selected, the base type will be instantiated (e.g. "Node3D", "Control", "Resource"), then the script will be loaded and set to this object.

 **Note:** The base type is the base engine class which this type's class hierarchy inherits, not any custom type parent classes.

You can use the virtual method [_handles()](class_editorplugin.md#class_EditorPlugin_private_method__handles) to check if your custom object is being edited by checking the script or using the `is` keyword.

During run-time, this will be a simple object with a script so this function does not need to be called then.

 **Note:** Custom types added this way are not true classes. They are just a helper to create a node with specific script.

---

<span id="class_EditorPlugin_method_add_debugger_plugin"></span>

void **add_debugger_plugin** ( script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_debugger_plugin)

Adds a [Script](class_script.md#class_Script) as debugger plugin to the Debugger. The script must extend [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin).

---

<span id="class_EditorPlugin_method_add_dock"></span>

void **add_dock** ( dock: [EditorDock](class_editordock.md#class_EditorDock) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_dock)

Adds a new dock.

When your plugin is deactivated, make sure to remove your custom dock with [remove_dock()](class_editorplugin.md#class_EditorPlugin_method_remove_dock) and free it with [Node.queue_free()](class_node.md#class_Node_method_queue_free).

---

<span id="class_EditorPlugin_method_add_export_platform"></span>

void **add_export_platform** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_export_platform)

Registers a new [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform). Export platforms provides functionality of exporting to the specific platform.

---

<span id="class_EditorPlugin_method_add_export_plugin"></span>

void **add_export_plugin** ( plugin: [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_export_plugin)

Registers a new [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin). Export plugins are used to perform tasks when the project is being exported.

See [add_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin) for an example of how to register a plugin.

---

<span id="class_EditorPlugin_method_add_import_plugin"></span>

void **add_import_plugin** ( importer: [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin), first_priority: [bool](class_bool.md#class_bool) = false ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_import_plugin)

Registers a new [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin). Import plugins are used to import custom and unsupported assets as a custom [Resource](class_resource.md#class_Resource) type.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

 **Note:** If you want to import custom 3D asset formats use [add_scene_format_importer_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_scene_format_importer_plugin) instead.

See [add_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin) for an example of how to register a plugin.

---

<span id="class_EditorPlugin_method_add_inspector_plugin"></span>

void **add_inspector_plugin** ( plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin)

Registers a new [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin). Inspector plugins are used to extend [EditorInspector](class_editorinspector.md#class_EditorInspector) and provide custom configuration tools for your object's properties.

 **Note:** Always use [remove_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_remove_inspector_plugin) to remove the registered [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) when your **EditorPlugin** is disabled to prevent leaks and an unexpected behavior.

.. tabs::

```
```

    const MyInspectorPlugin = preload("res://addons/your_addon/path/to/your/script.gd")
    var inspector_plugin = MyInspectorPlugin.new()

    func _enter_tree():
        add_inspector_plugin(inspector_plugin)

    func _exit_tree():
        remove_inspector_plugin(inspector_plugin)

---

<span id="class_EditorPlugin_method_add_node_3d_gizmo_plugin"></span>

void **add_node_3d_gizmo_plugin** ( plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class_EditorNode3DGizmoPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_node_3d_gizmo_plugin)

Registers a new [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class_EditorNode3DGizmoPlugin). Gizmo plugins are used to add custom gizmos to the 3D preview viewport for a [Node3D](class_node3d.md#class_Node3D).

See [add_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin) for an example of how to register a plugin.

---

<span id="class_EditorPlugin_method_add_resource_conversion_plugin"></span>

void **add_resource_conversion_plugin** ( plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_resource_conversion_plugin)

Registers a new [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin). Resource conversion plugins are used to add custom resource converters to the editor inspector.

See [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin) for an example of how to create a resource conversion plugin.

---

<span id="class_EditorPlugin_method_add_scene_format_importer_plugin"></span>

void **add_scene_format_importer_plugin** ( scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter), first_priority: [bool](class_bool.md#class_bool) = false ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_scene_format_importer_plugin)

Registers a new [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter). Scene importers are used to import custom 3D asset formats as scenes.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---

<span id="class_EditorPlugin_method_add_scene_post_import_plugin"></span>

void **add_scene_post_import_plugin** ( scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin), first_priority: [bool](class_bool.md#class_bool) = false ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_scene_post_import_plugin)

Add an [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin). These plugins allow customizing the import process of 3D assets by adding new options to the import dialogs.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---

<span id="class_EditorPlugin_method_add_tool_menu_item"></span>

void **add_tool_menu_item** ( name: [String](class_string.md#class_String), callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_tool_menu_item)

Adds a custom menu item to **Project > Tools** named `name`. When clicked, the provided `callable` will be called.

---

<span id="class_EditorPlugin_method_add_tool_submenu_item"></span>

void **add_tool_submenu_item** ( name: [String](class_string.md#class_String), submenu: [PopupMenu](class_popupmenu.md#class_PopupMenu) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_tool_submenu_item)

Adds a custom [PopupMenu](class_popupmenu.md#class_PopupMenu) submenu under **Project > Tools >** `name`. Use [remove_tool_menu_item()](class_editorplugin.md#class_EditorPlugin_method_remove_tool_menu_item) on plugin clean up to remove the menu.

---

<span id="class_EditorPlugin_method_add_translation_parser_plugin"></span>

void **add_translation_parser_plugin** ( parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class_EditorTranslationParserPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_translation_parser_plugin)

Registers a custom translation parser plugin for extracting translatable strings from custom files.

---

<span id="class_EditorPlugin_method_add_undo_redo_inspector_hook_callback"></span>

void **add_undo_redo_inspector_hook_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_add_undo_redo_inspector_hook_callback)

Hooks a callback into the undo/redo action creation when a property is modified in the inspector. This allows, for example, to save other properties that may be lost when a given property is modified.

The callback should have 4 arguments: [Object](class_object.md#class_Object) `undo_redo`, [Object](class_object.md#class_Object) `modified_object`, [String](class_string.md#class_String) `property` and [Variant](class_variant.md#class_Variant) `new_value`. They are, respectively, the [UndoRedo](class_undoredo.md#class_UndoRedo) object used by the inspector, the currently modified object, the name of the modified property and the new value the property is about to take.

---

<span id="class_EditorPlugin_method_get_editor_interface"></span>

[EditorInterface](class_editorinterface.md#class_EditorInterface) **get_editor_interface** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_get_editor_interface)

**Deprecated:** [EditorInterface](class_editorinterface.md#class_EditorInterface) is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface](class_editorinterface.md#class_EditorInterface) singleton instance.

---

<span id="class_EditorPlugin_method_get_export_as_menu"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_export_as_menu** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_get_export_as_menu)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) under **Scene > Export As...**.

---

<span id="class_EditorPlugin_method_get_plugin_version"></span>

[String](class_string.md#class_String) **get_plugin_version** ( ) *const* [🔗](class_editorplugin.md#class_EditorPlugin_method_get_plugin_version)

Provide the version of the plugin declared in the `plugin.cfg` config file.

---

<span id="class_EditorPlugin_method_get_script_create_dialog"></span>

[ScriptCreateDialog](class_scriptcreatedialog.md#class_ScriptCreateDialog) **get_script_create_dialog** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_get_script_create_dialog)

Gets the Editor's dialog used for making scripts.

 **Note:** Users can configure it before use.

 **Warning:** Removing and freeing this node will render a part of the editor useless and may cause a crash.

---

<span id="class_EditorPlugin_method_get_undo_redo"></span>

[EditorUndoRedoManager](class_editorundoredomanager.md#class_EditorUndoRedoManager) **get_undo_redo** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_get_undo_redo)

Gets the undo/redo object. Most actions in the editor can be undoable, so use this object to make sure this happens when it's worth it.

---

<span id="class_EditorPlugin_method_hide_bottom_panel"></span>

void **hide_bottom_panel** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_hide_bottom_panel)

Minimizes the bottom panel.

---

<span id="class_EditorPlugin_method_make_bottom_panel_item_visible"></span>

void **make_bottom_panel_item_visible** ( item: [Control](class_control.md#class_Control) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_make_bottom_panel_item_visible)

Makes a specific item in the bottom panel visible.

---

<span id="class_EditorPlugin_method_queue_save_layout"></span>

void **queue_save_layout** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_queue_save_layout)

Queue save the project's editor layout.

---

<span id="class_EditorPlugin_method_remove_autoload_singleton"></span>

void **remove_autoload_singleton** ( name: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_autoload_singleton)

Removes an Autoload `name` from the list.

---

<span id="class_EditorPlugin_method_remove_context_menu_plugin"></span>

void **remove_context_menu_plugin** ( plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_context_menu_plugin)

Removes the specified context menu plugin.

---

<span id="class_EditorPlugin_method_remove_control_from_bottom_panel"></span>

void **remove_control_from_bottom_panel** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_bottom_panel)

**Deprecated:** Use [remove_dock()](class_editorplugin.md#class_EditorPlugin_method_remove_dock) instead.

Removes the control from the bottom panel. You have to manually [Node.queue_free()](class_node.md#class_Node_method_queue_free) the control.

---

<span id="class_EditorPlugin_method_remove_control_from_container"></span>

void **remove_control_from_container** ( container: [CustomControlContainer](class_editorplugin.md#enum_EditorPlugin_CustomControlContainer), control: [Control](class_control.md#class_Control) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_container)

Removes the control from the specified container. You have to manually [Node.queue_free()](class_node.md#class_Node_method_queue_free) the control.

---

<span id="class_EditorPlugin_method_remove_control_from_docks"></span>

void **remove_control_from_docks** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_control_from_docks)

**Deprecated:** Use [remove_dock()](class_editorplugin.md#class_EditorPlugin_method_remove_dock) instead.

Removes the control from the dock. You have to manually [Node.queue_free()](class_node.md#class_Node_method_queue_free) the control.

---

<span id="class_EditorPlugin_method_remove_custom_type"></span>

void **remove_custom_type** ( type: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_custom_type)

Removes a custom type added by [add_custom_type()](class_editorplugin.md#class_EditorPlugin_method_add_custom_type).

---

<span id="class_EditorPlugin_method_remove_debugger_plugin"></span>

void **remove_debugger_plugin** ( script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_debugger_plugin)

Removes the debugger plugin with given script from the Debugger.

---

<span id="class_EditorPlugin_method_remove_dock"></span>

void **remove_dock** ( dock: [EditorDock](class_editordock.md#class_EditorDock) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_dock)

Removes `dock` from the available docks. You should manually call [Node.queue_free()](class_node.md#class_Node_method_queue_free) to free it.

---

<span id="class_EditorPlugin_method_remove_export_platform"></span>

void **remove_export_platform** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_export_platform)

Removes an export platform registered by [add_export_platform()](class_editorplugin.md#class_EditorPlugin_method_add_export_platform).

---

<span id="class_EditorPlugin_method_remove_export_plugin"></span>

void **remove_export_plugin** ( plugin: [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_export_plugin)

Removes an export plugin registered by [add_export_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_export_plugin).

---

<span id="class_EditorPlugin_method_remove_import_plugin"></span>

void **remove_import_plugin** ( importer: [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_import_plugin)

Removes an import plugin registered by [add_import_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_import_plugin).

---

<span id="class_EditorPlugin_method_remove_inspector_plugin"></span>

void **remove_inspector_plugin** ( plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_inspector_plugin)

Removes an inspector plugin registered by [add_inspector_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_inspector_plugin).

---

<span id="class_EditorPlugin_method_remove_node_3d_gizmo_plugin"></span>

void **remove_node_3d_gizmo_plugin** ( plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class_EditorNode3DGizmoPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_node_3d_gizmo_plugin)

Removes a gizmo plugin registered by [add_node_3d_gizmo_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_node_3d_gizmo_plugin).

---

<span id="class_EditorPlugin_method_remove_resource_conversion_plugin"></span>

void **remove_resource_conversion_plugin** ( plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_resource_conversion_plugin)

Removes a resource conversion plugin registered by [add_resource_conversion_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_resource_conversion_plugin).

---

<span id="class_EditorPlugin_method_remove_scene_format_importer_plugin"></span>

void **remove_scene_format_importer_plugin** ( scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_scene_format_importer_plugin)

Removes a scene format importer registered by [add_scene_format_importer_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_scene_format_importer_plugin).

---

<span id="class_EditorPlugin_method_remove_scene_post_import_plugin"></span>

void **remove_scene_post_import_plugin** ( scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_scene_post_import_plugin)

Remove the [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin), added with [add_scene_post_import_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_scene_post_import_plugin).

---

<span id="class_EditorPlugin_method_remove_tool_menu_item"></span>

void **remove_tool_menu_item** ( name: [String](class_string.md#class_String) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_tool_menu_item)

Removes a menu `name` from **Project > Tools**.

---

<span id="class_EditorPlugin_method_remove_translation_parser_plugin"></span>

void **remove_translation_parser_plugin** ( parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class_EditorTranslationParserPlugin) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_translation_parser_plugin)

Removes a custom translation parser plugin registered by [add_translation_parser_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_translation_parser_plugin).

---

<span id="class_EditorPlugin_method_remove_undo_redo_inspector_hook_callback"></span>

void **remove_undo_redo_inspector_hook_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_remove_undo_redo_inspector_hook_callback)

Removes a callback previously added by [add_undo_redo_inspector_hook_callback()](class_editorplugin.md#class_EditorPlugin_method_add_undo_redo_inspector_hook_callback).

---

<span id="class_EditorPlugin_method_set_dock_tab_icon"></span>

void **set_dock_tab_icon** ( control: [Control](class_control.md#class_Control), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_editorplugin.md#class_EditorPlugin_method_set_dock_tab_icon)

**Deprecated:** Use [EditorDock.dock_icon](class_editordock.md#class_EditorDock_property_dock_icon) instead.

Sets the tab icon for the given control in a dock slot. Setting to `null` removes the icon.

---

<span id="class_EditorPlugin_method_set_force_draw_over_forwarding_enabled"></span>

void **set_force_draw_over_forwarding_enabled** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_set_force_draw_over_forwarding_enabled)

Enables calling of [_forward_canvas_force_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport) for the 2D editor and [_forward_3d_force_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport) for the 3D editor when their viewports are updated. You need to call this method only once and it will work permanently for this plugin.

---

<span id="class_EditorPlugin_method_set_input_event_forwarding_always_enabled"></span>

void **set_input_event_forwarding_always_enabled** ( ) [🔗](class_editorplugin.md#class_EditorPlugin_method_set_input_event_forwarding_always_enabled)

Use this method if you always want to receive inputs from 3D view screen inside [_forward_3d_gui_input()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_gui_input). It might be especially usable if your plugin will want to use raycast in the scene.

---

<span id="class_EditorPlugin_method_update_overlays"></span>

[int](class_int.md#class_int) **update_overlays** ( ) *const* [🔗](class_editorplugin.md#class_EditorPlugin_method_update_overlays)

Updates the overlays of the 2D and 3D editor viewport. Causes methods [_forward_canvas_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_draw_over_viewport), [_forward_canvas_force_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport), [_forward_3d_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_draw_over_viewport) and [_forward_3d_force_draw_over_viewport()](class_editorplugin.md#class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport) to be called.
