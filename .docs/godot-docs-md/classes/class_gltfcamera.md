<span id="class_GLTFCamera"></span>

## GLTFCamera

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a glTF camera.

### Description

Represents a camera as defined by the base glTF spec.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

- glTF camera detailed specification

- glTF camera spec and example file

### Properties


| [float](class_float.md#class_float) | [depth_far](class_gltfcamera.md#class_GLTFCamera_property_depth_far) | `4000.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [depth_near](class_gltfcamera.md#class_GLTFCamera_property_depth_near) | `0.05` |
| [float](class_float.md#class_float) | [fov](class_gltfcamera.md#class_GLTFCamera_property_fov) | `1.3089969` |
| [bool](class_bool.md#class_bool) | [perspective](class_gltfcamera.md#class_GLTFCamera_property_perspective) | `true` |
| [float](class_float.md#class_float) | [size_mag](class_gltfcamera.md#class_GLTFCamera_property_size_mag) | `0.5` |

### Methods


| [GLTFCamera](class_gltfcamera.md#class_GLTFCamera) | [from_dictionary](class_gltfcamera.md#class_GLTFCamera_method_from_dictionary) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) static |
| --- | --- |
| [GLTFCamera](class_gltfcamera.md#class_GLTFCamera) | [from_node](class_gltfcamera.md#class_GLTFCamera_method_from_node) ( camera_node: [Camera3D](class_camera3d.md#class_Camera3D) ) static |
| [Dictionary](class_dictionary.md#class_Dictionary) | [to_dictionary](class_gltfcamera.md#class_GLTFCamera_method_to_dictionary) ( ) const |
| [Camera3D](class_camera3d.md#class_Camera3D) | [to_node](class_gltfcamera.md#class_GLTFCamera_method_to_node) ( ) const |

---

### Property Descriptions

<span id="class_GLTFCamera_property_depth_far"></span>

[float](class_float.md#class_float) **depth_far** = `4000.0` [🔗](class_gltfcamera.md#class_GLTFCamera_property_depth_far)

- void **set_depth_far** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_far** ( )

The distance to the far culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `zfar` property.

---

<span id="class_GLTFCamera_property_depth_near"></span>

[float](class_float.md#class_float) **depth_near** = `0.05` [🔗](class_gltfcamera.md#class_GLTFCamera_property_depth_near)

- void **set_depth_near** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_near** ( )

The distance to the near culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `znear` property.

---

<span id="class_GLTFCamera_property_fov"></span>

[float](class_float.md#class_float) **fov** = `1.3089969` [🔗](class_gltfcamera.md#class_GLTFCamera_property_fov)

- void **set_fov** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fov** ( )

The FOV of the camera. This class and glTF define the camera FOV in radians, while Godot uses degrees. This maps to glTF's `yfov` property. This value is only used for perspective cameras, when [perspective](class_gltfcamera.md#class_GLTFCamera_property_perspective) is `true`.

---

<span id="class_GLTFCamera_property_perspective"></span>

[bool](class_bool.md#class_bool) **perspective** = `true` [🔗](class_gltfcamera.md#class_GLTFCamera_property_perspective)

- void **set_perspective** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_perspective** ( )

If `true`, the camera is in perspective mode. Otherwise, the camera is in orthographic/orthogonal mode. This maps to glTF's camera `type` property. See [Camera3D.projection](class_camera3d.md#class_Camera3D_property_projection) and the glTF spec for more information.

---

<span id="class_GLTFCamera_property_size_mag"></span>

[float](class_float.md#class_float) **size_mag** = `0.5` [🔗](class_gltfcamera.md#class_GLTFCamera_property_size_mag)

- void **set_size_mag** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_size_mag** ( )

The size of the camera. This class and glTF define the camera size magnitude as a radius in meters, while Godot defines it as a diameter in meters. This maps to glTF's `ymag` property. This value is only used for orthographic/orthogonal cameras, when [perspective](class_gltfcamera.md#class_GLTFCamera_property_perspective) is `false`.

---

### Method Descriptions

<span id="class_GLTFCamera_method_from_dictionary"></span>

[GLTFCamera](class_gltfcamera.md#class_GLTFCamera) **from_dictionary** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *static* [🔗](class_gltfcamera.md#class_GLTFCamera_method_from_dictionary)

Creates a new GLTFCamera instance by parsing the given [Dictionary](class_dictionary.md#class_Dictionary).

---

<span id="class_GLTFCamera_method_from_node"></span>

[GLTFCamera](class_gltfcamera.md#class_GLTFCamera) **from_node** ( camera_node: [Camera3D](class_camera3d.md#class_Camera3D) ) *static* [🔗](class_gltfcamera.md#class_GLTFCamera_method_from_node)

Create a new GLTFCamera instance from the given Godot [Camera3D](class_camera3d.md#class_Camera3D) node.

---

<span id="class_GLTFCamera_method_to_dictionary"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **to_dictionary** ( ) *const* [🔗](class_gltfcamera.md#class_GLTFCamera_method_to_dictionary)

Serializes this GLTFCamera instance into a [Dictionary](class_dictionary.md#class_Dictionary).

---

<span id="class_GLTFCamera_method_to_node"></span>

[Camera3D](class_camera3d.md#class_Camera3D) **to_node** ( ) *const* [🔗](class_gltfcamera.md#class_GLTFCamera_method_to_node)

Converts this GLTFCamera instance into a Godot [Camera3D](class_camera3d.md#class_Camera3D) node.
