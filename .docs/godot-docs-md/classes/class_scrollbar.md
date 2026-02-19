<span id="class_ScrollBar"></span>

## ScrollBar

**Inherits:** [Range](class_range.md#class_Range) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HScrollBar](class_hscrollbar.md#class_HScrollBar), [VScrollBar](class_vscrollbar.md#class_VScrollBar)

Abstract base class for scrollbars.

### Description

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are [Range](class_range.md#class_Range)-based controls.

### Properties


| [float](class_float.md#class_float) | [custom_step](class_scrollbar.md#class_ScrollBar_property_custom_step) | `-1.0` |
| --- | --- | --- |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [float](class_float.md#class_float) | step | `0.0` (overrides [Range](class_range.md#class_Range_property_step)) |

### Theme Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement](class_scrollbar.md#class_ScrollBar_theme_icon_decrement) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement_highlight](class_scrollbar.md#class_ScrollBar_theme_icon_decrement_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement_pressed](class_scrollbar.md#class_ScrollBar_theme_icon_decrement_pressed) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment](class_scrollbar.md#class_ScrollBar_theme_icon_increment) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment_highlight](class_scrollbar.md#class_ScrollBar_theme_icon_increment_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment_pressed](class_scrollbar.md#class_ScrollBar_theme_icon_increment_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [grabber](class_scrollbar.md#class_ScrollBar_theme_style_grabber) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [grabber_highlight](class_scrollbar.md#class_ScrollBar_theme_style_grabber_highlight) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [grabber_pressed](class_scrollbar.md#class_ScrollBar_theme_style_grabber_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [scroll](class_scrollbar.md#class_ScrollBar_theme_style_scroll) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [scroll_focus](class_scrollbar.md#class_ScrollBar_theme_style_scroll_focus) |

---

### Signals

<span id="class_ScrollBar_signal_scrolling"></span>

**scrolling** ( ) [🔗](class_scrollbar.md#class_ScrollBar_signal_scrolling)

Emitted when the scrollbar is being scrolled.

---

### Property Descriptions

<span id="class_ScrollBar_property_custom_step"></span>

[float](class_float.md#class_float) **custom_step** = `-1.0` [🔗](class_scrollbar.md#class_ScrollBar_property_custom_step)

- void **set_custom_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_custom_step** ( )

Overrides the step used when clicking increment and decrement buttons or when using arrow keys when the **ScrollBar** is focused.

---

### Theme Property Descriptions

<span id="class_ScrollBar_theme_icon_decrement"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_decrement)

Icon used as a button to scroll the **ScrollBar** left/up. Supports custom step using the [custom_step](class_scrollbar.md#class_ScrollBar_property_custom_step) property.

---

<span id="class_ScrollBar_theme_icon_decrement_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement_highlight** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_decrement_highlight)

Displayed when the mouse cursor hovers over the decrement button.

---

<span id="class_ScrollBar_theme_icon_decrement_pressed"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement_pressed** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_decrement_pressed)

Displayed when the decrement button is being pressed.

---

<span id="class_ScrollBar_theme_icon_increment"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_increment)

Icon used as a button to scroll the **ScrollBar** right/down. Supports custom step using the [custom_step](class_scrollbar.md#class_ScrollBar_property_custom_step) property.

---

<span id="class_ScrollBar_theme_icon_increment_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment_highlight** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_increment_highlight)

Displayed when the mouse cursor hovers over the increment button.

---

<span id="class_ScrollBar_theme_icon_increment_pressed"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment_pressed** [🔗](class_scrollbar.md#class_ScrollBar_theme_icon_increment_pressed)

Displayed when the increment button is being pressed.

---

<span id="class_ScrollBar_theme_style_grabber"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **grabber** [🔗](class_scrollbar.md#class_ScrollBar_theme_style_grabber)

Used as texture for the grabber, the draggable element representing current scroll.

---

<span id="class_ScrollBar_theme_style_grabber_highlight"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **grabber_highlight** [🔗](class_scrollbar.md#class_ScrollBar_theme_style_grabber_highlight)

Used when the mouse hovers over the grabber.

---

<span id="class_ScrollBar_theme_style_grabber_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **grabber_pressed** [🔗](class_scrollbar.md#class_ScrollBar_theme_style_grabber_pressed)

Used when the grabber is being dragged.

---

<span id="class_ScrollBar_theme_style_scroll"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **scroll** [🔗](class_scrollbar.md#class_ScrollBar_theme_style_scroll)

Used as background of this **ScrollBar**.

---

<span id="class_ScrollBar_theme_style_scroll_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **scroll_focus** [🔗](class_scrollbar.md#class_ScrollBar_theme_style_scroll_focus)

Used as background when the **ScrollBar** has the GUI focus.
