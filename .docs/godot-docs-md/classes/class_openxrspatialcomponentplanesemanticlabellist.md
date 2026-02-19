<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList"></span>

## OpenXRSpatialComponentPlaneSemanticLabelList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries plane semantic label result data.

### Description

Object for storing the queries plane semantic label result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) | [get_plane_semantic_label](class_openxrspatialcomponentplanesemanticlabellist.md#class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |

---

### Enumerations

<span id="enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel"></span>

enum **PlaneSemanticLabel**: [🔗](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel)

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_constant_PLANE_SEMANTIC_LABEL_UNCATEGORIZED"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **PLANE_SEMANTIC_LABEL_UNCATEGORIZED** = `1`

Uncategorized plane.

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_constant_PLANE_SEMANTIC_LABEL_FLOOR"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **PLANE_SEMANTIC_LABEL_FLOOR** = `2`

Plane represents a floor.

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_constant_PLANE_SEMANTIC_LABEL_WALL"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **PLANE_SEMANTIC_LABEL_WALL** = `3`

Plane represents a wall.

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_constant_PLANE_SEMANTIC_LABEL_CEILING"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **PLANE_SEMANTIC_LABEL_CEILING** = `4`

Plane represents a ceiling.

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_constant_PLANE_SEMANTIC_LABEL_TABLE"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **PLANE_SEMANTIC_LABEL_TABLE** = `5`

Plane represents the surface of a table.

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label"></span>

[PlaneSemanticLabel](class_openxrspatialcomponentplanesemanticlabellist.md#enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel) **get_plane_semantic_label** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentplanesemanticlabellist.md#class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label)

Returns the plane semantic label for the parent entity at this `index`.
