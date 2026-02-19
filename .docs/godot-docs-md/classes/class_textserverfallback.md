<span id="class_TextServerFallback"></span>

## TextServerFallback

**Inherits:** [TextServerExtension](class_textserverextension.md#class_TextServerExtension) **<** [TextServer](class_textserver.md#class_TextServer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A fallback implementation of Godot's text server, without support for BiDi and complex text layout.

### Description

A fallback implementation of Godot's text server. This fallback is faster than [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced) for processing a lot of text, but it does not support BiDi and complex text layout.

 **Note:** This text server is not part of official Godot binaries. If you want to use it, compile the engine with the option `module_text_server_fb_enabled=yes`. When building with **TextServerFallback**, consider also disabling [TextServerAdvanced](class_textserveradvanced.md#class_TextServerAdvanced) with `module_text_server_adv_enabled=no` to reduce binary size.
