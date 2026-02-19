<span id="class_EditorContextMenuPlugin"></span>

## EditorContextMenuPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plugin for adding custom context menus in the editor.

### Description

**EditorContextMenuPlugin** allows for the addition of custom options in the editor's context menu.

Currently, context menus are supported for three commonly used areas: the file system, scene tree, and editor script list panel.

### Methods


| void | [_popup_menu](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) ( paths: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) virtual |
| --- | --- |
| void | [add_context_menu_item](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item) ( name: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) |
| void | [add_context_menu_item_from_shortcut](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut) ( name: [String](class_string.md#class_String), shortcut: [Shortcut](class_shortcut.md#class_Shortcut), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) |
| void | [add_context_submenu_item](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_submenu_item) ( name: [String](class_string.md#class_String), menu: [PopupMenu](class_popupmenu.md#class_PopupMenu), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) |
| void | [add_menu_shortcut](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_menu_shortcut) ( shortcut: [Shortcut](class_shortcut.md#class_Shortcut), callback: [Callable](class_callable.md#class_Callable) ) |

---

### Enumerations

<span id="enum_EditorContextMenuPlugin_ContextMenuSlot"></span>

enum **ContextMenuSlot**: [🔗](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot)

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_SCENE_TREE"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_SCENE_TREE** = `0`

Context menu of Scene dock. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) will be called with a list of paths to currently selected nodes, while option callback will receive the list of currently selected nodes.

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_FILESYSTEM"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_FILESYSTEM** = `1`

Context menu of FileSystem dock. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) and option callback will be called with list of paths of the currently selected files.

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_SCRIPT_EDITOR"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_SCRIPT_EDITOR** = `2`

Context menu of Script editor's script tabs. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) will be called with the path to the currently edited script, while option callback will receive reference to that script.

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_FILESYSTEM_CREATE"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_FILESYSTEM_CREATE** = `3`

The "Create..." submenu of FileSystem dock's context menu, or the "New" section of the main context menu when empty space is clicked. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) and option callback will be called with the path of the currently selected folder. When clicking the empty space, the list of paths for popup method will be empty.

::

    func _popup_menu(paths):
        if paths.is_empty():
            add_context_menu_item("New Image File...", create_image)
        else:
            add_context_menu_item("Image File...", create_image)

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_SCRIPT_EDITOR_CODE"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_SCRIPT_EDITOR_CODE** = `4`

Context menu of Script editor's code editor. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) will be called with the path to the [CodeEdit](class_codeedit.md#class_CodeEdit) node. You can fetch it using this code:

::

    func _popup_menu(paths):
        var code_edit = Engine.get_main_loop().root.get_node(paths[0]);

The option callback will receive reference to that node. You can use [CodeEdit](class_codeedit.md#class_CodeEdit) methods to perform symbol lookups etc.

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_SCENE_TABS"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_SCENE_TABS** = `5`

Context menu of scene tabs. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) will be called with the path of the clicked scene, or empty [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) if the menu was opened on empty space. The option callback will receive the path of the clicked scene, or empty [String](class_string.md#class_String) if none was clicked.

<span id="class_EditorContextMenuPlugin_constant_CONTEXT_SLOT_2D_EDITOR"></span>

[ContextMenuSlot](class_editorcontextmenuplugin.md#enum_EditorContextMenuPlugin_ContextMenuSlot) **CONTEXT_SLOT_2D_EDITOR** = `6`

Context menu of 2D editor's basic right-click menu. [_popup_menu()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu) will be called with paths to all [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes under the cursor. You can fetch them using this code:

::

    func _popup_menu(paths):
        var canvas_item = Engine.get_main_loop().root.get_node(paths[0]); # Replace 0 with the desired index.

The paths array is empty if there weren't any nodes under cursor. The option callback will receive a typed array of [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes.

---

### Method Descriptions

<span id="class_EditorContextMenuPlugin_private_method__popup_menu"></span>

void **_popup_menu** ( paths: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* [🔗](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_private_method__popup_menu)

Called when creating a context menu, custom options can be added by using the [add_context_menu_item()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item) or [add_context_menu_item_from_shortcut()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut) functions. `paths` contains currently selected paths (depending on menu), which can be used to conditionally add options.

---

<span id="class_EditorContextMenuPlugin_method_add_context_menu_item"></span>

void **add_context_menu_item** ( name: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) [🔗](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item)

Add custom option to the context menu of the plugin's specified slot. When the option is activated, `callback` will be called. Callback should take single [Array](class_array.md#class_Array) argument; array contents depend on context menu slot.

::

    func _popup_menu(paths):
        add_context_menu_item("File Custom options", handle, ICON)

If you want to assign shortcut to the menu item, use [add_context_menu_item_from_shortcut()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut) instead.

---

<span id="class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut"></span>

void **add_context_menu_item_from_shortcut** ( name: [String](class_string.md#class_String), shortcut: [Shortcut](class_shortcut.md#class_Shortcut), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) [🔗](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut)

Add custom option to the context menu of the plugin's specified slot. The option will have the `shortcut` assigned and reuse its callback. The shortcut has to be registered beforehand with [add_menu_shortcut()](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_menu_shortcut).

::

    func _init():
        add_menu_shortcut(SHORTCUT, handle)

    func _popup_menu(paths):
        add_context_menu_item_from_shortcut("File Custom options", SHORTCUT, ICON)

---

<span id="class_EditorContextMenuPlugin_method_add_context_submenu_item"></span>

void **add_context_submenu_item** ( name: [String](class_string.md#class_String), menu: [PopupMenu](class_popupmenu.md#class_PopupMenu), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) [🔗](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_context_submenu_item)

Add a submenu to the context menu of the plugin's specified slot. The submenu is not automatically handled, you need to connect to its signals yourself. Also the submenu is freed on every popup, so provide a new [PopupMenu](class_popupmenu.md#class_PopupMenu) every time.

::

    func _popup_menu(paths):
        var popup_menu = PopupMenu.new()
        popup_menu.add_item("Blue")
        popup_menu.add_item("White")
        popup_menu.id_pressed.connect(_on_color_submenu_option)

        add_context_submenu_item("Set Node Color", popup_menu)

---

<span id="class_EditorContextMenuPlugin_method_add_menu_shortcut"></span>

void **add_menu_shortcut** ( shortcut: [Shortcut](class_shortcut.md#class_Shortcut), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_editorcontextmenuplugin.md#class_EditorContextMenuPlugin_method_add_menu_shortcut)

Registers a shortcut associated with the plugin's context menu. This method should be called once (e.g. in plugin's [Object._init()](class_object.md#class_Object_private_method__init)). `callback` will be called when user presses the specified `shortcut` while the menu's context is in effect (e.g. FileSystem dock is focused). Callback should take single [Array](class_array.md#class_Array) argument; array contents depend on context menu slot.

::

    func _init():
        add_menu_shortcut(SHORTCUT, handle)
