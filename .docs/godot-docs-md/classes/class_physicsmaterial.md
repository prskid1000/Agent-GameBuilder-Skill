<span id="class_PhysicsMaterial"></span>

## PhysicsMaterial

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds physics-related properties of a surface, namely its roughness and bounciness.

### Description

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

### Properties


| [bool](class_bool.md#class_bool) | [absorbent](class_physicsmaterial.md#class_PhysicsMaterial_property_absorbent) | `false` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [bounce](class_physicsmaterial.md#class_PhysicsMaterial_property_bounce) | `0.0` |
| [float](class_float.md#class_float) | [friction](class_physicsmaterial.md#class_PhysicsMaterial_property_friction) | `1.0` |
| [bool](class_bool.md#class_bool) | [rough](class_physicsmaterial.md#class_PhysicsMaterial_property_rough) | `false` |

---

### Property Descriptions

<span id="class_PhysicsMaterial_property_absorbent"></span>

[bool](class_bool.md#class_bool) **absorbent** = `false` [🔗](class_physicsmaterial.md#class_PhysicsMaterial_property_absorbent)

- void **set_absorbent** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_absorbent** ( )

If `true`, subtracts the bounciness from the colliding object's bounciness instead of adding it.

---

<span id="class_PhysicsMaterial_property_bounce"></span>

[float](class_float.md#class_float) **bounce** = `0.0` [🔗](class_physicsmaterial.md#class_PhysicsMaterial_property_bounce)

- void **set_bounce** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bounce** ( )

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

 **Note:** Even with [bounce](class_physicsmaterial.md#class_PhysicsMaterial_property_bounce) set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a physics body that preserves all its energy over time, set [bounce](class_physicsmaterial.md#class_PhysicsMaterial_property_bounce) to `1.0`, the body's linear damp mode to **Replace** (if applicable), its linear damp to `0.0`, its angular damp mode to **Replace** (if applicable), and its angular damp to `0.0`.

---

<span id="class_PhysicsMaterial_property_friction"></span>

[float](class_float.md#class_float) **friction** = `1.0` [🔗](class_physicsmaterial.md#class_PhysicsMaterial_property_friction)

- void **set_friction** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_friction** ( )

The body's friction. Values range from `0` (frictionless) to `1` (maximum friction).

---

<span id="class_PhysicsMaterial_property_rough"></span>

[bool](class_bool.md#class_bool) **rough** = `false` [🔗](class_physicsmaterial.md#class_PhysicsMaterial_property_rough)

- void **set_rough** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_rough** ( )

If `true`, the physics engine will use the friction of the object marked as "rough" when two objects collide. If `false`, the physics engine will use the lowest friction of all colliding objects instead. If `true` for both colliding objects, the physics engine will use the highest friction.
