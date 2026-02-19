<span id="class_TextureRect"></span>

## TextureRect

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control that displays a texture.

### Description

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with the [stretch_mode](class_texturerect.md#class_TextureRect_property_stretch_mode) property. It can scale, tile, or stay centered inside its bounding rectangle.

### Tutorials

- 3D Voxel Demo

### Properties


| [ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) | [expand_mode](class_texturerect.md#class_TextureRect_property_expand_mode) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [flip_h](class_texturerect.md#class_TextureRect_property_flip_h) | `false` |
| [bool](class_bool.md#class_bool) | [flip_v](class_texturerect.md#class_TextureRect_property_flip_v) | `false` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `1` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |
| [StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) | [stretch_mode](class_texturerect.md#class_TextureRect_property_stretch_mode) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_texturerect.md#class_TextureRect_property_texture) |

---

### Enumerations

<span id="enum_TextureRect_ExpandMode"></span>

enum **ExpandMode**: [🔗](class_texturerect.md#enum_TextureRect_ExpandMode)

<span id="class_TextureRect_constant_EXPAND_KEEP_SIZE"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_KEEP_SIZE** = `0`

The minimum size will be equal to texture size, i.e. **TextureRect** can't be smaller than the texture.

<span id="class_TextureRect_constant_EXPAND_IGNORE_SIZE"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_IGNORE_SIZE** = `1`

The size of the texture won't be considered for minimum size calculation, so the **TextureRect** can be shrunk down past the texture size.

<span id="class_TextureRect_constant_EXPAND_FIT_WIDTH"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_FIT_WIDTH** = `2`

The height of the texture will be ignored. Minimum width will be equal to the current height. Useful for horizontal layouts, e.g. inside [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer).

<span id="class_TextureRect_constant_EXPAND_FIT_WIDTH_PROPORTIONAL"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_FIT_WIDTH_PROPORTIONAL** = `3`

Same as [EXPAND_FIT_WIDTH](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_WIDTH), but keeps texture's aspect ratio.

<span id="class_TextureRect_constant_EXPAND_FIT_HEIGHT"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_FIT_HEIGHT** = `4`

The width of the texture will be ignored. Minimum height will be equal to the current width. Useful for vertical layouts, e.g. inside [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer).

<span id="class_TextureRect_constant_EXPAND_FIT_HEIGHT_PROPORTIONAL"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **EXPAND_FIT_HEIGHT_PROPORTIONAL** = `5`

Same as [EXPAND_FIT_HEIGHT](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_HEIGHT), but keeps texture's aspect ratio.

---

<span id="enum_TextureRect_StretchMode"></span>

enum **StretchMode**: [🔗](class_texturerect.md#enum_TextureRect_StretchMode)

<span id="class_TextureRect_constant_STRETCH_SCALE"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.

<span id="class_TextureRect_constant_STRETCH_TILE"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.

<span id="class_TextureRect_constant_STRETCH_KEEP"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.

<span id="class_TextureRect_constant_STRETCH_KEEP_CENTERED"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.

<span id="class_TextureRect_constant_STRETCH_KEEP_ASPECT"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.

<span id="class_TextureRect_constant_STRETCH_KEEP_ASPECT_CENTERED"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it and maintain its aspect ratio.

<span id="class_TextureRect_constant_STRETCH_KEEP_ASPECT_COVERED"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

---

### Property Descriptions

<span id="class_TextureRect_property_expand_mode"></span>

[ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **expand_mode** = `0` [🔗](class_texturerect.md#class_TextureRect_property_expand_mode)

- void **set_expand_mode** ( value: [ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) )
- [ExpandMode](class_texturerect.md#enum_TextureRect_ExpandMode) **get_expand_mode** ( )

**Experimental:** Using [EXPAND_FIT_WIDTH](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_WIDTH), [EXPAND_FIT_WIDTH_PROPORTIONAL](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_WIDTH_PROPORTIONAL), [EXPAND_FIT_HEIGHT](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_HEIGHT), or [EXPAND_FIT_HEIGHT_PROPORTIONAL](class_texturerect.md#class_TextureRect_constant_EXPAND_FIT_HEIGHT_PROPORTIONAL) may result in unstable behavior in some [Container](class_container.md#class_Container) controls. This behavior may be re-evaluated and changed in the future.

Defines how minimum size is determined based on the texture's size.

---

<span id="class_TextureRect_property_flip_h"></span>

[bool](class_bool.md#class_bool) **flip_h** = `false` [🔗](class_texturerect.md#class_TextureRect_property_flip_h)

- void **set_flip_h** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flipped_h** ( )

If `true`, texture is flipped horizontally.

---

<span id="class_TextureRect_property_flip_v"></span>

[bool](class_bool.md#class_bool) **flip_v** = `false` [🔗](class_texturerect.md#class_TextureRect_property_flip_v)

- void **set_flip_v** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flipped_v** ( )

If `true`, texture is flipped vertically.

---

<span id="class_TextureRect_property_stretch_mode"></span>

[StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **stretch_mode** = `0` [🔗](class_texturerect.md#class_TextureRect_property_stretch_mode)

- void **set_stretch_mode** ( value: [StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) )
- [StretchMode](class_texturerect.md#enum_TextureRect_StretchMode) **get_stretch_mode** ( )

Controls the texture's behavior when resizing the node's bounding rectangle.

---

<span id="class_TextureRect_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_texturerect.md#class_TextureRect_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The node's [Texture2D](class_texture2d.md#class_Texture2D) resource.
