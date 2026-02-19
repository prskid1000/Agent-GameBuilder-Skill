<span id="class_EditorVCSInterface"></span>

## EditorVCSInterface

**Inherits:** [Object](class_object.md#class_Object)

Version Control System (VCS) interface, which reads and writes to the local VCS in use.

### Description

Defines the API that the editor uses to extract information from the underlying VCS. The implementation of this API is included in VCS plugins, which are GDExtension plugins that inherit **EditorVCSInterface** and are attached (on demand) to the singleton instance of **EditorVCSInterface**. Instead of performing the task themselves, all the virtual functions listed below are calling the internally overridden functions in the VCS plugins to provide a plug-n-play experience. A custom VCS plugin is supposed to inherit from **EditorVCSInterface** and override each of these virtual functions.

### Tutorials

- [Version control systems](../tutorials/best_practices/version_control_systems.md)

### Methods


| [bool](class_bool.md#class_bool) | [_checkout_branch](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__checkout_branch) ( branch_name: [String](class_string.md#class_String) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_commit](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__commit) ( msg: [String](class_string.md#class_String) ) | virtual | required |
| void | [_create_branch](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__create_branch) ( branch_name: [String](class_string.md#class_String) ) | virtual | required |
| void | [_create_remote](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__create_remote) ( remote_name: [String](class_string.md#class_String), remote_url: [String](class_string.md#class_String) ) | virtual | required |
| void | [_discard_file](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__discard_file) ( file_path: [String](class_string.md#class_String) ) | virtual | required |
| void | [_fetch](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__fetch) ( remote: [String](class_string.md#class_String) ) | virtual | required |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [_get_branch_list](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_branch_list) ( ) | virtual | required |
| [String](class_string.md#class_String) | [_get_current_branch_name](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_current_branch_name) ( ) | virtual | required |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_diff](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_diff) ( identifier: [String](class_string.md#class_String), area: [int](class_int.md#class_int) ) | virtual | required |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_line_diff](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_line_diff) ( file_path: [String](class_string.md#class_String), text: [String](class_string.md#class_String) ) | virtual | required |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_modified_files_data](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_modified_files_data) ( ) | virtual | required |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_previous_commits](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_previous_commits) ( max_commits: [int](class_int.md#class_int) ) | virtual | required |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [_get_remotes](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_remotes) ( ) | virtual | required |
| [String](class_string.md#class_String) | [_get_vcs_name](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_vcs_name) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_initialize](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__initialize) ( project_path: [String](class_string.md#class_String) ) | virtual | required |
| void | [_pull](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__pull) ( remote: [String](class_string.md#class_String) ) | virtual | required |
| void | [_push](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__push) ( remote: [String](class_string.md#class_String), force: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_remove_branch](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__remove_branch) ( branch_name: [String](class_string.md#class_String) ) | virtual | required |
| void | [_remove_remote](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__remove_remote) ( remote_name: [String](class_string.md#class_String) ) | virtual | required |
| void | [_set_credentials](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__set_credentials) ( username: [String](class_string.md#class_String), password: [String](class_string.md#class_String), ssh_public_key_path: [String](class_string.md#class_String), ssh_private_key_path: [String](class_string.md#class_String), ssh_passphrase: [String](class_string.md#class_String) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_shut_down](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__shut_down) ( ) | virtual | required |
| void | [_stage_file](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__stage_file) ( file_path: [String](class_string.md#class_String) ) | virtual | required |
| void | [_unstage_file](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__unstage_file) ( file_path: [String](class_string.md#class_String) ) | virtual | required |
| [Dictionary](class_dictionary.md#class_Dictionary) | [add_diff_hunks_into_diff_file](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_diff_hunks_into_diff_file) ( diff_file: [Dictionary](class_dictionary.md#class_Dictionary), diff_hunks: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [add_line_diffs_into_diff_hunk](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk) ( diff_hunk: [Dictionary](class_dictionary.md#class_Dictionary), line_diffs: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [create_commit](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_commit) ( msg: [String](class_string.md#class_String), author: [String](class_string.md#class_String), id: [String](class_string.md#class_String), unix_timestamp: [int](class_int.md#class_int), offset_minutes: [int](class_int.md#class_int) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [create_diff_file](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_file) ( new_file: [String](class_string.md#class_String), old_file: [String](class_string.md#class_String) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [create_diff_hunk](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_hunk) ( old_start: [int](class_int.md#class_int), new_start: [int](class_int.md#class_int), old_lines: [int](class_int.md#class_int), new_lines: [int](class_int.md#class_int) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [create_diff_line](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_line) ( new_line_no: [int](class_int.md#class_int), old_line_no: [int](class_int.md#class_int), content: [String](class_string.md#class_String), status: [String](class_string.md#class_String) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [create_status_file](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_status_file) ( file_path: [String](class_string.md#class_String), change_type: [ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType), area: [TreeArea](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea) ) |
| void | [popup_error](class_editorvcsinterface.md#class_EditorVCSInterface_method_popup_error) ( msg: [String](class_string.md#class_String) ) |

---

### Enumerations

<span id="enum_EditorVCSInterface_ChangeType"></span>

enum **ChangeType**: [🔗](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType)

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_NEW"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_NEW** = `0`

A new file has been added.

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_MODIFIED"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_MODIFIED** = `1`

An earlier added file has been modified.

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_RENAMED"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_RENAMED** = `2`

An earlier added file has been renamed.

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_DELETED"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_DELETED** = `3`

An earlier added file has been deleted.

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_TYPECHANGE"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_TYPECHANGE** = `4`

An earlier added file has been typechanged.

<span id="class_EditorVCSInterface_constant_CHANGE_TYPE_UNMERGED"></span>

[ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType) **CHANGE_TYPE_UNMERGED** = `5`

A file is left unmerged.

---

<span id="enum_EditorVCSInterface_TreeArea"></span>

enum **TreeArea**: [🔗](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea)

<span id="class_EditorVCSInterface_constant_TREE_AREA_COMMIT"></span>

[TreeArea](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea) **TREE_AREA_COMMIT** = `0`

A commit is encountered from the commit area.

<span id="class_EditorVCSInterface_constant_TREE_AREA_STAGED"></span>

[TreeArea](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea) **TREE_AREA_STAGED** = `1`

A file is encountered from the staged area.

<span id="class_EditorVCSInterface_constant_TREE_AREA_UNSTAGED"></span>

[TreeArea](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea) **TREE_AREA_UNSTAGED** = `2`

A file is encountered from the unstaged area.

---

### Method Descriptions

<span id="class_EditorVCSInterface_private_method__checkout_branch"></span>

[bool](class_bool.md#class_bool) **_checkout_branch** ( branch_name: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__checkout_branch)

Checks out a `branch_name` in the VCS.

---

<span id="class_EditorVCSInterface_private_method__commit"></span>

void **_commit** ( msg: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__commit)

Commits the currently staged changes and applies the commit `msg` to the resulting commit.

---

<span id="class_EditorVCSInterface_private_method__create_branch"></span>

void **_create_branch** ( branch_name: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__create_branch)

Creates a new branch named `branch_name` in the VCS.

---

<span id="class_EditorVCSInterface_private_method__create_remote"></span>

void **_create_remote** ( remote_name: [String](class_string.md#class_String), remote_url: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__create_remote)

Creates a new remote destination with name `remote_name` and points it to `remote_url`. This can be an HTTPS remote or an SSH remote.

---

<span id="class_EditorVCSInterface_private_method__discard_file"></span>

void **_discard_file** ( file_path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__discard_file)

Discards the changes made in a file present at `file_path`.

---

<span id="class_EditorVCSInterface_private_method__fetch"></span>

void **_fetch** ( remote: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__fetch)

Fetches new changes from the `remote`, but doesn't write changes to the current working directory. Equivalent to `git fetch`.

---

<span id="class_EditorVCSInterface_private_method__get_branch_list"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **_get_branch_list** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_branch_list)

Gets an instance of an [Array](class_array.md#class_Array) of [String](class_string.md#class_String) s containing available branch names in the VCS.

---

<span id="class_EditorVCSInterface_private_method__get_current_branch_name"></span>

[String](class_string.md#class_String) **_get_current_branch_name** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_current_branch_name)

Gets the current branch name defined in the VCS.

---

<span id="class_EditorVCSInterface_private_method__get_diff"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_diff** ( identifier: [String](class_string.md#class_String), area: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_diff)

Returns an array of [Dictionary](class_dictionary.md#class_Dictionary) items (see [create_diff_file()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_file), [create_diff_hunk()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_hunk), [create_diff_line()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_line), [add_line_diffs_into_diff_hunk()](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk) and [add_diff_hunks_into_diff_file()](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_diff_hunks_into_diff_file)), each containing information about a diff. If `identifier` is a file path, returns a file diff, and if it is a commit identifier, then returns a commit diff.

---

<span id="class_EditorVCSInterface_private_method__get_line_diff"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_line_diff** ( file_path: [String](class_string.md#class_String), text: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_line_diff)

Returns an [Array](class_array.md#class_Array) of [Dictionary](class_dictionary.md#class_Dictionary) items (see [create_diff_hunk()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_hunk)), each containing a line diff between a file at `file_path` and the `text` which is passed in.

---

<span id="class_EditorVCSInterface_private_method__get_modified_files_data"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_modified_files_data** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_modified_files_data)

Returns an [Array](class_array.md#class_Array) of [Dictionary](class_dictionary.md#class_Dictionary) items (see [create_status_file()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_status_file)), each containing the status data of every modified file in the project folder.

---

<span id="class_EditorVCSInterface_private_method__get_previous_commits"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_previous_commits** ( max_commits: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_previous_commits)

Returns an [Array](class_array.md#class_Array) of [Dictionary](class_dictionary.md#class_Dictionary) items (see [create_commit()](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_commit)), each containing the data for a past commit.

---

<span id="class_EditorVCSInterface_private_method__get_remotes"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **_get_remotes** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_remotes)

Returns an [Array](class_array.md#class_Array) of [String](class_string.md#class_String) s, each containing the name of a remote configured in the VCS.

---

<span id="class_EditorVCSInterface_private_method__get_vcs_name"></span>

[String](class_string.md#class_String) **_get_vcs_name** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__get_vcs_name)

Returns the name of the underlying VCS provider.

---

<span id="class_EditorVCSInterface_private_method__initialize"></span>

[bool](class_bool.md#class_bool) **_initialize** ( project_path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__initialize)

Initializes the VCS plugin when called from the editor. Returns whether or not the plugin was successfully initialized. A VCS project is initialized at `project_path`.

---

<span id="class_EditorVCSInterface_private_method__pull"></span>

void **_pull** ( remote: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__pull)

Pulls changes from the remote. This can give rise to merge conflicts.

---

<span id="class_EditorVCSInterface_private_method__push"></span>

void **_push** ( remote: [String](class_string.md#class_String), force: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__push)

Pushes changes to the `remote`. If `force` is `true`, a force push will override the change history already present on the remote.

---

<span id="class_EditorVCSInterface_private_method__remove_branch"></span>

void **_remove_branch** ( branch_name: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__remove_branch)

Remove a branch from the local VCS.

---

<span id="class_EditorVCSInterface_private_method__remove_remote"></span>

void **_remove_remote** ( remote_name: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__remove_remote)

Remove a remote from the local VCS.

---

<span id="class_EditorVCSInterface_private_method__set_credentials"></span>

void **_set_credentials** ( username: [String](class_string.md#class_String), password: [String](class_string.md#class_String), ssh_public_key_path: [String](class_string.md#class_String), ssh_private_key_path: [String](class_string.md#class_String), ssh_passphrase: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__set_credentials)

Set user credentials in the underlying VCS. `username` and `password` are used only during HTTPS authentication unless not already mentioned in the remote URL. `ssh_public_key_path`, `ssh_private_key_path`, and `ssh_passphrase` are only used during SSH authentication.

---

<span id="class_EditorVCSInterface_private_method__shut_down"></span>

[bool](class_bool.md#class_bool) **_shut_down** ( ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__shut_down)

Shuts down VCS plugin instance. Called when the user either closes the editor or shuts down the VCS plugin through the editor UI.

---

<span id="class_EditorVCSInterface_private_method__stage_file"></span>

void **_stage_file** ( file_path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__stage_file)

Stages the file present at `file_path` to the staged area.

---

<span id="class_EditorVCSInterface_private_method__unstage_file"></span>

void **_unstage_file** ( file_path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_private_method__unstage_file)

Unstages the file present at `file_path` from the staged area to the unstaged area.

---

<span id="class_EditorVCSInterface_method_add_diff_hunks_into_diff_file"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **add_diff_hunks_into_diff_file** ( diff_file: [Dictionary](class_dictionary.md#class_Dictionary), diff_hunks: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_diff_hunks_into_diff_file)

Helper function to add an array of `diff_hunks` into a `diff_file`.

---

<span id="class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **add_line_diffs_into_diff_hunk** ( diff_hunk: [Dictionary](class_dictionary.md#class_Dictionary), line_diffs: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk)

Helper function to add an array of `line_diffs` into a `diff_hunk`.

---

<span id="class_EditorVCSInterface_method_create_commit"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **create_commit** ( msg: [String](class_string.md#class_String), author: [String](class_string.md#class_String), id: [String](class_string.md#class_String), unix_timestamp: [int](class_int.md#class_int), offset_minutes: [int](class_int.md#class_int) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_commit)

Helper function to create a commit [Dictionary](class_dictionary.md#class_Dictionary) item. `msg` is the commit message of the commit. `author` is a single human-readable string containing all the author's details, e.g. the email and name configured in the VCS. `id` is the identifier of the commit, in whichever format your VCS may provide an identifier to commits. `unix_timestamp` is the UTC Unix timestamp of when the commit was created. `offset_minutes` is the timezone offset in minutes, recorded from the system timezone where the commit was created.

---

<span id="class_EditorVCSInterface_method_create_diff_file"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **create_diff_file** ( new_file: [String](class_string.md#class_String), old_file: [String](class_string.md#class_String) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_file)

Helper function to create a [Dictionary](class_dictionary.md#class_Dictionary) for storing old and new diff file paths.

---

<span id="class_EditorVCSInterface_method_create_diff_hunk"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **create_diff_hunk** ( old_start: [int](class_int.md#class_int), new_start: [int](class_int.md#class_int), old_lines: [int](class_int.md#class_int), new_lines: [int](class_int.md#class_int) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_hunk)

Helper function to create a [Dictionary](class_dictionary.md#class_Dictionary) for storing diff hunk data. `old_start` is the starting line number in old file. `new_start` is the starting line number in new file. `old_lines` is the number of lines in the old file. `new_lines` is the number of lines in the new file.

---

<span id="class_EditorVCSInterface_method_create_diff_line"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **create_diff_line** ( new_line_no: [int](class_int.md#class_int), old_line_no: [int](class_int.md#class_int), content: [String](class_string.md#class_String), status: [String](class_string.md#class_String) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_diff_line)

Helper function to create a [Dictionary](class_dictionary.md#class_Dictionary) for storing a line diff. `new_line_no` is the line number in the new file (can be `-1` if the line is deleted). `old_line_no` is the line number in the old file (can be `-1` if the line is added). `content` is the diff text. `status` is a single character string which stores the line origin.

---

<span id="class_EditorVCSInterface_method_create_status_file"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **create_status_file** ( file_path: [String](class_string.md#class_String), change_type: [ChangeType](class_editorvcsinterface.md#enum_EditorVCSInterface_ChangeType), area: [TreeArea](class_editorvcsinterface.md#enum_EditorVCSInterface_TreeArea) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_create_status_file)

Helper function to create a [Dictionary](class_dictionary.md#class_Dictionary) used by editor to read the status of a file.

---

<span id="class_EditorVCSInterface_method_popup_error"></span>

void **popup_error** ( msg: [String](class_string.md#class_String) ) [🔗](class_editorvcsinterface.md#class_EditorVCSInterface_method_popup_error)

Pops up an error message in the editor which is shown as coming from the underlying VCS. Use this to show VCS specific error messages.
