<span id="class_VisibleOnScreenEnabler3D"></span>

## VisibleOnScreenEnabler3D

**Inherits:** [VisibleOnScreenNotifier3D](class_visibleonscreennotifier3d.md#class_VisibleOnScreenNotifier3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A box-shaped region of 3D space that, when visible on screen, enables a target node.

### Description

**VisibleOnScreenEnabler3D** contains a box-shaped region of 3D space and a target node. The target node will be automatically enabled (via its [Node.process_mode](class_node.md#class_Node_property_process_mode) property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

See [VisibleOnScreenNotifier3D](class_visibleonscreennotifier3d.md#class_VisibleOnScreenNotifier3D) if you only want to be notified when the region is visible on screen.

 **Note:** **VisibleOnScreenEnabler3D** uses an approximate heuristic that doesn't take walls and other occlusion into account, unless occlusion culling is used. It also won't function unless [Node3D.visible](class_node3d.md#class_Node3D_property_visible) is set to `true`.

### Properties


| [EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) | [enable_mode](class_visibleonscreenenabler3d.md#class_VisibleOnScreenEnabler3D_property_enable_mode) | `0` |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [enable_node_path](class_visibleonscreenenabler3d.md#class_VisibleOnScreenEnabler3D_property_enable_node_path) | `NodePath("..")` |

---

### Enumerations

<span id="enum_VisibleOnScreenEnabler3D_EnableMode"></span>

enum **EnableMode**: [🔗](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode)

<span id="class_VisibleOnScreenEnabler3D_constant_ENABLE_MODE_INHERIT"></span>

[EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) **ENABLE_MODE_INHERIT** = `0`

Corresponds to [Node.PROCESS_MODE_INHERIT](class_node.md#class_Node_constant_PROCESS_MODE_INHERIT).

<span id="class_VisibleOnScreenEnabler3D_constant_ENABLE_MODE_ALWAYS"></span>

[EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) **ENABLE_MODE_ALWAYS** = `1`

Corresponds to [Node.PROCESS_MODE_ALWAYS](class_node.md#class_Node_constant_PROCESS_MODE_ALWAYS).

<span id="class_VisibleOnScreenEnabler3D_constant_ENABLE_MODE_WHEN_PAUSED"></span>

[EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) **ENABLE_MODE_WHEN_PAUSED** = `2`

Corresponds to [Node.PROCESS_MODE_WHEN_PAUSED](class_node.md#class_Node_constant_PROCESS_MODE_WHEN_PAUSED).

---

### Property Descriptions

<span id="class_VisibleOnScreenEnabler3D_property_enable_mode"></span>

[EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) **enable_mode** = `0` [🔗](class_visibleonscreenenabler3d.md#class_VisibleOnScreenEnabler3D_property_enable_mode)

- void **set_enable_mode** ( value: [EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) )
- [EnableMode](class_visibleonscreenenabler3d.md#enum_VisibleOnScreenEnabler3D_EnableMode) **get_enable_mode** ( )

Determines how the target node is enabled. Corresponds to [ProcessMode](class_node.md#enum_Node_ProcessMode). When the node is disabled, it always uses [Node.PROCESS_MODE_DISABLED](class_node.md#class_Node_constant_PROCESS_MODE_DISABLED).

---

<span id="class_VisibleOnScreenEnabler3D_property_enable_node_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **enable_node_path** = `NodePath("..")` [🔗](class_visibleonscreenenabler3d.md#class_VisibleOnScreenEnabler3D_property_enable_node_path)

- void **set_enable_node_path** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_enable_node_path** ( )

The path to the target node, relative to the **VisibleOnScreenEnabler3D**. The target node is cached; it's only assigned when setting this property (if the **VisibleOnScreenEnabler3D** is inside the scene tree) and every time the **VisibleOnScreenEnabler3D** enters the scene tree. If the path is empty, no node will be affected. If the path is invalid, an error is also generated.
