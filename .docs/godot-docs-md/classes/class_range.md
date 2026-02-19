<span id="class_Range"></span>

## Range

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorSpinSlider](class_editorspinslider.md#class_EditorSpinSlider), [ProgressBar](class_progressbar.md#class_ProgressBar), [ScrollBar](class_scrollbar.md#class_ScrollBar), [Slider](class_slider.md#class_Slider), [SpinBox](class_spinbox.md#class_SpinBox), [TextureProgressBar](class_textureprogressbar.md#class_TextureProgressBar)

Abstract base class for controls that represent a number within a range.

### Description

Range is an abstract base class for controls that represent a number within a range, using a configured [step](class_range.md#class_Range_property_step) and [page](class_range.md#class_Range_property_page) size. See e.g. [ScrollBar](class_scrollbar.md#class_ScrollBar) and [Slider](class_slider.md#class_Slider) for examples of higher-level nodes using Range.

### Properties


| [bool](class_bool.md#class_bool) | [allow_greater](class_range.md#class_Range_property_allow_greater) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [allow_lesser](class_range.md#class_Range_property_allow_lesser) | `false` |
| [bool](class_bool.md#class_bool) | [exp_edit](class_range.md#class_Range_property_exp_edit) | `false` |
| [float](class_float.md#class_float) | [max_value](class_range.md#class_Range_property_max_value) | `100.0` |
| [float](class_float.md#class_float) | [min_value](class_range.md#class_Range_property_min_value) | `0.0` |
| [float](class_float.md#class_float) | [page](class_range.md#class_Range_property_page) | `0.0` |
| [float](class_float.md#class_float) | [ratio](class_range.md#class_Range_property_ratio) |
| [bool](class_bool.md#class_bool) | [rounded](class_range.md#class_Range_property_rounded) | `false` |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_vertical | `0` (overrides [Control](class_control.md#class_Control_property_size_flags_vertical)) |
| [float](class_float.md#class_float) | [step](class_range.md#class_Range_property_step) | `0.01` |
| [float](class_float.md#class_float) | [value](class_range.md#class_Range_property_value) | `0.0` |

### Methods


| void | [_value_changed](class_range.md#class_Range_private_method__value_changed) ( new_value: [float](class_float.md#class_float) ) virtual |
| --- | --- |
| void | [set_value_no_signal](class_range.md#class_Range_method_set_value_no_signal) ( value: [float](class_float.md#class_float) ) |
| void | [share](class_range.md#class_Range_method_share) ( with: [Node](class_node.md#class_Node) ) |
| void | [unshare](class_range.md#class_Range_method_unshare) ( ) |

---

### Signals

<span id="class_Range_signal_changed"></span>

**changed** ( ) [🔗](class_range.md#class_Range_signal_changed)

Emitted when [min_value](class_range.md#class_Range_property_min_value), [max_value](class_range.md#class_Range_property_max_value), [page](class_range.md#class_Range_property_page), or [step](class_range.md#class_Range_property_step) change.

---

<span id="class_Range_signal_value_changed"></span>

**value_changed** ( value: [float](class_float.md#class_float) ) [🔗](class_range.md#class_Range_signal_value_changed)

Emitted when [value](class_range.md#class_Range_property_value) changes. When used on a [Slider](class_slider.md#class_Slider), this is called continuously while dragging (potentially every frame). If you are performing an expensive operation in a function connected to [value_changed](class_range.md#class_Range_signal_value_changed), consider using a *debouncing* [Timer](class_timer.md#class_Timer) to call the function less often.

 **Note:** Unlike signals such as [LineEdit.text_changed](class_lineedit.md#class_LineEdit_signal_text_changed), [value_changed](class_range.md#class_Range_signal_value_changed) is also emitted when `value` is set directly via code.

---

### Property Descriptions

<span id="class_Range_property_allow_greater"></span>

[bool](class_bool.md#class_bool) **allow_greater** = `false` [🔗](class_range.md#class_Range_property_allow_greater)

- void **set_allow_greater** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_greater_allowed** ( )

If `true`, [value](class_range.md#class_Range_property_value) may be greater than [max_value](class_range.md#class_Range_property_max_value).

---

<span id="class_Range_property_allow_lesser"></span>

[bool](class_bool.md#class_bool) **allow_lesser** = `false` [🔗](class_range.md#class_Range_property_allow_lesser)

- void **set_allow_lesser** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_lesser_allowed** ( )

If `true`, [value](class_range.md#class_Range_property_value) may be less than [min_value](class_range.md#class_Range_property_min_value).

---

<span id="class_Range_property_exp_edit"></span>

[bool](class_bool.md#class_bool) **exp_edit** = `false` [🔗](class_range.md#class_Range_property_exp_edit)

- void **set_exp_ratio** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_ratio_exp** ( )

If `true`, and [min_value](class_range.md#class_Range_property_min_value) is greater or equal to `0`, [value](class_range.md#class_Range_property_value) will be represented exponentially rather than linearly.

---

<span id="class_Range_property_max_value"></span>

[float](class_float.md#class_float) **max_value** = `100.0` [🔗](class_range.md#class_Range_property_max_value)

- void **set_max** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max** ( )

Maximum value. Range is clamped if [value](class_range.md#class_Range_property_value) is greater than [max_value](class_range.md#class_Range_property_max_value).

---

<span id="class_Range_property_min_value"></span>

[float](class_float.md#class_float) **min_value** = `0.0` [🔗](class_range.md#class_Range_property_min_value)

- void **set_min** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min** ( )

Minimum value. Range is clamped if [value](class_range.md#class_Range_property_value) is less than [min_value](class_range.md#class_Range_property_min_value).

---

<span id="class_Range_property_page"></span>

[float](class_float.md#class_float) **page** = `0.0` [🔗](class_range.md#class_Range_property_page)

- void **set_page** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_page** ( )

Page size. Used mainly for [ScrollBar](class_scrollbar.md#class_ScrollBar). A [ScrollBar](class_scrollbar.md#class_ScrollBar)'s grabber length is the [ScrollBar](class_scrollbar.md#class_ScrollBar)'s size multiplied by [page](class_range.md#class_Range_property_page) over the difference between [min_value](class_range.md#class_Range_property_min_value) and [max_value](class_range.md#class_Range_property_max_value).

---

<span id="class_Range_property_ratio"></span>

[float](class_float.md#class_float) **ratio** [🔗](class_range.md#class_Range_property_ratio)

- void **set_as_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_as_ratio** ( )

The value mapped between 0 and 1.

---

<span id="class_Range_property_rounded"></span>

[bool](class_bool.md#class_bool) **rounded** = `false` [🔗](class_range.md#class_Range_property_rounded)

- void **set_use_rounded_values** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_rounded_values** ( )

If `true`, [value](class_range.md#class_Range_property_value) will always be rounded to the nearest integer.

---

<span id="class_Range_property_step"></span>

[float](class_float.md#class_float) **step** = `0.01` [🔗](class_range.md#class_Range_property_step)

- void **set_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_step** ( )

If greater than `0.0`, [value](class_range.md#class_Range_property_value) will always be rounded to a multiple of this property's value above [min_value](class_range.md#class_Range_property_min_value). For example, if [min_value](class_range.md#class_Range_property_min_value) is `0.1` and step is `0.2`, then [value](class_range.md#class_Range_property_value) is limited to `0.1`, `0.3`, `0.5`, and so on. If [rounded](class_range.md#class_Range_property_rounded) is also `true`, [value](class_range.md#class_Range_property_value) will first be rounded to a multiple of this property's value, then rounded to the nearest integer.

---

<span id="class_Range_property_value"></span>

[float](class_float.md#class_float) **value** = `0.0` [🔗](class_range.md#class_Range_property_value)

- void **set_value** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_value** ( )

Range's current value. Changing this property (even via code) will trigger [value_changed](class_range.md#class_Range_signal_value_changed) signal. Use [set_value_no_signal()](class_range.md#class_Range_method_set_value_no_signal) if you want to avoid it.

---

### Method Descriptions

<span id="class_Range_private_method__value_changed"></span>

void **_value_changed** ( new_value: [float](class_float.md#class_float) ) *virtual* [🔗](class_range.md#class_Range_private_method__value_changed)

Called when the **Range**'s value is changed (following the same conditions as [value_changed](class_range.md#class_Range_signal_value_changed)).

---

<span id="class_Range_method_set_value_no_signal"></span>

void **set_value_no_signal** ( value: [float](class_float.md#class_float) ) [🔗](class_range.md#class_Range_method_set_value_no_signal)

Sets the **Range**'s current value to the specified `value`, without emitting the [value_changed](class_range.md#class_Range_signal_value_changed) signal.

---

<span id="class_Range_method_share"></span>

void **share** ( with: [Node](class_node.md#class_Node) ) [🔗](class_range.md#class_Range_method_share)

Binds two **Range** s together along with any ranges previously grouped with either of them. When any of range's member variables change, it will share the new value with all other ranges in its group.

---

<span id="class_Range_method_unshare"></span>

void **unshare** ( ) [🔗](class_range.md#class_Range_method_unshare)

Stops the **Range** from sharing its member variables with any other.
