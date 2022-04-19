import Vue from "vue";

const fetchUser = async (username) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}`,
      {
        headers: {
        "X-token-id":  Vue.$cookies.get("X-token-id"),
        "content-type": "application/json",
        },
      }
    );

    const user = await response.json();

    return user;
  } catch (error) {
    console.error(error);
  }
};

const updateUserProfile = async (username, body) => {
  body = clean(body);
  if (Object.keys(body).length > 0) {
    try {
      await fetch(`${process.env.VUE_APP_API_URL}/users/${username}`, {
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

const deleteUser = async (username) => {
    try {
        await fetch(`${process.env.VUE_APP_API_URL}/users/${username}`, {
        method: "DELETE",
        });
    } catch (error) {
        console.error(error);
    }
};

export const fetchUsersByText = async (text) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users?filter=${text}`,
    );

    const users = await response.json();

    return users.users;
  } catch (error) {
    console.error(error);
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

export { fetchUser, updateUserProfile, deleteUser };
