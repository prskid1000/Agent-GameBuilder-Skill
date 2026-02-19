<span id="class_Noise"></span>

## Noise

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [FastNoiseLite](class_fastnoiselite.md#class_FastNoiseLite)

Abstract base class for noise generators.

### Description

This class defines the interface for noise generation libraries to inherit from.

A default [get_seamless_image()](class_noise.md#class_Noise_method_get_seamless_image) implementation is provided for libraries that do not provide seamless noise. This function requests a larger image from the [get_image()](class_noise.md#class_Noise_method_get_image) method, reverses the quadrants of the image, then uses the strips of extra width to blend over the seams.

Inheriting noise classes can optionally override this function to provide a more optimal algorithm.

### Methods


| [Image](class_image.md#class_Image) | [get_image](class_noise.md#class_Noise_method_get_image) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, in_3d_space: [bool](class_bool.md#class_bool) = false, normalize: [bool](class_bool.md#class_bool) = true ) const |
| --- | --- |
| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [get_image_3d](class_noise.md#class_Noise_method_get_image_3d) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, normalize: [bool](class_bool.md#class_bool) = true ) const |
| [float](class_float.md#class_float) | [get_noise_1d](class_noise.md#class_Noise_method_get_noise_1d) ( x: [float](class_float.md#class_float) ) const |
| [float](class_float.md#class_float) | [get_noise_2d](class_noise.md#class_Noise_method_get_noise_2d) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) const |
| [float](class_float.md#class_float) | [get_noise_2dv](class_noise.md#class_Noise_method_get_noise_2dv) ( v: [Vector2](class_vector2.md#class_Vector2) ) const |
| [float](class_float.md#class_float) | [get_noise_3d](class_noise.md#class_Noise_method_get_noise_3d) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float) ) const |
| [float](class_float.md#class_float) | [get_noise_3dv](class_noise.md#class_Noise_method_get_noise_3dv) ( v: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Image](class_image.md#class_Image) | [get_seamless_image](class_noise.md#class_Noise_method_get_seamless_image) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, in_3d_space: [bool](class_bool.md#class_bool) = false, skirt: [float](class_float.md#class_float) = 0.1, normalize: [bool](class_bool.md#class_bool) = true ) const |
| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [get_seamless_image_3d](class_noise.md#class_Noise_method_get_seamless_image_3d) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, skirt: [float](class_float.md#class_float) = 0.1, normalize: [bool](class_bool.md#class_bool) = true ) const |

---

### Method Descriptions

<span id="class_Noise_method_get_image"></span>

[Image](class_image.md#class_Image) **get_image** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, in_3d_space: [bool](class_bool.md#class_bool) = false, normalize: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_noise.md#class_Noise_method_get_image)

Returns an [Image](class_image.md#class_Image) containing 2D noise values.

 **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

<span id="class_Noise_method_get_image_3d"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **get_image_3d** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, normalize: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_noise.md#class_Noise_method_get_image_3d)

Returns an [Array](class_array.md#class_Array) of [Image](class_image.md#class_Image) s containing 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class_ImageTexture3D_method_create).

 **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

<span id="class_Noise_method_get_noise_1d"></span>

[float](class_float.md#class_float) **get_noise_1d** ( x: [float](class_float.md#class_float) ) *const* [🔗](class_noise.md#class_Noise_method_get_noise_1d)

Returns the 1D noise value at the given (x) coordinate.

---

<span id="class_Noise_method_get_noise_2d"></span>

[float](class_float.md#class_float) **get_noise_2d** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float) ) *const* [🔗](class_noise.md#class_Noise_method_get_noise_2d)

Returns the 2D noise value at the given position.

---

<span id="class_Noise_method_get_noise_2dv"></span>

[float](class_float.md#class_float) **get_noise_2dv** ( v: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_noise.md#class_Noise_method_get_noise_2dv)

Returns the 2D noise value at the given position.

---

<span id="class_Noise_method_get_noise_3d"></span>

[float](class_float.md#class_float) **get_noise_3d** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float) ) *const* [🔗](class_noise.md#class_Noise_method_get_noise_3d)

Returns the 3D noise value at the given position.

---

<span id="class_Noise_method_get_noise_3dv"></span>

[float](class_float.md#class_float) **get_noise_3dv** ( v: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_noise.md#class_Noise_method_get_noise_3dv)

Returns the 3D noise value at the given position.

---

<span id="class_Noise_method_get_seamless_image"></span>

[Image](class_image.md#class_Image) **get_seamless_image** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, in_3d_space: [bool](class_bool.md#class_bool) = false, skirt: [float](class_float.md#class_float) = 0.1, normalize: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_noise.md#class_Noise_method_get_seamless_image)

Returns an [Image](class_image.md#class_Image) containing seamless 2D noise values.

 **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

<span id="class_Noise_method_get_seamless_image_3d"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **get_seamless_image_3d** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) = false, skirt: [float](class_float.md#class_float) = 0.1, normalize: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_noise.md#class_Noise_method_get_seamless_image_3d)

Returns an [Array](class_array.md#class_Array) of [Image](class_image.md#class_Image) s containing seamless 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class_ImageTexture3D_method_create).

 **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.
