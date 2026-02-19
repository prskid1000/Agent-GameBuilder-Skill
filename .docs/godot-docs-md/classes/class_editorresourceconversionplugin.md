<span id="class_EditorResourceConversionPlugin"></span>

## EditorResourceConversionPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plugin for adding custom converters from one resource format to another in the editor resource picker context menu; for example, converting a [StandardMaterial3D](class_standardmaterial3d.md#class_StandardMaterial3D) to a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial).

### Description

**EditorResourceConversionPlugin** is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

Below shows an example of a basic plugin that will convert an [ImageTexture](class_imagetexture.md#class_ImageTexture) to a [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D).

.. tabs::

```
```

    extends EditorResourceConversionPlugin

    func _handles(resource: Resource):
        return resource is ImageTexture

    func _converts_to():
        return "PortableCompressedTexture2D"

    func _convert(itex: Resource):
        var ptex = PortableCompressedTexture2D.new()
        ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS)
        return ptex

To use an **EditorResourceConversionPlugin**, register it using the [EditorPlugin.add_resource_conversion_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_resource_conversion_plugin) method first.

### Methods


| [Resource](class_resource.md#class_Resource) | [_convert](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__convert) ( resource: [Resource](class_resource.md#class_Resource) ) | virtual | const |
| --- | --- | --- | --- |
| [String](class_string.md#class_String) | [_converts_to](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__converts_to) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_handles](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__handles) ( resource: [Resource](class_resource.md#class_Resource) ) | virtual | const |

---

### Method Descriptions

<span id="class_EditorResourceConversionPlugin_private_method__convert"></span>

[Resource](class_resource.md#class_Resource) **_convert** ( resource: [Resource](class_resource.md#class_Resource) ) *virtual* *const* [🔗](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__convert)

Takes an input [Resource](class_resource.md#class_Resource) and converts it to the type given in [_converts_to()](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__converts_to). The returned [Resource](class_resource.md#class_Resource) is the result of the conversion, and the input [Resource](class_resource.md#class_Resource) remains unchanged.

---

<span id="class_EditorResourceConversionPlugin_private_method__converts_to"></span>

[String](class_string.md#class_String) **_converts_to** ( ) *virtual* *const* [🔗](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__converts_to)

Returns the class name of the target type of [Resource](class_resource.md#class_Resource) that this plugin converts source resources to.

---

<span id="class_EditorResourceConversionPlugin_private_method__handles"></span>

[bool](class_bool.md#class_bool) **_handles** ( resource: [Resource](class_resource.md#class_Resource) ) *virtual* *const* [🔗](class_editorresourceconversionplugin.md#class_EditorResourceConversionPlugin_private_method__handles)

Called to determine whether a particular [Resource](class_resource.md#class_Resource) can be converted to the target resource type by this plugin.
