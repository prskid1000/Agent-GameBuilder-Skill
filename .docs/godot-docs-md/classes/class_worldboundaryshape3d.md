<span id="class_WorldBoundaryShape3D"></span>

## WorldBoundaryShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D world boundary (half-space) shape used for physics collision.

### Description

A 3D world boundary shape, intended for use in physics. **WorldBoundaryShape3D** works like an infinite plane that forces all physics bodies to stay above it. The [plane](class_worldboundaryshape3d.md#class_WorldBoundaryShape3D_property_plane)'s normal determines which direction is considered as "above" and in the editor, the line over the plane represents this direction. It can for example be used for endless flat floors.

 **Note:** When the physics engine is set to **Jolt Physics** in the project settings (ProjectSettings.physics/3d/physics_engine), **WorldBoundaryShape3D** has a finite size (centered at the shape's origin). It can be adjusted by changing ProjectSettings.physics/jolt_physics_3d/limits/world_boundary_shape_size.

### Properties


| [Plane](class_plane.md#class_Plane) | [plane](class_worldboundaryshape3d.md#class_WorldBoundaryShape3D_property_plane) | `Plane(0, 1, 0, 0)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_WorldBoundaryShape3D_property_plane"></span>

[Plane](class_plane.md#class_Plane) **plane** = `Plane(0, 1, 0, 0)` [🔗](class_worldboundaryshape3d.md#class_WorldBoundaryShape3D_property_plane)

- void **set_plane** ( value: [Plane](class_plane.md#class_Plane) )
- [Plane](class_plane.md#class_Plane) **get_plane** ( )

The [Plane](class_plane.md#class_Plane) used by the **WorldBoundaryShape3D** for collision.
