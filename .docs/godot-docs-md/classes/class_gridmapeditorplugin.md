.. meta::
	:keywords: tilemap

<span id="class_GridMapEditorPlugin"></span>

## GridMapEditorPlugin

**Inherits:** [EditorPlugin](class_editorplugin.md#class_EditorPlugin) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Editor for [GridMap](class_gridmap.md#class_GridMap) nodes.

### Description

GridMapEditorPlugin provides access to the [GridMap](class_gridmap.md#class_GridMap) editor functionality.

### Methods


| void | [clear_selection](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_clear_selection) ( ) |
| --- | --- |
| [GridMap](class_gridmap.md#class_GridMap) | [get_current_grid_map](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_current_grid_map) ( ) const |
| [Array](class_array.md#class_Array) | [get_selected_cells](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selected_cells) ( ) const |
| [int](class_int.md#class_int) | [get_selected_palette_item](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selected_palette_item) ( ) const |
| [AABB](class_aabb.md#class_AABB) | [get_selection](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selection) ( ) const |
| [bool](class_bool.md#class_bool) | [has_selection](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_has_selection) ( ) const |
| void | [set_selected_palette_item](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_set_selected_palette_item) ( item: [int](class_int.md#class_int) ) const |
| void | [set_selection](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_set_selection) ( begin: [Vector3i](class_vector3i.md#class_Vector3i), end: [Vector3i](class_vector3i.md#class_Vector3i) ) |

---

### Method Descriptions

<span id="class_GridMapEditorPlugin_method_clear_selection"></span>

void **clear_selection** ( ) [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_clear_selection)

Deselects any currently selected cells.

---

<span id="class_GridMapEditorPlugin_method_get_current_grid_map"></span>

[GridMap](class_gridmap.md#class_GridMap) **get_current_grid_map** ( ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_current_grid_map)

Returns the [GridMap](class_gridmap.md#class_GridMap) node currently edited by the grid map editor.

---

<span id="class_GridMapEditorPlugin_method_get_selected_cells"></span>

[Array](class_array.md#class_Array) **get_selected_cells** ( ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selected_cells)

Returns an array of [Vector3i](class_vector3i.md#class_Vector3i) s with the selected cells' coordinates.

---

<span id="class_GridMapEditorPlugin_method_get_selected_palette_item"></span>

[int](class_int.md#class_int) **get_selected_palette_item** ( ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selected_palette_item)

Returns the index of the selected [MeshLibrary](class_meshlibrary.md#class_MeshLibrary) item in the grid map editor's palette or `-1` if no item is selected.

 **Note:** The indices might not be in the same order as they appear in the editor's interface.

---

<span id="class_GridMapEditorPlugin_method_get_selection"></span>

[AABB](class_aabb.md#class_AABB) **get_selection** ( ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_get_selection)

Returns the cell coordinate bounds of the current selection. Use [has_selection()](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_has_selection) to check if there is an active selection.

---

<span id="class_GridMapEditorPlugin_method_has_selection"></span>

[bool](class_bool.md#class_bool) **has_selection** ( ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_has_selection)

Returns `true` if there are selected cells.

---

<span id="class_GridMapEditorPlugin_method_set_selected_palette_item"></span>

void **set_selected_palette_item** ( item: [int](class_int.md#class_int) ) *const* [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_set_selected_palette_item)

Selects the [MeshLibrary](class_meshlibrary.md#class_MeshLibrary) item with the given index in the grid map editor's palette. If a negative index is given, no item will be selected. If a value greater than the last index is given, the last item will be selected.

 **Note:** The indices might not be in the same order as they appear in the editor's interface.

---

<span id="class_GridMapEditorPlugin_method_set_selection"></span>

void **set_selection** ( begin: [Vector3i](class_vector3i.md#class_Vector3i), end: [Vector3i](class_vector3i.md#class_Vector3i) ) [🔗](class_gridmapeditorplugin.md#class_GridMapEditorPlugin_method_set_selection)

Selects the cells inside the given bounds from `begin` to `end`.
