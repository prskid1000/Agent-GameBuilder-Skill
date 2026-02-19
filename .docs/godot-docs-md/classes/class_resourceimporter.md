<span id="class_ResourceImporter"></span>

## ResourceImporter

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin), [ResourceImporterBitMap](class_resourceimporterbitmap.md#class_ResourceImporterBitMap), [ResourceImporterBMFont](class_resourceimporterbmfont.md#class_ResourceImporterBMFont), [ResourceImporterCSVTranslation](class_resourceimportercsvtranslation.md#class_ResourceImporterCSVTranslation), [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont), [ResourceImporterImage](class_resourceimporterimage.md#class_ResourceImporterImage), [ResourceImporterImageFont](class_resourceimporterimagefont.md#class_ResourceImporterImageFont), [ResourceImporterLayeredTexture](class_resourceimporterlayeredtexture.md#class_ResourceImporterLayeredTexture), [ResourceImporterMP3](class_resourceimportermp3.md#class_ResourceImporterMP3), [ResourceImporterOBJ](class_resourceimporterobj.md#class_ResourceImporterOBJ), [ResourceImporterOggVorbis](class_resourceimporteroggvorbis.md#class_ResourceImporterOggVorbis), [ResourceImporterScene](class_resourceimporterscene.md#class_ResourceImporterScene), [ResourceImporterShaderFile](class_resourceimportershaderfile.md#class_ResourceImporterShaderFile), [ResourceImporterSVG](class_resourceimportersvg.md#class_ResourceImporterSVG), [ResourceImporterTexture](class_resourceimportertexture.md#class_ResourceImporterTexture), [ResourceImporterTextureAtlas](class_resourceimportertextureatlas.md#class_ResourceImporterTextureAtlas), [ResourceImporterWAV](class_resourceimporterwav.md#class_ResourceImporterWAV)

Base class for resource importers.

### Description

This is the base class for Godot's resource importers. To implement your own resource importers using editor plugins, see [EditorImportPlugin](class_editorimportplugin.md#class_EditorImportPlugin).

### Tutorials

- [Import plugins](../tutorials/plugins/editor/import_plugins.md)

### Methods


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_build_dependencies](class_resourceimporter.md#class_ResourceImporter_private_method__get_build_dependencies) ( path: [String](class_string.md#class_String) ) | virtual | const |
| --- | --- | --- | --- |

---

### Enumerations

<span id="enum_ResourceImporter_ImportOrder"></span>

enum **ImportOrder**: [🔗](class_resourceimporter.md#enum_ResourceImporter_ImportOrder)

<span id="class_ResourceImporter_constant_IMPORT_ORDER_DEFAULT"></span>

[ImportOrder](class_resourceimporter.md#enum_ResourceImporter_ImportOrder) **IMPORT_ORDER_DEFAULT** = `0`

The default import order.

<span id="class_ResourceImporter_constant_IMPORT_ORDER_SCENE"></span>

[ImportOrder](class_resourceimporter.md#enum_ResourceImporter_ImportOrder) **IMPORT_ORDER_SCENE** = `100`

The import order for scenes, which ensures scenes are imported *after* all other core resources such as textures. Custom importers should generally have an import order lower than `100` to avoid issues when importing scenes that rely on custom resources.

---

### Method Descriptions

<span id="class_ResourceImporter_private_method__get_build_dependencies"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_build_dependencies** ( path: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_resourceimporter.md#class_ResourceImporter_private_method__get_build_dependencies)

Called when the engine compilation profile editor wants to check what build options an imported resource needs. For example, [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont) has a property called [ResourceImporterDynamicFont.multichannel_signed_distance_field](class_resourceimporterdynamicfont.md#class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field), that depends on the engine to be build with the "msdfgen" module. If that resource happened to be a custom one, it would be handled like this:

::

    func _get_build_dependencies(path):
        var resource = load(path)
        var dependencies = PackedStringArray()

        if resource.multichannel_signed_distance_field:
            dependencies.push_back("module_msdfgen_enabled")

        return dependencies
