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

export { fetchUserByUsername };
