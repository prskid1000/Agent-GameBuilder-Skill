<span id="class_OpenXRSpatialContextPersistenceConfig"></span>

## OpenXRSpatialContextPersistenceConfig

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRStructureBase](class_openxrstructurebase.md#class_OpenXRStructureBase) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration header for spatial persistence.

### Description

Configuration header for spatial persistence. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_create_spatial_context) as the next parameter to create a spatial context with spatial persistence capabilities.

### Methods


| void | [add_persistence_context](class_openxrspatialcontextpersistenceconfig.md#class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context) ( persistence_context: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| void | [remove_persistence_context](class_openxrspatialcontextpersistenceconfig.md#class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context) ( persistence_context: [RID](class_rid.md#class_RID) ) |

---

### Method Descriptions

<span id="class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context"></span>

void **add_persistence_context** ( persistence_context: [RID](class_rid.md#class_RID) ) [🔗](class_openxrspatialcontextpersistenceconfig.md#class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context)

Adds a persistence context to this configuration. You must add at least one persistence context to create a valid configuration. You can create a persistence context by calling [OpenXRSpatialAnchorCapability.create_persistence_context()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_persistence_context).

---

<span id="class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context"></span>

void **remove_persistence_context** ( persistence_context: [RID](class_rid.md#class_RID) ) [🔗](class_openxrspatialcontextpersistenceconfig.md#class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context)

Removes a persistence context.
