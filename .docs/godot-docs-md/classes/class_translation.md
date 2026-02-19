<span id="class_Translation"></span>

## Translation

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OptimizedTranslation](class_optimizedtranslation.md#class_OptimizedTranslation)

A language translation that maps a collection of strings to their individual translations.

### Description

**Translation** maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

A **Translation** consists of messages. A message is identified by its context and untranslated string. Unlike gettext, using an empty context string in Godot means not using any context.

### Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)

- [Localization using gettext](../tutorials/i18n/localization_using_gettext.md)

- [Locales](../tutorials/i18n/locales.md)

### Properties


| [String](class_string.md#class_String) | [locale](class_translation.md#class_Translation_property_locale) | `"en"` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [plural_rules_override](class_translation.md#class_Translation_property_plural_rules_override) | `""` |

### Methods


| [StringName](class_stringname.md#class_StringName) | [_get_message](class_translation.md#class_Translation_private_method__get_message) ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| --- | --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [_get_plural_message](class_translation.md#class_Translation_private_method__get_plural_message) ( src_message: [StringName](class_stringname.md#class_StringName), src_plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| void | [add_message](class_translation.md#class_Translation_method_add_message) ( src_message: [StringName](class_stringname.md#class_StringName), xlated_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) |
| void | [add_plural_message](class_translation.md#class_Translation_method_add_plural_message) ( src_message: [StringName](class_stringname.md#class_StringName), xlated_messages: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), context: [StringName](class_stringname.md#class_StringName) = &"" ) |
| void | [erase_message](class_translation.md#class_Translation_method_erase_message) ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) |
| [StringName](class_stringname.md#class_StringName) | [get_message](class_translation.md#class_Translation_method_get_message) ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_message_count](class_translation.md#class_Translation_method_get_message_count) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_message_list](class_translation.md#class_Translation_method_get_message_list) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_plural_message](class_translation.md#class_Translation_method_get_plural_message) ( src_message: [StringName](class_stringname.md#class_StringName), src_plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_translated_message_list](class_translation.md#class_Translation_method_get_translated_message_list) ( ) const |

---

### Property Descriptions

<span id="class_Translation_property_locale"></span>

[String](class_string.md#class_String) **locale** = `"en"` [🔗](class_translation.md#class_Translation_property_locale)

- void **set_locale** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_locale** ( )

The locale of the translation.

---

<span id="class_Translation_property_plural_rules_override"></span>

[String](class_string.md#class_String) **plural_rules_override** = `""` [🔗](class_translation.md#class_Translation_property_plural_rules_override)

- void **set_plural_rules_override** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_plural_rules_override** ( )

The plural rules string to enforce. See GNU gettext for examples and more info.

If empty or invalid, default plural rules from [TranslationServer.get_plural_rules()](class_translationserver.md#class_TranslationServer_method_get_plural_rules) are used. The English plural rules are used as a fallback.

---

### Method Descriptions

<span id="class_Translation_private_method__get_message"></span>

[StringName](class_stringname.md#class_StringName) **_get_message** ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_translation.md#class_Translation_private_method__get_message)

Virtual method to override [get_message()](class_translation.md#class_Translation_method_get_message).

---

<span id="class_Translation_private_method__get_plural_message"></span>

[StringName](class_stringname.md#class_StringName) **_get_plural_message** ( src_message: [StringName](class_stringname.md#class_StringName), src_plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_translation.md#class_Translation_private_method__get_plural_message)

Virtual method to override [get_plural_message()](class_translation.md#class_Translation_method_get_plural_message).

---

<span id="class_Translation_method_add_message"></span>

void **add_message** ( src_message: [StringName](class_stringname.md#class_StringName), xlated_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) [🔗](class_translation.md#class_Translation_method_add_message)

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---

<span id="class_Translation_method_add_plural_message"></span>

void **add_plural_message** ( src_message: [StringName](class_stringname.md#class_StringName), xlated_messages: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), context: [StringName](class_stringname.md#class_StringName) = &"" ) [🔗](class_translation.md#class_Translation_method_add_plural_message)

Adds a message involving plural translation if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---

<span id="class_Translation_method_erase_message"></span>

void **erase_message** ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) [🔗](class_translation.md#class_Translation_method_erase_message)

Erases a message.

---

<span id="class_Translation_method_get_message"></span>

[StringName](class_stringname.md#class_StringName) **get_message** ( src_message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translation.md#class_Translation_method_get_message)

Returns a message's translation.

---

<span id="class_Translation_method_get_message_count"></span>

[int](class_int.md#class_int) **get_message_count** ( ) *const* [🔗](class_translation.md#class_Translation_method_get_message_count)

Returns the number of existing messages.

---

<span id="class_Translation_method_get_message_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_message_list** ( ) *const* [🔗](class_translation.md#class_Translation_method_get_message_list)

Returns the keys of all messages, that is, the context and untranslated strings of each message.

 **Note:** If a message does not use a context, the corresponding element is the untranslated string. Otherwise, the corresponding element is the context and untranslated string separated by the EOT character (`U+0004`). This is done for compatibility purposes.

::

    for key in translation.get_message_list():
        var p = key.find("\u0004")
        if p == -1:
            var untranslated = key
            print("Message %s" % untranslated)
        else:
            var context = key.substr(0, p)
            var untranslated = key.substr(p + 1)
            print("Message %s with context %s" % [untranslated, context])

---

<span id="class_Translation_method_get_plural_message"></span>

[StringName](class_stringname.md#class_StringName) **get_plural_message** ( src_message: [StringName](class_stringname.md#class_StringName), src_plural_message: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translation.md#class_Translation_method_get_plural_message)

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

 **Note:** Plurals are only supported in [gettext-based translations (PO)](../tutorials/i18n/localization_using_gettext.md), not CSV.

---

<span id="class_Translation_method_get_translated_message_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_translated_message_list** ( ) *const* [🔗](class_translation.md#class_Translation_method_get_translated_message_list)

Returns all the translated strings.
