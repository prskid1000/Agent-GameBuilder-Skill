<span id="class_StyleBox"></span>

## StyleBox

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty), [StyleBoxFlat](class_styleboxflat.md#class_StyleBoxFlat), [StyleBoxLine](class_styleboxline.md#class_StyleBoxLine), [StyleBoxTexture](class_styleboxtexture.md#class_StyleBoxTexture)

Abstract base class for defining stylized boxes for UI elements.

### Description

**StyleBox** is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, [LineEdit](class_lineedit.md#class_LineEdit) backgrounds, [Tree](class_tree.md#class_Tree) backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a **StyleBox** assigned as mask to a control, clicks and motion signals will go through it to the one below.

 **Note:** For control nodes that have *Theme Properties*, the `focus` **StyleBox** is displayed over the `normal`, `hover` or `pressed` **StyleBox**. This makes the `focus` **StyleBox** more reusable across different nodes.

### Properties


| [float](class_float.md#class_float) | [content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom) | `-1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [content_margin_left](class_stylebox.md#class_StyleBox_property_content_margin_left) | `-1.0` |
| [float](class_float.md#class_float) | [content_margin_right](class_stylebox.md#class_StyleBox_property_content_margin_right) | `-1.0` |
| [float](class_float.md#class_float) | [content_margin_top](class_stylebox.md#class_StyleBox_property_content_margin_top) | `-1.0` |

### Methods


| void | [_draw](class_stylebox.md#class_StyleBox_private_method__draw) ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [Rect2](class_rect2.md#class_Rect2) | [_get_draw_rect](class_stylebox.md#class_StyleBox_private_method__get_draw_rect) ( rect: [Rect2](class_rect2.md#class_Rect2) ) | virtual | const |
| [Vector2](class_vector2.md#class_Vector2) | [_get_minimum_size](class_stylebox.md#class_StyleBox_private_method__get_minimum_size) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_test_mask](class_stylebox.md#class_StyleBox_private_method__test_mask) ( point: [Vector2](class_vector2.md#class_Vector2), rect: [Rect2](class_rect2.md#class_Rect2) ) | virtual | const |
| void | [draw](class_stylebox.md#class_StyleBox_method_draw) ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) ) const |
| [float](class_float.md#class_float) | [get_content_margin](class_stylebox.md#class_StyleBox_method_get_content_margin) ( margin: Side ) const |
| [CanvasItem](class_canvasitem.md#class_CanvasItem) | [get_current_item_drawn](class_stylebox.md#class_StyleBox_method_get_current_item_drawn) ( ) const |
| [float](class_float.md#class_float) | [get_margin](class_stylebox.md#class_StyleBox_method_get_margin) ( margin: Side ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_minimum_size](class_stylebox.md#class_StyleBox_method_get_minimum_size) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_offset](class_stylebox.md#class_StyleBox_method_get_offset) ( ) const |
| void | [set_content_margin](class_stylebox.md#class_StyleBox_method_set_content_margin) ( margin: Side, offset: [float](class_float.md#class_float) ) |
| void | [set_content_margin_all](class_stylebox.md#class_StyleBox_method_set_content_margin_all) ( offset: [float](class_float.md#class_float) ) |
| [bool](class_bool.md#class_bool) | [test_mask](class_stylebox.md#class_StyleBox_method_test_mask) ( point: [Vector2](class_vector2.md#class_Vector2), rect: [Rect2](class_rect2.md#class_Rect2) ) const |

---

### Property Descriptions

<span id="class_StyleBox_property_content_margin_bottom"></span>

[float](class_float.md#class_float) **content_margin_bottom** = `-1.0` [🔗](class_stylebox.md#class_StyleBox_property_content_margin_bottom)

- void **set_content_margin** ( margin: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_content_margin** ( margin: Side ) *const*

The bottom margin for the contents of this style box. Increasing this value reduces the space available to the contents from the bottom.

If this value is negative, it is ignored and a child-specific margin is used instead. For example, for [StyleBoxFlat](class_styleboxflat.md#class_StyleBoxFlat), the border thickness (if any) is used instead.

It is up to the code using this style box to decide what these contents are: for example, a [Button](class_button.md#class_Button) respects this content margin for the textual contents of the button.

 [get_margin()](class_stylebox.md#class_StyleBox_method_get_margin) should be used to fetch this value as consumer instead of reading these properties directly. This is because it correctly respects negative values and the fallback mentioned above.

---

<span id="class_StyleBox_property_content_margin_left"></span>

[float](class_float.md#class_float) **content_margin_left** = `-1.0` [🔗](class_stylebox.md#class_StyleBox_property_content_margin_left)

- void **set_content_margin** ( margin: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_content_margin** ( margin: Side ) *const*

The left margin for the contents of this style box. Increasing this value reduces the space available to the contents from the left.

Refer to [content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom) for extra considerations.

---

<span id="class_StyleBox_property_content_margin_right"></span>

[float](class_float.md#class_float) **content_margin_right** = `-1.0` [🔗](class_stylebox.md#class_StyleBox_property_content_margin_right)

- void **set_content_margin** ( margin: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_content_margin** ( margin: Side ) *const*

The right margin for the contents of this style box. Increasing this value reduces the space available to the contents from the right.

Refer to [content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom) for extra considerations.

---

<span id="class_StyleBox_property_content_margin_top"></span>

[float](class_float.md#class_float) **content_margin_top** = `-1.0` [🔗](class_stylebox.md#class_StyleBox_property_content_margin_top)

- void **set_content_margin** ( margin: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_content_margin** ( margin: Side ) *const*

The top margin for the contents of this style box. Increasing this value reduces the space available to the contents from the top.

Refer to [content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom) for extra considerations.

---

### Method Descriptions

<span id="class_StyleBox_private_method__draw"></span>

void **_draw** ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) ) *virtual* |required| *const* [🔗](class_stylebox.md#class_StyleBox_private_method__draw)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_StyleBox_private_method__get_draw_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **_get_draw_rect** ( rect: [Rect2](class_rect2.md#class_Rect2) ) *virtual* *const* [🔗](class_stylebox.md#class_StyleBox_private_method__get_draw_rect)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_StyleBox_private_method__get_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_get_minimum_size** ( ) *virtual* *const* [🔗](class_stylebox.md#class_StyleBox_private_method__get_minimum_size)

Virtual method to be implemented by the user. Returns a custom minimum size that the stylebox must respect when drawing. By default [get_minimum_size()](class_stylebox.md#class_StyleBox_method_get_minimum_size) only takes content margins into account. This method can be overridden to add another size restriction. A combination of the default behavior and the output of this method will be used, to account for both sizes.

---

<span id="class_StyleBox_private_method__test_mask"></span>

[bool](class_bool.md#class_bool) **_test_mask** ( point: [Vector2](class_vector2.md#class_Vector2), rect: [Rect2](class_rect2.md#class_Rect2) ) *virtual* *const* [🔗](class_stylebox.md#class_StyleBox_private_method__test_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_StyleBox_method_draw"></span>

void **draw** ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_stylebox.md#class_StyleBox_method_draw)

Draws this stylebox using a canvas item identified by the given [RID](class_rid.md#class_RID).

The [RID](class_rid.md#class_RID) value can either be the result of [CanvasItem.get_canvas_item()](class_canvasitem.md#class_CanvasItem_method_get_canvas_item) called on an existing [CanvasItem](class_canvasitem.md#class_CanvasItem)-derived node, or directly from creating a canvas item in the [RenderingServer](class_renderingserver.md#class_RenderingServer) with [RenderingServer.canvas_item_create()](class_renderingserver.md#class_RenderingServer_method_canvas_item_create).

---

<span id="class_StyleBox_method_get_content_margin"></span>

[float](class_float.md#class_float) **get_content_margin** ( margin: Side ) *const* [🔗](class_stylebox.md#class_StyleBox_method_get_content_margin)

Returns the default margin of the specified Side.

---

<span id="class_StyleBox_method_get_current_item_drawn"></span>

[CanvasItem](class_canvasitem.md#class_CanvasItem) **get_current_item_drawn** ( ) *const* [🔗](class_stylebox.md#class_StyleBox_method_get_current_item_drawn)

Returns the [CanvasItem](class_canvasitem.md#class_CanvasItem) that handles its [CanvasItem.NOTIFICATION_DRAW](class_canvasitem.md#class_CanvasItem_constant_NOTIFICATION_DRAW) or [CanvasItem._draw()](class_canvasitem.md#class_CanvasItem_private_method__draw) callback at this moment.

---

<span id="class_StyleBox_method_get_margin"></span>

[float](class_float.md#class_float) **get_margin** ( margin: Side ) *const* [🔗](class_stylebox.md#class_StyleBox_method_get_margin)

Returns the content margin offset for the specified Side.

Positive values reduce size inwards, unlike [Control](class_control.md#class_Control)'s margin values.

---

<span id="class_StyleBox_method_get_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_minimum_size** ( ) *const* [🔗](class_stylebox.md#class_StyleBox_method_get_minimum_size)

Returns the minimum size that this stylebox can be shrunk to.

---

<span id="class_StyleBox_method_get_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **get_offset** ( ) *const* [🔗](class_stylebox.md#class_StyleBox_method_get_offset)

Returns the "offset" of a stylebox. This helper function returns a value equivalent to `Vector2(style.get_margin(MARGIN_LEFT), style.get_margin(MARGIN_TOP))`.

---

<span id="class_StyleBox_method_set_content_margin"></span>

void **set_content_margin** ( margin: Side, offset: [float](class_float.md#class_float) ) [🔗](class_stylebox.md#class_StyleBox_method_set_content_margin)

Sets the default value of the specified Side to `offset` pixels.

---

<span id="class_StyleBox_method_set_content_margin_all"></span>

void **set_content_margin_all** ( offset: [float](class_float.md#class_float) ) [🔗](class_stylebox.md#class_StyleBox_method_set_content_margin_all)

Sets the default margin to `offset` pixels for all sides.

---

<span id="class_StyleBox_method_test_mask"></span>

[bool](class_bool.md#class_bool) **test_mask** ( point: [Vector2](class_vector2.md#class_Vector2), rect: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_stylebox.md#class_StyleBox_method_test_mask)

Test a position in a rectangle, return whether it passes the mask test.
