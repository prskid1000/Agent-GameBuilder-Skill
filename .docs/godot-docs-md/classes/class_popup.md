<span id="class_Popup"></span>

## Popup

**Inherits:** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [PopupMenu](class_popupmenu.md#class_PopupMenu), [PopupPanel](class_popuppanel.md#class_PopupPanel)

Base class for contextual windows and panels with fixed position.

### Description

**Popup** is a base class for contextual windows and panels with fixed position. It's a modal by default (see [Window.popup_window](class_window.md#class_Window_property_popup_window)) and provides methods for implementing custom popup behavior.

 **Note:** **Popup** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class_Window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped).

### Properties


| [bool](class_bool.md#class_bool) | borderless | `true` (overrides [Window](class_window.md#class_Window_property_borderless)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | maximize_disabled | `true` (overrides [Window](class_window.md#class_Window_property_maximize_disabled)) |
| [bool](class_bool.md#class_bool) | minimize_disabled | `true` (overrides [Window](class_window.md#class_Window_property_minimize_disabled)) |
| [bool](class_bool.md#class_bool) | popup_window | `true` (overrides [Window](class_window.md#class_Window_property_popup_window)) |
| [bool](class_bool.md#class_bool) | popup_wm_hint | `true` (overrides [Window](class_window.md#class_Window_property_popup_wm_hint)) |
| [bool](class_bool.md#class_bool) | transient | `true` (overrides [Window](class_window.md#class_Window_property_transient)) |
| [bool](class_bool.md#class_bool) | unresizable | `true` (overrides [Window](class_window.md#class_Window_property_unresizable)) |
| [bool](class_bool.md#class_bool) | visible | `false` (overrides [Window](class_window.md#class_Window_property_visible)) |
| [bool](class_bool.md#class_bool) | wrap_controls | `true` (overrides [Window](class_window.md#class_Window_property_wrap_controls)) |

---

### Signals

<span id="class_Popup_signal_popup_hide"></span>

**popup_hide** ( ) [🔗](class_popup.md#class_Popup_signal_popup_hide)

Emitted when the popup is hidden.
