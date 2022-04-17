const fetchUserRecentRepositories = async (userId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${userId}/repositories`
    );

    const data = await response.json();

    const repositories = data.repositories;
    repositories.sort((a, b) => a.id - b.id);

    return repositories.slice(0, 5);
  } catch (error) {
    console.error(error);
  }
};

const fetchUserRepositories = async (userId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${userId}/repositories`
    );

    const data = await response.json();

    const repositories = data.repositories;
    repositories.sort((a, b) => a.id - b.id);

    return repositories;
  } catch (error) {
    console.error(error);
  }
};

const fetchExploreRepositories = async () => {
  try {
    const response = await fetch(`${process.env.VUE_APP_API_URL}/repositories`);

    const data = await response.json();

    const repositories = data.repositories;

    return shuffle(repositories);
  } catch (error) {
    console.error(error);
  }
};

const fetchRepository = async (repositoryId) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/repositories/${repositoryId}`
    );

    const repository = await response.json();

    return repository;
  } catch (error) {
    console.error(error);
  }
};

const fetchRepositoryByUsernameAndName = async (username, name) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${name}`
    );

    const repository = await response.json();

    return repository;
  } catch (error) {
    console.error(error);
  }
};

const fetchRepositoryBranches = async (username, name) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${name}/branches`
    );

    const data = await response.json();

    const branches = data.branches.map((branch) =>
      branch.replace("*", "").trim()
    );

    return branches;
  } catch (error) {
    console.error(error);
  }
};

const fetchRepositoryFiles = async (username, name, branch) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${name}/files?branch=${branch}`
    );

    const data = await response.json();

    const files = data.files;

    return files;
  } catch (error) {
    console.error(error);
  }
};

const fetchFileContent = async (username, name, path, branch) => {
  try {
    const response = await fetch(
      `${process.env.VUE_APP_API_URL}/users/${username}/repositories/${name}/files?path=${path}&branch=${branch}`
    );

    const data = await response.text();

    return data;
  } catch (error) {
    console.error(error);
  }
};

const createRepository = async (body) => {
  clean(body);
  if (Object.keys(body).length > 0) {
    try {
      const response = await fetch(
        `${process.env.VUE_APP_API_URL}/repositories`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
        }
      );
      return response.status;
    } catch (error) {
      console.error(error);
    }
  }
};

const updateRepository = async (repositoryId, body) => {
  clean(body);
  if (Object.keys(body).length > 0) {
    try {
      await fetch(
        `${process.env.VUE_APP_API_URL}/repositories/${repositoryId}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
        }
      );
    } catch (error) {
      console.error(error);
    }
  }
};

// From https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array?page=1&tab=trending#tab-top
function shuffle(array) {
  let currentIndex = array.length,
    randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex != 0) {
    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }

  return array;
}

// From https://stackoverflow.com/questions/286141/remove-blank-attributes-from-an-object-in-javascript
function clean(obj) {
  for (var propName in obj) {
    if (obj[propName] === null || obj[propName] === undefined) {
      delete obj[propName];
    }
  }
  return obj;
}

export {
  fetchUserRecentRepositories,
  fetchUserRepositories,
  fetchExploreRepositories,
  fetchRepository,
  fetchRepositoryByUsernameAndName,
  fetchRepositoryFiles,
  fetchFileContent,
  fetchRepositoryBranches,
  createRepository,
  updateRepository,
};
