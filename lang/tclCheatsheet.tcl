# first off, i absolutely don't like tcl.
# but i learn it, because i have to modify some code at work. 

# C integration

# The tcl/tk system comes with libraries which allow a C program to call the tcl/tk interpreter and run tcl/tk scripts.
# 
# C Functions as tcl/tk procedures
# Tcl_CreateCommand( interp, "myFunctionName", Myfunc, (ClientData)NULL, (Tcl_CmdDeleteProc *)NULL );
# 
#     The client data pointer provides a means for Tcl commands to have data associated with them that is not global to the C program nor included in the Tcl core. Client data is essential in a multi-interpreter environment (where a single program has created and is making use of multiple Tcl interpreters) for the C routines to maintain any permanent data they need on a per-interpreter basis. Otherwise there would be reentrancy problems. Tcl solves this through the client data mechanism. When you are about to call Tcl_CreateCommand to add a new command to an interpreter, if that command needs to keep some read/write data across invocations, you should allocate the space, preferably using ckalloc, then pass the address of that space as the ClientData pointer to Tcl_CreateCommand.
#     When your command is called from Tcl, the ClientData pointer you gave to Tcl_CreateCommand when you added the command to that interpreter is passed to your C routine through the ClientData pointer calling argument.



# here are some infos about the language TCL and TK

set someWidget [tixNoteBook .someWidget]

# [] is evaluating it's contents (similar to backtick in bash; the keyword for this is "command substitution").
# 
#     synposis: tixNoteBook pathName ?options?
# 
#     The tixNoteBook command creates a new Tcl command whose name is the same as the path name of the NoteBook widget's window. This command may be used to invoke various operations on the widget.
# 
# the command tixNoteBook returns the parameter it's given, here ".someWidget". so $someWidget contains ".someWidget".
# 
# btw: "tixNoteBook" is last millenium's name for "tab panel"
# 
# what's that dot you'll find all over the place?
# apparently something with widgets. but why is there one in the first position?
# here's what some book has to say about that:
# 
#     Tk uses a naming system for the widgets that reflects their position in a hierarchy of wid-
#     gets. The root of the hierarchy is the main window of the application, and its
#     name is simply “.”. This is similar to the naming convention for directories in
#     UNIX where the root directory is named “/”, and then / is used to separate com-
#     ponents of a file name. Tk uses “.” in the same way. Each widget that is a child
#     of the main window is named something like .foo. A child widget of .foo would
#     be .foo.bar , and so on. Just as file systems have directories that are containers
#     for files (and other directories), the Tk window hierarchy uses frame widgets
#     that are containers for widgets (and other frames).
# 
# in tcl, Everything Is A String (EIAS). even "commands". (well, not really; they coined the term "shimmering"; if you feel like it, look it up, e.g. here http://wiki.tcl.tk/3033).
# for example, the following prints "shot" (command "puts" is similar to printf):
set d p
set u u
set m t
set p s
$d$u$m$p shot

# in tcl, there's no assignment operator. variables are declared, defined (and also read! O_o) with command "set".
# 
# incidentally: not only is everything just a string (yet, not really :-/), a tcl program is also just commands with parameters - a script is being worked through from top to bottom. that's really what constitutes a TCL program:
# every line is a list of strings with " " as delim while the list head is being considered a command.
# 
# what does the following do?
set tabs($label) [$someWidget add $label -label "I am a Tab" -createcmd "" -raisecmd "TabRaise"]

# set and $someWidget are commands.
# [] evaluates to string ".someWidget.nbframe.someView" while, at the same time, functionally adding a tab to the "notebook" with the "add" parameter to the command hidden behind $someWidget.
# tabs is an associative array (remember the EIAS mantra? well, you're better off if you don't). $label is it's key, the eval result from the [] it's value.
# 
# iterating all keys (= "names" in tcl-speak) from assoc'array aka "map" aka "dict":
foreach aValue [array names aDict]

# somewhere, there's
set label someView

# somewhere else, there's
set w $tabs($label)

# which evaluates to ".someWidget.nbframe.someView"
# 
# "" is the same as {}, namely grouping words together, with one difference: "" substitutes $variables, {} doesn't (keyword for this is "variable substitution").
# 
# The return command is optional - the Tcl interpreter will return the value of the last command in the body as the value of the procedure.
# 
# you want to pass an array as argument to a function (then use foreach in there)? cool, should be trivial. EIAS, right? well, again, not really.
# 
#     Entire arrays, however, are not currently able to be passed by value to a Tcl procedure (despite the damage this does to the EIAS dogma).
# 
# seriously? hmpf. now what?
# 
# basically, it's possible. see also #tclpassingdatastructuresaround
# see also: http://wiki.tcl.tk/3262
# 
# layout
# 
#     Tk has three built-in layout managers: the pack, grid and place managers. The pack geometry manager organises widgets in vertical and horizontal boxes. The grid geometry managers places widgets in a two dimensional grid. Finally, the place geometry manager places widgets in their containers using absolute positioning.


