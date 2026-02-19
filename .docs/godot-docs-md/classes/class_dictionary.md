<span id="class_Dictionary"></span>

## Dictionary

A built-in data structure that holds key-value pairs.

### Description

Dictionaries are associative containers that contain values referenced by unique keys. Dictionaries will preserve the insertion order when adding new entries. In other programming languages, this data structure is often referred to as a hash map or an associative array.

You can define a dictionary by placing a comma-separated list of `key: value` pairs inside curly braces `{}`.

Creating a dictionary:

.. tabs::

```
```

    var my_dict = {} # Creates an empty dictionary.

    var dict_variable_key = "Another key name"
    var dict_variable_value = "value2"
    var another_dict = {
        "Some key name": "value1",
        dict_variable_key: dict_variable_value,
    }

    var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }

    # Alternative Lua-style syntax.
    # Doesn't require quotes around keys, but only string constants can be used as key names.
    # Additionally, key names must start with a letter or an underscore.
    # Here, `some_key` is a string literal, not a variable!
    another_dict = {
        some_key = 42,
    }

```
```

    var myDict = new Godot.Collections.Dictionary(); // Creates an empty dictionary.
    var pointsDict = new Godot.Collections.Dictionary
    {
        { "White", 50 },
        { "Yellow", 75 },
        { "Orange", 100 },
    };

You can access a dictionary's value by referencing its corresponding key. In the above example, `points_dict["White"]` will return `50`. You can also write `points_dict.White`, which is equivalent. However, you'll have to use the bracket syntax if the key you're accessing the dictionary with isn't a fixed string (such as a number or variable).

.. tabs::

```
```

    @export_enum("White", "Yellow", "Orange") var my_color: String
    var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
    func _ready():
        # We can't use dot syntax here as `my_color` is a variable.
        var points = points_dict[my_color]

```
```

    [Export(PropertyHint.Enum, "White,Yellow,Orange")]
    public string MyColor { get; set; }
    private Godot.Collections.Dictionary _pointsDict = new Godot.Collections.Dictionary
    {
        { "White", 50 },
        { "Yellow", 75 },
        { "Orange", 100 },
    };

    public override void _Ready()
    {
        int points = (int)_pointsDict[MyColor];
    }

In the above code, `points` will be assigned the value that is paired with the appropriate color selected in `my_color`.

Dictionaries can contain more complex data:

.. tabs::

```
```

    var my_dict = {
        "First Array": [1, 2, 3, 4] # Assigns an Array to a String key.
    }

```
```

    var myDict = new Godot.Collections.Dictionary
    {
        { "First Array", new Godot.Collections.Array { 1, 2, 3, 4 } }
    };

To add a key to an existing dictionary, access it like an existing key and assign to it:

.. tabs::

```
```

    var points_dict = { "White": 50, "Yellow": 75, "Orange": 100 }
    points_dict["Blue"] = 150 # Add "Blue" as a key and assign 150 as its value.

```
```

    var pointsDict = new Godot.Collections.Dictionary
    {
        { "White", 50 },
        { "Yellow", 75 },
        { "Orange", 100 },
    };
    pointsDict["Blue"] = 150; // Add "Blue" as a key and assign 150 as its value.

Finally, untyped dictionaries can contain different types of keys and values in the same dictionary:

.. tabs::

```
```

    # This is a valid dictionary.
    # To access the string "Nested value" below, use `my_dict.sub_dict.sub_key` or `my_dict["sub_dict"]["sub_key"]`.
    # Indexing styles can be mixed and matched depending on your needs.
    var my_dict = {
        "String Key": 5,
        4: [1, 2, 3],
        7: "Hello",
        "sub_dict": { "sub_key": "Nested value" },
    }

```
```

    // This is a valid dictionary.
    // To access the string "Nested value" below, use `((Godot.Collections.Dictionary)myDict["sub_dict"])["sub_key"]`.
    var myDict = new Godot.Collections.Dictionary {
        { "String Key", 5 },
        { 4, new Godot.Collections.Array { 1, 2, 3 } },
        { 7, "Hello" },
        { "sub_dict", new Godot.Collections.Dictionary { { "sub_key", "Nested value" } } },
    };

The keys of a dictionary can be iterated with the `for` keyword:

.. tabs::

