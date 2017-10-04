# first off, i absolutely don't like tcl.
# but i learn it, because i have to modify some code at work. 


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
# trace variable SPAGHETTI_TIME write "puts 'it's SPAGHETTI_TIME'"

# set also reads a variable a.k.a. toggle a variable
set x 1
set onoff  $x
puts $onoff
