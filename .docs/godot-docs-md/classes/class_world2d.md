<span id="class_World2D"></span>

## World2D

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A resource that holds all components of a 2D world, such as a canvas and a physics space.

### Description

Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

### Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)

### Properties


| [RID](class_rid.md#class_RID) | [canvas](class_world2d.md#class_World2D_property_canvas) |
| --- | --- |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) | [direct_space_state](class_world2d.md#class_World2D_property_direct_space_state) |
| [RID](class_rid.md#class_RID) | [navigation_map](class_world2d.md#class_World2D_property_navigation_map) |
| [RID](class_rid.md#class_RID) | [space](class_world2d.md#class_World2D_property_space) |

---

### Property Descriptions

<span id="class_World2D_property_canvas"></span>

[RID](class_rid.md#class_RID) **canvas** [🔗](class_world2d.md#class_World2D_property_canvas)

- [RID](class_rid.md#class_RID) **get_canvas** ( )

The [RID](class_rid.md#class_RID) of this world's canvas resource. Used by the [RenderingServer](class_renderingserver.md#class_RenderingServer) for 2D drawing.

---

<span id="class_World2D_property_direct_space_state"></span>

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) **direct_space_state** [🔗](class_world2d.md#class_World2D_property_direct_space_state)

- [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) **get_direct_space_state** ( )

Direct access to the world's physics 2D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) in the main thread.

---

<span id="class_World2D_property_navigation_map"></span>

[RID](class_rid.md#class_RID) **navigation_map** [🔗](class_world2d.md#class_World2D_property_navigation_map)

- [RID](class_rid.md#class_RID) **get_navigation_map** ( )

The [RID](class_rid.md#class_RID) of this world's navigation map. Used by the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D).

---

<span id="class_World2D_property_space"></span>

[RID](class_rid.md#class_RID) **space** [🔗](class_world2d.md#class_World2D_property_space)

- [RID](class_rid.md#class_RID) **get_space** ( )

The [RID](class_rid.md#class_RID) of this world's physics space resource. Used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) for 2D physics, treating it as both a space and an area.