# passing datastructures around

# rule #1: tcl does argument passing (to and from procs) byval.
# 
# so you could ask yourself "if i formulate a solution which adheres to that rule, is it the most elegant one"?
# passing byval
# 
# if you judge yes, that means you're only interested in passing the content of the variable. you can do
# set myVar SomeProc $myVar
# 
# which takes the content of myVar, transforms it with SomeProc and puts the modified content back into myVar.
# 
# now, if you want to pass an array (in the example above, imagine myVar is an array) and since spaces are the delim of choice in all of tcl, you're gonna run into some trouble. tcl will tell you "wrong # args" because it mistakes the spaces in your array as seperators for proc arguments. d'oh!
# you'll have to do it this way
proc someProc {mapAsString} {
    # array set turns a string representation into a tcl array
    array set mapAsMap $mapAsString
    # prints out the whole thing
    puts [array get mapAsMap]
}
 
#declare empty map
array set aMap []
 
#seems that keys can't have spaces
set aMap("akey1") "value 1"
set aMap("akey2") "value 2"
 
#"array get" turns a tcl array into a string representation.
someProc [array get aMap]

# the same goes for returnvalues.
# 
# btw: i'm talking about map here, because a datastructure named "array" in tcl would be commonly known as a "map" (since it's a collection of key/value pairs).
# args containing spaces a.k.a "wrong # args"
# 
# while this works, there's another caveat.
# in the above case, "somehow" (without the user of tcl being aware of it), tcl seems to know that the string passed to "someProc" is one argument containing spaces rather than many arguments seperated by spaces.
# 
# in case you want to do
after 1000 someProc [array get aMap]

#or

eval someProc [array get aMap]

# you would be back at the "wrong # args" problem again.
# why?
# it's not visible (explicit) to the coder, from the code as it stands there, that the "this is one argument with spaces" information is in fact lost (in eval and after).
# 
# to make this work, you can add the information manually by doing
after 1000 someProc \{[array get aMap]\}

# similarly
eval someProc \{[array get aMap]\}
# passing byref

# in reference to the initially posed question:
# if you judge no, you most likely think, that a more elegant solution would be, to pass a ref to a variable into the proc, which in turn modifies the variable's contents.

# in such cases, you can do
proc modify {nameOfVariable} {
    upvar #0 $nameOfVariable aLocalNameForAReference
    # modifies aGlobalVariableOrArrayOrWhatever
    set aLocalNameForAReference "1"
}
set aGlobalVariableOrArrayOrWhatever "0"
modify "aGlobalVariableOrArrayOrWhatever"
# prints "1"
puts $aGlobalVariableOrArrayOrWhatever

# note that modify is not called with "$...", but with the name of the variable as a string.

# "upvar #0 $someGlobalVar someGlobalVar" is equivalent with "global someGlobalVar" with the only difference that you can specify a name of a variable (content of $someGlobalVar) which in the current scope is henceforth known as something else (here, "someGlobalVar").

# tcl leaves it to it's users to know and to keep track of where in a function call stackframe a refered-to variable resides.
# if it's in the function before, you'd write "upvar 1", two before: "upvar 2", etc.
# changing the nested call order of procs might now break your code unless you're aware of how the call stack depth changes and you adjust all "upvar x" accordingly.
# with "upvar #x", you refer to an absolute call stack depth, with #0 being global scope.
# 
# so, that's all you can do about this business. you still have global variables (or variables in another scope), but you get to dynamically (=at runtime) select, which one you want to refer to.



# in tcl, an "array" is really a dictionary

# push-back:
set someArray(aKey) "aValue"
set someArray(anotherKey) "anotherValue"

# iterate keys
foreach key [array names someArray] {
    puts $key
}

# iterate values (names = keys)
foreach key [array names someArray] {
    puts $someArray($key)
}

# iterate keys & values
foreach {key value} [array get someArray] {
    puts "$key $value"
}


# trace is an oberver pattern.
# if anything happens to a variable, if a cmd is executed or modified, it executes a block of code.
#
# example: when variable SPAGHETTI_TIME is write accessed, a msg is printed.
trace variable SPAGHETTI_TIME write "puts 'it's SPAGHETTI_TIME'"

# set also reads a variable a.k.a. toggle a variable
set x 1
set onoff  $x
puts $onoff
