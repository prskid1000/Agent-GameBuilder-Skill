<span id="class_RichTextEffect"></span>

## RichTextEffect

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A custom effect for a [RichTextLabel](class_richtextlabel.md#class_RichTextLabel).

### Description

A custom effect for a [RichTextLabel](class_richtextlabel.md#class_RichTextLabel), which can be loaded in the [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) inspector or using [RichTextLabel.install_effect()](class_richtextlabel.md#class_RichTextLabel_method_install_effect).

 **Note:** For a **RichTextEffect** to be usable, a BBCode tag must be defined as a member variable called `bbcode` in the script.

.. tabs::

```
```

    # The RichTextEffect will be usable like this: `[example]Some text[/example]`
    var bbcode = "example"

```
```

    // The RichTextEffect will be usable like this: `[example]Some text[/example]`
    string bbcode = "example";

 **Note:** As soon as a [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) contains at least one **RichTextEffect**, it will continuously process the effect unless the project is paused. This may impact battery life negatively.

### Tutorials

- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel.md)

- RichTextEffect test project (third-party)

### Methods


| [bool](class_bool.md#class_bool) | [_process_custom_fx](class_richtexteffect.md#class_RichTextEffect_private_method__process_custom_fx) ( char_fx: [CharFXTransform](class_charfxtransform.md#class_CharFXTransform) ) | virtual | const |
| --- | --- | --- | --- |

---

### Method Descriptions

<span id="class_RichTextEffect_private_method__process_custom_fx"></span>

[bool](class_bool.md#class_bool) **_process_custom_fx** ( char_fx: [CharFXTransform](class_charfxtransform.md#class_CharFXTransform) ) *virtual* *const* [🔗](class_richtexteffect.md#class_RichTextEffect_private_method__process_custom_fx)

Override this method to modify properties in `char_fx`. The method must return `true` if the character could be transformed successfully. If the method returns `false`, it will skip transformation to avoid displaying broken text.
