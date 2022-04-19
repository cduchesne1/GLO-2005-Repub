import Vue from "vue";

const login = async (email, password) => {
  const response = await fetch(`${process.env.VUE_APP_API_URL}/login`, {
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      password: password,
    }),
    method: "POST",
  });
  if (response.status === 200) {
    const data = await response.json();
    await Vue.$cookies.set("X-token-id", data.token_id);
    return data;
  } else {
    return false;
  }
}

const logout = async () => {
  await fetch(`${process.env.VUE_APP_API_URL}/logout`, {
    headers: {
      "X-token-id":  Vue.$cookies.get("X-token-id"),
      "content-type": "application/json",
    },
    method: "POST",
  });
  await Vue.$cookies.remove("X-token-id");
};

const signup = async (email, username, name, password) => {
  const check = checkForm(email, username, name, password);
  if(check.passed) {
    const user = {
      email: email,
      name: name,
      username: username,
      password: password,
    };
    const response = await fetch(`${process.env.VUE_APP_API_URL}/signup`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(user),
    });
    if (response.status === 201) {
      return check;
    } else {
      const error = await response.json();
      if (error.desc === "Email already exists") {
        check.emailError = "Email already exists";
      } else if (error.desc === "Username already exists") {
        check.usernameError = "Username already exists";
      }
      check.passed = false;
      return check;
    }
  } else {
    return check;
  }
  
}

const checkForm = (email, username, name, password) => {
  let emailError = undefined;
  let nameError = undefined;
  let usernameError = undefined;
  let passwordError = undefined;
  if (email === "") {
    emailError = "Email is required";
  } else if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) === false) {
    emailError = "Email is invalid";
  }

  if (name === "") {
    nameError = "Name is required";
  }
  if (username === "") {
    usernameError = "Username is required";
  }
  if (password === "") {
    passwordError = "Password is required";
  }

  if (
    emailError ||
    nameError ||
    usernameError ||
    passwordError
  ) {
    return {
      "passed": false,
      "emailError": emailError,
      "nameError": nameError,
      "usernameError": usernameError,
      "passwordError": passwordError
    };
  }
  return {
    "passed": true,
    "emailError": emailError,
    "nameError": nameError,
    "usernameError": usernameError,
    "passwordError": passwordError
  };
}

export { login, logout, signup }