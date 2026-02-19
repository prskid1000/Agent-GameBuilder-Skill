<span id="class_OpenXRRenderModelExtension"></span>

## OpenXRRenderModelExtension

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) **<** [Object](class_object.md#class_Object)

This class implements the OpenXR Render Model Extension.

### Description

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.

### Methods


| [bool](class_bool.md#class_bool) | [is_active](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_is_active) ( ) const |
| --- | --- |
| [RID](class_rid.md#class_RID) | [render_model_create](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_create) ( render_model_id: [int](class_int.md#class_int) ) |
| void | [render_model_destroy](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_destroy) ( render_model: [RID](class_rid.md#class_RID) ) |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [render_model_get_all](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_all) ( ) |
| [int](class_int.md#class_int) | [render_model_get_animatable_node_count](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count) ( render_model: [RID](class_rid.md#class_RID) ) const |
| [String](class_string.md#class_String) | [render_model_get_animatable_node_name](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name) ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [render_model_get_animatable_node_transform](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform) ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) | [render_model_get_confidence](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_confidence) ( render_model: [RID](class_rid.md#class_RID) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [render_model_get_root_transform](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_root_transform) ( render_model: [RID](class_rid.md#class_RID) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [render_model_get_subaction_paths](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths) ( render_model: [RID](class_rid.md#class_RID) ) |
| [String](class_string.md#class_String) | [render_model_get_top_level_path](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_top_level_path) ( render_model: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [render_model_is_animatable_node_visible](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible) ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Node3D](class_node3d.md#class_Node3D) | [render_model_new_scene_instance](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_new_scene_instance) ( render_model: [RID](class_rid.md#class_RID) ) const |

---

### Signals

<span id="class_OpenXRRenderModelExtension_signal_render_model_added"></span>

**render_model_added** ( render_model: [RID](class_rid.md#class_RID) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_signal_render_model_added)

Emitted when a new render model is added.

---

<span id="class_OpenXRRenderModelExtension_signal_render_model_removed"></span>

**render_model_removed** ( render_model: [RID](class_rid.md#class_RID) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_signal_render_model_removed)

Emitted when a render model is removed.

---

<span id="class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed"></span>

**render_model_top_level_path_changed** ( render_model: [RID](class_rid.md#class_RID) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed)

Emitted when the top level path associated with a render model changed.

---

### Method Descriptions

<span id="class_OpenXRRenderModelExtension_method_is_active"></span>

[bool](class_bool.md#class_bool) **is_active** ( ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_is_active)

Returns `true` if OpenXR's render model extension is supported and enabled.

 **Note:** This only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_create"></span>

[RID](class_rid.md#class_RID) **render_model_create** ( render_model_id: [int](class_int.md#class_int) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_create)

Creates a render model object within OpenXR using a render model id.

 **Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_destroy"></span>

void **render_model_destroy** ( render_model: [RID](class_rid.md#class_RID) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_destroy)

Destroys a render model object within OpenXR that was previously created with [render_model_create()](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_create).

 **Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_all"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **render_model_get_all** ( ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_all)

Returns an array of all currently active render models registered with this extension.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count"></span>

[int](class_int.md#class_int) **render_model_get_animatable_node_count** ( render_model: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count)

Returns the number of animatable nodes this render model has.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name"></span>

[String](class_string.md#class_String) **render_model_get_animatable_node_name** ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name)

Returns the name of the given animatable node.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **render_model_get_animatable_node_transform** ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform)

Returns the current local transform for an animatable node. This is updated every frame.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_confidence"></span>

[TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **render_model_get_confidence** ( render_model: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_confidence)

Returns the tracking confidence of the tracking data for the render model.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_root_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **render_model_get_root_transform** ( render_model: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_root_transform)

Returns the root transform of a render model. This is the tracked position relative to our [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) node.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **render_model_get_subaction_paths** ( render_model: [RID](class_rid.md#class_RID) ) [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths)

Returns a list of active subaction paths for this `render_model`.

 **Note:** If different devices are bound to your actions than available in suggested interaction bindings, this information shows paths related to the interaction bindings being mimicked by that device.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_get_top_level_path"></span>

[String](class_string.md#class_String) **render_model_get_top_level_path** ( render_model: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_get_top_level_path)

Returns the top level path associated with this `render_model`. If provided this identifies whether the render model is associated with the player's hands or other body part.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible"></span>

[bool](class_bool.md#class_bool) **render_model_is_animatable_node_visible** ( render_model: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible)

Returns `true` if this animatable node should be visible.

---

<span id="class_OpenXRRenderModelExtension_method_render_model_new_scene_instance"></span>

[Node3D](class_node3d.md#class_Node3D) **render_model_new_scene_instance** ( render_model: [RID](class_rid.md#class_RID) ) *const* [🔗](class_openxrrendermodelextension.md#class_OpenXRRenderModelExtension_method_render_model_new_scene_instance)

Returns an instance of a subscene that contains all [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) nodes that allow you to visualize the render model.
