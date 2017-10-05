#!/usr/bin/node  --es_staging --harmony --use_strict
let input = new Map()
input.set("A", Array([2.3,"f"], [0.0,"g"], [0.3,"h"]))
input.set("B", Array([0.3001,"i"], [0.01,"j"], [9.3,"kx"]))
input.set("C", Array([1000.7,"l"], [9.3,"m"], [9.2999,"n"]))

let output = new Set()

// forEach can destructure map, for/of can't.
input.forEach( (v, k) => {
	let x = v.filter( (el) => el[0]>=0.3 && el[0]<9.3 );
	for (let e of x) {output.add([k, e[1]])}
});

for (let e of output) {console.log(e)}
