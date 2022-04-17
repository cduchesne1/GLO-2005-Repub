const fetchUserByUsername = async (username) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}`
    );

    const user = await response.json();

    return user;
  } catch (error) {
    console.error(error);
  }
};

const fetchUser = async (userId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${userId}`
    );

    const user = await response.json();

    return user;
  } catch (error) {
    console.error(error);
  }
};

const updateUserProfile = async (userId, body) => {
  body = clean(body);
  if (Object.keys(body).length > 0) {
    try {
      await fetch(`${process.env.VUE_APP_API_URL}/users/${userId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });
    } catch (error) {
      console.error(error);
    }
  }
};

// From https://stackoverflow.com/questions/286141/remove-blank-attributes-from-an-object-in-javascript
function clean(obj) {
  for (var propName in obj) {
    if (obj[propName] === null || obj[propName] === undefined) {
      delete obj[propName];
    }
  }
  return obj;
}

export { fetchUserByUsername, fetchUser, updateUserProfile };
