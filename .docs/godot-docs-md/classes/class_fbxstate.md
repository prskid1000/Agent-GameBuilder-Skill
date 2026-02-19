<span id="class_FBXState"></span>

## FBXState

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFState](class_gltfstate.md#class_GLTFState) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

### Description

The FBXState handles the state data imported from FBX files.

### Properties


| [bool](class_bool.md#class_bool) | [allow_geometry_helper_nodes](class_fbxstate.md#class_FBXState_property_allow_geometry_helper_nodes) | `false` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_FBXState_property_allow_geometry_helper_nodes"></span>

[bool](class_bool.md#class_bool) **allow_geometry_helper_nodes** = `false` [🔗](class_fbxstate.md#class_FBXState_property_allow_geometry_helper_nodes)

- void **set_allow_geometry_helper_nodes** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_allow_geometry_helper_nodes** ( )

If `true`, the import process used auxiliary nodes called geometry helper nodes. These nodes help preserve the pivots and transformations of the original 3D model during import.
