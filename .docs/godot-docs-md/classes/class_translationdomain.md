<span id="class_TranslationDomain"></span>

## TranslationDomain

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A self-contained collection of [Translation](class_translation.md#class_Translation) resources.

### Description

**TranslationDomain** is a self-contained collection of [Translation](class_translation.md#class_Translation) resources. Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to use the wrap methods on [TranslationServer](class_translationserver.md#class_TranslationServer).

### Properties


| [bool](class_bool.md#class_bool) | [enabled](class_translationdomain.md#class_TranslationDomain_property_enabled) | `true` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [pseudolocalization_accents_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_accents_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [pseudolocalization_double_vowels_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_double_vowels_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [pseudolocalization_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_enabled) | `false` |
| [float](class_float.md#class_float) | [pseudolocalization_expansion_ratio](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_expansion_ratio) | `0.0` |
| [bool](class_bool.md#class_bool) | [pseudolocalization_fake_bidi_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [pseudolocalization_override_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_override_enabled) | `false` |
| [String](class_string.md#class_String) | [pseudolocalization_prefix](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_prefix) | `"["` |
| [bool](class_bool.md#class_bool) | [pseudolocalization_skip_placeholders_enabled](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled) | `true` |
| [String](class_string.md#class_String) | [pseudolocalization_suffix](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_suffix) | `"]"` |

### Methods


| void | [add_translation](class_translationdomain.md#class_TranslationDomain_method_add_translation) ( translation: [Translation](class_translation.md#class_Translation) ) |
| --- | --- |
| void | [clear](class_translationdomain.md#class_TranslationDomain_method_clear) ( ) |
| [Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] | [find_translations](class_translationdomain.md#class_TranslationDomain_method_find_translations) ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) const |
| [String](class_string.md#class_String) | [get_locale_override](class_translationdomain.md#class_TranslationDomain_method_get_locale_override) ( ) const |
| [Translation](class_translation.md#class_Translation) | [get_translation_object](class_translationdomain.md#class_TranslationDomain_method_get_translation_object) ( locale: [String](class_string.md#class_String) ) const |
| [Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] | [get_translations](class_translationdomain.md#class_TranslationDomain_method_get_translations) ( ) const |
| [bool](class_bool.md#class_bool) | [has_translation](class_translationdomain.md#class_TranslationDomain_method_has_translation) ( translation: [Translation](class_translation.md#class_Translation) ) const |
| [bool](class_bool.md#class_bool) | [has_translation_for_locale](class_translationdomain.md#class_TranslationDomain_method_has_translation_for_locale) ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) const |
| [StringName](class_stringname.md#class_StringName) | [pseudolocalize](class_translationdomain.md#class_TranslationDomain_method_pseudolocalize) ( message: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_translation](class_translationdomain.md#class_TranslationDomain_method_remove_translation) ( translation: [Translation](class_translation.md#class_Translation) ) |
| void | [set_locale_override](class_translationdomain.md#class_TranslationDomain_method_set_locale_override) ( locale: [String](class_string.md#class_String) ) |
| [StringName](class_stringname.md#class_StringName) | [translate](class_translationdomain.md#class_TranslationDomain_method_translate) ( message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [StringName](class_stringname.md#class_StringName) | [translate_plural](class_translationdomain.md#class_TranslationDomain_method_translate_plural) ( message: [StringName](class_stringname.md#class_StringName), message_plural: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) const |

---

### Property Descriptions

<span id="class_TranslationDomain_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_translationdomain.md#class_TranslationDomain_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_enabled** ( )

If `true`, translation is enabled. Otherwise, [translate()](class_translationdomain.md#class_TranslationDomain_method_translate) and [translate_plural()](class_translationdomain.md#class_TranslationDomain_method_translate_plural) will return the input message unchanged regardless of the current locale.

---

<span id="class_TranslationDomain_property_pseudolocalization_accents_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_accents_enabled** = `true` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_accents_enabled)

- void **set_pseudolocalization_accents_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_accents_enabled** ( )

Replace all characters with their accented variants during pseudolocalization.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_double_vowels_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_double_vowels_enabled** = `false` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_double_vowels_enabled)

- void **set_pseudolocalization_double_vowels_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_double_vowels_enabled** ( )

Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_enabled** = `false` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_enabled)

- void **set_pseudolocalization_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_enabled** ( )

If `true`, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_expansion_ratio"></span>

[float](class_float.md#class_float) **pseudolocalization_expansion_ratio** = `0.0` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_expansion_ratio)

- void **set_pseudolocalization_expansion_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pseudolocalization_expansion_ratio** ( )

The expansion ratio to use during pseudolocalization. A value of `0.3` is sufficient for most practical purposes, and will increase the length of each string by 30%.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_fake_bidi_enabled** = `false` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled)

- void **set_pseudolocalization_fake_bidi_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_fake_bidi_enabled** ( )

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_override_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_override_enabled** = `false` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_override_enabled)

- void **set_pseudolocalization_override_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_override_enabled** ( )

Replace all characters in the string with `*`. Useful for finding non-localizable strings.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_prefix"></span>

[String](class_string.md#class_String) **pseudolocalization_prefix** = `"["` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_prefix)

- void **set_pseudolocalization_prefix** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_pseudolocalization_prefix** ( )

Prefix that will be prepended to the pseudolocalized string.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled"></span>

[bool](class_bool.md#class_bool) **pseudolocalization_skip_placeholders_enabled** = `true` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled)

- void **set_pseudolocalization_skip_placeholders_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pseudolocalization_skip_placeholders_enabled** ( )

Skip placeholders for string formatting like `%s` or `%f` during pseudolocalization. Useful to identify strings which need additional control characters to display correctly.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

<span id="class_TranslationDomain_property_pseudolocalization_suffix"></span>

[String](class_string.md#class_String) **pseudolocalization_suffix** = `"]"` [🔗](class_translationdomain.md#class_TranslationDomain_property_pseudolocalization_suffix)

- void **set_pseudolocalization_suffix** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_pseudolocalization_suffix** ( )

Suffix that will be appended to the pseudolocalized string.

 **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) notification manually after you have finished modifying pseudolocalization related options.

---

### Method Descriptions

<span id="class_TranslationDomain_method_add_translation"></span>

void **add_translation** ( translation: [Translation](class_translation.md#class_Translation) ) [🔗](class_translationdomain.md#class_TranslationDomain_method_add_translation)

Adds a translation.

---

<span id="class_TranslationDomain_method_clear"></span>

void **clear** ( ) [🔗](class_translationdomain.md#class_TranslationDomain_method_clear)

Removes all translations.

---

<span id="class_TranslationDomain_method_find_translations"></span>

[Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] **find_translations** ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_find_translations)

Returns the [Translation](class_translation.md#class_Translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class_TranslationServer_method_compare_locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---

<span id="class_TranslationDomain_method_get_locale_override"></span>

[String](class_string.md#class_String) **get_locale_override** ( ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_get_locale_override)

Returns the locale override of the domain. Returns an empty string if locale override is disabled.

---

<span id="class_TranslationDomain_method_get_translation_object"></span>

[Translation](class_translation.md#class_Translation) **get_translation_object** ( locale: [String](class_string.md#class_String) ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_get_translation_object)

**Deprecated:** Use [find_translations()](class_translationdomain.md#class_TranslationDomain_method_find_translations) instead.

Returns the [Translation](class_translation.md#class_Translation) instance that best matches `locale`. Returns `null` if there are no matches.

---

<span id="class_TranslationDomain_method_get_translations"></span>

[Array](class_array.md#class_Array)\[[Translation](class_translation.md#class_Translation)\] **get_translations** ( ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_get_translations)

Returns all available [Translation](class_translation.md#class_Translation) instances as added by [add_translation()](class_translationdomain.md#class_TranslationDomain_method_add_translation).

---

<span id="class_TranslationDomain_method_has_translation"></span>

[bool](class_bool.md#class_bool) **has_translation** ( translation: [Translation](class_translation.md#class_Translation) ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_has_translation)

Returns `true` if this translation domain contains the given `translation`.

---

<span id="class_TranslationDomain_method_has_translation_for_locale"></span>

[bool](class_bool.md#class_bool) **has_translation_for_locale** ( locale: [String](class_string.md#class_String), exact: [bool](class_bool.md#class_bool) ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_has_translation_for_locale)

Returns `true` if there are any [Translation](class_translation.md#class_Translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class_TranslationServer_method_compare_locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---

<span id="class_TranslationDomain_method_pseudolocalize"></span>

[StringName](class_stringname.md#class_StringName) **pseudolocalize** ( message: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_pseudolocalize)

Returns the pseudolocalized string based on the `message` passed in.

---

<span id="class_TranslationDomain_method_remove_translation"></span>

void **remove_translation** ( translation: [Translation](class_translation.md#class_Translation) ) [🔗](class_translationdomain.md#class_TranslationDomain_method_remove_translation)

Removes the given translation.

---

<span id="class_TranslationDomain_method_set_locale_override"></span>

void **set_locale_override** ( locale: [String](class_string.md#class_String) ) [🔗](class_translationdomain.md#class_TranslationDomain_method_set_locale_override)

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise, `locale` will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

 **Note:** Calling this method does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED) signal manually.

---

<span id="class_TranslationDomain_method_translate"></span>

[StringName](class_stringname.md#class_StringName) **translate** ( message: [StringName](class_stringname.md#class_StringName), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_translate)

Returns the current locale's translation for the given message and context.

---

<span id="class_TranslationDomain_method_translate_plural"></span>

[StringName](class_stringname.md#class_StringName) **translate_plural** ( message: [StringName](class_stringname.md#class_StringName), message_plural: [StringName](class_stringname.md#class_StringName), n: [int](class_int.md#class_int), context: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_translationdomain.md#class_TranslationDomain_method_translate_plural)

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.
