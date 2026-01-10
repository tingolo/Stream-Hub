const loginButton = document.getElementById("login-btn")
const emailInput = document.getElementById("email-input")
const passwordInput = document.getElementById("password-input")

function validateDetails(email, password) {
    if (!email || !password) {
        alert("Please fill all the details!")
        return false
    }

    if (!emailInput.checkValidity()) {
        alert("Please provide a valid email!")
        return false
    }

    return true
}

loginButton.addEventListener("click", async () => {
    email = emailInput.value
    password = passwordInput.value
    
    if (!validateDetails(email, password)) {
        return
    }

    payload = {
        "email": email,
        "password": password,
    }

    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            
            body: JSON.stringify(payload)
        })

        const data = await response.json()
        if (data.status == "success") {
            alert("Login was successful.")
        }
        else {
            alert(data.message)
        }
    }

    catch(error) {
        alert("Login failed due to server error.")
    }
})