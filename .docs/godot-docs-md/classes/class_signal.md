<span id="class_Signal"></span>

## Signal

A built-in type representing a signal of an [Object](class_object.md#class_Object).

### Description

**Signal** is a built-in [Variant](class_variant.md#class_Variant) type that represents a signal of an [Object](class_object.md#class_Object) instance. Like all [Variant](class_variant.md#class_Variant) types, it can be stored in variables and passed to functions. Signals allow all connected [Callable](class_callable.md#class_Callable) s (and by extension their respective objects) to listen and react to events, without directly referencing one another. This keeps the code flexible and easier to manage. You can check whether an [Object](class_object.md#class_Object) has a given signal name using [Object.has_signal()](class_object.md#class_Object_method_has_signal).

In GDScript, signals can be declared with the `signal` keyword. In C#, you may use the `[Signal]` attribute on a delegate.

.. tabs::

```
```

    signal attacked

    # Additional arguments may be declared.
    # These arguments must be passed when the signal is emitted.
    signal item_dropped(item_name, amount)

```
```

    [Signal]
    delegate void AttackedEventHandler();

    // Additional arguments may be declared.
    // These arguments must be passed when the signal is emitted.
    [Signal]
    delegate void ItemDroppedEventHandler(string itemName, int amount);

Connecting signals is one of the most common operations in Godot and the API gives many options to do so, which are described further down. The code block below shows the recommended approach.

.. tabs::

```
```

    func _ready():
        var button = Button.new()
        # `button_down` here is a Signal Variant type. We therefore call the Signal.connect() method, not Object.connect().
        # See discussion below for a more in-depth overview of the API.
        button.button_down.connect(_on_button_down)

        # This assumes that a `Player` class exists, which defines a `hit` signal.
        var player = Player.new()
        # We use Signal.connect() again, and we also use the Callable.bind() method,
        # which returns a new Callable with the parameter binds.
        player.hit.connect(_on_player_hit.bind("sword", 100))

    func _on_button_down():
        print("Button down!")

    func _on_player_hit(weapon_type, damage):
        print("Hit with weapon %s for %d damage." % [weapon_type, damage])

```
```

    public override void _Ready()
    {
        var button = new Button();
        // C# supports passing signals as events, so we can use this idiomatic construct:
        button.ButtonDown += OnButtonDown;

        // This assumes that a `Player` class exists, which defines a `Hit` signal.
        var player = new Player();
        // We can use lambdas when we need to bind additional parameters.
        player.Hit += () => OnPlayerHit("sword", 100);
    }

    private void OnButtonDown()
    {
        GD.Print("Button down!");
    }

    private void OnPlayerHit(string weaponType, int damage)
    {
        GD.Print($"Hit with weapon {weaponType} for {damage} damage.");
    }

 ** `Object.connect()` or `Signal.connect()`?**

As seen above, the recommended method to connect signals is not [Object.connect()](class_object.md#class_Object_method_connect). The code block below shows the four options for connecting signals, using either this legacy method or the recommended [connect()](class_signal.md#class_Signal_method_connect), and using either an implicit [Callable](class_callable.md#class_Callable) or a manually defined one.

.. tabs::

```
```

    func _ready():
        var button = Button.new()
        # Option 1: Object.connect() with an implicit Callable for the defined function.
        button.connect("button_down", _on_button_down)
        # Option 2: Object.connect() with a constructed Callable using a target object and method name.
        button.connect("button_down", Callable(self, "_on_button_down"))
        # Option 3: Signal.connect() with an implicit Callable for the defined function.
        button.button_down.connect(_on_button_down)
        # Option 4: Signal.connect() with a constructed Callable using a target object and method name.
        button.button_down.connect(Callable(self, "_on_button_down"))

    func _on_button_down():
        print("Button down!")

```
```

    public override void _Ready()
    {
        var button = new Button();
        // Option 1: In C#, we can use signals as events and connect with this idiomatic syntax:
        button.ButtonDown += OnButtonDown;
        // Option 2: GodotObject.Connect() with a constructed Callable from a method group.
        button.Connect(Button.SignalName.ButtonDown, Callable.From(OnButtonDown));
        // Option 3: GodotObject.Connect() with a constructed Callable using a target object and method name.
        button.Connect(Button.SignalName.ButtonDown, new Callable(this, MethodName.OnButtonDown));
    }

    private void OnButtonDown()
    {
        GD.Print("Button down!");
    }

While all options have the same outcome (`button`'s [BaseButton.button_down](class_basebutton.md#class_BaseButton_signal_button_down) signal will be connected to `_on_button_down`), **option 3** offers the best validation: it will print a compile-time error if either the `button_down` **Signal** or the `_on_button_down` [Callable](class_callable.md#class_Callable) are not defined. On the other hand, **option 2** only relies on string names and will only be able to validate either names at runtime: it will generate an error at runtime if `"button_down"` is not a signal, or if `"_on_button_down"` is not a method in the object `self`. The main reason for using options 1, 2, or 4 would be if you actually need to use strings (e.g. to connect signals programmatically based on strings read from a configuration file). Otherwise, option 3 is the recommended (and fastest) method.

 **Binding and passing parameters:**

The syntax to bind parameters is through [Callable.bind()](class_callable.md#class_Callable_method_bind), which returns a copy of the [Callable](class_callable.md#class_Callable) with its parameters bound.

When calling [emit()](class_signal.md#class_Signal_method_emit) or [Object.emit_signal()](class_object.md#class_Object_method_emit_signal), the signal parameters can be also passed. The examples below show the relationship between these signal parameters and bound parameters.

.. tabs::

```
```

    func _ready():
        # This assumes that a `Player` class exists, which defines a `hit` signal.
        var player = Player.new()
        # Using Callable.bind().
        player.hit.connect(_on_player_hit.bind("sword", 100))

        # Parameters added when emitting the signal are passed first.
        player.hit.emit("Dark lord", 5)

    # We pass two arguments when emitting (`hit_by`, `level`),
    # and bind two more arguments when connecting (`weapon_type`, `damage`).
    func _on_player_hit(hit_by, level, weapon_type, damage):
        print("Hit by %s (level %d) with weapon %s for %d damage." % [hit_by, level, weapon_type, damage])

```
```

    public override void _Ready()
    {
        // This assumes that a `Player` class exists, which defines a `Hit` signal.
        var player = new Player();
        // Using lambda expressions that create a closure that captures the additional parameters.
        // The lambda only receives the parameters defined by the signal's delegate.
        player.Hit += (hitBy, level) => OnPlayerHit(hitBy, level, "sword", 100);

        // Parameters added when emitting the signal are passed first.
        player.EmitSignal(SignalName.Hit, "Dark lord", 5);
    }

    // We pass two arguments when emitting (`hit_by`, `level`),
    // and bind two more arguments when connecting (`weapon_type`, `damage`).
    private void OnPlayerHit(string hitBy, int level, string weaponType, int damage)
    {
        GD.Print($"Hit by {hitBy} (level {level}) with weapon {weaponType} for {damage} damage.");
    }

 **Note:** In a boolean context, a signal will evaluate to `false` if it's null (see [is_null()](class_signal.md#class_Signal_method_is_null)). Otherwise, a signal will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Using Signals](../getting_started/step_by_step/signals.md)

- `GDScript Basics <../tutorials/scripting/gdscript/gdscript_basics.html#signals>`__

### Constructors


| [Signal](class_signal.md#class_Signal) | [Signal](class_signal.md#class_Signal_constructor_Signal) ( ) |
| --- | --- |
| [Signal](class_signal.md#class_Signal) | [Signal](class_signal.md#class_Signal_constructor_Signal) ( from: [Signal](class_signal.md#class_Signal) ) |
| [Signal](class_signal.md#class_Signal) | [Signal](class_signal.md#class_Signal_constructor_Signal) ( object: [Object](class_object.md#class_Object), signal: [StringName](class_stringname.md#class_StringName) ) |

### Methods


| [int](class_int.md#class_int) | [connect](class_signal.md#class_Signal_method_connect) ( callable: [Callable](class_callable.md#class_Callable), flags: [int](class_int.md#class_int) = 0 ) |
| --- | --- |
| void | [disconnect](class_signal.md#class_Signal_method_disconnect) ( callable: [Callable](class_callable.md#class_Callable) ) |
| void | [emit](class_signal.md#class_Signal_method_emit) ( ... ) | vararg | const |
| [Array](class_array.md#class_Array) | [get_connections](class_signal.md#class_Signal_method_get_connections) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_name](class_signal.md#class_Signal_method_get_name) ( ) const |
| [Object](class_object.md#class_Object) | [get_object](class_signal.md#class_Signal_method_get_object) ( ) const |
| [int](class_int.md#class_int) | [get_object_id](class_signal.md#class_Signal_method_get_object_id) ( ) const |
| [bool](class_bool.md#class_bool) | [has_connections](class_signal.md#class_Signal_method_has_connections) ( ) const |
| [bool](class_bool.md#class_bool) | [is_connected](class_signal.md#class_Signal_method_is_connected) ( callable: [Callable](class_callable.md#class_Callable) ) const |
| [bool](class_bool.md#class_bool) | [is_null](class_signal.md#class_Signal_method_is_null) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_signal.md#class_Signal_operator_neq_Signal) ( right: [Signal](class_signal.md#class_Signal) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [operator ==](class_signal.md#class_Signal_operator_eq_Signal) ( right: [Signal](class_signal.md#class_Signal) ) |

---

### Constructor Descriptions

<span id="class_Signal_constructor_Signal"></span>

[Signal](class_signal.md#class_Signal) **Signal** ( ) [🔗](class_signal.md#class_Signal_constructor_Signal)

Constructs an empty **Signal** with no object nor signal name bound.

---

[Signal](class_signal.md#class_Signal) **Signal** ( from: [Signal](class_signal.md#class_Signal) )

Constructs a **Signal** as a copy of the given **Signal**.

---

[Signal](class_signal.md#class_Signal) **Signal** ( object: [Object](class_object.md#class_Object), signal: [StringName](class_stringname.md#class_StringName) )

Creates a **Signal** object referencing a signal named `signal` in the specified `object`.

---

### Method Descriptions

<span id="class_Signal_method_connect"></span>

[int](class_int.md#class_int) **connect** ( callable: [Callable](class_callable.md#class_Callable), flags: [int](class_int.md#class_int) = 0 ) [🔗](class_signal.md#class_Signal_method_connect)

Connects this signal to the specified `callable`. Optional `flags` can be also added to configure the connection's behavior (see [ConnectFlags](class_object.md#enum_Object_ConnectFlags) constants). You can provide additional arguments to the connected `callable` by using [Callable.bind()](class_callable.md#class_Callable_method_bind).

A signal can only be connected once to the same [Callable](class_callable.md#class_Callable). If the signal is already connected, this method returns @GlobalScope.ERR_INVALID_PARAMETER and generates an error, unless the signal is connected with [Object.CONNECT_REFERENCE_COUNTED](class_object.md#class_Object_constant_CONNECT_REFERENCE_COUNTED). To prevent this, use [is_connected()](class_signal.md#class_Signal_method_is_connected) first to check for existing connections.

::

    for button in $Buttons.get_children():
        button.pressed.connect(_on_pressed.bind(button))

    func _on_pressed(button):
        print(button.name, " was pressed")

 **Note:** If the `callable`'s object is freed, the connection will be lost.

---

<span id="class_Signal_method_disconnect"></span>

void **disconnect** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_signal.md#class_Signal_method_disconnect)

Disconnects this signal from the specified [Callable](class_callable.md#class_Callable). If the connection does not exist, generates an error. Use [is_connected()](class_signal.md#class_Signal_method_is_connected) to make sure that the connection exists.

---

<span id="class_Signal_method_emit"></span>

void **emit** ( ... ) *vararg* *const* [🔗](class_signal.md#class_Signal_method_emit)

Emits this signal. All [Callable](class_callable.md#class_Callable) s connected to this signal will be triggered. This method supports a variable number of arguments, so parameters can be passed as a comma separated list.

---

<span id="class_Signal_method_get_connections"></span>

[Array](class_array.md#class_Array) **get_connections** ( ) *const* [🔗](class_signal.md#class_Signal_method_get_connections)

Returns an [Array](class_array.md#class_Array) of connections for this signal. Each connection is represented as a [Dictionary](class_dictionary.md#class_Dictionary) that contains three entries:

- `signal` is a reference to this signal;

- `callable` is a reference to the connected [Callable](class_callable.md#class_Callable);

- `flags` is a combination of [ConnectFlags](class_object.md#enum_Object_ConnectFlags).

---

<span id="class_Signal_method_get_name"></span>

[StringName](class_stringname.md#class_StringName) **get_name** ( ) *const* [🔗](class_signal.md#class_Signal_method_get_name)

Returns the name of this signal.

---

<span id="class_Signal_method_get_object"></span>

[Object](class_object.md#class_Object) **get_object** ( ) *const* [🔗](class_signal.md#class_Signal_method_get_object)

Returns the object emitting this signal.

---

<span id="class_Signal_method_get_object_id"></span>

[int](class_int.md#class_int) **get_object_id** ( ) *const* [🔗](class_signal.md#class_Signal_method_get_object_id)

Returns the ID of the object emitting this signal (see [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id)).

---

<span id="class_Signal_method_has_connections"></span>

[bool](class_bool.md#class_bool) **has_connections** ( ) *const* [🔗](class_signal.md#class_Signal_method_has_connections)

Returns `true` if any [Callable](class_callable.md#class_Callable) is connected to this signal.

---

<span id="class_Signal_method_is_connected"></span>

[bool](class_bool.md#class_bool) **is_connected** ( callable: [Callable](class_callable.md#class_Callable) ) *const* [🔗](class_signal.md#class_Signal_method_is_connected)

Returns `true` if the specified [Callable](class_callable.md#class_Callable) is connected to this signal.

---

<span id="class_Signal_method_is_null"></span>

[bool](class_bool.md#class_bool) **is_null** ( ) *const* [🔗](class_signal.md#class_Signal_method_is_null)

Returns `true` if this **Signal** has no object and the signal name is empty. Equivalent to `signal == Signal()`.

---

### Operator Descriptions

<span id="class_Signal_operator_neq_Signal"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Signal](class_signal.md#class_Signal) ) [🔗](class_signal.md#class_Signal_operator_neq_Signal)

Returns `true` if the signals do not share the same object and name.

---

<span id="class_Signal_operator_eq_Signal"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Signal](class_signal.md#class_Signal) ) [🔗](class_signal.md#class_Signal_operator_eq_Signal)

Returns `true` if both signals share the same object and name.
