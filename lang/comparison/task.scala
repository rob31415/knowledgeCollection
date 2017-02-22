object Task {
	def main(args: Array[String]) {
		val input = Map(
			"A" -> List((2.3,"f"), (0.01,"g"), (0.3,"h")),
			"B" -> List((0.3001,"i"), (0.01,"j"), (9.3,"kx")),
			"C" -> List((1000.7,"l"), (9.3,"m"), (9.2999,"n")))

		var output = scala.collection.mutable.Set[Tuple2[String,String]]()

		for((k, v) <- input) {
			val x = v.filter( {case (a,b) => a>=0.3 && a<9.3} )
			for(e <- x) output += Tuple2(k, e._2)
		}

		for(e <- output) println(e)
	}
}
