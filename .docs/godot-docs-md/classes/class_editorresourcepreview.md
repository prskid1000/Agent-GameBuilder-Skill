<span id="class_EditorResourcePreview"></span>

## EditorResourcePreview

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node used to generate previews of resources or files.

### Description

This node is used to generate previews for resources or files.

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_previewer()](class_editorinterface.md#class_EditorInterface_method_get_resource_previewer).

### Methods


| void | [add_preview_generator](class_editorresourcepreview.md#class_EditorResourcePreview_method_add_preview_generator) ( generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator) ) |
| --- | --- |
| void | [check_for_invalidation](class_editorresourcepreview.md#class_EditorResourcePreview_method_check_for_invalidation) ( path: [String](class_string.md#class_String) ) |
| void | [queue_edited_resource_preview](class_editorresourcepreview.md#class_EditorResourcePreview_method_queue_edited_resource_preview) ( resource: [Resource](class_resource.md#class_Resource), receiver: [Object](class_object.md#class_Object), receiver_func: [StringName](class_stringname.md#class_StringName), userdata: [Variant](class_variant.md#class_Variant) ) |
| void | [queue_resource_preview](class_editorresourcepreview.md#class_EditorResourcePreview_method_queue_resource_preview) ( path: [String](class_string.md#class_String), receiver: [Object](class_object.md#class_Object), receiver_func: [StringName](class_stringname.md#class_StringName), userdata: [Variant](class_variant.md#class_Variant) ) |
| void | [remove_preview_generator](class_editorresourcepreview.md#class_EditorResourcePreview_method_remove_preview_generator) ( generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator) ) |

---

### Signals

<span id="class_EditorResourcePreview_signal_preview_invalidated"></span>

**preview_invalidated** ( path: [String](class_string.md#class_String) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_signal_preview_invalidated)

Emitted if a preview was invalidated (changed). `path` corresponds to the path of the preview.

---

### Method Descriptions

<span id="class_EditorResourcePreview_method_add_preview_generator"></span>

void **add_preview_generator** ( generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_method_add_preview_generator)

Create an own, custom preview generator.

---

<span id="class_EditorResourcePreview_method_check_for_invalidation"></span>

void **check_for_invalidation** ( path: [String](class_string.md#class_String) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_method_check_for_invalidation)

Check if the resource changed, if so, it will be invalidated and the corresponding signal emitted.

---

<span id="class_EditorResourcePreview_method_queue_edited_resource_preview"></span>

void **queue_edited_resource_preview** ( resource: [Resource](class_resource.md#class_Resource), receiver: [Object](class_object.md#class_Object), receiver_func: [StringName](class_stringname.md#class_StringName), userdata: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_method_queue_edited_resource_preview)

Queue the `resource` being edited for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class_String) path, [Texture2D](class_texture2d.md#class_Texture2D) preview, [Texture2D](class_texture2d.md#class_Texture2D) thumbnail_preview, [Variant](class_variant.md#class_Variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

 **Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---

<span id="class_EditorResourcePreview_method_queue_resource_preview"></span>

void **queue_resource_preview** ( path: [String](class_string.md#class_String), receiver: [Object](class_object.md#class_Object), receiver_func: [StringName](class_stringname.md#class_StringName), userdata: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_method_queue_resource_preview)

Queue a resource file located at `path` for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class_String) path, [Texture2D](class_texture2d.md#class_Texture2D) preview, [Texture2D](class_texture2d.md#class_Texture2D) thumbnail_preview, [Variant](class_variant.md#class_Variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

 **Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---

<span id="class_EditorResourcePreview_method_remove_preview_generator"></span>

void **remove_preview_generator** ( generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator) ) [🔗](class_editorresourcepreview.md#class_EditorResourcePreview_method_remove_preview_generator)

Removes a custom preview generator.
