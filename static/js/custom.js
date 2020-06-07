document.addEventListener("load", displayMessageBox());

/*
Function checks to see if a message exists after the page loads.
If it does, it hides the associated div element and displays
the message in an alert box. If there is no message, the 
function doesn't do anything.
*/
function displayMessageBox() {
    
    let message;
    let element = document.getElementById("message-popup");

    try {
        message = element.innerHTML;
    }

    catch(error) {

        console.log("Error is " +error)
        message = null;
    }
    
    if(message) {

        element.style.display = "none";
        alert(message);
    }
}