```
```

    var groceries = { "Orange": 20, "Apple": 2, "Banana": 4 }
    for fruit in groceries:
        var amount = groceries[fruit]

```
```

    var groceries = new Godot.Collections.Dictionary { { "Orange", 20 }, { "Apple", 2 }, { "Banana", 4 } };
    foreach (var (fruit, amount) in groceries)
    {
        // `fruit` is the key, `amount` is the value.
    }

To enforce a certain type for keys and values, you can create a *typed dictionary*. Typed dictionaries can only contain keys and values of the given types, or that inherit from the given classes:

.. tabs::

```
```

    # Creates a typed dictionary with String keys and int values.
    # Attempting to use any other type for keys or values will result in an error.
    var typed_dict: Dictionary[String, int] = {
        "some_key": 1,
        "some_other_key": 2,
    }

    # Creates a typed dictionary with String keys and values of any type.
    # Attempting to use any other type for keys will result in an error.
    var typed_dict_key_only: Dictionary[String, Variant] = {
        "some_key": 12.34,
        "some_other_key": "string",
    }

```
```

    // Creates a typed dictionary with String keys and int values.
    // Attempting to use any other type for keys or values will result in an error.
    var typedDict = new Godot.Collections.Dictionary<String, int> {
        {"some_key", 1},
        {"some_other_key", 2},
    };

    // Creates a typed dictionary with String keys and values of any type.
    // Attempting to use any other type for keys will result in an error.
    var typedDictKeyOnly = new Godot.Collections.Dictionary<String, Variant> {
        {"some_key", 12.34},
        {"some_other_key", "string"},
    };

 **Note:** Dictionaries are always passed by reference. To get a copy of a dictionary which can be modified independently of the original dictionary, use [duplicate()](class_dictionary.md#class_Dictionary_method_duplicate).

 **Note:** Erasing elements while iterating over dictionaries is **not** supported and will result in unpredictable behavior.

 **Note:** In a boolean context, a dictionary will evaluate to `false` if it's empty (`{}`). Otherwise, a dictionary will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- `GDScript basics: Dictionary <../tutorials/scripting/gdscript/gdscript_basics.html#dictionary>`__

- 3D Voxel Demo

- Operating System Testing Demo

### Constructors


| [Dictionary](class_dictionary.md#class_Dictionary) | [Dictionary](class_dictionary.md#class_Dictionary_constructor_Dictionary) ( ) |
| --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [Dictionary](class_dictionary.md#class_Dictionary_constructor_Dictionary) ( base: [Dictionary](class_dictionary.md#class_Dictionary), key_type: [int](class_int.md#class_int), key_class_name: [StringName](class_stringname.md#class_StringName), key_script: [Variant](class_variant.md#class_Variant), value_type: [int](class_int.md#class_int), value_class_name: [StringName](class_stringname.md#class_StringName), value_script: [Variant](class_variant.md#class_Variant) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [Dictionary](class_dictionary.md#class_Dictionary_constructor_Dictionary) ( from: [Dictionary](class_dictionary.md#class_Dictionary) ) |

### Methods


| void | [assign](class_dictionary.md#class_Dictionary_method_assign) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| --- | --- |
| void | [clear](class_dictionary.md#class_Dictionary_method_clear) ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [duplicate](class_dictionary.md#class_Dictionary_method_duplicate) ( deep: [bool](class_bool.md#class_bool) = false ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [duplicate_deep](class_dictionary.md#class_Dictionary_method_duplicate_deep) ( deep_subresources_mode: [int](class_int.md#class_int) = 1 ) const |
| [bool](class_bool.md#class_bool) | [erase](class_dictionary.md#class_Dictionary_method_erase) ( key: [Variant](class_variant.md#class_Variant) ) |
| [Variant](class_variant.md#class_Variant) | [find_key](class_dictionary.md#class_Dictionary_method_find_key) ( value: [Variant](class_variant.md#class_Variant) ) const |
| [Variant](class_variant.md#class_Variant) | [get](class_dictionary.md#class_Dictionary_method_get) ( key: [Variant](class_variant.md#class_Variant), default: [Variant](class_variant.md#class_Variant) = null ) const |
| [Variant](class_variant.md#class_Variant) | [get_or_add](class_dictionary.md#class_Dictionary_method_get_or_add) ( key: [Variant](class_variant.md#class_Variant), default: [Variant](class_variant.md#class_Variant) = null ) |
| [int](class_int.md#class_int) | [get_typed_key_builtin](class_dictionary.md#class_Dictionary_method_get_typed_key_builtin) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_typed_key_class_name](class_dictionary.md#class_Dictionary_method_get_typed_key_class_name) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_typed_key_script](class_dictionary.md#class_Dictionary_method_get_typed_key_script) ( ) const |
| [int](class_int.md#class_int) | [get_typed_value_builtin](class_dictionary.md#class_Dictionary_method_get_typed_value_builtin) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_typed_value_class_name](class_dictionary.md#class_Dictionary_method_get_typed_value_class_name) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_typed_value_script](class_dictionary.md#class_Dictionary_method_get_typed_value_script) ( ) const |
| [bool](class_bool.md#class_bool) | [has](class_dictionary.md#class_Dictionary_method_has) ( key: [Variant](class_variant.md#class_Variant) ) const |
| [bool](class_bool.md#class_bool) | [has_all](class_dictionary.md#class_Dictionary_method_has_all) ( keys: [Array](class_array.md#class_Array) ) const |
| [int](class_int.md#class_int) | [hash](class_dictionary.md#class_Dictionary_method_hash) ( ) const |
| [bool](class_bool.md#class_bool) | [is_empty](class_dictionary.md#class_Dictionary_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [is_read_only](class_dictionary.md#class_Dictionary_method_is_read_only) ( ) const |
| [bool](class_bool.md#class_bool) | [is_same_typed](class_dictionary.md#class_Dictionary_method_is_same_typed) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) const |
| [bool](class_bool.md#class_bool) | [is_same_typed_key](class_dictionary.md#class_Dictionary_method_is_same_typed_key) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) const |
| [bool](class_bool.md#class_bool) | [is_same_typed_value](class_dictionary.md#class_Dictionary_method_is_same_typed_value) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) const |
| [bool](class_bool.md#class_bool) | [is_typed](class_dictionary.md#class_Dictionary_method_is_typed) ( ) const |
| [bool](class_bool.md#class_bool) | [is_typed_key](class_dictionary.md#class_Dictionary_method_is_typed_key) ( ) const |
| [bool](class_bool.md#class_bool) | [is_typed_value](class_dictionary.md#class_Dictionary_method_is_typed_value) ( ) const |
| [Array](class_array.md#class_Array) | [keys](class_dictionary.md#class_Dictionary_method_keys) ( ) const |
| void | [make_read_only](class_dictionary.md#class_Dictionary_method_make_read_only) ( ) |
| void | [merge](class_dictionary.md#class_Dictionary_method_merge) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), overwrite: [bool](class_bool.md#class_bool) = false ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [merged](class_dictionary.md#class_Dictionary_method_merged) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), overwrite: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [recursive_equal](class_dictionary.md#class_Dictionary_method_recursive_equal) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), recursion_count: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [set](class_dictionary.md#class_Dictionary_method_set) ( key: [Variant](class_variant.md#class_Variant), value: [Variant](class_variant.md#class_Variant) ) |
| [int](class_int.md#class_int) | [size](class_dictionary.md#class_Dictionary_method_size) ( ) const |
| void | [sort](class_dictionary.md#class_Dictionary_method_sort) ( ) |
| [Array](class_array.md#class_Array) | [values](class_dictionary.md#class_Dictionary_method_values) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_dictionary.md#class_Dictionary_operator_neq_Dictionary) ( right: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [operator ==](class_dictionary.md#class_Dictionary_operator_eq_Dictionary) ( right: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| [Variant](class_variant.md#class_Variant) | [operator []](class_dictionary.md#class_Dictionary_operator_idx_Variant) ( key: [Variant](class_variant.md#class_Variant) ) |

---

### Constructor Descriptions

<span id="class_Dictionary_constructor_Dictionary"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **Dictionary** ( ) [🔗](class_dictionary.md#class_Dictionary_constructor_Dictionary)

Constructs an empty **Dictionary**.

---

[Dictionary](class_dictionary.md#class_Dictionary) **Dictionary** ( base: [Dictionary](class_dictionary.md#class_Dictionary), key_type: [int](class_int.md#class_int), key_class_name: [StringName](class_stringname.md#class_StringName), key_script: [Variant](class_variant.md#class_Variant), value_type: [int](class_int.md#class_int), value_class_name: [StringName](class_stringname.md#class_StringName), value_script: [Variant](class_variant.md#class_Variant) )

Creates a typed dictionary from the `base` dictionary. A typed dictionary can only contain keys and values of the given types, or that inherit from the given classes, as described by this constructor's parameters.

---

[Dictionary](class_dictionary.md#class_Dictionary) **Dictionary** ( from: [Dictionary](class_dictionary.md#class_Dictionary) )

Returns the same dictionary as `from`. If you need a copy of the dictionary, use [duplicate()](class_dictionary.md#class_Dictionary_method_duplicate).

---

### Method Descriptions

<span id="class_Dictionary_method_assign"></span>

void **assign** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_dictionary.md#class_Dictionary_method_assign)

Assigns elements of another `dictionary` into the dictionary. Resizes the dictionary to match `dictionary`. Performs type conversions if the dictionary is typed.

---

<span id="class_Dictionary_method_clear"></span>

void **clear** ( ) [🔗](class_dictionary.md#class_Dictionary_method_clear)

Clears the dictionary, removing all entries from it.

---

<span id="class_Dictionary_method_duplicate"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **duplicate** ( deep: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_dictionary.md#class_Dictionary_method_duplicate)

Returns a new copy of the dictionary.

By default, a **shallow** copy is returned: all nested [Array](class_array.md#class_Array), **Dictionary**, and [Resource](class_resource.md#class_Resource) keys and values are shared with the original dictionary. Modifying any of those in one dictionary will also affect them in the other.

If `deep` is `true`, a **deep** copy is returned: all nested arrays and dictionaries are also duplicated (recursively). Any [Resource](class_resource.md#class_Resource) is still shared with the original dictionary, though.

---

<span id="class_Dictionary_method_duplicate_deep"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **duplicate_deep** ( deep_subresources_mode: [int](class_int.md#class_int) = 1 ) *const* [🔗](class_dictionary.md#class_Dictionary_method_duplicate_deep)

Duplicates this dictionary, deeply, like [duplicate()](class_dictionary.md#class_Dictionary_method_duplicate) when passing `true`, with extra control over how subresources are handled.

 `deep_subresources_mode` must be one of the values from [DeepDuplicateMode](class_resource.md#enum_Resource_DeepDuplicateMode). By default, only internal resources will be duplicated (recursively).

---

<span id="class_Dictionary_method_erase"></span>

[bool](class_bool.md#class_bool) **erase** ( key: [Variant](class_variant.md#class_Variant) ) [🔗](class_dictionary.md#class_Dictionary_method_erase)

Removes the dictionary entry by key, if it exists. Returns `true` if the given `key` existed in the dictionary, otherwise `false`.

 **Note:** Do not erase entries while iterating over the dictionary. You can iterate over the [keys()](class_dictionary.md#class_Dictionary_method_keys) array instead.

---

<span id="class_Dictionary_method_find_key"></span>

[Variant](class_variant.md#class_Variant) **find_key** ( value: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_find_key)

Finds and returns the first key whose associated value is equal to `value`, or `null` if it is not found.

 **Note:** `null` is also a valid key. If inside the dictionary, [find_key()](class_dictionary.md#class_Dictionary_method_find_key) may give misleading results.

---

<span id="class_Dictionary_method_get"></span>

[Variant](class_variant.md#class_Variant) **get** ( key: [Variant](class_variant.md#class_Variant), default: [Variant](class_variant.md#class_Variant) = null ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get)

Returns the corresponding value for the given `key` in the dictionary. If the `key` does not exist, returns `default`, or `null` if the parameter is omitted.

---

<span id="class_Dictionary_method_get_or_add"></span>

[Variant](class_variant.md#class_Variant) **get_or_add** ( key: [Variant](class_variant.md#class_Variant), default: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_dictionary.md#class_Dictionary_method_get_or_add)

Gets a value and ensures the key is set. If the `key` exists in the dictionary, this behaves like [get()](class_dictionary.md#class_Dictionary_method_get). Otherwise, the `default` value is inserted into the dictionary and returned.

---

<span id="class_Dictionary_method_get_typed_key_builtin"></span>

[int](class_int.md#class_int) **get_typed_key_builtin** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_key_builtin)

Returns the built-in [Variant](class_variant.md#class_Variant) type of the typed dictionary's keys as a Variant.Type constant. If the keys are not typed, returns @GlobalScope.TYPE_NIL. See also [is_typed_key()](class_dictionary.md#class_Dictionary_method_is_typed_key).

---

<span id="class_Dictionary_method_get_typed_key_class_name"></span>

[StringName](class_stringname.md#class_StringName) **get_typed_key_class_name** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_key_class_name)

Returns the **built-in** class name of the typed dictionary's keys, if the built-in [Variant](class_variant.md#class_Variant) type is @GlobalScope.TYPE_OBJECT. Otherwise, returns an empty [StringName](class_stringname.md#class_StringName). See also [is_typed_key()](class_dictionary.md#class_Dictionary_method_is_typed_key) and [Object.get_class()](class_object.md#class_Object_method_get_class).

---

<span id="class_Dictionary_method_get_typed_key_script"></span>

[Variant](class_variant.md#class_Variant) **get_typed_key_script** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_key_script)

Returns the [Script](class_script.md#class_Script) instance associated with this typed dictionary's keys, or `null` if it does not exist. See also [is_typed_key()](class_dictionary.md#class_Dictionary_method_is_typed_key).

---

<span id="class_Dictionary_method_get_typed_value_builtin"></span>

[int](class_int.md#class_int) **get_typed_value_builtin** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_value_builtin)

Returns the built-in [Variant](class_variant.md#class_Variant) type of the typed dictionary's values as a Variant.Type constant. If the values are not typed, returns @GlobalScope.TYPE_NIL. See also [is_typed_value()](class_dictionary.md#class_Dictionary_method_is_typed_value).

---

<span id="class_Dictionary_method_get_typed_value_class_name"></span>

[StringName](class_stringname.md#class_StringName) **get_typed_value_class_name** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_value_class_name)

Returns the **built-in** class name of the typed dictionary's values, if the built-in [Variant](class_variant.md#class_Variant) type is @GlobalScope.TYPE_OBJECT. Otherwise, returns an empty [StringName](class_stringname.md#class_StringName). See also [is_typed_value()](class_dictionary.md#class_Dictionary_method_is_typed_value) and [Object.get_class()](class_object.md#class_Object_method_get_class).

---

<span id="class_Dictionary_method_get_typed_value_script"></span>

[Variant](class_variant.md#class_Variant) **get_typed_value_script** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_get_typed_value_script)

Returns the [Script](class_script.md#class_Script) instance associated with this typed dictionary's values, or `null` if it does not exist. See also [is_typed_value()](class_dictionary.md#class_Dictionary_method_is_typed_value).

---

<span id="class_Dictionary_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( key: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_has)

Returns `true` if the dictionary contains an entry with the given `key`.

.. tabs::

```
```

    var my_dict = {
        "Godot" : 4,
        210 : null,
    }

    print(my_dict.has("Godot")) # Prints true
    print(my_dict.has(210))     # Prints true
    print(my_dict.has(4))       # Prints false

```
```

    var myDict = new Godot.Collections.Dictionary
    {
        { "Godot", 4 },
        { 210, default },
    };

    GD.Print(myDict.ContainsKey("Godot")); // Prints True
    GD.Print(myDict.ContainsKey(210));     // Prints True
    GD.Print(myDict.ContainsKey(4));       // Prints False

In GDScript, this is equivalent to the `in` operator:

::

    if "Godot" in { "Godot": 4 }:
        print("The key is here!") # Will be printed.

 **Note:** This method returns `true` as long as the `key` exists, even if its corresponding value is `null`.

---

<span id="class_Dictionary_method_has_all"></span>

[bool](class_bool.md#class_bool) **has_all** ( keys: [Array](class_array.md#class_Array) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_has_all)

Returns `true` if the dictionary contains all keys in the given `keys` array.

::

    var data = { "width": 10, "height": 20 }
    data.has_all(["height", "width"]) # Returns true

---

<span id="class_Dictionary_method_hash"></span>

[int](class_int.md#class_int) **hash** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_hash)

Returns a hashed 32-bit integer value representing the dictionary contents.

.. tabs::

```
```

    var dict1 = { "A": 10, "B": 2 }
    var dict2 = { "A": 10, "B": 2 }

    print(dict1.hash() == dict2.hash()) # Prints true

```
```

    var dict1 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };
    var dict2 = new Godot.Collections.Dictionary { { "A", 10 }, { "B", 2 } };

    // Godot.Collections.Dictionary has no Hash() method. Use GD.Hash() instead.
    GD.Print(GD.Hash(dict1) == GD.Hash(dict2)); // Prints True

 **Note:** Dictionaries with the same entries but in a different order will not have the same hash.

 **Note:** Dictionaries with equal hash values are *not* guaranteed to be the same, because of hash collisions. On the contrary, dictionaries with different hash values are guaranteed to be different.

---

<span id="class_Dictionary_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_empty)

Returns `true` if the dictionary is empty (its size is `0`). See also [size()](class_dictionary.md#class_Dictionary_method_size).

---

<span id="class_Dictionary_method_is_read_only"></span>

[bool](class_bool.md#class_bool) **is_read_only** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_read_only)

Returns `true` if the dictionary is read-only. See [make_read_only()](class_dictionary.md#class_Dictionary_method_make_read_only). Dictionaries are automatically read-only if declared with `const` keyword.

---

<span id="class_Dictionary_method_is_same_typed"></span>

[bool](class_bool.md#class_bool) **is_same_typed** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_same_typed)

Returns `true` if the dictionary is typed the same as `dictionary`.

---

<span id="class_Dictionary_method_is_same_typed_key"></span>

[bool](class_bool.md#class_bool) **is_same_typed_key** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_same_typed_key)

Returns `true` if the dictionary's keys are typed the same as `dictionary`'s keys.

---

<span id="class_Dictionary_method_is_same_typed_value"></span>

[bool](class_bool.md#class_bool) **is_same_typed_value** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_same_typed_value)

Returns `true` if the dictionary's values are typed the same as `dictionary`'s values.

---

<span id="class_Dictionary_method_is_typed"></span>

[bool](class_bool.md#class_bool) **is_typed** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_typed)

Returns `true` if the dictionary is typed. Typed dictionaries can only store keys/values of their associated type and provide type safety for the `[]` operator. Methods of typed dictionary still return [Variant](class_variant.md#class_Variant).

---

<span id="class_Dictionary_method_is_typed_key"></span>

[bool](class_bool.md#class_bool) **is_typed_key** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_typed_key)

Returns `true` if the dictionary's keys are typed.

---

<span id="class_Dictionary_method_is_typed_value"></span>

[bool](class_bool.md#class_bool) **is_typed_value** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_is_typed_value)

Returns `true` if the dictionary's values are typed.

---

<span id="class_Dictionary_method_keys"></span>

[Array](class_array.md#class_Array) **keys** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_keys)

Returns the list of keys in the dictionary.

---

<span id="class_Dictionary_method_make_read_only"></span>

void **make_read_only** ( ) [🔗](class_dictionary.md#class_Dictionary_method_make_read_only)

Makes the dictionary read-only, i.e. disables modification of the dictionary's contents. Does not apply to nested content, e.g. content of nested dictionaries.

---

<span id="class_Dictionary_method_merge"></span>

void **merge** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), overwrite: [bool](class_bool.md#class_bool) = false ) [🔗](class_dictionary.md#class_Dictionary_method_merge)

Adds entries from `dictionary` to this dictionary. By default, duplicate keys are not copied over, unless `overwrite` is `true`.

.. tabs::

```
```

    var dict = { "item": "sword", "quantity": 2 }
    var other_dict = { "quantity": 15, "color": "silver" }

    # Overwriting of existing keys is disabled by default.
    dict.merge(other_dict)
    print(dict)  # { "item": "sword", "quantity": 2, "color": "silver" }

    # With overwriting of existing keys enabled.
    dict.merge(other_dict, true)
    print(dict)  # { "item": "sword", "quantity": 15, "color": "silver" }

```
```

    var dict = new Godot.Collections.Dictionary
    {
        ["item"] = "sword",
        ["quantity"] = 2,
    };

    var otherDict = new Godot.Collections.Dictionary
    {
        ["quantity"] = 15,
        ["color"] = "silver",
    };

    // Overwriting of existing keys is disabled by default.
    dict.Merge(otherDict);
    GD.Print(dict); // { "item": "sword", "quantity": 2, "color": "silver" }

    // With overwriting of existing keys enabled.
    dict.Merge(otherDict, true);
    GD.Print(dict); // { "item": "sword", "quantity": 15, "color": "silver" }

 **Note:** [merge()](class_dictionary.md#class_Dictionary_method_merge) is *not* recursive. Nested dictionaries are considered as keys that can be overwritten or not depending on the value of `overwrite`, but they will never be merged together.

---

<span id="class_Dictionary_method_merged"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **merged** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), overwrite: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_dictionary.md#class_Dictionary_method_merged)

Returns a copy of this dictionary merged with the other `dictionary`. By default, duplicate keys are not copied over, unless `overwrite` is `true`. See also [merge()](class_dictionary.md#class_Dictionary_method_merge).

This method is useful for quickly making dictionaries with default values:

::

    var base = { "fruit": "apple", "vegetable": "potato" }
    var extra = { "fruit": "orange", "dressing": "vinegar" }
    # Prints { "fruit": "orange", "vegetable": "potato", "dressing": "vinegar" }
    print(extra.merged(base))
    # Prints { "fruit": "apple", "vegetable": "potato", "dressing": "vinegar" }
    print(extra.merged(base, true))

---

<span id="class_Dictionary_method_recursive_equal"></span>

[bool](class_bool.md#class_bool) **recursive_equal** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary), recursion_count: [int](class_int.md#class_int) ) *const* [🔗](class_dictionary.md#class_Dictionary_method_recursive_equal)

Returns `true` if the two dictionaries contain the same keys and values, inner **Dictionary** and [Array](class_array.md#class_Array) keys and values are compared recursively.

---

<span id="class_Dictionary_method_set"></span>

[bool](class_bool.md#class_bool) **set** ( key: [Variant](class_variant.md#class_Variant), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_dictionary.md#class_Dictionary_method_set)

Sets the value of the element at the given `key` to the given `value`. Returns `true` if the value is set successfully. Fails and returns `false` if the dictionary is read-only, or if `key` and `value` don't match the dictionary's types. This is the same as using the `[]` operator (`dict[key] = value`).

---

<span id="class_Dictionary_method_size"></span>

[int](class_int.md#class_int) **size** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_size)

Returns the number of entries in the dictionary. Empty dictionaries (`{ }`) always return `0`. See also [is_empty()](class_dictionary.md#class_Dictionary_method_is_empty).

---

<span id="class_Dictionary_method_sort"></span>

void **sort** ( ) [🔗](class_dictionary.md#class_Dictionary_method_sort)

Sorts the dictionary in ascending order, by key. The final order is dependent on the "less than" (`<`) comparison between keys.

.. tabs::

```
```

    var numbers = { "c": 2, "a": 0, "b": 1 }
    numbers.sort()
    print(numbers) # Prints { "a": 0, "b": 1, "c": 2 }

This method ensures that the dictionary's entries are ordered consistently when [keys()](class_dictionary.md#class_Dictionary_method_keys) or [values()](class_dictionary.md#class_Dictionary_method_values) are called, or when the dictionary needs to be converted to a string through @GlobalScope.str() or [JSON.stringify()](class_json.md#class_JSON_method_stringify).

---

<span id="class_Dictionary_method_values"></span>

[Array](class_array.md#class_Array) **values** ( ) *const* [🔗](class_dictionary.md#class_Dictionary_method_values)

Returns the list of values in this dictionary.

---

### Operator Descriptions

<span id="class_Dictionary_operator_neq_Dictionary"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_dictionary.md#class_Dictionary_operator_neq_Dictionary)

Returns `true` if the two dictionaries do not contain the same keys and values.

---

<span id="class_Dictionary_operator_eq_Dictionary"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_dictionary.md#class_Dictionary_operator_eq_Dictionary)

Returns `true` if the two dictionaries contain the same keys and values. The order of the entries does not matter.

 **Note:** In C#, by convention, this operator compares by **reference**. If you need to compare by value, iterate over both dictionaries.

---

<span id="class_Dictionary_operator_idx_Variant"></span>

[Variant](class_variant.md#class_Variant) **operator []** ( key: [Variant](class_variant.md#class_Variant) ) [🔗](class_dictionary.md#class_Dictionary_operator_idx_Variant)

Returns the corresponding value for the given `key` in the dictionary. If the entry does not exist, fails and returns `null`. For safe access, use [get()](class_dictionary.md#class_Dictionary_method_get) or [has()](class_dictionary.md#class_Dictionary_method_has).
