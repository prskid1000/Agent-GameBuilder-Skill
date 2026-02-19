<span id="class_World3D"></span>

## World3D

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A resource that holds all components of a 3D world, such as a visual scenario and a physics space.

### Description

Class that has everything pertaining to a world: A physics space, a visual scenario, and a sound space. 3D nodes register their resources into the current 3D world.

### Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)

### Properties


| [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) | [camera_attributes](class_world3d.md#class_World3D_property_camera_attributes) |
| --- | --- |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) | [direct_space_state](class_world3d.md#class_World3D_property_direct_space_state) |
| [Environment](class_environment.md#class_Environment) | [environment](class_world3d.md#class_World3D_property_environment) |
| [Environment](class_environment.md#class_Environment) | [fallback_environment](class_world3d.md#class_World3D_property_fallback_environment) |
| [RID](class_rid.md#class_RID) | [navigation_map](class_world3d.md#class_World3D_property_navigation_map) |
| [RID](class_rid.md#class_RID) | [scenario](class_world3d.md#class_World3D_property_scenario) |
| [RID](class_rid.md#class_RID) | [space](class_world3d.md#class_World3D_property_space) |

---

### Property Descriptions

<span id="class_World3D_property_camera_attributes"></span>

[CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **camera_attributes** [🔗](class_world3d.md#class_World3D_property_camera_attributes)

- void **set_camera_attributes** ( value: [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) )
- [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **get_camera_attributes** ( )

The default [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) resource to use if none set on the [Camera3D](class_camera3d.md#class_Camera3D).

---

<span id="class_World3D_property_direct_space_state"></span>

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) **direct_space_state** [🔗](class_world3d.md#class_World3D_property_direct_space_state)

- [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) **get_direct_space_state** ( )

Direct access to the world's physics 3D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) in the main thread.

---

<span id="class_World3D_property_environment"></span>

[Environment](class_environment.md#class_Environment) **environment** [🔗](class_world3d.md#class_World3D_property_environment)

- void **set_environment** ( value: [Environment](class_environment.md#class_Environment) )
- [Environment](class_environment.md#class_Environment) **get_environment** ( )

The World3D's [Environment](class_environment.md#class_Environment).

---

<span id="class_World3D_property_fallback_environment"></span>

[Environment](class_environment.md#class_Environment) **fallback_environment** [🔗](class_world3d.md#class_World3D_property_fallback_environment)

- void **set_fallback_environment** ( value: [Environment](class_environment.md#class_Environment) )
- [Environment](class_environment.md#class_Environment) **get_fallback_environment** ( )

The World3D's fallback environment will be used if [environment](class_world3d.md#class_World3D_property_environment) fails or is missing.

---

<span id="class_World3D_property_navigation_map"></span>

[RID](class_rid.md#class_RID) **navigation_map** [🔗](class_world3d.md#class_World3D_property_navigation_map)

- [RID](class_rid.md#class_RID) **get_navigation_map** ( )

The [RID](class_rid.md#class_RID) of this world's navigation map. Used by the [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D).

---

<span id="class_World3D_property_scenario"></span>

[RID](class_rid.md#class_RID) **scenario** [🔗](class_world3d.md#class_World3D_property_scenario)

- [RID](class_rid.md#class_RID) **get_scenario** ( )

The World3D's visual scenario.

---

<span id="class_World3D_property_space"></span>

[RID](class_rid.md#class_RID) **space** [🔗](class_world3d.md#class_World3D_property_space)

- [RID](class_rid.md#class_RID) **get_space** ( )

The World3D's physics space.
