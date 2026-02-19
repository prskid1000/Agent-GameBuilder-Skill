<span id="class_NavigationPathQueryResult3D"></span>

## NavigationPathQueryResult3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents the result of a 3D pathfinding query.

### Description

This class stores the result of a 3D navigation path query from the [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D).

### Tutorials

- [Using NavigationPathQueryObjects](../tutorials/navigation/navigation_using_navigationpathqueryobjects.md)

### Properties


| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [path](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path) | `PackedVector3Array()` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [path_length](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_length) | `0.0` |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [path_owner_ids](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_owner_ids) | `PackedInt64Array()` |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [path_rids](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_rids) | `[]` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [path_types](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_types) | `PackedInt32Array()` |

### Methods


| void | [reset](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_method_reset) ( ) |
| --- | --- |

---

### Enumerations

<span id="enum_NavigationPathQueryResult3D_PathSegmentType"></span>

enum **PathSegmentType**: [🔗](class_navigationpathqueryresult3d.md#enum_NavigationPathQueryResult3D_PathSegmentType)

<span id="class_NavigationPathQueryResult3D_constant_PATH_SEGMENT_TYPE_REGION"></span>

[PathSegmentType](class_navigationpathqueryresult3d.md#enum_NavigationPathQueryResult3D_PathSegmentType) **PATH_SEGMENT_TYPE_REGION** = `0`

This segment of the path goes through a region.

<span id="class_NavigationPathQueryResult3D_constant_PATH_SEGMENT_TYPE_LINK"></span>

[PathSegmentType](class_navigationpathqueryresult3d.md#enum_NavigationPathQueryResult3D_PathSegmentType) **PATH_SEGMENT_TYPE_LINK** = `1`

This segment of the path goes through a link.

---

### Property Descriptions

<span id="class_NavigationPathQueryResult3D_property_path"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **path** = `PackedVector3Array()` [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path)

- void **set_path** ( value: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) )
- [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_path** ( )

The resulting path array from the navigation query. All path array positions are in global coordinates. Without customized query parameters this is the same path as returned by [NavigationServer3D.map_get_path()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) for more details.

---

<span id="class_NavigationPathQueryResult3D_property_path_length"></span>

[float](class_float.md#class_float) **path_length** = `0.0` [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_length)

- void **set_path_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_path_length** ( )

Returns the length of the path.

---

<span id="class_NavigationPathQueryResult3D_property_path_owner_ids"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **path_owner_ids** = `PackedInt64Array()` [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_owner_ids)

- void **set_path_owner_ids** ( value: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) )
- [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_path_owner_ids** ( )

The `ObjectID` s of the [Object](class_object.md#class_Object) s which manage the regions and links each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) for more details.

---

<span id="class_NavigationPathQueryResult3D_property_path_rids"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **path_rids** = `[]` [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_rids)

- void **set_path_rids** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_path_rids** ( )

The [RID](class_rid.md#class_RID) s of the regions and links that each point of the path goes through.

---

<span id="class_NavigationPathQueryResult3D_property_path_types"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **path_types** = `PackedInt32Array()` [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_property_path_types)

- void **set_path_types** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_path_types** ( )

The type of navigation primitive (region or link) that each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

### Method Descriptions

<span id="class_NavigationPathQueryResult3D_method_reset"></span>

void **reset** ( ) [🔗](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D_method_reset)

Reset the result object to its initial state. This is useful to reuse the object across multiple queries.
