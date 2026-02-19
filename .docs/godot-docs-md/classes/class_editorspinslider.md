<span id="class_EditorSpinSlider"></span>

## EditorSpinSlider

**Inherits:** [Range](class_range.md#class_Range) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's control for editing numeric values.

### Description

This [Control](class_control.md#class_Control) node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class_EditorInspectorPlugin) to recreate the same behavior.

If the [Range.step](class_range.md#class_Range_property_step) value is `1`, the **EditorSpinSlider** will display up/down arrows, similar to [SpinBox](class_spinbox.md#class_SpinBox). If the [Range.step](class_range.md#class_Range_property_step) value is not `1`, a slider will be displayed instead.

### Properties


| [ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) | [control_state](class_editorspinslider.md#class_EditorSpinSlider_property_control_state) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [editing_integer](class_editorspinslider.md#class_EditorSpinSlider_property_editing_integer) | `false` |
| [bool](class_bool.md#class_bool) | [flat](class_editorspinslider.md#class_EditorSpinSlider_property_flat) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [hide_slider](class_editorspinslider.md#class_EditorSpinSlider_property_hide_slider) | `false` |
| [String](class_string.md#class_String) | [label](class_editorspinslider.md#class_EditorSpinSlider_property_label) | `""` |
| [bool](class_bool.md#class_bool) | [read_only](class_editorspinslider.md#class_EditorSpinSlider_property_read_only) | `false` |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_vertical | `1` (overrides [Control](class_control.md#class_Control_property_size_flags_vertical)) |
| [float](class_float.md#class_float) | step | `1.0` (overrides [Range](class_range.md#class_Range_property_step)) |
| [String](class_string.md#class_String) | [suffix](class_editorspinslider.md#class_EditorSpinSlider_property_suffix) | `""` |

### Theme Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [updown](class_editorspinslider.md#class_EditorSpinSlider_theme_icon_updown) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [updown_disabled](class_editorspinslider.md#class_EditorSpinSlider_theme_icon_updown_disabled) |

---

### Signals

<span id="class_EditorSpinSlider_signal_grabbed"></span>

**grabbed** ( ) [🔗](class_editorspinslider.md#class_EditorSpinSlider_signal_grabbed)

Emitted when the spinner/slider is grabbed.

---

<span id="class_EditorSpinSlider_signal_ungrabbed"></span>

**ungrabbed** ( ) [🔗](class_editorspinslider.md#class_EditorSpinSlider_signal_ungrabbed)

Emitted when the spinner/slider is ungrabbed.

---

<span id="class_EditorSpinSlider_signal_updown_pressed"></span>

**updown_pressed** ( ) [🔗](class_editorspinslider.md#class_EditorSpinSlider_signal_updown_pressed)

Emitted when the updown button is pressed.

---

<span id="class_EditorSpinSlider_signal_value_focus_entered"></span>

**value_focus_entered** ( ) [🔗](class_editorspinslider.md#class_EditorSpinSlider_signal_value_focus_entered)

Emitted when the value form gains focus.

---

<span id="class_EditorSpinSlider_signal_value_focus_exited"></span>

**value_focus_exited** ( ) [🔗](class_editorspinslider.md#class_EditorSpinSlider_signal_value_focus_exited)

Emitted when the value form loses focus.

---

### Enumerations

<span id="enum_EditorSpinSlider_ControlState"></span>

enum **ControlState**: [🔗](class_editorspinslider.md#enum_EditorSpinSlider_ControlState)

<span id="class_EditorSpinSlider_constant_CONTROL_STATE_DEFAULT"></span>

[ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) **CONTROL_STATE_DEFAULT** = `0`

The type of control used will depend on the value of [editing_integer](class_editorspinslider.md#class_EditorSpinSlider_property_editing_integer). Up-down arrows if `true`, a slider if `false`.

<span id="class_EditorSpinSlider_constant_CONTROL_STATE_PREFER_SLIDER"></span>

[ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) **CONTROL_STATE_PREFER_SLIDER** = `1`

A slider will always be used, even if [editing_integer](class_editorspinslider.md#class_EditorSpinSlider_property_editing_integer) is enabled.

<span id="class_EditorSpinSlider_constant_CONTROL_STATE_HIDE"></span>

[ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) **CONTROL_STATE_HIDE** = `2`

Neither the up-down arrows nor the slider will be shown.

---

### Property Descriptions

<span id="class_EditorSpinSlider_property_control_state"></span>

[ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) **control_state** = `0` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_control_state)

- void **set_control_state** ( value: [ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) )
- [ControlState](class_editorspinslider.md#enum_EditorSpinSlider_ControlState) **get_control_state** ( )

The state in which the control used to manipulate the value will be.

---

<span id="class_EditorSpinSlider_property_editing_integer"></span>

[bool](class_bool.md#class_bool) **editing_integer** = `false` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_editing_integer)

- void **set_editing_integer** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_integer** ( )

If `true`, the **EditorSpinSlider** is considered to be editing an integer value. If `false`, the **EditorSpinSlider** is considered to be editing a floating-point value. This is used to determine whether a slider should be drawn by default. The slider is only drawn for floats; integers use up-down arrows similar to [SpinBox](class_spinbox.md#class_SpinBox) instead, unless [control_state](class_editorspinslider.md#class_EditorSpinSlider_property_control_state) is set to [CONTROL_STATE_PREFER_SLIDER](class_editorspinslider.md#class_EditorSpinSlider_constant_CONTROL_STATE_PREFER_SLIDER). It will also use EditorSettings.interface/inspector/integer_drag_speed instead of EditorSettings.interface/inspector/float_drag_speed if the slider is available.

---

<span id="class_EditorSpinSlider_property_flat"></span>

[bool](class_bool.md#class_bool) **flat** = `false` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_flat)

- void **set_flat** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flat** ( )

If `true`, the slider will not draw background.

---

<span id="class_EditorSpinSlider_property_hide_slider"></span>

[bool](class_bool.md#class_bool) **hide_slider** = `false` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_hide_slider)

- void **set_hide_slider** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hiding_slider** ( )

**Deprecated:** Use [control_state](class_editorspinslider.md#class_EditorSpinSlider_property_control_state) instead.

If `true`, the slider and up/down arrows are hidden.

---

<span id="class_EditorSpinSlider_property_label"></span>

[String](class_string.md#class_String) **label** = `""` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_label)

- void **set_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_label** ( )

The text that displays to the left of the value.

---

<span id="class_EditorSpinSlider_property_read_only"></span>

[bool](class_bool.md#class_bool) **read_only** = `false` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_read_only)

- void **set_read_only** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_read_only** ( )

If `true`, the slider can't be interacted with.

---

<span id="class_EditorSpinSlider_property_suffix"></span>

[String](class_string.md#class_String) **suffix** = `""` [🔗](class_editorspinslider.md#class_EditorSpinSlider_property_suffix)

- void **set_suffix** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_suffix** ( )

The suffix to display after the value (in a faded color). This should generally be a plural word. You may have to use an abbreviation if the suffix is too long to be displayed.

---

### Theme Property Descriptions

<span id="class_EditorSpinSlider_theme_icon_updown"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **updown** [🔗](class_editorspinslider.md#class_EditorSpinSlider_theme_icon_updown)

Single texture representing both the up and down buttons.

---

<span id="class_EditorSpinSlider_theme_icon_updown_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **updown_disabled** [🔗](class_editorspinslider.md#class_EditorSpinSlider_theme_icon_updown_disabled)

Single texture representing both the up and down buttons, when the control is readonly or disabled.
