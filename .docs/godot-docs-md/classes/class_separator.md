<span id="class_Separator"></span>

## Separator

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HSeparator](class_hseparator.md#class_HSeparator), [VSeparator](class_vseparator.md#class_VSeparator)

Abstract base class for separators.

### Description

Abstract base class for separators, used for separating other controls. **Separator** s are purely visual and normally drawn as a [StyleBoxLine](class_styleboxline.md#class_StyleBoxLine).

### Theme Properties


| [int](class_int.md#class_int) | [separation](class_separator.md#class_Separator_theme_constant_separation) | `0` |
| --- | --- | --- |
| [StyleBox](class_stylebox.md#class_StyleBox) | [separator](class_separator.md#class_Separator_theme_style_separator) |

---

### Theme Property Descriptions

<span id="class_Separator_theme_constant_separation"></span>

[int](class_int.md#class_int) **separation** = `0` [🔗](class_separator.md#class_Separator_theme_constant_separation)

The size of the area covered by the separator. Effectively works like a minimum width/height.

---

<span id="class_Separator_theme_style_separator"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **separator** [🔗](class_separator.md#class_Separator_theme_style_separator)

The style for the separator line. Works best with [StyleBoxLine](class_styleboxline.md#class_StyleBoxLine) (remember to enable [StyleBoxLine.vertical](class_styleboxline.md#class_StyleBoxLine_property_vertical) for [VSeparator](class_vseparator.md#class_VSeparator)).
