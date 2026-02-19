<span id="class_OpenXRSpatialAnchorCapability"></span>

## OpenXRSpatialAnchorCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) **<** [Object](class_object.md#class_Object)

Implementation for handling spatial entity anchor logic.

### Description

This is an internal class that handles the OpenXR anchor spatial entity extension.

### Methods


| [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker) | [create_new_anchor](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_new_anchor) ( transform: [Transform3D](class_transform3d.md#class_Transform3D), spatial_context: [RID](class_rid.md#class_RID) = RID() ) |
| --- | --- |
| [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) | [create_persistence_context](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_persistence_context) ( scope: [PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [free_persistence_context](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_free_persistence_context) ( persistence_context: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [get_persistence_context_handle](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_get_persistence_context_handle) ( persistence_context: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [is_persistence_scope_supported](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_persistence_scope_supported) ( scope: [PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope) ) |
| [bool](class_bool.md#class_bool) | [is_spatial_anchor_supported](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_spatial_anchor_supported) ( ) |
| [bool](class_bool.md#class_bool) | [is_spatial_persistence_supported](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_spatial_persistence_supported) ( ) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) | [persist_anchor](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_persist_anchor) ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker), persistence_context: [RID](class_rid.md#class_RID) = RID(), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [remove_anchor](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_remove_anchor) ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker) ) |
| [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) | [unpersist_anchor](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_unpersist_anchor) ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker), persistence_context: [RID](class_rid.md#class_RID) = RID(), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) |

---

### Enumerations

<span id="enum_OpenXRSpatialAnchorCapability_PersistenceScope"></span>

enum **PersistenceScope**: [🔗](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope)

<span id="class_OpenXRSpatialAnchorCapability_constant_PERSISTENCE_SCOPE_SYSTEM_MANAGED"></span>

[PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope) **PERSISTENCE_SCOPE_SYSTEM_MANAGED** = `1`

Provides the application with read-only access (i.e. application cannot modify this scope) to spatial entities persisted and managed by the system. The application can use the UUID in the persistence component for this scope to correlate entities across spatial contexts and device reboots.

<span id="class_OpenXRSpatialAnchorCapability_constant_PERSISTENCE_SCOPE_LOCAL_ANCHORS"></span>

[PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope) **PERSISTENCE_SCOPE_LOCAL_ANCHORS** = `1000781000`

Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and same app (using [persist_anchor()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_persist_anchor) and [unpersist_anchor()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_unpersist_anchor) functions)

---

### Method Descriptions

<span id="class_OpenXRSpatialAnchorCapability_method_create_new_anchor"></span>

[OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker) **create_new_anchor** ( transform: [Transform3D](class_transform3d.md#class_Transform3D), spatial_context: [RID](class_rid.md#class_RID) = RID() ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_new_anchor)

Creates a new anchor that will be tracked by the XR runtime. The `transform` should be a transform in the local space of your [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) node. If `spatial_context` is not specified the default will be used, this requires ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection to be set. The returned tracker will track the location in case our reference space changes.

---

<span id="class_OpenXRSpatialAnchorCapability_method_create_persistence_context"></span>

[OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) **create_persistence_context** ( scope: [PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_persistence_context)

Creates a new persistence context for storing persistent data.

 **Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is the [RID](class_rid.md#class_RID) for our persistence context.

---

<span id="class_OpenXRSpatialAnchorCapability_method_free_persistence_context"></span>

void **free_persistence_context** ( persistence_context: [RID](class_rid.md#class_RID) ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_free_persistence_context)

Frees a persistence context previously created with [create_persistence_context()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_persistence_context).

---

<span id="class_OpenXRSpatialAnchorCapability_method_get_persistence_context_handle"></span>

[int](class_int.md#class_int) **get_persistence_context_handle** ( persistence_context: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_get_persistence_context_handle)

Returns the internal handle for this persistence context.

 **Note:** For GDExtension implementations.

---

<span id="class_OpenXRSpatialAnchorCapability_method_is_persistence_scope_supported"></span>

[bool](class_bool.md#class_bool) **is_persistence_scope_supported** ( scope: [PersistenceScope](class_openxrspatialanchorcapability.md#enum_OpenXRSpatialAnchorCapability_PersistenceScope) ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_persistence_scope_supported)

Returns `true` if this persistence scope is supported by our spatial anchor capability.

 **Note:** Only valid after an OpenXR instance has been created.

---

<span id="class_OpenXRSpatialAnchorCapability_method_is_spatial_anchor_supported"></span>

[bool](class_bool.md#class_bool) **is_spatial_anchor_supported** ( ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_spatial_anchor_supported)

Returns `true` if spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRSpatialAnchorCapability_method_is_spatial_persistence_supported"></span>

[bool](class_bool.md#class_bool) **is_spatial_persistence_supported** ( ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_is_spatial_persistence_supported)

Returns `true` if persistent spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRSpatialAnchorCapability_method_persist_anchor"></span>

[OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) **persist_anchor** ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker), persistence_context: [RID](class_rid.md#class_RID) = RID(), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_persist_anchor)

Changes this anchor into a persistent anchor. This means its location will be stored on the device and the anchor will be restored the next time your application starts. If `persistence_context` is not specified the default will be used, this requires ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection to be set.

 **Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.

---

<span id="class_OpenXRSpatialAnchorCapability_method_remove_anchor"></span>

void **remove_anchor** ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker) ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_remove_anchor)

Remove an anchor previously created with [create_new_anchor()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_create_new_anchor). If this anchor was persistent you must first call [unpersist_anchor()](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_unpersist_anchor) and await its callback.

---

<span id="class_OpenXRSpatialAnchorCapability_method_unpersist_anchor"></span>

[OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) **unpersist_anchor** ( anchor_tracker: [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker), persistence_context: [RID](class_rid.md#class_RID) = RID(), user_callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_openxrspatialanchorcapability.md#class_OpenXRSpatialAnchorCapability_method_unpersist_anchor)

Removes the persistent data from this anchor. The runtime will not recreate the anchor when your application restarts. If `persistence_context` is not specified the default will be used, this requires ProjectSettings.xr/openxr/extensions/spatial_entity/enabled to be set.

 **Note:** This is an asynchronous method and returns an [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.
