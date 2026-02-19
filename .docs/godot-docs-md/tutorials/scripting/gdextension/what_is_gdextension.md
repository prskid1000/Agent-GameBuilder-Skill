<span id="doc_what_is_gdextension"></span>

## What is GDExtension?

**GDExtension** is a Godot-specific technology that lets the engine interact with
native shared libraries
at runtime. You can use it to run native code without compiling it with the engine.

There are three primary methods with which this is achieved:

* `gdextension_interface.h`: A set of C functions that Godot and a GDExtension can use to communicate.
* `extension_api.json`: A list of C functions that are exposed from Godot APIs ([Core Features](../index.md#doc_scripting_core_features)).
* [*.gdextension](gdextension_file.md#doc_gdextension_file): A file format read by Godot to load a GDExtension.

Most people create GDExtensions with some existing language binding, such as [godot-cpp (for C++)](../cpp/index.md#doc_godot_cpp),
or one of the [community-made ones](../other_languages.md#doc_what_is_gdnative_third_party_bindings).

### Version compatibility

See [godot-cpp Version Compatibility](../cpp/about_godot_cpp.md#doc_what_is_gdextension_version_compatibility), which applies to all GDExtensions.
