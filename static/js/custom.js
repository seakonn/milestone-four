document.addEventListener("load", displayMessageBox());

/*
Function checks to see if a message exists after the page loads.
If it does, it hides the associated div element and displays
the message in an alert box. If there is no message, the 
function doesn't do anything.
*/
function displayMessageBox() {
    
    let message;
    try {
        message = document.getElementById("message-popup").innerHTML
    }

    catch(error) {
        console.log("Error is " +error)
        message = null;
    }
    

}