var square = [];
var squaretri = [];

var search = function(array, target) {
	var lower = 0;
	var upper = array.length;
	
	while (lower < upper) {
		var x = lower + (upper - lower) / 2;
		var val = array[x]
		
		if (target === val) {
			return x;
			
		} else if (target > val) {
			if (lower === x) {
				return false;
				break;
			}
			lower = x;
			
		} else if (target < val) {
			upper = x;
		}
	}
}

for (var x = 1; x < 100; x++) {
	square.push(x * x);
}
	
for (var n = 1; n < 100; n++) {
	var val = 0.5 * n * (n + 1);
	var r = search(square, val);
	
	if (r != false) {
		squaretri.push(val);
	}
}

console.log(squaretri);