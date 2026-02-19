<span id="class_CanvasLayer"></span>

## CanvasLayer

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ParallaxBackground](class_parallaxbackground.md#class_ParallaxBackground)

A node used for independent rendering of objects within a 2D scene.

### Description

[CanvasItem](class_canvasitem.md#class_CanvasItem)-derived nodes that are direct or indirect children of a **CanvasLayer** will be drawn in that layer. The layer is a numeric index that defines the draw order. The default 2D scene renders with index `0`, so a **CanvasLayer** with index `-1` will be drawn below, and a **CanvasLayer** with index `1` will be drawn above. This order will hold regardless of the [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) of the nodes within each layer.

 **CanvasLayer** s can be hidden and they can also optionally follow the viewport. This makes them useful for HUDs like health bar overlays (on layers `1` and higher) or backgrounds (on layers `-1` and lower).

 **Note:** Embedded [Window](class_window.md#class_Window) s are placed on layer `1024`. [CanvasItem](class_canvasitem.md#class_CanvasItem) s on layers `1025` and higher appear in front of embedded windows.

 **Note:** Each **CanvasLayer** is drawn on one specific [Viewport](class_viewport.md#class_Viewport) and cannot be shared between multiple [Viewport](class_viewport.md#class_Viewport) s, see [custom_viewport](class_canvaslayer.md#class_CanvasLayer_property_custom_viewport). When using multiple [Viewport](class_viewport.md#class_Viewport) s, for example in a split-screen game, you need to create an individual **CanvasLayer** for each [Viewport](class_viewport.md#class_Viewport) you want it to be drawn on.

### Tutorials

- [Viewport and canvas transforms](../tutorials/2d/2d_transforms.md)

- [Canvas layers](../tutorials/2d/canvas_layers.md)

- 2D Dodge The Creeps Demo

### Properties


| [Node](class_node.md#class_Node) | [custom_viewport](class_canvaslayer.md#class_CanvasLayer_property_custom_viewport) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [follow_viewport_enabled](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_enabled) | `false` |
| [float](class_float.md#class_float) | [follow_viewport_scale](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_scale) | `1.0` |
| [int](class_int.md#class_int) | [layer](class_canvaslayer.md#class_CanvasLayer_property_layer) | `1` |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_canvaslayer.md#class_CanvasLayer_property_offset) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [rotation](class_canvaslayer.md#class_CanvasLayer_property_rotation) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [scale](class_canvaslayer.md#class_CanvasLayer_property_scale) | `Vector2(1, 1)` |
| [Transform2D](class_transform2d.md#class_Transform2D) | [transform](class_canvaslayer.md#class_CanvasLayer_property_transform) | `Transform2D(1, 0, 0, 1, 0, 0)` |
| [bool](class_bool.md#class_bool) | [visible](class_canvaslayer.md#class_CanvasLayer_property_visible) | `true` |

### Methods


| [RID](class_rid.md#class_RID) | [get_canvas](class_canvaslayer.md#class_CanvasLayer_method_get_canvas) ( ) const |
| --- | --- |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_final_transform](class_canvaslayer.md#class_CanvasLayer_method_get_final_transform) ( ) const |
| void | [hide](class_canvaslayer.md#class_CanvasLayer_method_hide) ( ) |
| void | [show](class_canvaslayer.md#class_CanvasLayer_method_show) ( ) |

---

### Signals

<span id="class_CanvasLayer_signal_visibility_changed"></span>

**visibility_changed** ( ) [🔗](class_canvaslayer.md#class_CanvasLayer_signal_visibility_changed)

Emitted when visibility of the layer is changed. See [visible](class_canvaslayer.md#class_CanvasLayer_property_visible).

---

### Property Descriptions

<span id="class_CanvasLayer_property_custom_viewport"></span>

[Node](class_node.md#class_Node) **custom_viewport** [🔗](class_canvaslayer.md#class_CanvasLayer_property_custom_viewport)

- void **set_custom_viewport** ( value: [Node](class_node.md#class_Node) )
- [Node](class_node.md#class_Node) **get_custom_viewport** ( )

The custom [Viewport](class_viewport.md#class_Viewport) node assigned to the **CanvasLayer**. If `null`, uses the default viewport instead.

---

<span id="class_CanvasLayer_property_follow_viewport_enabled"></span>

[bool](class_bool.md#class_bool) **follow_viewport_enabled** = `false` [🔗](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_enabled)

- void **set_follow_viewport** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_following_viewport** ( )

If enabled, the **CanvasLayer** maintains its position in world space. If disabled, the **CanvasLayer** stays in a fixed position on the screen.

Together with [follow_viewport_scale](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_scale), this can be used for a pseudo-3D effect.

---

<span id="class_CanvasLayer_property_follow_viewport_scale"></span>

[float](class_float.md#class_float) **follow_viewport_scale** = `1.0` [🔗](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_scale)

- void **set_follow_viewport_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_follow_viewport_scale** ( )

Scales the layer when using [follow_viewport_enabled](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_enabled). Layers moving into the foreground should have increasing scales, while layers moving into the background should have decreasing scales.

---

<span id="class_CanvasLayer_property_layer"></span>

[int](class_int.md#class_int) **layer** = `1` [🔗](class_canvaslayer.md#class_CanvasLayer_property_layer)

- void **set_layer** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_layer** ( )

Layer index for draw order. Lower values are drawn behind higher values.

 **Note:** If multiple CanvasLayers have the same layer index, [CanvasItem](class_canvasitem.md#class_CanvasItem) children of one CanvasLayer are drawn behind the [CanvasItem](class_canvasitem.md#class_CanvasItem) children of the other CanvasLayer. Which CanvasLayer is drawn in front is non-deterministic.

 **Note:** The layer index should be between [RenderingServer.CANVAS_LAYER_MIN](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MIN) and [RenderingServer.CANVAS_LAYER_MAX](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MAX) (inclusive). Any other value will wrap around.

---

<span id="class_CanvasLayer_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_canvaslayer.md#class_CanvasLayer_property_offset)

- void **set_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_offset** ( )

The layer's base offset.

---

<span id="class_CanvasLayer_property_rotation"></span>

[float](class_float.md#class_float) **rotation** = `0.0` [🔗](class_canvaslayer.md#class_CanvasLayer_property_rotation)

- void **set_rotation** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rotation** ( )

The layer's rotation in radians.

---

<span id="class_CanvasLayer_property_scale"></span>

[Vector2](class_vector2.md#class_Vector2) **scale** = `Vector2(1, 1)` [🔗](class_canvaslayer.md#class_CanvasLayer_property_scale)

- void **set_scale** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_scale** ( )

The layer's scale.

---

<span id="class_CanvasLayer_property_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **transform** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗](class_canvaslayer.md#class_CanvasLayer_property_transform)

- void **set_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_transform** ( )

The layer's transform.

---

<span id="class_CanvasLayer_property_visible"></span>

[bool](class_bool.md#class_bool) **visible** = `true` [🔗](class_canvaslayer.md#class_CanvasLayer_property_visible)

- void **set_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_visible** ( )

If `false`, any [CanvasItem](class_canvasitem.md#class_CanvasItem) under this **CanvasLayer** will be hidden.

Unlike [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible), visibility of a **CanvasLayer** isn't propagated to underlying layers.

---

### Method Descriptions

<span id="class_CanvasLayer_method_get_canvas"></span>

[RID](class_rid.md#class_RID) **get_canvas** ( ) *const* [🔗](class_canvaslayer.md#class_CanvasLayer_method_get_canvas)

Returns the RID of the canvas used by this layer.

---

<span id="class_CanvasLayer_method_get_final_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_final_transform** ( ) *const* [🔗](class_canvaslayer.md#class_CanvasLayer_method_get_final_transform)

Returns the transform from the **CanvasLayer** s coordinate system to the [Viewport](class_viewport.md#class_Viewport) s coordinate system.

---

<span id="class_CanvasLayer_method_hide"></span>

void **hide** ( ) [🔗](class_canvaslayer.md#class_CanvasLayer_method_hide)

Hides any [CanvasItem](class_canvasitem.md#class_CanvasItem) under this **CanvasLayer**. This is equivalent to setting [visible](class_canvaslayer.md#class_CanvasLayer_property_visible) to `false`.

---

<span id="class_CanvasLayer_method_show"></span>

void **show** ( ) [🔗](class_canvaslayer.md#class_CanvasLayer_method_show)

Shows any [CanvasItem](class_canvasitem.md#class_CanvasItem) under this **CanvasLayer**. This is equivalent to setting [visible](class_canvaslayer.md#class_CanvasLayer_property_visible) to `true`.
