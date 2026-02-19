<span id="class_GridContainer"></span>

## GridContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A container that arranges its child controls in a grid layout.

### Description

**GridContainer** arranges its child controls in a grid layout. The number of columns is specified by the [columns](class_gridcontainer.md#class_GridContainer_property_columns) property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

 **Note:** **GridContainer** only works with child nodes inheriting from [Control](class_control.md#class_Control). It won't rearrange child nodes inheriting from [Node2D](class_node2d.md#class_Node2D).

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

- Operating System Testing Demo

### Properties


| [int](class_int.md#class_int) | [columns](class_gridcontainer.md#class_GridContainer_property_columns) | `1` |
| --- | --- | --- |

### Theme Properties


| [int](class_int.md#class_int) | [h_separation](class_gridcontainer.md#class_GridContainer_theme_constant_h_separation) | `4` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [v_separation](class_gridcontainer.md#class_GridContainer_theme_constant_v_separation) | `4` |

---

### Property Descriptions

<span id="class_GridContainer_property_columns"></span>

[int](class_int.md#class_int) **columns** = `1` [🔗](class_gridcontainer.md#class_GridContainer_property_columns)

- void **set_columns** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_columns** ( )

The number of columns in the **GridContainer**. If modified, **GridContainer** reorders its Control-derived children to accommodate the new layout.

---

### Theme Property Descriptions

<span id="class_GridContainer_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_gridcontainer.md#class_GridContainer_theme_constant_h_separation)

The horizontal separation of child nodes.

---

<span id="class_GridContainer_theme_constant_v_separation"></span>

[int](class_int.md#class_int) **v_separation** = `4` [🔗](class_gridcontainer.md#class_GridContainer_theme_constant_v_separation)

The vertical separation of child nodes.
