<span id="class_TextureButton"></span>

## TextureButton

**Inherits:** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Texture-based button. Supports Pressed, Hover, Disabled and Focused states.

### Description

**TextureButton** has the same functionality as [Button](class_button.md#class_Button), except it uses sprites instead of Godot's [Theme](class_theme.md#class_Theme) resource. It is faster to create, but it doesn't support localization like more complex [Control](class_control.md#class_Control) s.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

 **Note:** Setting a texture for the "normal" state ([texture_normal](class_texturebutton.md#class_TextureButton_property_texture_normal)) is recommended. If [texture_normal](class_texturebutton.md#class_TextureButton_property_texture_normal) is not set, the **TextureButton** will still receive input events and be clickable, but the user will not be able to see it unless they activate another one of its states with a texture assigned (e.g., hover over it to show [texture_hover](class_texturebutton.md#class_TextureButton_property_texture_hover)).

### Tutorials

- 3D Voxel Demo

### Properties


| [bool](class_bool.md#class_bool) | [flip_h](class_texturebutton.md#class_TextureButton_property_flip_h) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [flip_v](class_texturebutton.md#class_TextureButton_property_flip_v) | `false` |
| [bool](class_bool.md#class_bool) | [ignore_texture_size](class_texturebutton.md#class_TextureButton_property_ignore_texture_size) | `false` |
| [StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) | [stretch_mode](class_texturebutton.md#class_TextureButton_property_stretch_mode) | `2` |
| [BitMap](class_bitmap.md#class_BitMap) | [texture_click_mask](class_texturebutton.md#class_TextureButton_property_texture_click_mask) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_disabled](class_texturebutton.md#class_TextureButton_property_texture_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_focused](class_texturebutton.md#class_TextureButton_property_texture_focused) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_hover](class_texturebutton.md#class_TextureButton_property_texture_hover) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_normal](class_texturebutton.md#class_TextureButton_property_texture_normal) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_pressed](class_texturebutton.md#class_TextureButton_property_texture_pressed) |

---

### Enumerations

<span id="enum_TextureButton_StretchMode"></span>

enum **StretchMode**: [🔗](class_texturebutton.md#enum_TextureButton_StretchMode)

<span id="class_TextureButton_constant_STRETCH_SCALE"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.

<span id="class_TextureButton_constant_STRETCH_TILE"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.

<span id="class_TextureButton_constant_STRETCH_KEEP"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.

<span id="class_TextureButton_constant_STRETCH_KEEP_CENTERED"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.

<span id="class_TextureButton_constant_STRETCH_KEEP_ASPECT"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.

<span id="class_TextureButton_constant_STRETCH_KEEP_ASPECT_CENTERED"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it, and maintain its aspect ratio.

<span id="class_TextureButton_constant_STRETCH_KEEP_ASPECT_COVERED"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

---

### Property Descriptions

<span id="class_TextureButton_property_flip_h"></span>

[bool](class_bool.md#class_bool) **flip_h** = `false` [🔗](class_texturebutton.md#class_TextureButton_property_flip_h)

- void **set_flip_h** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flipped_h** ( )

If `true`, texture is flipped horizontally.

---

<span id="class_TextureButton_property_flip_v"></span>

[bool](class_bool.md#class_bool) **flip_v** = `false` [🔗](class_texturebutton.md#class_TextureButton_property_flip_v)

- void **set_flip_v** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flipped_v** ( )

If `true`, texture is flipped vertically.

---

<span id="class_TextureButton_property_ignore_texture_size"></span>

[bool](class_bool.md#class_bool) **ignore_texture_size** = `false` [🔗](class_texturebutton.md#class_TextureButton_property_ignore_texture_size)

- void **set_ignore_texture_size** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_ignore_texture_size** ( )

If `true`, the size of the texture won't be considered for minimum size calculation, so the **TextureButton** can be shrunk down past the texture size.

---

<span id="class_TextureButton_property_stretch_mode"></span>

[StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **stretch_mode** = `2` [🔗](class_texturebutton.md#class_TextureButton_property_stretch_mode)

- void **set_stretch_mode** ( value: [StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) )
- [StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) **get_stretch_mode** ( )

Controls the texture's behavior when you resize the node's bounding rectangle. See the [StretchMode](class_texturebutton.md#enum_TextureButton_StretchMode) constants for available options.

---

<span id="class_TextureButton_property_texture_click_mask"></span>

[BitMap](class_bitmap.md#class_BitMap) **texture_click_mask** [🔗](class_texturebutton.md#class_TextureButton_property_texture_click_mask)

- void **set_click_mask** ( value: [BitMap](class_bitmap.md#class_BitMap) )
- [BitMap](class_bitmap.md#class_BitMap) **get_click_mask** ( )

Pure black and white [BitMap](class_bitmap.md#class_BitMap) image to use for click detection. On the mask, white pixels represent the button's clickable area. Use it to create buttons with curved shapes.

---

<span id="class_TextureButton_property_texture_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_disabled** [🔗](class_texturebutton.md#class_TextureButton_property_texture_disabled)

- void **set_texture_disabled** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_disabled** ( )

Texture to display when the node is disabled. See [BaseButton.disabled](class_basebutton.md#class_BaseButton_property_disabled). If not assigned, the **TextureButton** displays [texture_normal](class_texturebutton.md#class_TextureButton_property_texture_normal) instead.

---

<span id="class_TextureButton_property_texture_focused"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_focused** [🔗](class_texturebutton.md#class_TextureButton_property_texture_focused)

- void **set_texture_focused** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_focused** ( )

Texture to *overlay on the base texture* when the node has mouse or keyboard focus. Because [texture_focused](class_texturebutton.md#class_TextureButton_property_texture_focused) is displayed on top of the base texture, a partially transparent texture should be used to ensure the base texture remains visible. A texture that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a fully transparent texture of any size. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_TextureButton_property_texture_hover"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_hover** [🔗](class_texturebutton.md#class_TextureButton_property_texture_hover)

- void **set_texture_hover** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_hover** ( )

Texture to display when the mouse hovers over the node. If not assigned, the **TextureButton** displays [texture_normal](class_texturebutton.md#class_TextureButton_property_texture_normal) instead when hovered over.

---

<span id="class_TextureButton_property_texture_normal"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_normal** [🔗](class_texturebutton.md#class_TextureButton_property_texture_normal)

- void **set_texture_normal** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_normal** ( )

Texture to display by default, when the node is **not** in the disabled, hover or pressed state. This texture is still displayed in the focused state, with [texture_focused](class_texturebutton.md#class_TextureButton_property_texture_focused) drawn on top.

---

<span id="class_TextureButton_property_texture_pressed"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_pressed** [🔗](class_texturebutton.md#class_TextureButton_property_texture_pressed)

- void **set_texture_pressed** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_pressed** ( )

Texture to display on mouse down over the node, if the node has keyboard focus and the player presses the Enter key or if the player presses the [BaseButton.shortcut](class_basebutton.md#class_BaseButton_property_shortcut) key. If not assigned, the **TextureButton** displays [texture_hover](class_texturebutton.md#class_TextureButton_property_texture_hover) instead when pressed.
