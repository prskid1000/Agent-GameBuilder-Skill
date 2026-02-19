<span id="class_FastNoiseLite"></span>

## FastNoiseLite

**Inherits:** [Noise](class_noise.md#class_Noise) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Generates noise using the FastNoiseLite library.

### Description

This class generates noise using the FastNoiseLite library, which is a collection of several noise algorithms including Cellular, Perlin, Value, and more.

Most generated noise values are in the range of `[-1, 1]`, but not always. Some of the cellular noise algorithms return results above `1`.

### Properties


| [CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) | [cellular_distance_function](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_distance_function) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [cellular_jitter](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_jitter) | `1.0` |
| [CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) | [cellular_return_type](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_return_type) | `1` |
| [float](class_float.md#class_float) | [domain_warp_amplitude](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_amplitude) | `30.0` |
| [bool](class_bool.md#class_bool) | [domain_warp_enabled](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_enabled) | `false` |
| [float](class_float.md#class_float) | [domain_warp_fractal_gain](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_gain) | `0.5` |
| [float](class_float.md#class_float) | [domain_warp_fractal_lacunarity](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_lacunarity) | `6.0` |
| [int](class_int.md#class_int) | [domain_warp_fractal_octaves](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_octaves) | `5` |
| [DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) | [domain_warp_fractal_type](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_type) | `1` |
| [float](class_float.md#class_float) | [domain_warp_frequency](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_frequency) | `0.05` |
| [DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) | [domain_warp_type](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_type) | `0` |
| [float](class_float.md#class_float) | [fractal_gain](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_gain) | `0.5` |
| [float](class_float.md#class_float) | [fractal_lacunarity](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_lacunarity) | `2.0` |
| [int](class_int.md#class_int) | [fractal_octaves](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_octaves) | `5` |
| [float](class_float.md#class_float) | [fractal_ping_pong_strength](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_ping_pong_strength) | `2.0` |
| [FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) | [fractal_type](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_type) | `1` |
| [float](class_float.md#class_float) | [fractal_weighted_strength](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_weighted_strength) | `0.0` |
| [float](class_float.md#class_float) | [frequency](class_fastnoiselite.md#class_FastNoiseLite_property_frequency) | `0.01` |
| [NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) | [noise_type](class_fastnoiselite.md#class_FastNoiseLite_property_noise_type) | `1` |
| [Vector3](class_vector3.md#class_Vector3) | [offset](class_fastnoiselite.md#class_FastNoiseLite_property_offset) | `Vector3(0, 0, 0)` |
| [int](class_int.md#class_int) | [seed](class_fastnoiselite.md#class_FastNoiseLite_property_seed) | `0` |

---

### Enumerations

<span id="enum_FastNoiseLite_NoiseType"></span>

enum **NoiseType**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType)

<span id="class_FastNoiseLite_constant_TYPE_VALUE"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_VALUE** = `5`

A lattice of points are assigned random values then interpolated based on neighboring values.

<span id="class_FastNoiseLite_constant_TYPE_VALUE_CUBIC"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_VALUE_CUBIC** = `4`

Similar to value noise ([TYPE_VALUE](class_fastnoiselite.md#class_FastNoiseLite_constant_TYPE_VALUE)), but slower. Has more variance in peaks and valleys.

Cubic noise can be used to avoid certain artifacts when using value noise to create a bumpmap. In general, you should always use this mode if the value noise is being used for a heightmap or bumpmap.

<span id="class_FastNoiseLite_constant_TYPE_PERLIN"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_PERLIN** = `3`

A lattice of random gradients. Their dot products are interpolated to obtain values in between the lattices.

<span id="class_FastNoiseLite_constant_TYPE_CELLULAR"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_CELLULAR** = `2`

Cellular includes both Worley noise and Voronoi diagrams which creates various regions of the same value.

<span id="class_FastNoiseLite_constant_TYPE_SIMPLEX"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_SIMPLEX** = `0`

As opposed to [TYPE_PERLIN](class_fastnoiselite.md#class_FastNoiseLite_constant_TYPE_PERLIN), gradients exist in a simplex lattice rather than a grid lattice, avoiding directional artifacts. Internally uses FastNoiseLite's OpenSimplex2 noise type.

<span id="class_FastNoiseLite_constant_TYPE_SIMPLEX_SMOOTH"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **TYPE_SIMPLEX_SMOOTH** = `1`

Modified, higher quality version of [TYPE_SIMPLEX](class_fastnoiselite.md#class_FastNoiseLite_constant_TYPE_SIMPLEX), but slower. Internally uses FastNoiseLite's OpenSimplex2S noise type.

---

<span id="enum_FastNoiseLite_FractalType"></span>

enum **FractalType**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_FractalType)

<span id="class_FastNoiseLite_constant_FRACTAL_NONE"></span>

[FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **FRACTAL_NONE** = `0`

No fractal noise.

<span id="class_FastNoiseLite_constant_FRACTAL_FBM"></span>

[FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **FRACTAL_FBM** = `1`

Method using Fractional Brownian Motion to combine octaves into a fractal.

<span id="class_FastNoiseLite_constant_FRACTAL_RIDGED"></span>

[FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **FRACTAL_RIDGED** = `2`

Method of combining octaves into a fractal resulting in a "ridged" look.

<span id="class_FastNoiseLite_constant_FRACTAL_PING_PONG"></span>

[FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **FRACTAL_PING_PONG** = `3`

Method of combining octaves into a fractal with a ping pong effect.

---

<span id="enum_FastNoiseLite_CellularDistanceFunction"></span>

enum **CellularDistanceFunction**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction)

<span id="class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN"></span>

[CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **DISTANCE_EUCLIDEAN** = `0`

Euclidean distance to the nearest point.

<span id="class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN_SQUARED"></span>

[CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **DISTANCE_EUCLIDEAN_SQUARED** = `1`

Squared Euclidean distance to the nearest point.

<span id="class_FastNoiseLite_constant_DISTANCE_MANHATTAN"></span>

[CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **DISTANCE_MANHATTAN** = `2`

Manhattan distance (taxicab metric) to the nearest point.

<span id="class_FastNoiseLite_constant_DISTANCE_HYBRID"></span>

[CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **DISTANCE_HYBRID** = `3`

Blend of [DISTANCE_EUCLIDEAN](class_fastnoiselite.md#class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN) and [DISTANCE_MANHATTAN](class_fastnoiselite.md#class_FastNoiseLite_constant_DISTANCE_MANHATTAN) to give curved cell boundaries.

---

<span id="enum_FastNoiseLite_CellularReturnType"></span>

enum **CellularReturnType**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType)

<span id="class_FastNoiseLite_constant_RETURN_CELL_VALUE"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_CELL_VALUE** = `0`

The cellular distance function will return the same value for all points within a cell.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE** = `1`

The cellular distance function will return a value determined by the distance to the nearest point.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE2"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE2** = `2`

The cellular distance function returns the distance to the second-nearest point.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE2_ADD"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE2_ADD** = `3`

The distance to the nearest point is added to the distance to the second-nearest point.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE2_SUB"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE2_SUB** = `4`

The distance to the nearest point is subtracted from the distance to the second-nearest point.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE2_MUL"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE2_MUL** = `5`

The distance to the nearest point is multiplied with the distance to the second-nearest point.

<span id="class_FastNoiseLite_constant_RETURN_DISTANCE2_DIV"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **RETURN_DISTANCE2_DIV** = `6`

The distance to the nearest point is divided by the distance to the second-nearest point.

---

<span id="enum_FastNoiseLite_DomainWarpType"></span>

enum **DomainWarpType**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType)

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_SIMPLEX"></span>

[DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) **DOMAIN_WARP_SIMPLEX** = `0`

The domain is warped using the simplex noise algorithm.

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_SIMPLEX_REDUCED"></span>

[DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) **DOMAIN_WARP_SIMPLEX_REDUCED** = `1`

The domain is warped using a simplified version of the simplex noise algorithm.

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_BASIC_GRID"></span>

[DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) **DOMAIN_WARP_BASIC_GRID** = `2`

The domain is warped using a simple noise grid (not as smooth as the other methods, but more performant).

---

<span id="enum_FastNoiseLite_DomainWarpFractalType"></span>

enum **DomainWarpFractalType**: [🔗](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType)

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_NONE"></span>

[DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) **DOMAIN_WARP_FRACTAL_NONE** = `0`

No fractal noise for warping the space.

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_PROGRESSIVE"></span>

[DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) **DOMAIN_WARP_FRACTAL_PROGRESSIVE** = `1`

Warping the space progressively, octave for octave, resulting in a more "liquified" distortion.

<span id="class_FastNoiseLite_constant_DOMAIN_WARP_FRACTAL_INDEPENDENT"></span>

[DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) **DOMAIN_WARP_FRACTAL_INDEPENDENT** = `2`

Warping the space independently for each octave, resulting in a more chaotic distortion.

---

### Property Descriptions

<span id="class_FastNoiseLite_property_cellular_distance_function"></span>

[CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **cellular_distance_function** = `0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_distance_function)

- void **set_cellular_distance_function** ( value: [CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) )
- [CellularDistanceFunction](class_fastnoiselite.md#enum_FastNoiseLite_CellularDistanceFunction) **get_cellular_distance_function** ( )

Determines how the distance to the nearest/second-nearest point is computed.

---

<span id="class_FastNoiseLite_property_cellular_jitter"></span>

[float](class_float.md#class_float) **cellular_jitter** = `1.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_jitter)

- void **set_cellular_jitter** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cellular_jitter** ( )

Maximum distance a point can move off of its grid position. Set to `0` for an even grid.

---

<span id="class_FastNoiseLite_property_cellular_return_type"></span>

[CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **cellular_return_type** = `1` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_cellular_return_type)

- void **set_cellular_return_type** ( value: [CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) )
- [CellularReturnType](class_fastnoiselite.md#enum_FastNoiseLite_CellularReturnType) **get_cellular_return_type** ( )

Return type from cellular noise calculations.

---

<span id="class_FastNoiseLite_property_domain_warp_amplitude"></span>

[float](class_float.md#class_float) **domain_warp_amplitude** = `30.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_amplitude)

- void **set_domain_warp_amplitude** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_domain_warp_amplitude** ( )

Sets the maximum warp distance from the origin.

---

<span id="class_FastNoiseLite_property_domain_warp_enabled"></span>

[bool](class_bool.md#class_bool) **domain_warp_enabled** = `false` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_enabled)

- void **set_domain_warp_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_domain_warp_enabled** ( )

If enabled, another FastNoiseLite instance is used to warp the space, resulting in a distortion of the noise.

---

<span id="class_FastNoiseLite_property_domain_warp_fractal_gain"></span>

[float](class_float.md#class_float) **domain_warp_fractal_gain** = `0.5` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_gain)

- void **set_domain_warp_fractal_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_domain_warp_fractal_gain** ( )

Determines the strength of each subsequent layer of the noise which is used to warp the space.

A low value places more emphasis on the lower frequency base layers, while a high value puts more emphasis on the higher frequency layers.

---

<span id="class_FastNoiseLite_property_domain_warp_fractal_lacunarity"></span>

[float](class_float.md#class_float) **domain_warp_fractal_lacunarity** = `6.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_lacunarity)

- void **set_domain_warp_fractal_lacunarity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_domain_warp_fractal_lacunarity** ( )

The change in frequency between octaves, also known as "lacunarity", of the fractal noise which warps the space. Increasing this value results in higher octaves, producing noise with finer details and a rougher appearance.

---

<span id="class_FastNoiseLite_property_domain_warp_fractal_octaves"></span>

[int](class_int.md#class_int) **domain_warp_fractal_octaves** = `5` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_octaves)

- void **set_domain_warp_fractal_octaves** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_domain_warp_fractal_octaves** ( )

The number of noise layers that are sampled to get the final value for the fractal noise which warps the space.

---

<span id="class_FastNoiseLite_property_domain_warp_fractal_type"></span>

[DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) **domain_warp_fractal_type** = `1` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_fractal_type)

- void **set_domain_warp_fractal_type** ( value: [DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) )
- [DomainWarpFractalType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpFractalType) **get_domain_warp_fractal_type** ( )

The method for combining octaves into a fractal which is used to warp the space.

---

<span id="class_FastNoiseLite_property_domain_warp_frequency"></span>

[float](class_float.md#class_float) **domain_warp_frequency** = `0.05` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_frequency)

- void **set_domain_warp_frequency** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_domain_warp_frequency** ( )

Frequency of the noise which warps the space. Low frequency results in smooth noise while high frequency results in rougher, more granular noise.

---

<span id="class_FastNoiseLite_property_domain_warp_type"></span>

[DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) **domain_warp_type** = `0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_domain_warp_type)

- void **set_domain_warp_type** ( value: [DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) )
- [DomainWarpType](class_fastnoiselite.md#enum_FastNoiseLite_DomainWarpType) **get_domain_warp_type** ( )

The warp algorithm.

---

<span id="class_FastNoiseLite_property_fractal_gain"></span>

[float](class_float.md#class_float) **fractal_gain** = `0.5` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_gain)

- void **set_fractal_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fractal_gain** ( )

Determines the strength of each subsequent layer of noise in fractal noise.

A low value places more emphasis on the lower frequency base layers, while a high value puts more emphasis on the higher frequency layers.

---

<span id="class_FastNoiseLite_property_fractal_lacunarity"></span>

[float](class_float.md#class_float) **fractal_lacunarity** = `2.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_lacunarity)

- void **set_fractal_lacunarity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fractal_lacunarity** ( )

Frequency multiplier between subsequent octaves. Increasing this value results in higher octaves producing noise with finer details and a rougher appearance.

---

<span id="class_FastNoiseLite_property_fractal_octaves"></span>

[int](class_int.md#class_int) **fractal_octaves** = `5` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_octaves)

- void **set_fractal_octaves** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fractal_octaves** ( )

The number of noise layers that are sampled to get the final value for fractal noise types.

---

<span id="class_FastNoiseLite_property_fractal_ping_pong_strength"></span>

[float](class_float.md#class_float) **fractal_ping_pong_strength** = `2.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_ping_pong_strength)

- void **set_fractal_ping_pong_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fractal_ping_pong_strength** ( )

Sets the strength of the fractal ping pong type.

---

<span id="class_FastNoiseLite_property_fractal_type"></span>

[FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **fractal_type** = `1` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_type)

- void **set_fractal_type** ( value: [FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) )
- [FractalType](class_fastnoiselite.md#enum_FastNoiseLite_FractalType) **get_fractal_type** ( )

The method for combining octaves into a fractal.

---

<span id="class_FastNoiseLite_property_fractal_weighted_strength"></span>

[float](class_float.md#class_float) **fractal_weighted_strength** = `0.0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_fractal_weighted_strength)

- void **set_fractal_weighted_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fractal_weighted_strength** ( )

Higher weighting means higher octaves have less impact if lower octaves have a large impact.

---

<span id="class_FastNoiseLite_property_frequency"></span>

[float](class_float.md#class_float) **frequency** = `0.01` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_frequency)

- void **set_frequency** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_frequency** ( )

The frequency for all noise types. Low frequency results in smooth noise while high frequency results in rougher, more granular noise.

---

<span id="class_FastNoiseLite_property_noise_type"></span>

[NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **noise_type** = `1` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_noise_type)

- void **set_noise_type** ( value: [NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) )
- [NoiseType](class_fastnoiselite.md#enum_FastNoiseLite_NoiseType) **get_noise_type** ( )

The noise algorithm used.

---

<span id="class_FastNoiseLite_property_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **offset** = `Vector3(0, 0, 0)` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_offset)

- void **set_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_offset** ( )

Translate the noise input coordinates by the given [Vector3](class_vector3.md#class_Vector3).

---

<span id="class_FastNoiseLite_property_seed"></span>

[int](class_int.md#class_int) **seed** = `0` [🔗](class_fastnoiselite.md#class_FastNoiseLite_property_seed)

- void **set_seed** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_seed** ( )

The random number seed for all noise types.
