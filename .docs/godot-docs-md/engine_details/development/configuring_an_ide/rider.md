<span id="doc_configuring_an_ide_rider"></span>

## JetBrains Rider

JetBrains Rider is a commercial
JetBrains IDE for C++, C# and GDScript that uses the same solution system as Visual Studio.

> **Note:** This documentation is for contributing to the game engine, not for using JetBrains Rider as a C# or GDScript editor. To code C# or GDScript in an external editor, see :ref:`the C# guide to configure an external editor <doc_c_sharp_setup_external_editor>`.
### Importing the project

.. tip:: If you already use Visual Studio as your main IDE, you can use the same solution file in Rider.
         Rider and Visual Studio use the same solution format, so you can switch between the two IDEs without rebuilding the solution file.
         Debug configurations need to be changed when going from one IDE to another.

If you are starting from the scratch, please follow [instructions](../compiling/index.md#doc_compiling_index), specifically:

- Install all the dependencies.
- Figure out the scons command for compiling to target a specific platform.

Provide scons with additional arguments to request a solution file generation:

- Add `vsproj=yes dev_build=yes` to the scons command

The `vsproj` parameter signals that you want Visual Studio solution generated.
The `dev_build` parameter ensures the debug symbols are included, allowing to e.g. step through code using breakpoints.

- Open the generated `godot.sln` in Rider.

> **Note:** Rider toolbar. It affects resolve of the SDKs, code analysis, build, run, etc.
### Compiling and debugging the project
Rider comes with a built-in debugger that can be used to debug the Godot project. You can launch the debugger
by pressing the **Debug** icon at the top of the screen, this only works for the Project Manager,
if you want to debug the editor, you need to configure the debugger first.

.. figure:: img/rider_run_debug.webp
   :align: center

- Click on the **Godot > Edit Configurations** option at the top of the screen.

.. figure:: img/rider_configurations.webp
   :align: center

- Ensure the following values for the C++ Project Run Configuration:

    - Exe Path : `$(LocalDebuggerCommand)`
    - Program Arguments: `-e --path <path to the Godot project>`
    - Working Directory: `$(LocalDebuggerWorkingDirectory)`
    - Before Launch has a value of "Build Project"

This will tell the executable to debug the specified project without opening the Project Manager.
Use the root path to the project folder, not `project.godot` file path.

.. figure:: img/rider_configurations_changed.webp
   :align: center

- Finally click on "Apply" and "OK" to save the changes.

- When you press the **Debug** icon at the top of the screen, JetBrains Rider will launch the Godot editor with the debugger attached.

Alternatively you can use **Run > Attach to Process** to attach the debugger to a running Godot instance.

.. figure:: img/rider_attach_to_process.webp
   :align: center

- You can find the Godot instance by searching for `godot.editor` and then clicking `Attach with LLDB`

.. figure:: img/rider_attach_to_process_dialog.webp
   :align: center

|

### Debug visualizers
Debug visualizers customize how complex data structures are displayed during debugging.
For Windows "natvis" (short for "Native Visualization") built-in with Godot are automatically used.
For other operating systems, similar functionality can be setup manually.

Please follow RIDER-123535.

### Unit testing
Leverage Rider [doctest](../../architecture/unit_testing.md#doc_unit_testing) support.
Please refer to the instructions.

### Profiling
Please refer to the profiling instructions.

Please consult the JetBrains Rider documentation for any specific information about the JetBrains IDE.

### Known issues
Debugging Windows MinGV build - symbols are not loaded. Reported RIDER-106816.
