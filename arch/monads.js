


function identityMONAD() {
  return function unit(value) {
    var monad = Object.create(null);
    monad.bind = function (func) {
      return func(value);
    };
    return monad;
  };  
}

var identity = identityMONAD();
var monad1 = identity("Hello world");
monad1.bind(console.log);




function ajaxMONAD() {
	var prototype = Object.create(null);
	function unit(value) {
		var monad = Object.create(prototype);
		monad.bind = function (func, args) {
			//return func(value, ...args);
			return func.apply(undefined,[value].concat(Array.prototype.slice.apply(args || [])));
		};
		return monad;
	}

	unit.method = function (name, func) {
		prototype[name] = func;
		return unit;
	}

	unit.lift = function (name, func) {
		prototype[name] = function (args) {
			return unit(this.bind(func,args));
		};
		return unit;
	}

	return unit;
}

var ajax = ajaxMONAD().lift("alert", console.log);
var monad2 = ajax("Hello world");
monad2.alert();



// wip: doesn't work yet
function maybeMONAD(modifier) {
	var prototype = Object.create(null);
	function unit(value) {
		var monad = Object.create(prototype);
		monad.bind = function (func, args) {
			return func(value, args);
		};
		if(typeof modifier === 'function') {
			modifier(monad, value);
		}
		return monad;
	}
	return unit;
}

var maybe = maybeMONAD(function (monad, value) {
	if (value === null || value === undefined) {
		monad.is_null = true;
		monad.bind = function () {
			return monad;
		};
	}
});

var monad3 = maybe(null);
monad3.bind(console.log);
