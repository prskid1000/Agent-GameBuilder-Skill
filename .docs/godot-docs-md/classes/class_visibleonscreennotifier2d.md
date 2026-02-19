<span id="class_VisibleOnScreenNotifier2D"></span>

## VisibleOnScreenNotifier2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisibleOnScreenEnabler2D](class_visibleonscreenenabler2d.md#class_VisibleOnScreenEnabler2D)

A rectangular region of 2D space that detects whether it is visible on screen.

### Description

**VisibleOnScreenNotifier2D** represents a rectangular region of 2D space. When any part of this region becomes visible on screen or in a viewport, it will emit a [screen_entered](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_signal_screen_entered) signal, and likewise it will emit a [screen_exited](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_signal_screen_exited) signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use [VisibleOnScreenEnabler2D](class_visibleonscreenenabler2d.md#class_VisibleOnScreenEnabler2D).

 **Note:** **VisibleOnScreenNotifier2D** uses the render culling code to determine whether it's visible on screen, so it won't function unless [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) is set to `true`.

### Tutorials

- 2D Dodge The Creeps Demo

### Properties


| [Rect2](class_rect2.md#class_Rect2) | [rect](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_property_rect) | `Rect2(-10, -10, 20, 20)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [show_rect](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_property_show_rect) | `true` |

### Methods


| [bool](class_bool.md#class_bool) | [is_on_screen](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_method_is_on_screen) ( ) const |
| --- | --- |

---

### Signals

<span id="class_VisibleOnScreenNotifier2D_signal_screen_entered"></span>

**screen_entered** ( ) [🔗](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_signal_screen_entered)

Emitted when the VisibleOnScreenNotifier2D enters the screen.

---

<span id="class_VisibleOnScreenNotifier2D_signal_screen_exited"></span>

**screen_exited** ( ) [🔗](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_signal_screen_exited)

Emitted when the VisibleOnScreenNotifier2D exits the screen.

---

### Property Descriptions

<span id="class_VisibleOnScreenNotifier2D_property_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **rect** = `Rect2(-10, -10, 20, 20)` [🔗](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_property_rect)

- void **set_rect** ( value: [Rect2](class_rect2.md#class_Rect2) )
- [Rect2](class_rect2.md#class_Rect2) **get_rect** ( )

The VisibleOnScreenNotifier2D's bounding rectangle.

---

<span id="class_VisibleOnScreenNotifier2D_property_show_rect"></span>

[bool](class_bool.md#class_bool) **show_rect** = `true` [🔗](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_property_show_rect)

- void **set_show_rect** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_rect** ( )

If `true`, shows the rectangle area of [rect](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_property_rect) in the editor with a translucent magenta fill. Unlike changing the visibility of the VisibleOnScreenNotifier2D, this does not affect the screen culling detection.

---

### Method Descriptions

<span id="class_VisibleOnScreenNotifier2D_method_is_on_screen"></span>

[bool](class_bool.md#class_bool) **is_on_screen** ( ) *const* [🔗](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D_method_is_on_screen)

If `true`, the bounding rectangle is on the screen.

 **Note:** It takes one frame for the **VisibleOnScreenNotifier2D**'s visibility to be determined once added to the scene tree, so this method will always return `false` right after it is instantiated, before the draw pass.
