<span id="doc_engine_module_api"></span>

## Engine extension APIs

This section introduces various ways in which you can extend the engine with C++ code.
You can use these APIs by creating a [module](custom_modules_in_cpp.md#doc_custom_modules_in_cpp).
Note that you can change the engine in many more ways than presented here — this section just presents
a subselection of common and useful ways to do it.

Alternatively, some of the functions presented here are also available through the
[GDExtension](../../tutorials/scripting/gdextension/what_is_gdextension.md#doc_what_is_gdextension) API.
You can use them in C++ by using creating a [godot-cpp](../../tutorials/scripting/cpp/about_godot_cpp.md#doc_about_godot_cpp) based GDExtension,
or with any of the [community-created GDExtension implementations](../../tutorials/scripting/other_languages.md#doc_scripting_languages). Note though
that some aspects of the code or directory structures may be different in GDExtension compared to the module APIs.

- [Custom Modules In Cpp](custom_modules_in_cpp.md)
- [Binding To External Libraries](binding_to_external_libraries.md)
- [Custom Godot Servers](custom_godot_servers.md)
- [Custom Resource Format Loaders](custom_resource_format_loaders.md)
- [Custom Audiostreams](custom_audiostreams.md)
- [Custom Platform Ports](custom_platform_ports.md)
