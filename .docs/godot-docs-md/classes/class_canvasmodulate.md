.. meta::
	:keywords: color

<span id="class_CanvasModulate"></span>

## CanvasModulate

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node that applies a color tint to a canvas.

### Description

**CanvasModulate** applies a color tint to all nodes on a canvas. Only one can be used to tint a canvas, but [CanvasLayer](class_canvaslayer.md#class_CanvasLayer) s can be used to render things independently.

### Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

### Properties


| [Color](class_color.md#class_Color) | [color](class_canvasmodulate.md#class_CanvasModulate_property_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_CanvasModulate_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_canvasmodulate.md#class_CanvasModulate_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

The tint color to apply.
