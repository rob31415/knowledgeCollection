#!node --es_staging --harmony --use_strict task.js
let input = new Map()
input.set("A", Array([2.3,"f"], [0.0,"g"], [0.3,"h"]))
input.set("B", Array([0.3001,"i"], [0.01,"j"], [9.3,"kx"]))
input.set("C", Array([1000.7,"l"], [9.3,"m"], [9.2999,"n"]))

let output = new Set()
input.forEach( (v, k) => {
	let x = v.filter( (el) => el[0]>=0.3 && el[0]<9.3 );
	x.forEach( (e) => output.add({k:e[1]}) );	//TODO: how do i get k in there?
});

output.forEach( (e) => {console.log(e)} );
