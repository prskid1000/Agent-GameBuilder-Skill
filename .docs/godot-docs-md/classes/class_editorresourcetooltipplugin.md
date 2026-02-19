<span id="class_EditorResourceTooltipPlugin"></span>

## EditorResourceTooltipPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A plugin that advanced tooltip for its handled resource type.

### Description

Resource tooltip plugins are used by [FileSystemDock](class_filesystemdock.md#class_FileSystemDock) to generate customized tooltips for specific resources. E.g. tooltip for a [Texture2D](class_texture2d.md#class_Texture2D) displays a bigger preview and the texture's dimensions.

A plugin must be first registered with [FileSystemDock.add_resource_tooltip_plugin()](class_filesystemdock.md#class_FileSystemDock_method_add_resource_tooltip_plugin). When the user hovers a resource in filesystem dock which is handled by the plugin, [_make_tooltip_for_path()](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path) is called to create the tooltip. It works similarly to [Control._make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip).

### Methods


| [bool](class_bool.md#class_bool) | [_handles](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__handles) ( type: [String](class_string.md#class_String) ) | virtual | const |
| --- | --- | --- | --- |
| [Control](class_control.md#class_Control) | [_make_tooltip_for_path](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path) ( path: [String](class_string.md#class_String), metadata: [Dictionary](class_dictionary.md#class_Dictionary), base: [Control](class_control.md#class_Control) ) | virtual | const |
| void | [request_thumbnail](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_method_request_thumbnail) ( path: [String](class_string.md#class_String), control: [TextureRect](class_texturerect.md#class_TextureRect) ) const |

---

### Method Descriptions

<span id="class_EditorResourceTooltipPlugin_private_method__handles"></span>

[bool](class_bool.md#class_bool) **_handles** ( type: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__handles)

Return `true` if the plugin is going to handle the given [Resource](class_resource.md#class_Resource) `type`.

---

<span id="class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path"></span>

[Control](class_control.md#class_Control) **_make_tooltip_for_path** ( path: [String](class_string.md#class_String), metadata: [Dictionary](class_dictionary.md#class_Dictionary), base: [Control](class_control.md#class_Control) ) *virtual* *const* [🔗](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path)

Create and return a tooltip that will be displayed when the user hovers a resource under the given `path` in filesystem dock.

The `metadata` dictionary is provided by preview generator (see [EditorResourcePreviewGenerator._generate()](class_editorresourcepreviewgenerator.md#class_EditorResourcePreviewGenerator_private_method__generate)).

 `base` is the base default tooltip, which is a [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer) with a file name, type and size labels. If another plugin handled the same file type, `base` will be output from the previous plugin. For best result, make sure the base tooltip is part of the returned [Control](class_control.md#class_Control).

 **Note:** It's unadvised to use [ResourceLoader.load()](class_resourceloader.md#class_ResourceLoader_method_load), especially with heavy resources like models or textures, because it will make the editor unresponsive when creating the tooltip. You can use [request_thumbnail()](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_method_request_thumbnail) if you want to display a preview in your tooltip.

 **Note:** If you decide to discard the `base`, make sure to call [Node.queue_free()](class_node.md#class_Node_method_queue_free), because it's not freed automatically.

::

    func _make_tooltip_for_path(path, metadata, base):
        var t_rect = TextureRect.new()
        request_thumbnail(path, t_rect)
        base.add_child(t_rect) # The TextureRect will appear at the bottom of the tooltip.
        return base

---

<span id="class_EditorResourceTooltipPlugin_method_request_thumbnail"></span>

void **request_thumbnail** ( path: [String](class_string.md#class_String), control: [TextureRect](class_texturerect.md#class_TextureRect) ) *const* [🔗](class_editorresourcetooltipplugin.md#class_EditorResourceTooltipPlugin_method_request_thumbnail)

Requests a thumbnail for the given [TextureRect](class_texturerect.md#class_TextureRect). The thumbnail is created asynchronously by [EditorResourcePreview](class_editorresourcepreview.md#class_EditorResourcePreview) and automatically set when available.
