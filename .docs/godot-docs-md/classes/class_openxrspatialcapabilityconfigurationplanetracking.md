<span id="class_OpenXRSpatialCapabilityConfigurationPlaneTracking"></span>

## OpenXRSpatialCapabilityConfigurationPlaneTracking

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader](class_openxrspatialcapabilityconfigurationbaseheader.md#class_OpenXRSpatialCapabilityConfigurationBaseHeader) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration header for plane tracking.

### Description

Configuration header for plane tracking. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_create_spatial_context) to create a spatial context with plane tracking capabilities.

### Methods


| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [get_enabled_components](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_get_enabled_components) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [supports_labels](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_labels) ( ) |
| [bool](class_bool.md#class_bool) | [supports_mesh_2d](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_mesh_2d) ( ) |
| [bool](class_bool.md#class_bool) | [supports_polygons](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_polygons) ( ) |

---

### Method Descriptions

<span id="class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_get_enabled_components"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_enabled_components** ( ) *const* [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_get_enabled_components)

Returns the components enabled by this configuration.

 **Note:** Only valid after this configuration was used to create a spatial context.

---

<span id="class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_labels"></span>

[bool](class_bool.md#class_bool) **supports_labels** ( ) [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_labels)

Returns `true` if we support the plane semantic label component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class_OpenXRSpatialComponentPlaneSemanticLabelList) data object.

---

<span id="class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_mesh_2d"></span>

[bool](class_bool.md#class_bool) **supports_mesh_2d** ( ) [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_mesh_2d)

Returns `true` if we support the mesh 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class_OpenXRSpatialComponentMesh2DList) data object.

---

<span id="class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_polygons"></span>

[bool](class_bool.md#class_bool) **supports_polygons** ( ) [🔗](class_openxrspatialcapabilityconfigurationplanetracking.md#class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_polygons)

Returns `true` if we support the polygon 2D component (only valid after the OpenXR session has started). You can query these using the [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList) data object.
