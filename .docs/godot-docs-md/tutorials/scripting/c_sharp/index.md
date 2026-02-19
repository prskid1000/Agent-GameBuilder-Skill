<span id="doc_c_sharp"></span>

## C#/.NET

C# is a high-level programming language developed by Microsoft. Godot supports
C# as an option for a scripting language, alongside Godot's own
[GDScript](../gdscript/index.md#doc_gdscript).

The standard Godot executable does not contain C# support out of the box. Instead,
to enable C# support for your project you need to download a .NET version
of the editor from the Godot website.

- [C Sharp Basics](c_sharp_basics.md)
- [C Sharp Features](c_sharp_features.md)
- [C Sharp Style Guide](c_sharp_style_guide.md)
- [Diagnostics/Index](diagnostics/index.md)
- [Godot Api For C#](Godot API for C#.md)
- [                ](----------------.md)
- [As A General Purpose Game Engine Godot Offers Some High Level Features As A Part](As a general purpose game engine Godot offers some high-level features as a part.md)
- [Of Its Api. Articles Below Explain How These Features Integrate Into C# And How](of its API. Articles below explain how these features integrate into C# and how.md)
- [C# Api May Be Different From Gdscript.](C# API may be different from GDScript..md)
- [C Sharp Differences](c_sharp_differences.md)
- [C Sharp Collections](c_sharp_collections.md)
- [C Sharp Variant](c_sharp_variant.md)
- [C Sharp Signals](c_sharp_signals.md)
- [C Sharp Exports](c_sharp_exports.md)
- [C Sharp Global Classes](c_sharp_global_classes.md)
- [C# Platform Support](C# platform support.md)
- [                   ](-------------------.md)
.. seealso::

    See [doc_system_requirements](../../../about/system_requirements.md#doc_system_requirements) for hardware and software version
    requirements for the Godot engine.

> **Note:** Since C# projects use the .NET runtime, also check the system requirements for the version of .NET that you'll be using. See `supported OS <https://github.com/dotnet/core/tree/main/release-notes#supported-os>`_.
Since Godot 4.2, projects written in C# support all desktop platforms (Windows, Linux,
and macOS), as well as Android and iOS.

Android support is currently experimental.

iOS support is currently experimental and has a few limitations.

- The official export templates for the iOS simulator only supports the `x64` architecture.

- Exporting to iOS can only be done from a MacOS device.

Currently, projects written in C# cannot be exported to the web platform. To use C#
on that platform, consider Godot 3 instead.
