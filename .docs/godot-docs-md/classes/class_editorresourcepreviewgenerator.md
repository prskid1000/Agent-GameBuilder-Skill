<span id="class_EditorResourcePreviewGenerator"></span>

## EditorResourcePreviewGenerator

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Custom generator of previews.

### Description

Custom code to generate previews. Check EditorSettings.filesystem/file_dialog/thumbnail_size to find a proper size to generate previews at.

### Methods


| [bool](class_bool.md#class_bool) | [_can_generate_small_preview](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview) ( ) | virtual | const |
| --- | --- | --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_generate](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate) ( resource: [Resource](class_resource.md#class_Resource), size: [Vector2i](class_vector2i.md#class_Vector2i), metadata: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | required | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_generate_from_path](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_from_path) ( path: [String](class_string.md#class_String), size: [Vector2i](class_vector2i.md#class_Vector2i), metadata: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_generate_small_preview_automatically](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_handles](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__handles) ( type: [String](class_string.md#class_String) ) | virtual | required | const |
| void | [request_draw_and_wait](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_method_request_draw_and_wait) ( viewport: [RID](class_rid.md#class_RID) ) const |

---

### Method Descriptions

<span id="class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview"></span>

[bool](class_bool.md#class_bool) **_can_generate_small_preview** ( ) *virtual* *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview)

If this function returns `true`, the generator will call [_generate()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate) or [_generate_from_path()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_from_path) for small previews as well.

By default, it returns `false`.

---

<span id="class_EditorResourcePreviewGenerator_private_method__generate"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_generate** ( resource: [Resource](class_resource.md#class_Resource), size: [Vector2i](class_vector2i.md#class_Vector2i), metadata: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* |required| *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate)

Generate a preview from a given resource with the specified size. This must always be implemented.

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

 `metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path) (like image size, sample length etc.).

---

<span id="class_EditorResourcePreviewGenerator_private_method__generate_from_path"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_generate_from_path** ( path: [String](class_string.md#class_String), size: [Vector2i](class_vector2i.md#class_Vector2i), metadata: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_from_path)

Generate a preview directly from a path with the specified size. Implementing this is optional, as default code will load and call [_generate()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate).

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

 `metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path) (like image size, sample length etc.).

---

<span id="class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically"></span>

[bool](class_bool.md#class_bool) **_generate_small_preview_automatically** ( ) *virtual* *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically)

If this function returns `true`, the generator will automatically generate the small previews from the normal preview texture generated by the methods [_generate()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate) or [_generate_from_path()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate_from_path).

By default, it returns `false`.

---

<span id="class_EditorResourcePreviewGenerator_private_method__handles"></span>

[bool](class_bool.md#class_bool) **_handles** ( type: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__handles)

Returns `true` if your generator supports the resource of type `type`.

---

<span id="class_EditorResourcePreviewGenerator_method_request_draw_and_wait"></span>

void **request_draw_and_wait** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_method_request_draw_and_wait)

Call from within [_generate()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate) to request the rendering server draw to the `viewport`.
