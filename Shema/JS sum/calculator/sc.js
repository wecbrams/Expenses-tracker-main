// Display Helpers
function getHistory() {
    return document.getElementById("history-value").innerText;
}

function printHistory(num) {
    document.getElementById("history-value").innerText = num;
}

function getOutput() {
    return document.getElementById("output-value").innerText;
}

function printOutput(num) {
    if (num === "") {
        document.getElementById("output-value").innerText = "";
    } else {
        document.getElementById("output-value").innerText = formatNumber(num);
    }
}

/* Number Formatting */
function formatNumber(num) {
    if (num === "" || num === "-") return num;
    return Number(num).toLocaleString("en");
}

function reverseNumberFormat(num) {
    if (num === "") return "";
    return Number(num.replace(/,/g, ""));
}

// Operator Buttons 
var operators = document.getElementsByClassName("operator");

for (var i = 0; i < operators.length; i++) {
    operators[i].addEventListener("click", function () {

        var output = getOutput();
        var history = getHistory();

        if (this.id === "clear") {
            printHistory("");
            printOutput("");
            return;
        }

        if (this.id === "backspace") {
            output = reverseNumberFormat(output).toString();
            output = output.slice(0, -1);
            printOutput(output);
            return;
        }

        // Prevent double operators
        if (output === "" && history !== "") {
            if (isNaN(history[history.length - 1])) {
                history = history.slice(0, -1);
            }
        }

        // MAin calcuation logic
        if (output !== "" || history !== "") {
            output = output === "" ? "" : reverseNumberFormat(output);
            history = history + output;

            if (this.id === "=") {
                try {
                    var result = eval(history);
                    printOutput(result);
                    printHistory("");
                } catch {
                    printOutput("Error");
                    printHistory("");
                }
            } else {
                history = history + this.id;
                printHistory(history);
                printOutput("");
            }
        }
    });
}

// Number Buttons
var numbers = document.getElementsByClassName("number");

for (var i = 0; i < numbers.length; i++) {
    numbers[i].addEventListener("click", function () {
        // playSound();

        var output = reverseNumberFormat(getOutput());

        if (!isNaN(output)) {
            output = output + this.id;
            printOutput(output);
        }
    });
}

//Click Sound 
// function playSound() {
//     var sound = document.getElementById("click-sound");
//     if (sound) {
//         sound.currentTime = 0;
//         sound.play();
//     }
// }

// // /* ===== Theme Toggle ===== */
// var themeToggle = document.getElementById("theme-toggle");
// if (themeToggle) {
//     themeToggle.onclick = function () {
//         document.body.classList.toggle("light");
//         this.textContent = document.body.classList.contains("light") ? "☀️" : "🌙";
//     };
// }

// function getHistory(){
//     return document.getElementById("history-value").innerText;
// }
// function printHistory(num){
//     document.getElementById("history-value").innerText = num;
// }
// function getOutput(){
//     return document.getElementById("output-value").innerText;
// }
// function printOutput(num){
//     if(num==""){
//         document.getElementById("output-value").innerText = num;
//     }else{
//         document.getElementById("output-value").innerText = getFormattedNumber(num);
//     }
// }
// function getFormattedNumber(num){
//     if(num=="-"){ return ""; }
//     return Number(num).toLocaleString("en"); ///Type casting == "  100" 
// }
// function reverseNumberFormat(num){
//     return Number(num.replace(/,/g,''));  
// }

// /* Operator buttons */
// var operator = document.getElementsByClassName("operator");
// for(var i=0;i<operator.length;i++){
//     operator[i].addEventListener("click",function(){
//         playSound();
//         if(this.id=="clear"){
//             printHistory("");
//             printOutput("");
//         }
//         else if(this.id=="backspace"){
//             var output = reverseNumberFormat(getOutput()).toString();
//             if(output){
//                 output = output.substr(0, output.length-1);
//                 printOutput(output);
//             }
//         }
//         else{
//             var output = getOutput();
//             var history = getHistory();
//             if(output=="" && history!=""){
//                 if(isNaN(history[history.length-1])){
//                     history = history.substr(0, history.length-1);
//                 }
//             }
//             if(output!="" || history!=""){
//                 output = output=="" ? output : reverseNumberFormat(output);
//                 history = history + output;
//                 if(this.id=="="){
//                     var result = eval(history);
//                     printOutput(result);
//                     printHistory("");
//                 }else{
//                     history = history + this.id;
//                     printHistory(history);
//                     printOutput("");
//                 }
//             }
//         }
//     });
// }

// /* Number buttons */
// var number = document.getElementsByClassName("number");
// for(var i=0;i<number.length;i++){
//     number[i].addEventListener("click",function(){
//         playSound();
//         var output = reverseNumberFormat(getOutput());
//         if(output!=NaN){
//             output = output + this.id;
//             printOutput(output);
//         }
//     });
// }

// /* Click sound */
// function playSound(){
//     var sound = document.getElementById("click-sound");
//     sound.currentTime = 0;
//     sound.play();
// }

// /* Theme toggle */
// document.getElementById("theme-toggle").onclick = function(){
//     document.body.classList.toggle("light");
//     this.textContent = document.body.classList.contains("light") ? "☀️" : "🌙";
// };


// // function getHistory(){
// // 	return document.getElementById("history-value").innerText;
// // }
// // function printHistory(num){
// // 	document.getElementById("history-value").innerText=num;
// // }
// // function getOutput(){
// // 	return document.getElementById("output-value").innerText;
// // }
// // function printOutput(num){
// // 	if(num==""){
// // 		document.getElementById("output-value").innerText=num;
// // 	}
// // 	else{
// // 		document.getElementById("output-value").innerText=getFormattedNumber(num);
// // 	}	
// // }
// // function getFormattedNumber(num){
// // 	if(num=="-"){
// // 		return "";
// // 	}
// // 	var n = Number(num);
// // 	var value = n.toLocaleString("en");
// // 	return value;
// // }
// // function reverseNumberFormat(num){
// // 	return Number(num.replace(/,/g,''));
// // }
// // var operator = document.getElementsByClassName("operator");
// // for(var i =0;i<operator.length;i++){
// // 	operator[i].addEventListener('click',function(){
// // 		if(this.id=="clear"){
// // 			printHistory("");
// // 			printOutput("");
// // 		}
// // 		else if(this.id=="backspace"){
// // 			var output=reverseNumberFormat(getOutput()).toString();
// // 			if(output){           //if output has a value
// // 				output= output.substr(0,output.length-1);
// // 				printOutput(output);
// // 			}
// // 		}
// // 		else{
// // 			var output=getOutput();
// // 			var history=getHistory();
// // 			if(output==""&&history!=""){
// // 				if(isNaN(history[history.length-1])){
// // 					history= history.substr(0,history.length-1);
// // 				}
// // 			}
// // 			if(output!="" || history!=""){
// // 				output= output==""?output:reverseNumberFormat(output);
// // 				history=history+output;
// // 				if(this.id=="="){
// // 					var result=eval(history);
// // 					printOutput(result);
// // 					printHistory("");
// // 				}
// // 				else{
// // 					history=history+this.id;
// // 					printHistory(history);
// // 					printOutput("");
// // 				}
// // 			}
// // 		}
		
// // 	});
// // }
// // var number = document.getElementsByClassName("number");
// // for(var i =0;i<number.length;i++){
// // 	number[i].addEventListener('click',function(){
// // 		var output=reverseNumberFormat(getOutput());
// // 		if(output!=NaN){ //if output is a number
// // 			output=output+this.id;
// // 			printOutput(output);
// // 		}
// // 	});
// // }
