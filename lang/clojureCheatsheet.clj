
(comment 
"first off, this is a comment")


(comment 
"forms are codeblocks in braces that are evaluated. forms are a list, whose first term is evaluated - e.g. as a function call - and following elements are arguments.")


(comment
"there are scalar data types: integers, floats, rationals, symbols, keywords, strings, characters, booleans,
and regex patterns")


(comment
"symbols vs keywords:

symbols refer to any legal clojure value/reference.

keywords are the same as ruby's symbols, akin to C's #define or C's enums.
they look like :thisIsAKeyword.
they eval to themselves, they just exist, dont refer to a value.

and remember this: symbols and keywords aren't members of any given namespace!")

(def thisSymbolRefersToAString "Hoihoi")
(println thisSymbolRefersToAString )
(comment "prints Hoihoi. def binds a symbol to a string. it's similar to a variable declaration+definition.")

(def aDefinedSymbolDoesntHaveToBeBoundRightAway)  ;neither do keywords


(comment
"basic collections:

(aList 2 3.4)

[aVector 3 4]

{1 "aMap" 2 "two" 3 "trois"}

#{this is a set}

notice the absence of commatas.")


(comment "functions (fn) take a vector as arguments. this one returns a set.")
(def thisSymbolIsBoundToAFunction (fn [arg1 arg2] #{arg1 arg2}))
(println (thisSymbolIsBoundToAFunction  "Eins" "Zwo"))

(defn isMoreConvenient
  "...than fn and also its got this nice docstring"
  ([arg1] #{arg1})            ;returns a set
  ([arg1 arg2] {arg1 arg2})   ;returns a map
)
(comment "btw: in a repl, you can search for docstrings of things with find-doc")

(println (isMoreConvenient "oneArg")) ; returns a set containing oneArg
(println (isMoreConvenient "oneArg" :twoArgs))  ; returns a map. both functions are accessed via the same symbol


(do         ;a sequence form. btw. this is a line comment.
  (+ 3 4)   ;a sequence
  12        ;then this
  (* 2 2)   ;this is the last and only it's value is returned
)


(let  ;let form lets you declare locals. theyre scoped inside the let form.
  [aConstant 5]
  (println aConstant)
)


(comment "now following, 3 loop constructs")

(defn loop-using-when-and-recur [x]
  (when (pos? x)
    (print x)
    (recur (dec x)))
)
(loop-using-when-and-recur 4)


(defn loop-using-if [sum x]
  (if (pos? x)
    (recur (+ sum x) (dec x))   ;the "then" clause.
    sum)                        ;"else" clause
)
(println (loop-using-if 0 3))


(defn loop-using-loopform [x0]    ;notice we got rid of sum arg
  (loop [sum 0 x x0]
    (if (pos? x)
      (recur (+ sum x) (dec x))
      sum)
  )
)
(println (loop-using-loopform 3))


(comment "now following, a little bit of quoting stuff")

(quote (notEvaluated 2 3 4))  ; the first element in a list is evaluated. but not if it's quoted.

;(cons 1 (:bla 3))            ;this doesnt work. 'bla' is not evaluable
(cons 1 (quote ("bla" 3)) )   ;this works
(cons 1 '("bla" 3) )          ;this is equivalent to "quote". btw. cons contructs a list.

'(+ 10 (* 3 2))     ; doesnt eval the expression (i.e. evals it to itself)
`(+ 10 ~(* 3 2))    ; "10 6", because ~ unquotes. but then, the "syntax quote" ` is needed instead of '

(let [x '(2 3)] `(1 ~x))    ;(1 (2 3))
(let [x '(2 3)] `(1 ~@x))   ;(1 2 3)  @ unpacks and splices it in; needs ` to work

`unqualifiedSymbol#   ;creates a not fully qualified symbol


(def bla #(println "bla"))  ; #() defines in-place funtions (aka anonymous fct)
(def bla2 #(println "bla2"))
[bla bla2]  ; this prints nothing, because [] doesnt evaluate its contents


(comment "now following, positional destructuring with vector")

(defn positionalDestructuring [a b] #(println "dudl"))
(positionalDestructuring "Hi" "World")

(def sicknesses ["schnupfen" "sinusitis" "pregnancy" "restlessleg" "idiocy"])
(let [[a b & allTheRest :as everything] sicknesses]
  (println a b allTheRest "everything:" everything))
  
(comment "destructuring (with) a map by key:")
(def cars {:golf "green" :toyota "blue" :audi "black"})

(let [{a :golf b :audi} cars] (println "golf is" a "and audi is" b))

(comment 
":keys makes clojure look for keys, which are given in a vector.
if a key is missing, :or specifies a default.")
(let [{:keys [audi golf somecar], :or {somecar "default"} } cars] (println audi golf somecar))

(comment 
":syms tells clojure to look for symbol-type keys, :strs for string-type keys")

(comment "you can also go positional into a vector")
(let [{first 0 last 3} ["one" "two" "three" "four"] ]
(println first last)
)

(comment "destructuring can be used with functions, too")
(defn printFirst [{:keys [audi]}]
(println audi))
(printFirst cars)


(defn aConditionExample [x]
  (cond (= x :doThis)
      (println "I did this")
      :else
      (println "I did something else")
   )
)
(aConditionExample :doThis)


(comment
"namespaces

you can get definitions from other namespaces into the current ns
in four ways:
:require, which doesn't map the other's ns symbols onto the current.
:use, which does such a mapping.
:refer, which is like :use, but only works for previously already loaded ns's.
:import gets java stuff

:only [..], :exclude [..], :rename [..] or as[..] can be additionally specified.")

(comment "in a repl, you can do report-ns to find out whats current")

(ns createSomeNamespace1 (:require clojure.set))
(clojure.set/intersection #{1 2 3} #{3 4 5})

(ns createSomeNamespace2 (:require [clojure.set :as s]))
(s/intersection #{1 2 3} #{3 4 5})

(ns createSomeNamespace3 (:use clojure.set))
(intersection #{1 2 3} #{3 4 5})

(ns createSomeNamespace4 (:refer createSomeNamespace1))

(ns createSomeNamespace4 (:import [java.util HashMap]))


(comment
"metadata influences identity and equality
btw: metadata can be attached to various objects, not just keywords.")

(let [x (with-meta 'goat {:horny true})
      y (with-meta 'goat {:horny false})]
  [(identical? y x) ; false, because identity considers metadata 
  (= y x)           ; true, because equality doesn't
  (meta x)          ; {:horny true}
  (meta y)]         ; {:horny false}
)


(comment 
"there's a lisp-1 and a lisp-2.
in lisp-1, function and name resolution are similar.
in lisp-2, they're not.
clojure is a lisp-1.")
