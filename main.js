	var years=20;
		var name="Collins";

		document.write("My name is"+name+" and i am"+years);

//condition
var food="apple";

if (food=="Apple") {

	alert("Some");
}else{
	alert("no");
}
var i=1;

//conditional while loop
while(i<5){
	document.write("The number is "+i);
	i++;
}


//function and if statement
function batting(player,distance){
	if (distance>350) {
		document.write(player+" hit the ball");
	}
}
batting("Collins",500);
