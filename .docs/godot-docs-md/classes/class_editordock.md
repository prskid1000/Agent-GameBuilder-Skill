<span id="class_EditorDock"></span>

## EditorDock

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [MarginContainer](class_margincontainer.md#class_MarginContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [FileSystemDock](class_filesystemdock.md#class_FileSystemDock)

Dockable container for the editor.

### Description

EditorDock is a [Container](class_container.md#class_Container) node that can be docked in one of the editor's dock slots. Docks are added by plugins to provide space for controls related to an [EditorPlugin](class_editorplugin.md#class_EditorPlugin). The editor comes with a few built-in docks, such as the Scene dock, FileSystem dock, etc.

You can add a dock by using [EditorPlugin.add_dock()](class_editorplugin.md#class_EditorPlugin_method_add_dock). The dock can be customized by changing its properties.

::

    @tool
    extends EditorPlugin

    # Dock reference.
    var dock

    # Plugin initialization.
    func _enter_tree():
        dock = EditorDock.new()
        dock.title = "My Dock"
        dock.dock_icon = preload("./dock_icon.png")
        dock.default_slot = EditorDock.DOCK_SLOT_RIGHT_UL
        var dock_content = preload("./dock_content.tscn").instantiate()
        dock.add_child(dock_content)
        add_dock(dock)

    # Plugin clean-up.
    func _exit_tree():
        remove_dock(dock)
        dock.queue_free()
        dock = null

### Tutorials

- [Making plugins](../tutorials/plugins/editor/making_plugins.md)

### Properties


| bitfield | \[[DockLayout](class_editordock.md#enum_EditorDock_DockLayout)\] | [available_layouts](class_editordock.md#class_EditorDock_property_available_layouts) | `5` |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [closable](class_editordock.md#class_EditorDock_property_closable) | `false` |
| [DockSlot](class_editordock.md#enum_EditorDock_DockSlot) | [default_slot](class_editordock.md#class_EditorDock_property_default_slot) | `-1` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [dock_icon](class_editordock.md#class_EditorDock_property_dock_icon) |
| [Shortcut](class_shortcut.md#class_Shortcut) | [dock_shortcut](class_editordock.md#class_EditorDock_property_dock_shortcut) |
| [bool](class_bool.md#class_bool) | [force_show_icon](class_editordock.md#class_EditorDock_property_force_show_icon) | `false` |
| [bool](class_bool.md#class_bool) | [global](class_editordock.md#class_EditorDock_property_global) | `true` |
| [StringName](class_stringname.md#class_StringName) | [icon_name](class_editordock.md#class_EditorDock_property_icon_name) | `&""` |
| [String](class_string.md#class_String) | [layout_key](class_editordock.md#class_EditorDock_property_layout_key) | `""` |
| [String](class_string.md#class_String) | [title](class_editordock.md#class_EditorDock_property_title) | `""` |
| [Color](class_color.md#class_Color) | [title_color](class_editordock.md#class_EditorDock_property_title_color) | `Color(0, 0, 0, 0)` |
| [bool](class_bool.md#class_bool) | [transient](class_editordock.md#class_EditorDock_property_transient) | `false` |

### Methods


| void | [_load_layout_from_config](class_editordock.md#class_EditorDock_private_method__load_layout_from_config) ( config: [ConfigFile](class_configfile.md#class_ConfigFile), section: [String](class_string.md#class_String) ) virtual |
| --- | --- |
| void | [_save_layout_to_config](class_editordock.md#class_EditorDock_private_method__save_layout_to_config) ( config: [ConfigFile](class_configfile.md#class_ConfigFile), section: [String](class_string.md#class_String) ) | virtual | const |
| void | [_update_layout](class_editordock.md#class_EditorDock_private_method__update_layout) ( layout: [int](class_int.md#class_int) ) virtual |
| void | [close](class_editordock.md#class_EditorDock_method_close) ( ) |
| void | [make_visible](class_editordock.md#class_EditorDock_method_make_visible) ( ) |
| void | [open](class_editordock.md#class_EditorDock_method_open) ( ) |

---

### Signals

<span id="class_EditorDock_signal_closed"></span>

**closed** ( ) [🔗](class_editordock.md#class_EditorDock_signal_closed)

Emitted when the dock is closed with the Close button in the context popup, before it's removed from its parent. See [closable](class_editordock.md#class_EditorDock_property_closable).

---

<span id="class_EditorDock_signal_opened"></span>

**opened** ( ) [🔗](class_editordock.md#class_EditorDock_signal_opened)

Emitted when the dock is opened via the Editor > Editor Docks menu, before it's made visible.

---

### Enumerations

<span id="enum_EditorDock_DockLayout"></span>

flags **DockLayout**: [🔗](class_editordock.md#enum_EditorDock_DockLayout)

<span id="class_EditorDock_constant_DOCK_LAYOUT_VERTICAL"></span>

[DockLayout](class_editordock.md#enum_EditorDock_DockLayout) **DOCK_LAYOUT_VERTICAL** = `1`

Allows placing the dock in the vertical dock slots on either side of the editor.

<span id="class_EditorDock_constant_DOCK_LAYOUT_HORIZONTAL"></span>

[DockLayout](class_editordock.md#enum_EditorDock_DockLayout) **DOCK_LAYOUT_HORIZONTAL** = `2`

Allows placing the dock in the editor's bottom panel.

<span id="class_EditorDock_constant_DOCK_LAYOUT_FLOATING"></span>

[DockLayout](class_editordock.md#enum_EditorDock_DockLayout) **DOCK_LAYOUT_FLOATING** = `4`

Allows making the dock floating (opened as a separate window).

<span id="class_EditorDock_constant_DOCK_LAYOUT_ALL"></span>

[DockLayout](class_editordock.md#enum_EditorDock_DockLayout) **DOCK_LAYOUT_ALL** = `7`

Allows placing the dock in all available slots.

---

<span id="enum_EditorDock_DockSlot"></span>

enum **DockSlot**: [🔗](class_editordock.md#enum_EditorDock_DockSlot)

<span id="class_EditorDock_constant_DOCK_SLOT_NONE"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_NONE** = `-1`

The dock is closed.

<span id="class_EditorDock_constant_DOCK_SLOT_LEFT_UL"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

<span id="class_EditorDock_constant_DOCK_SLOT_LEFT_BL"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

<span id="class_EditorDock_constant_DOCK_SLOT_LEFT_UR"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).

<span id="class_EditorDock_constant_DOCK_SLOT_LEFT_BR"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem and History docks).

<span id="class_EditorDock_constant_DOCK_SLOT_RIGHT_UL"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Signal, and Group docks).

<span id="class_EditorDock_constant_DOCK_SLOT_RIGHT_BL"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

<span id="class_EditorDock_constant_DOCK_SLOT_RIGHT_UR"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

<span id="class_EditorDock_constant_DOCK_SLOT_RIGHT_BR"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

<span id="class_EditorDock_constant_DOCK_SLOT_BOTTOM"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.

<span id="class_EditorDock_constant_DOCK_SLOT_MAX"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **DOCK_SLOT_MAX** = `9`

Represents the size of the [DockSlot](class_editordock.md#enum_EditorDock_DockSlot) enum.

---

### Property Descriptions

<span id="class_EditorDock_property_available_layouts"></span>

*BitField*\[[DockLayout](class_editordock.md#enum_EditorDock_DockLayout)\] **available_layouts** = `5` [🔗](class_editordock.md#class_EditorDock_property_available_layouts)

- void **set_available_layouts** ( value: *BitField*\[[DockLayout](class_editordock.md#enum_EditorDock_DockLayout)\] )
- *BitField*\[[DockLayout](class_editordock.md#enum_EditorDock_DockLayout)\] **get_available_layouts** ( )

The available layouts for this dock, as a bitmask. By default, the dock allows vertical and floating layouts.

---

<span id="class_EditorDock_property_closable"></span>

[bool](class_bool.md#class_bool) **closable** = `false` [🔗](class_editordock.md#class_EditorDock_property_closable)

- void **set_closable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_closable** ( )

If `true`, the dock can be closed with the Close button in the context popup. Docks with [global](class_editordock.md#class_EditorDock_property_global) enabled are always closable.

---

<span id="class_EditorDock_property_default_slot"></span>

[DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **default_slot** = `-1` [🔗](class_editordock.md#class_EditorDock_property_default_slot)

- void **set_default_slot** ( value: [DockSlot](class_editordock.md#enum_EditorDock_DockSlot) )
- [DockSlot](class_editordock.md#enum_EditorDock_DockSlot) **get_default_slot** ( )

The default dock slot used when adding the dock with [EditorPlugin.add_dock()](class_editorplugin.md#class_EditorPlugin_method_add_dock).

After the dock is added, it can be moved to a different slot and the editor will automatically remember its position between sessions. If you remove and re-add the dock, it will be reset to default.

---

<span id="class_EditorDock_property_dock_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **dock_icon** [🔗](class_editordock.md#class_EditorDock_property_dock_icon)

- void **set_dock_icon** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_dock_icon** ( )

The icon for the dock, as a texture. If specified, it will override [icon_name](class_editordock.md#class_EditorDock_property_icon_name).

---

<span id="class_EditorDock_property_dock_shortcut"></span>

[Shortcut](class_shortcut.md#class_Shortcut) **dock_shortcut** [🔗](class_editordock.md#class_EditorDock_property_dock_shortcut)

- void **set_dock_shortcut** ( value: [Shortcut](class_shortcut.md#class_Shortcut) )
- [Shortcut](class_shortcut.md#class_Shortcut) **get_dock_shortcut** ( )

The shortcut used to open the dock.

---

<span id="class_EditorDock_property_force_show_icon"></span>

[bool](class_bool.md#class_bool) **force_show_icon** = `false` [🔗](class_editordock.md#class_EditorDock_property_force_show_icon)

- void **set_force_show_icon** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_force_show_icon** ( )

If `true`, the dock will always display an icon, regardless of EditorSettings.interface/editor/dock_tab_style or EditorSettings.interface/editor/bottom_dock_tab_style.

---

<span id="class_EditorDock_property_global"></span>

[bool](class_bool.md#class_bool) **global** = `true` [🔗](class_editordock.md#class_EditorDock_property_global)

- void **set_global** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_global** ( )

If `true`, the dock appears in the **Editor > Editor Docks** menu and can be closed. Non-global docks can still be closed using [close()](class_editordock.md#class_EditorDock_method_close) or when [closable](class_editordock.md#class_EditorDock_property_closable) is `true`.

---

<span id="class_EditorDock_property_icon_name"></span>

[StringName](class_stringname.md#class_StringName) **icon_name** = `&""` [🔗](class_editordock.md#class_EditorDock_property_icon_name)

- void **set_icon_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_icon_name** ( )

The icon for the dock, as a name from the `EditorIcons` theme type in the editor theme. You can find the list of available icons here.

---

<span id="class_EditorDock_property_layout_key"></span>

[String](class_string.md#class_String) **layout_key** = `""` [🔗](class_editordock.md#class_EditorDock_property_layout_key)

- void **set_layout_key** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_layout_key** ( )

The key representing this dock in the editor's layout file. If empty, the dock's displayed name will be used instead.

---

<span id="class_EditorDock_property_title"></span>

[String](class_string.md#class_String) **title** = `""` [🔗](class_editordock.md#class_EditorDock_property_title)

- void **set_title** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_title** ( )

The title of the dock's tab. If empty, the dock's [Node.name](class_node.md#class_Node_property_name) will be used. If the name is auto-generated (contains `@`), the first child's name will be used instead.

---

<span id="class_EditorDock_property_title_color"></span>

[Color](class_color.md#class_Color) **title_color** = `Color(0, 0, 0, 0)` [🔗](class_editordock.md#class_EditorDock_property_title_color)

- void **set_title_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_title_color** ( )

The color of the dock tab's title. If its alpha is `0.0`, the default font color will be used.

---

<span id="class_EditorDock_property_transient"></span>

[bool](class_bool.md#class_bool) **transient** = `false` [🔗](class_editordock.md#class_EditorDock_property_transient)

- void **set_transient** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_transient** ( )

If `true`, the dock is not automatically opened or closed when loading an editor layout, only moved. It also can't be opened using a shortcut. This is meant for docks that are opened and closed in specific cases, such as when selecting a [TileMap](class_tilemap.md#class_TileMap) or [AnimationTree](class_animationtree.md#class_AnimationTree) node.

---

### Method Descriptions

<span id="class_EditorDock_private_method__load_layout_from_config"></span>

void **_load_layout_from_config** ( config: [ConfigFile](class_configfile.md#class_ConfigFile), section: [String](class_string.md#class_String) ) *virtual* [🔗](class_editordock.md#class_EditorDock_private_method__load_layout_from_config)

Implement this method to handle loading this dock's layout. It's equivalent to [EditorPlugin._set_window_layout()](class_editorplugin.md#class_EditorPlugin_private_method__set_window_layout). `section` is a unique section based on [layout_key](class_editordock.md#class_EditorDock_property_layout_key).

---

<span id="class_EditorDock_private_method__save_layout_to_config"></span>

void **_save_layout_to_config** ( config: [ConfigFile](class_configfile.md#class_ConfigFile), section: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editordock.md#class_EditorDock_private_method__save_layout_to_config)

Implement this method to handle saving this dock's layout. It's equivalent to [EditorPlugin._get_window_layout()](class_editorplugin.md#class_EditorPlugin_private_method__get_window_layout). `section` is a unique section based on [layout_key](class_editordock.md#class_EditorDock_property_layout_key).

---

<span id="class_EditorDock_private_method__update_layout"></span>

void **_update_layout** ( layout: [int](class_int.md#class_int) ) *virtual* [🔗](class_editordock.md#class_EditorDock_private_method__update_layout)

Implement this method to handle the layout switching for this dock. `layout` is one of the [DockLayout](class_editordock.md#enum_EditorDock_DockLayout) constants.

::

    func _update_layout(layout):
        box_container.vertical = (layout == DOCK_LAYOUT_VERTICAL)

---

<span id="class_EditorDock_method_close"></span>

void **close** ( ) [🔗](class_editordock.md#class_EditorDock_method_close)

Closes the dock, making its tab hidden.

---

<span id="class_EditorDock_method_make_visible"></span>

void **make_visible** ( ) [🔗](class_editordock.md#class_EditorDock_method_make_visible)

Focuses the dock's tab (or window if it's floating). If the dock was closed, it will be opened. If it's a bottom dock, makes the bottom panel visible.

---

<span id="class_EditorDock_method_open"></span>

void **open** ( ) [🔗](class_editordock.md#class_EditorDock_method_open)

Opens the dock. It will appear in the last used dock slot. If the dock has no default slot, it will be opened floating.

 **Note:** This does not focus the dock. If you want to open and focus the dock, use [make_visible()](class_editordock.md#class_EditorDock_method_make_visible).
