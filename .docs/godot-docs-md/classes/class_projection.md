<span id="class_Projection"></span>

## Projection

A 4×4 matrix for 3D projective transformations.

### Description

A 4×4 matrix used for 3D projective transformations. It can represent transformations such as translation, rotation, scaling, shearing, and perspective division. It consists of four [Vector4](class_vector4.md#class_Vector4) columns.

For purely linear transformations (translation, rotation, and scale), it is recommended to use [Transform3D](class_transform3d.md#class_Transform3D), as it is more performant and requires less memory.

Used internally as [Camera3D](class_camera3d.md#class_Camera3D)'s projection matrix.

 **Note:** In a boolean context, a projection will evaluate to `false` if it's equal to [IDENTITY](class_projection.md#class_Projection_constant_IDENTITY). Otherwise, a projection will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Properties


| [Vector4](class_vector4.md#class_Vector4) | [w](class_projection.md#class_Projection_property_w) | `Vector4(0, 0, 0, 1)` |
| --- | --- | --- |
| [Vector4](class_vector4.md#class_Vector4) | [x](class_projection.md#class_Projection_property_x) | `Vector4(1, 0, 0, 0)` |
| [Vector4](class_vector4.md#class_Vector4) | [y](class_projection.md#class_Projection_property_y) | `Vector4(0, 1, 0, 0)` |
| [Vector4](class_vector4.md#class_Vector4) | [z](class_projection.md#class_Projection_property_z) | `Vector4(0, 0, 1, 0)` |

### Constructors


| [Projection](class_projection.md#class_Projection) | [Projection](class_projection.md#class_Projection_constructor_Projection) ( ) |
| --- | --- |
| [Projection](class_projection.md#class_Projection) | [Projection](class_projection.md#class_Projection_constructor_Projection) ( from: [Projection](class_projection.md#class_Projection) ) |
| [Projection](class_projection.md#class_Projection) | [Projection](class_projection.md#class_Projection_constructor_Projection) ( from: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [Projection](class_projection.md#class_Projection) | [Projection](class_projection.md#class_Projection_constructor_Projection) ( x_axis: [Vector4](class_vector4.md#class_Vector4), y_axis: [Vector4](class_vector4.md#class_Vector4), z_axis: [Vector4](class_vector4.md#class_Vector4), w_axis: [Vector4](class_vector4.md#class_Vector4) ) |

### Methods


| [Projection](class_projection.md#class_Projection) | [create_depth_correction](class_projection.md#class_Projection_method_create_depth_correction) ( flip_y: [bool](class_bool.md#class_bool) ) static |
| --- | --- |
| [Projection](class_projection.md#class_Projection) | [create_fit_aabb](class_projection.md#class_Projection_method_create_fit_aabb) ( aabb: [AABB](class_aabb.md#class_AABB) ) static |
| [Projection](class_projection.md#class_Projection) | [create_for_hmd](class_projection.md#class_Projection_method_create_for_hmd) ( eye: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), intraocular_dist: [float](class_float.md#class_float), display_width: [float](class_float.md#class_float), display_to_lens: [float](class_float.md#class_float), oversample: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) static |
| [Projection](class_projection.md#class_Projection) | [create_frustum](class_projection.md#class_Projection_method_create_frustum) ( left: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float), top: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) static |
| [Projection](class_projection.md#class_Projection) | [create_frustum_aspect](class_projection.md#class_Projection_method_create_frustum_aspect) ( size: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), offset: [Vector2](class_vector2.md#class_Vector2), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) static |
| [Projection](class_projection.md#class_Projection) | [create_light_atlas_rect](class_projection.md#class_Projection_method_create_light_atlas_rect) ( rect: [Rect2](class_rect2.md#class_Rect2) ) static |
| [Projection](class_projection.md#class_Projection) | [create_orthogonal](class_projection.md#class_Projection_method_create_orthogonal) ( left: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float), top: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) static |
| [Projection](class_projection.md#class_Projection) | [create_orthogonal_aspect](class_projection.md#class_Projection_method_create_orthogonal_aspect) ( size: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) static |
| [Projection](class_projection.md#class_Projection) | [create_perspective](class_projection.md#class_Projection_method_create_perspective) ( fovy: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) static |
| [Projection](class_projection.md#class_Projection) | [create_perspective_hmd](class_projection.md#class_Projection_method_create_perspective_hmd) ( fovy: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool), eye: [int](class_int.md#class_int), intraocular_dist: [float](class_float.md#class_float), convergence_dist: [float](class_float.md#class_float) ) static |
| [float](class_float.md#class_float) | [determinant](class_projection.md#class_Projection_method_determinant) ( ) const |
| [Projection](class_projection.md#class_Projection) | [flipped_y](class_projection.md#class_Projection_method_flipped_y) ( ) const |
| [float](class_float.md#class_float) | [get_aspect](class_projection.md#class_Projection_method_get_aspect) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_far_plane_half_extents](class_projection.md#class_Projection_method_get_far_plane_half_extents) ( ) const |
| [float](class_float.md#class_float) | [get_fov](class_projection.md#class_Projection_method_get_fov) ( ) const |
| [float](class_float.md#class_float) | [get_fovy](class_projection.md#class_Projection_method_get_fovy) ( fovx: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float) ) static |
| [float](class_float.md#class_float) | [get_lod_multiplier](class_projection.md#class_Projection_method_get_lod_multiplier) ( ) const |
| [int](class_int.md#class_int) | [get_pixels_per_meter](class_projection.md#class_Projection_method_get_pixels_per_meter) ( for_pixel_width: [int](class_int.md#class_int) ) const |
| [Plane](class_plane.md#class_Plane) | [get_projection_plane](class_projection.md#class_Projection_method_get_projection_plane) ( plane: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_viewport_half_extents](class_projection.md#class_Projection_method_get_viewport_half_extents) ( ) const |
| [float](class_float.md#class_float) | [get_z_far](class_projection.md#class_Projection_method_get_z_far) ( ) const |
| [float](class_float.md#class_float) | [get_z_near](class_projection.md#class_Projection_method_get_z_near) ( ) const |
| [Projection](class_projection.md#class_Projection) | [inverse](class_projection.md#class_Projection_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_orthogonal](class_projection.md#class_Projection_method_is_orthogonal) ( ) const |
| [Projection](class_projection.md#class_Projection) | [jitter_offseted](class_projection.md#class_Projection_method_jitter_offseted) ( offset: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Projection](class_projection.md#class_Projection) | [perspective_znear_adjusted](class_projection.md#class_Projection_method_perspective_znear_adjusted) ( new_znear: [float](class_float.md#class_float) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_projection.md#class_Projection_operator_neq_Projection) ( right: [Projection](class_projection.md#class_Projection) ) |
| --- | --- |
| [Projection](class_projection.md#class_Projection) | [operator *](class_projection.md#class_Projection_operator_mul_Projection) ( right: [Projection](class_projection.md#class_Projection) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_projection.md#class_Projection_operator_mul_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_projection.md#class_Projection_operator_eq_Projection) ( right: [Projection](class_projection.md#class_Projection) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator []](class_projection.md#class_Projection_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Enumerations

<span id="enum_Projection_Planes"></span>

enum **Planes**: [🔗](class_projection.md#enum_Projection_Planes)

<span id="class_Projection_constant_PLANE_NEAR"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_NEAR** = `0`

The index value of the projection's near clipping plane.

<span id="class_Projection_constant_PLANE_FAR"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_FAR** = `1`

The index value of the projection's far clipping plane.

<span id="class_Projection_constant_PLANE_LEFT"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_LEFT** = `2`

The index value of the projection's left clipping plane.

<span id="class_Projection_constant_PLANE_TOP"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_TOP** = `3`

The index value of the projection's top clipping plane.

<span id="class_Projection_constant_PLANE_RIGHT"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_RIGHT** = `4`

The index value of the projection's right clipping plane.

<span id="class_Projection_constant_PLANE_BOTTOM"></span>

[Planes](class_projection.md#enum_Projection_Planes) **PLANE_BOTTOM** = `5`

The index value of the projection bottom clipping plane.

---

### Constants

<span id="class_Projection_constant_IDENTITY"></span>

**IDENTITY** = `Projection(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)` [🔗](class_projection.md#class_Projection_constant_IDENTITY)

A **Projection** with no transformation defined. When applied to other data structures, no transformation is performed.

<span id="class_Projection_constant_ZERO"></span>

**ZERO** = `Projection(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)` [🔗](class_projection.md#class_Projection_constant_ZERO)

A **Projection** with all values initialized to 0. When applied to other data structures, they will be zeroed.

---

### Property Descriptions

<span id="class_Projection_property_w"></span>

[Vector4](class_vector4.md#class_Vector4) **w** = `Vector4(0, 0, 0, 1)` [🔗](class_projection.md#class_Projection_property_w)

The projection matrix's W vector (column 3). Equivalent to array index `3`.

---

<span id="class_Projection_property_x"></span>

[Vector4](class_vector4.md#class_Vector4) **x** = `Vector4(1, 0, 0, 0)` [🔗](class_projection.md#class_Projection_property_x)

The projection matrix's X vector (column 0). Equivalent to array index `0`.

---

<span id="class_Projection_property_y"></span>

[Vector4](class_vector4.md#class_Vector4) **y** = `Vector4(0, 1, 0, 0)` [🔗](class_projection.md#class_Projection_property_y)

The projection matrix's Y vector (column 1). Equivalent to array index `1`.

---

<span id="class_Projection_property_z"></span>

[Vector4](class_vector4.md#class_Vector4) **z** = `Vector4(0, 0, 1, 0)` [🔗](class_projection.md#class_Projection_property_z)

The projection matrix's Z vector (column 2). Equivalent to array index `2`.

---

### Constructor Descriptions

<span id="class_Projection_constructor_Projection"></span>

[Projection](class_projection.md#class_Projection) **Projection** ( ) [🔗](class_projection.md#class_Projection_constructor_Projection)

Constructs a default-initialized **Projection** identical to [IDENTITY](class_projection.md#class_Projection_constant_IDENTITY).

 **Note:** In C#, this constructs a **Projection** identical to [ZERO](class_projection.md#class_Projection_constant_ZERO).

---

[Projection](class_projection.md#class_Projection) **Projection** ( from: [Projection](class_projection.md#class_Projection) )

Constructs a **Projection** as a copy of the given **Projection**.

---

[Projection](class_projection.md#class_Projection) **Projection** ( from: [Transform3D](class_transform3d.md#class_Transform3D) )

Constructs a Projection as a copy of the given [Transform3D](class_transform3d.md#class_Transform3D).

---

[Projection](class_projection.md#class_Projection) **Projection** ( x_axis: [Vector4](class_vector4.md#class_Vector4), y_axis: [Vector4](class_vector4.md#class_Vector4), z_axis: [Vector4](class_vector4.md#class_Vector4), w_axis: [Vector4](class_vector4.md#class_Vector4) )

Constructs a Projection from four [Vector4](class_vector4.md#class_Vector4) values (matrix columns).

---

### Method Descriptions

<span id="class_Projection_method_create_depth_correction"></span>

[Projection](class_projection.md#class_Projection) **create_depth_correction** ( flip_y: [bool](class_bool.md#class_bool) ) *static* [🔗](class_projection.md#class_Projection_method_create_depth_correction)

Creates a new **Projection** that projects positions from a depth range of `-1` to `1` to one that ranges from `0` to `1`, and flips the projected positions vertically, according to `flip_y`.

---

<span id="class_Projection_method_create_fit_aabb"></span>

[Projection](class_projection.md#class_Projection) **create_fit_aabb** ( aabb: [AABB](class_aabb.md#class_AABB) ) *static* [🔗](class_projection.md#class_Projection_method_create_fit_aabb)

Creates a new **Projection** that scales a given projection to fit around a given [AABB](class_aabb.md#class_AABB) in projection space.

---

<span id="class_Projection_method_create_for_hmd"></span>

[Projection](class_projection.md#class_Projection) **create_for_hmd** ( eye: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), intraocular_dist: [float](class_float.md#class_float), display_width: [float](class_float.md#class_float), display_to_lens: [float](class_float.md#class_float), oversample: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) *static* [🔗](class_projection.md#class_Projection_method_create_for_hmd)

Creates a new **Projection** for projecting positions onto a head-mounted display with the given X:Y aspect ratio, distance between eyes, display width, distance to lens, oversampling factor, and depth clipping planes.

 `eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

---

<span id="class_Projection_method_create_frustum"></span>

[Projection](class_projection.md#class_Projection) **create_frustum** ( left: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float), top: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) *static* [🔗](class_projection.md#class_Projection_method_create_frustum)

Creates a new **Projection** that projects positions in a frustum with the given clipping planes.

---

<span id="class_Projection_method_create_frustum_aspect"></span>

[Projection](class_projection.md#class_Projection) **create_frustum_aspect** ( size: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), offset: [Vector2](class_vector2.md#class_Vector2), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) *static* [🔗](class_projection.md#class_Projection_method_create_frustum_aspect)

Creates a new **Projection** that projects positions in a frustum with the given size, X:Y aspect ratio, offset, and clipping planes.

 `flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

<span id="class_Projection_method_create_light_atlas_rect"></span>

[Projection](class_projection.md#class_Projection) **create_light_atlas_rect** ( rect: [Rect2](class_rect2.md#class_Rect2) ) *static* [🔗](class_projection.md#class_Projection_method_create_light_atlas_rect)

Creates a new **Projection** that projects positions into the given [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_Projection_method_create_orthogonal"></span>

[Projection](class_projection.md#class_Projection) **create_orthogonal** ( left: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float), top: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) *static* [🔗](class_projection.md#class_Projection_method_create_orthogonal)

Creates a new **Projection** that projects positions using an orthogonal projection with the given clipping planes.

---

<span id="class_Projection_method_create_orthogonal_aspect"></span>

[Projection](class_projection.md#class_Projection) **create_orthogonal_aspect** ( size: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) *static* [🔗](class_projection.md#class_Projection_method_create_orthogonal_aspect)

Creates a new **Projection** that projects positions using an orthogonal projection with the given size, X:Y aspect ratio, and clipping planes.

 `flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

<span id="class_Projection_method_create_perspective"></span>

[Projection](class_projection.md#class_Projection) **create_perspective** ( fovy: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool) = false ) *static* [🔗](class_projection.md#class_Projection_method_create_perspective)

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping planes.

 `flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

<span id="class_Projection_method_create_perspective_hmd"></span>

[Projection](class_projection.md#class_Projection) **create_perspective_hmd** ( fovy: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float), flip_fov: [bool](class_bool.md#class_bool), eye: [int](class_int.md#class_int), intraocular_dist: [float](class_float.md#class_float), convergence_dist: [float](class_float.md#class_float) ) *static* [🔗](class_projection.md#class_Projection_method_create_perspective_hmd)

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping distances. The projection is adjusted for a head-mounted display with the given distance between eyes and distance to a point that can be focused on.

 `eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

 `flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

<span id="class_Projection_method_determinant"></span>

[float](class_float.md#class_float) **determinant** ( ) *const* [🔗](class_projection.md#class_Projection_method_determinant)

Returns a scalar value that is the signed factor by which areas are scaled by this matrix. If the sign is negative, the matrix flips the orientation of the area.

The determinant can be used to calculate the invertibility of a matrix or solve linear systems of equations involving the matrix, among other applications.

---

<span id="class_Projection_method_flipped_y"></span>

[Projection](class_projection.md#class_Projection) **flipped_y** ( ) *const* [🔗](class_projection.md#class_Projection_method_flipped_y)

Returns a copy of this **Projection** with the signs of the values of the Y column flipped.

---

<span id="class_Projection_method_get_aspect"></span>

[float](class_float.md#class_float) **get_aspect** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_aspect)

Returns the X:Y aspect ratio of this **Projection**'s viewport.

---

<span id="class_Projection_method_get_far_plane_half_extents"></span>

[Vector2](class_vector2.md#class_Vector2) **get_far_plane_half_extents** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_far_plane_half_extents)

Returns the dimensions of the far clipping plane of the projection, divided by two.

---

<span id="class_Projection_method_get_fov"></span>

[float](class_float.md#class_float) **get_fov** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_fov)

Returns the horizontal field of view of the projection (in degrees).

---

<span id="class_Projection_method_get_fovy"></span>

[float](class_float.md#class_float) **get_fovy** ( fovx: [float](class_float.md#class_float), aspect: [float](class_float.md#class_float) ) *static* [🔗](class_projection.md#class_Projection_method_get_fovy)

Returns the vertical field of view of the projection (in degrees) associated with the given horizontal field of view (in degrees) and aspect ratio.

 **Note:** Unlike most methods of **Projection**, `aspect` is expected to be 1 divided by the X:Y aspect ratio.

---

<span id="class_Projection_method_get_lod_multiplier"></span>

[float](class_float.md#class_float) **get_lod_multiplier** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_lod_multiplier)

Returns the factor by which the visible level of detail is scaled by this **Projection**.

---

<span id="class_Projection_method_get_pixels_per_meter"></span>

[int](class_int.md#class_int) **get_pixels_per_meter** ( for_pixel_width: [int](class_int.md#class_int) ) *const* [🔗](class_projection.md#class_Projection_method_get_pixels_per_meter)

Returns `for_pixel_width` divided by the viewport's width measured in meters on the near plane, after this **Projection** is applied.

---

<span id="class_Projection_method_get_projection_plane"></span>

[Plane](class_plane.md#class_Plane) **get_projection_plane** ( plane: [int](class_int.md#class_int) ) *const* [🔗](class_projection.md#class_Projection_method_get_projection_plane)

Returns the clipping plane of this **Projection** whose index is given by `plane`.

 `plane` should be equal to one of [PLANE_NEAR](class_projection.md#class_Projection_constant_PLANE_NEAR), [PLANE_FAR](class_projection.md#class_Projection_constant_PLANE_FAR), [PLANE_LEFT](class_projection.md#class_Projection_constant_PLANE_LEFT), [PLANE_TOP](class_projection.md#class_Projection_constant_PLANE_TOP), [PLANE_RIGHT](class_projection.md#class_Projection_constant_PLANE_RIGHT), or [PLANE_BOTTOM](class_projection.md#class_Projection_constant_PLANE_BOTTOM).

---

<span id="class_Projection_method_get_viewport_half_extents"></span>

[Vector2](class_vector2.md#class_Vector2) **get_viewport_half_extents** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_viewport_half_extents)

Returns the dimensions of the viewport plane that this **Projection** projects positions onto, divided by two.

---

<span id="class_Projection_method_get_z_far"></span>

[float](class_float.md#class_float) **get_z_far** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_z_far)

Returns the distance for this **Projection** beyond which positions are clipped.

---

<span id="class_Projection_method_get_z_near"></span>

[float](class_float.md#class_float) **get_z_near** ( ) *const* [🔗](class_projection.md#class_Projection_method_get_z_near)

Returns the distance for this **Projection** before which positions are clipped.

---

<span id="class_Projection_method_inverse"></span>

[Projection](class_projection.md#class_Projection) **inverse** ( ) *const* [🔗](class_projection.md#class_Projection_method_inverse)

Returns a **Projection** that performs the inverse of this **Projection**'s projective transformation.

---

<span id="class_Projection_method_is_orthogonal"></span>

[bool](class_bool.md#class_bool) **is_orthogonal** ( ) *const* [🔗](class_projection.md#class_Projection_method_is_orthogonal)

Returns `true` if this **Projection** performs an orthogonal projection.

---

<span id="class_Projection_method_jitter_offseted"></span>

[Projection](class_projection.md#class_Projection) **jitter_offseted** ( offset: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_projection.md#class_Projection_method_jitter_offseted)

Returns a **Projection** with the X and Y values from the given [Vector2](class_vector2.md#class_Vector2) added to the first and second values of the final column respectively.

---

<span id="class_Projection_method_perspective_znear_adjusted"></span>

[Projection](class_projection.md#class_Projection) **perspective_znear_adjusted** ( new_znear: [float](class_float.md#class_float) ) *const* [🔗](class_projection.md#class_Projection_method_perspective_znear_adjusted)

Returns a **Projection** with the near clipping distance adjusted to be `new_znear`.

 **Note:** The original **Projection** must be a perspective projection.

---

### Operator Descriptions

<span id="class_Projection_operator_neq_Projection"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Projection](class_projection.md#class_Projection) ) [🔗](class_projection.md#class_Projection_operator_neq_Projection)

Returns `true` if the projections are not equal.

 **Note:** Due to floating-point precision errors, this may return `true`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

---

<span id="class_Projection_operator_mul_Projection"></span>

[Projection](class_projection.md#class_Projection) **operator *** ( right: [Projection](class_projection.md#class_Projection) ) [🔗](class_projection.md#class_Projection_operator_mul_Projection)

Returns a **Projection** that applies the combined transformations of this **Projection** and `right`.

---

<span id="class_Projection_operator_mul_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_projection.md#class_Projection_operator_mul_Vector4)

Projects (multiplies) the given [Vector4](class_vector4.md#class_Vector4) by this **Projection** matrix.

---

<span id="class_Projection_operator_eq_Projection"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Projection](class_projection.md#class_Projection) ) [🔗](class_projection.md#class_Projection_operator_eq_Projection)

Returns `true` if the projections are equal.

 **Note:** Due to floating-point precision errors, this may return `false`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

---

<span id="class_Projection_operator_idx_int"></span>

[Vector4](class_vector4.md#class_Vector4) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_projection.md#class_Projection_operator_idx_int)

Returns the column of the **Projection** with the given index.

Indices are in the following order: x, y, z, w.
