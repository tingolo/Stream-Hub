const registerButton = document.getElementById("register-btn")
const emailInput = document.getElementById("email-input")
const passwordInput = document.getElementById("password-input")
const reTypePasswordInput = document.getElementById("re-type-password-input")


function validateDetails(email, password, reTypePassword) {
    if (!email || !password || !reTypePassword) {
        alert("Please fill all the details!")
        return false
    }

    if (!emailInput.checkValidity()) {
        alert("Please provide a valid email!")
        return false
    }

    if (password !== reTypePassword) {
        alert("Password doesn't match!")
        return false
    }

    return true
}

registerButton.addEventListener("click", async () => {
    email = emailInput.value
    password = passwordInput.value
    reTypePassword = reTypePasswordInput.value
    
    if (!validateDetails(email, password, reTypePassword)) {
        return
    }

    payload = {
        "email": email,
        "password": password,
        "reTypedPassword": reTypePassword
    }

    try {
        const response = await fetch("/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            
            body: JSON.stringify(payload)
        })

        const data = await response.json()
        if (data.status == "success") {
            alert("Registeration was successful. Now please login.")
            window.location.href = "/auth/login"
        }
        else {
            alert(data.message)
        }
    }

    catch(error) {
        alert("Registeration failed due to server error.")
    }
})